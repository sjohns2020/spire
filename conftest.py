import pytest
import json

@pytest.fixture
def supply_AA_BB_CC():
    """Sample fixture"""
    aa=25
    bb =35
    cc=45
    return [aa,bb,cc]


@pytest.fixture(scope='session')
def telemetry_limits():
    """Loads a JSON file containing acceptance criteria and returns values dictionary"""
    file_id = 'acceptance_limits.json'
    with open(file_id) as lf:
        limits_file = json.load(lf)
    return limits_file


@pytest.fixture(scope='session')
def qualification_limits():
    """Loads a JSON file containing qualification criteria and returns values dictionary"""
    file_id = 'qualification_limits.json'
    with open(file_id) as lf:
        limits_file = json.load(lf)
    return limits_file

@pytest.fixture(scope='session')
def hardware_limits():
    """Loads a JSON file containing qualification criteria and returns values dictionary"""
    file_id = 'hardware_limits.json'
    with open(file_id) as lf:
        limits_file = json.load(lf)
    return limits_file
