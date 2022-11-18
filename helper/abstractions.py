from subprocess import CalledProcessError, check_output


class System:
    def __init__(self, config):
        try:
            output = check_output(["xrandr", "--verbose"])
        except (CalledProcessError, FileNotFoundError) as err:
            raise RuntimeError(f"Error retrieving xrandr util data: {err}") from None

        self.screens = []
        lines = output.splitlines()
        for i, line in enumerate(lines):
            line = line.decode().strip()
            if line.startswith("EDID:"):
                j = i + 1
                selection = ""
                # line has some sort of indentation in the start
                while lines[j].decode()[0:2].isspace():
                    selection += lines[j].decode().strip()
                    j += 1
                i = j
                self.screens.append(Screen(selection, config))

    def get_screen(self, screenNumber):
        return self.screens[screenNumber]


class Screen:
    def __init__(self, edid, config):
        self.edid = edid
        self.name = None
        self.setup_command = None
        self.config = config.get("screens")
        if self.config and self.config.get("edids", False):
            screenConfig = self.config.get("edids")
            screenNames = [k for k, v in screenConfig.items() if v == self.edid]
            if len(screenNames) > 0:
                self.name = str(screenNames[0])
        if self.name and self.config.get("setup-commands", False):
            self.setup_command = self.config.get("setup-commands").get(self.name, None)
