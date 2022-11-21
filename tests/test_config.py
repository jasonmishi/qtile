import pytest

from helper.config import Config, ConfigError


class TestScreen:
    def test_config_duplicate_edids(self):
        with pytest.raises(ConfigError, match="Duplicate screen EDIDS"):
            config = Config("duplicate_edids_config.toml")
