#!/usr/bin/python

import sys
import json
import time

class AnsibleModule(object):

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        stdin_input = sys.stdin.read()
        try:
            args = json.loads(stdin_input)
            if 'ANSIBLE_MODULE_ARGS' in args:
                self.params = args['ANSIBLE_MODULE_ARGS']
            else:
                self.params = dict()
        except Exception:
            pass
        if len(sys.argv) >= 2:
            with open(sys.argv[1]) as f:
                args = f.read()
                args = args.split(' ')
                args = [x.split('=') for x in args]
                args = [tuple(x) for x in args if len(x) == 2]
                args = dict(args)
                self.params = args

    def exit_json(self, **result):
        result['invocation'] = dict(module_args=self.params)
        print(json.dumps(result))


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
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
