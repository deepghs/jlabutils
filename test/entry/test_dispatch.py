import pytest
from hbutils.testing import simulate_entry

from jutils.config.meta import __VERSION__
from jutils.entry import jutilscli


@pytest.mark.unittest
class TestEntryDispatch:
    def test_version(self):
        result = simulate_entry(jutilscli, ['jutils', '-v'])
        assert result.exitcode == 0
        assert __VERSION__ in result.stdout
