#!/usr/bin/python

import os

env1 = dict(os.environ)
env1 = env1.copy()

import time
import sys

for line in sys.stdin:
    print(line)

from ansible.module_utils.basic import AnsibleModule

import ansible.module_utils.basic as basic

import sys
import json
import glob

args = sys.argv[:]
env2 = dict(os.environ)
env2 = env2.copy()


def run_module():
    module_args = dict(
        name=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        original_message='',
        message='',
        my_useful_info={},
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result['original_message'] = module.params['name']
    result['message'] = 'goodbye'
    result['my_useful_info'] = {
        'foo': 'bar',
        'answer': 42,
    }
    result['params'] = dict(module.params)
    result['args'] = args
    result['env1'] = env1
    result['env2'] = env2
    result['env3'] = dict(os.environ)
    #result['MODULE_COMPLEX_ARGS'] = basic.MODULE_COMPLEX_ARGS
    module.exit_json(**result)


def main():
    run_module()

if __name__ == '__main__':
    main()
