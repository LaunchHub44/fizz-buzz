import pytest
import main

def test_get369():
    assert main.get369(1) == '1'
    assert main.get369(3) == 'x'
    assert main.get369(13) == 'x'
    assert main.get369(32) == 'x'
    assert main.get369(33) == 'xx'
    assert main.get369(34) == 'x'
    assert main.get369(333) == 'xxx'
    assert main.get369(6666) == 'xxxx'

