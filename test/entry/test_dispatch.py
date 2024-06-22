import pytest
from hbutils.testing import simulate_entry

from jlabutils.config.meta import __VERSION__
from jlabutils.entry import jlabutilscli


@pytest.mark.unittest
class TestEntryDispatch:
    def test_version(self):
        result = simulate_entry(jlabutilscli, ['jlabutils', '-v'])
        assert result.exitcode == 0
        assert __VERSION__ in result.stdout
