#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

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
