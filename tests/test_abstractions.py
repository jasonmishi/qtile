from helper.abstractions import System
import string
import pytest


class TestScreen:

    def test_edid(self):
        screen = System()
        assert set(screen.get_screen(0).edid).issubset(string.hexdigits)
    

