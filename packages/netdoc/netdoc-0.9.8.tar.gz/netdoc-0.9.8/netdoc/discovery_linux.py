__author__     = 'Andrea Dainese'
__contact__    = 'andrea@adainese.it'
__copyright__  = 'Copyright 2022, Andrea Dainese'
__license__    = 'GPLv3'
__date__       = '2022-09-19'
__version__    = '0.9.8'

import json
from ctypes import addressof
from django.utils import timezone
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F
from . import models
from . import functions

def discovery(nr):
    """
    Discovery Linux devices
    """
    mode = "netmiko"
    platform = "linux"
    filtered_devices = nr.filter(platform=platform)
    enable=True
    logs = []

    # Define tasks
    def multiple_tasks(task):
        """
        Define tasks for the playbook. CMD line is passed also as name, so we
        can log cmdline, stdout (result) and parsed output.
        """
        task.run(
            task=netmiko_send_command,
            name="hostname",
            command_string="hostname",
            use_textfsm=False
        )
        task.run(
            task=netmiko_send_command,
            name="ip link show",
            command_string="ip link show",
            use_textfsm=False
        )
        task.run(task=netmiko_send_command, name="arp -a", command_string="arp -an", use_textfsm=False)
        task.run(task=netmiko_send_command, name="ip address show", command_string="ip address show", use_textfsm=False)
        task.run(task=netmiko_send_command, name="ip route show", command_string="ip route show", use_textfsm=False)
        task.run(
            task=netmiko_send_command, name="ip vrf show", command_string="ip vrf show", use_textfsm=False
        )

    # Run the playbook
    aggregated_results = filtered_devices.run(task=multiple_tasks)

    # Print the result
    print_result(aggregated_results)

    for key, multi_result in aggregated_results.items():
        vrfs = []
        current_nr = nr.filter(F(name=key))

        # MultiResult is an array of Result
        for result in multi_result:
            if result.name == "multiple_tasks":
                # Skip MultipleTask
                continue

            address = result.host.dict()["hostname"]
            discoverable = models.Discoverable.objects.get(address=address, mode=f'{mode}_{platform}')
            discoverable.last_discovered_at = timezone.now() # Update last_discovered_at
            discoverable.save()

            # Log locally
            log = functions.log_create(
                discoverable=discoverable,
                raw_output=result.result,
                request=result.name,
            )
            if result.name == 'hostname':
                # There is no parsing template for hostname command
                log.parsed_output = [{'hostname': log.raw_output}]
                log.parsed = True
                log.save()

            # Save log for later
            logs.append(log)

            # Save VRF list for later
            if result.name == "ip vrf show":
                try:
                    vrf_parsed_output = functions.parse_netmiko_output(result.result, platform=platform, command=result.name)
                except:
                    vrf_parsed_output = []
                for entry in vrf_parsed_output:
                    vrfs.append(entry)

        # Additional commands out of the multi result loop
        def additional_tasks(task):
            """
            Define additional tasks for the playbook.
            """
            # Per VRF commands
            for vrf in vrfs:
                task.run(task=netmiko_send_command, name=f'ip route show|ip route show table {vrf["name"]}', command_string=f'ip route show table {vrf["table"]}', use_textfsm=False)

        # Run the additional playbook
        additional_aggregated_results = current_nr.run(task=additional_tasks)

        # Print the result
        print_result(additional_aggregated_results)

        for key, additional_multi_result in additional_aggregated_results.items():
            # MultiResult is an array of Result
            for result in additional_multi_result:
                if result.name == "additional_tasks":
                    # Skip MultipleTask
                    continue

                # Log locally
                log = functions.log_create(
                    discoverable=discoverable,
                    raw_output=result.result,
                    request=result.name,
                )

                # Save log for later
                logs.append(log)
