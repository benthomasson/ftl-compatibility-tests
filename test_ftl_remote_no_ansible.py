

from faster_than_light import run_module, load_inventory
import pytest
from pprint import pprint


@pytest.mark.asyncio
async def test_argtest():
    result = await run_module(load_inventory('inventory3.yml'), ['modules'], 'argtest', module_args=dict(somekey='somevalue'))
    pprint(result)
    assert result is not None
    assert 'localhost' in result
    assert result['localhost']['args']
    assert result['localhost']['more_args'] == 'somekey=somevalue'
    assert result['localhost']['files']
    assert result['localhost']['executable']
    assert result['localhost']['env']


@pytest.mark.asyncio
async def test_argtestjson():
    result = await run_module(load_inventory('inventory3.yml'), ['modules'], 'argtestjson', module_args=dict(somekey='somevalue'))
    pprint(result)
    assert result is not None
    assert 'localhost' in result
    assert result['localhost']['args']
    assert result['localhost']['more_args'] == '{"somekey": "somevalue"}'
    assert result['localhost']['files']
    assert result['localhost']['executable']
    assert result['localhost']['env']


@pytest.mark.asyncio
async def test_timetest():
    result = await run_module(load_inventory('inventory3.yml'), ['modules'], 'timetest')
    assert result is not None
    assert 'localhost' in result
    assert 'time' in result['localhost']


@pytest.mark.asyncio
async def test_my_test_info():
    result = await run_module(load_inventory('inventory3.yml'), ['modules'], 'my_test_info', module_args=dict(name='foo'), dependencies=['ftl_module_utils'])
    assert result is not None
    assert 'localhost' in result
    assert 'original_message' in result['localhost']


@pytest.mark.asyncio
async def test_new_style_module():
    result = await run_module(load_inventory('inventory3.yml'), ['modules'], 'new_style_module', module_args=dict(name='foo'), dependencies=['ftl_module_utils'])
    assert result is not None
    assert 'localhost' in result
    assert 'original_message' in result['localhost']


@pytest.mark.asyncio
async def test_binary():
    result = await run_module(load_inventory('inventory3.yml'), ['modules'], 'helloworld', module_args=dict(name='foo'))
    assert result is not None
    assert 'localhost' in result
    assert 'msg' in result['localhost']
