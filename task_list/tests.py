import pytest


@pytest.fixture
def greeting():
    return 'Hello world!'


def test_say_hello(greeting):
    assert greeting == 'Hello world!'
