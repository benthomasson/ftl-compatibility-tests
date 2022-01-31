

from faster_than_light import run_module, load_inventory
import pytest
from pprint import pprint


@pytest.mark.asyncio
async def test_argtest():
    result = await run_module(load_inventory('inventory.yml'), ['modules'], 'argtest')
    assert result is not None
    assert 'localhost' in result


@pytest.mark.asyncio
async def test_timetest():
    result = await run_module(load_inventory('inventory.yml'), ['modules'], 'timetest')
    assert result is not None
    assert 'localhost' in result
    assert 'time' in result['localhost']


@pytest.mark.asyncio
async def test_my_test_info():
    result = await run_module(load_inventory('inventory.yml'), ['modules'], 'my_test_info', module_args=dict(name='foo'))
    assert result is not None
    assert 'localhost' in result
    assert 'original_message' in result['localhost']
