try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "../config.toml"
config_path = os.path.join(script_dir, rel_path)


class Config:
    def __init__(self):
        with open(config_path, mode="rb") as fp:
            self._config = tomllib.load(fp)
        screenConfig = self._config.get("screens", None)
        if screenConfig and screenConfig.get("edids", False):
            self.__clean_edids()

    def get(self, key):
        return self._config.get(key, None)

    def __clean_edids(self):
        screenEdids = self._config["screens"]["edids"]
        screenEdids.update((k, "".join(v.split())) for k, v in screenEdids.items())
