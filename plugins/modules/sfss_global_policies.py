#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for sfss_global_policies
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module:  sfss_global_policies
version_added: 1.0.0
notes:
- Idempotent is supported.
- Supports C(check_mode).
short_description: This module manages attributes of sfss Global Policies
description:
  - This module manages attributes of sfss Global Policies
author: Namrata Chatterjee (@nchatterjee)

options:
  config:
    description: A list of link aggregation group configurations.
    type: list
    elements: dict
    suboptions:
      instance_id:
        type: int
        description: The instance identifier
        required: True
      zoning_policy:
        type: bool
        description: Zoning policy enable or disable
      NameServerEntityPurgeTOV:
        type: str
        description:
        - Timeout value of name server entity
        choices:
        - NoTimeout
        - 4Hr
        - 24Hr
        - 8Hr
        - 48Hr
        - 5Sec
  state:
    description:
    - The state the configuration should be left in
    type: str
    choices:
    - merged
    default: merged
"""
EXAMPLES = """
# Using merged
#
# Before state:
# -------------
#
#redfish/v1/SFSS/1/GlobalPolicies
# {
#   "ZoningPolicy": "Disable",
#   "NameServerEntityPurgeTOV": "48Hr",
#   "@odata.id": "/redfish/v1/SFNC/2/GlobalPolicies",
#   "@odata.type": "#GlobalPolicies.GlobalPolicies",
#   "@odata.context": "/redfish/v1/SFNC/2/$metadata#GlobalPolicies/GlobalPolicies/$entity"
# }
#redfish/v1/SFSS/2/GlobalPolicies
# {
#   "ZoningPolicy": "Disable",
#   "NameServerEntityPurgeTOV": "48Hr",
#   "@odata.id": "/redfish/v1/SFNC/2/GlobalPolicies",
#   "@odata.type": "#GlobalPolicies.GlobalPolicies",
#   "@odata.context": "/redfish/v1/SFNC/2/$metadata#GlobalPolicies/GlobalPolicies/$entity"
# }
- name: Create Global Policies
  dellemc.sfss.sfss_global_policies:
    config:
    - zoning_policy: false
      NameServerEntityPurgeTOV: 4Hr
      instance_id: 1
    - zoning_policy: false
      NameServerEntityPurgeTOV: 8Hr
      instance_id: 2
#
# After state:
# -------------
#
#redfish/v1/SFSS/1/GlobalPolicies
# {
#   "ZoningPolicy": "Disable",
#   "NameServerEntityPurgeTOV": "4Hr",
#   "@odata.id": "/redfish/v1/SFNC/1/GlobalPolicies",
#   "@odata.type": "#GlobalPolicies.GlobalPolicies",
#   "@odata.context": "/redfish/v1/SFNC/1/$metadata#GlobalPolicies/GlobalPolicies/$entity"
# }
#redfish/v1/SFSS/2/GlobalPolicies
# {
#   "ZoningPolicy": "Disable",
#   "NameServerEntityPurgeTOV": "8Hr",
#   "@odata.id": "/redfish/v1/SFNC/2/GlobalPolicies",
#   "@odata.type": "#GlobalPolicies.GlobalPolicies",
#   "@odata.context": "/redfish/v1/SFNC/2/$metadata#GlobalPolicies/GlobalPolicies/$entity"
# }


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.argspec.global_policies.global_policies import Global_policiesArgs
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.config.global_policies.global_policies import Global_policies


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Global_policiesArgs.argument_spec,
                           supports_check_mode=True)

    result = Global_policies(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
