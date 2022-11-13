from subprocess import CalledProcessError, check_output

class System:
    def __init__(self):
        try:
            output = check_output(["xrandr", "--verbose"])
        except (CalledProcessError, FileNotFoundError) as err:
            raise RuntimeError(
                "Error retrieving xrandr util data: {}".format(err)
            ) from None

        self.screens = []
        lines = output.splitlines()
        for i, line in enumerate(lines):
            line = line.decode().strip()
            if line.startswith("EDID:"):
                j = i + 1
                selection = ""
                # line has some sort of indentation
                while lines[j].decode()[0:2].isspace():
                    selection += lines[j].decode().strip()
                    j+=1
                i = j
                self.screens.append(Screen(selection))


    def get_screen(self, screenNumber):
        return self.screens[screenNumber]

class Screen:
    def __init__(self, edid):
        self.edid = edid


