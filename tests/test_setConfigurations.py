import os
from components import setConfigurations

def test_get_resources():
    """Check if configurations.ini is loaded properly."""
    config = setConfigurations.get_resources()
    # We expect certain sections to exist
    assert 'default_parameters' in config
    assert 'supported_formats' in config
    assert 'logs' in config

    # Check a known key
    assert 'max_width' in config['default_parameters']
