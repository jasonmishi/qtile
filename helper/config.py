import os
import tomllib

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "../config.toml"
config_path = os.path.join(script_dir, rel_path)


class Config:
    def __init__(self, path=config_path):
        with open(path, mode="rb") as fp:
            self._config = tomllib.load(fp)
        screenConfig = self._config.get("screens", None)
        if screenConfig and screenConfig.get("edids", False):
            self.__clean_edids()
            self.validate_edids()

    def __clean_edids(self):
        screenEdids = self._config["screens"]["edids"]
        screenEdids.update((k, "".join(v.split())) for k, v in screenEdids.items())

    def validate_edids(self):
        screenEdids = self._config["screens"]["edids"]
        # duplicate EDIDS
        if len(screenEdids.values()) != len(set(screenEdids.values())):
            raise ConfigError("Duplicate screen EDIDS")

    @classmethod
    def from_file(cls, file_path):
        return cls(file_path)

    def get(self, key):
        return self._config.get(key, None)


class ConfigError(Exception):
    pass
