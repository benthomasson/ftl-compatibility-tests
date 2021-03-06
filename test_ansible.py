

from subprocess import check_output

from pprint import pprint


def test_argtest():
    cmd = ['ansible', '-M', 'modules', '-m', 'argtest', '-i', 'inventory.yml', 'all']
    print(' '.join(cmd))
    output = check_output(cmd)
    pprint(output)
    #assert False


def test_argtestjson():
    cmd = ['ansible', '-M', 'modules', '-m', 'argtestjson', '-i', 'inventory.yml', 'all']
    print(' '.join(cmd))
    output = check_output(cmd)
    pprint(output)
    #assert False


def test_timetest():
    cmd = ['ansible', '-M', 'modules', '-m', 'timetest', '-i', 'inventory.yml', 'all']
    print(' '.join(cmd))
    output = check_output(cmd)
    pprint(output)
    #assert False


def test_my_test_info():
    cmd = ['ansible', '-M', 'modules', '-m', 'my_test_info', '-i', 'inventory.yml', '-a', 'name=foo', 'all']
    print(' '.join(cmd))
    output = check_output(cmd)
    pprint(output)
    #assert False


def test_new_style_module():
    cmd = ['ansible', '-M', 'modules', '-m', 'new_style_module', '-i', 'inventory.yml', '-a', 'name=foo', 'all']
    print(' '.join(cmd))
    output = check_output(cmd)
    pprint(output)


def test_binary():
    cmd = ['ansible', '-M', 'modules', '-m', 'helloworld', '-i', 'inventory.yml', '-a', 'name=foo', 'all']
    print(' '.join(cmd))
    output = check_output(cmd)
    pprint(output)
