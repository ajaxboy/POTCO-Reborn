import argparse, os

from panda3d.core import loadPrcFile
loadPrcFile("config/Config.prc")

import direct.directbase.DirectStart

StartArgs = argparse.ArgumentParser()
# Game server is optional for now
StartArgs.add_argument("--game_server", help="Game Server IP (Optional)")
StartArgs.add_argument("login_cookie", help="Players Login Cookie (Username)", type=str)
args = StartArgs.parse_args()

# Check player exists
# This is done on the client for now - in the future it will be done on the server
from pirates.data.loadData import loadData
LoadAccount = loadData(args.login_cookie)

# Start Avatar Chooser - Call Networking in future
from pirates.piratesbase.AvatarChooser import AvatarChooser
AvatarChooser = AvatarChooser()

run()