import string

from helper.abstractions import System
from helper.config import Config


class TestScreen:
    config = Config()

    def test_edid(self):
        system = System(self.config)
        screen = system.get_screen(1)
        assert set(screen.edid).issubset(string.hexdigits)
