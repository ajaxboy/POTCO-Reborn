from pirates.loadscreen.loadscreen import loadscreen
LoadScreen = loadscreen("", 1)
from pirates.piratesgui.AvatarChooserGui import AvatarChooserGui
from pirates.world.worldCreator import worldCreator

class AvatarChooser:

	def __init__(self):
		print "Lol"
		CreateWorld = worldCreator()
		CreateWorld.renderScene(1)
		print "Lol"
		AvatarGui = AvatarChooserGui()
		AvatarGui.PlayGame()
		LoadScreen.destroy()