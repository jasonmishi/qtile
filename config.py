# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from typing import List  # noqa: F401

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# custom imports
import qtilehelper.screens as qhelper_screens
from helper.abstractions import System
from helper.config import Config

config = Config()
system = System(config)


@hook.subscribe.startup_once
def set_up_system():
    set_up_screens(system.screens)


def set_up_screens(screens):
    for screen in screens:
        if screen.setup_command:
            os.system(screen.setup_command)


@hook.subscribe.startup
def set_wallpaper():
    qhelper_screens.setWallpaper()


"""
#7339AB
#625AD8
#1F9CE4
#88F4FF

#ff00c1
#9600ff
#4900ff
#00b8ff
#00fff9
#00ff9f

#711c91
#ea00d9
#0abdc6
#133e7c
#091833
"""


# color pallet purple
body_dark = "#7339AB"
body_medium = "#483050"
body_light = "#918396"

# color pallet blue
bbody_dark = "#31394c"
bbody_medium = "#4c5784"
bbody_light = "#a1bded"

# color pallet keys
black = "#101012"
gray = "#7a797f"
light_gray = "#d8d9d5"

mod = "mod4"
terminal = "kitty"
# from libqtile.utils import guess_terminal
# terminal = guess_terminal()

screen = Screen(
    top=bar.Bar(
        [
            widget.CurrentLayout(foreground=light_gray),
            widget.GroupBox(),
            widget.Prompt(),
            widget.WindowName(),
            widget.Chord(
                chords_colors={
                    "launch": ("#ff0000", "#ffffff"),
                },
                name_transform=lambda name: name.upper(),
            ),
            widget.Systray(),
            widget.TextBox(text="\ue0be", fontsize=30, foreground="#625AD8", padding=0),
            widget.TextBox(
                text="\uf4bc ",
                font="FiraCode Nerd Font",
                fontsize=24,
                padding=4,
                background="#625AD8",
            ),
            widget.CPUGraph(background="#625AD8"),
            widget.TextBox(
                text="\ueb7f ",
                font="FiraCode Nerd Font",
                fontsize=24,
                padding=4,
                background="#625AD8",
            ),
            widget.MemoryGraph(background="#625AD8"),
            widget.TextBox(
                text="\uf0a0 ",
                font="FiraCode Nerd Font",
                fontsize=24,
                padding=4,
                background="#625AD8",
            ),
            widget.HDDBusyGraph(background="#625AD8"),
            widget.TextBox(
                text="\ue0be",
                fontsize=30,
                foreground="#1f9ce4",
                background="#625AD8",
                padding=0,
            ),
            widget.Battery(background="#1f9ce4", fontsize="16", battery=0),
            widget.Battery(background="#1f9ce4", fontsize="16", battery=1),
            widget.TextBox(
                fmt="\ue0be",
                fontsize=30,
                foreground="#ff00c1",
                background="#1f9ce4",
                padding=0,
            ),
            widget.Clock(
                format="%Y-%m-%d %a  %H:%M",
                background="#ff00c1",
                font="Roboto Bold",
                fontsize="16",
            ),
        ],
        32,
        background=body_dark,
    )
)

screenNoSystray = Screen(
    top=bar.Bar(
        [
            widget.CurrentLayout(foreground=light_gray),
            widget.GroupBox(),
            widget.Prompt(),
            widget.WindowName(),
            widget.Chord(
                chords_colors={
                    "launch": ("#ff0000", "#ffffff"),
                },
                name_transform=lambda name: name.upper(),
            ),
            widget.Battery(battery=0),
            widget.Battery(battery=1),
            widget.Clock(format="%Y-%m-%d %a  %H:%M"),
        ],
        32,
        background=body_dark,
    ),
)
screens = [screen]

if qhelper_screens.getNumberOfConnectedScreens() == 2:
    screens.append(screenNoSystray)

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Focus different screens
    Key([mod], "o", lazy.to_screen(0), desc="switch to first screen"),
    Key([mod], "p", lazy.to_screen(1), desc="switch to second screen"),
    # toggle window between floating and not
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating"),
]

groups = [Group(i) for i in "1234"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    # layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(),
    layout.Floating(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Roboto",
    fontsize=12,
    padding=4,
)
extension_defaults = widget_defaults.copy()

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
