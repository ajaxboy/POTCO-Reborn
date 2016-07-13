class worldGlobals:

	def __init__(self, sceneID, action):
		self.sceneID = sceneID
		self.action = action
		if self.sceneID == 1:
			self.AvatarIsland(self.action)
		elif self.sceneID == 2:
			self.TutorialJail(self.action)
		elif self.sceneID == 3:
			self.RambleShackIsland(self.action)
		elif self.sceneID == 4:
			self.PortRoyal(self.action)

	def AvatarIsland(self, action):
		from pirates.world.worlds.AvatarIsland import AvatarIsland
		if self.action == 0:
			self.avatarIsland = AvatarIsland()
		elif self.action == 1:
			self.avatarIsland.destroy()

	def TutorialJail(self, action):
		from pirates.world.worlds.TutorialJail import TutorialJail
		if self.action == 0:
			self.tutorialJail = TutorialJail()
		elif self.action == 1:
			self.tutorialJail.destroy()

	def RambleShackIsland(self, action):
		from pirates.world.worlds.RambleShackIsland import RambleShackIsland
		if self.action == 0:
			self.rambleshackIsland = RambleShackIsland()
		elif self.action == 1:
			self.rambleshackIsland.destroy()

	def PortRoyal(self, action):
		from pirates.world.worlds.PortRoyal import PortRoyal
		if self.action == 0:
			self.portRoyal = PortRoyal()
		elif self.action == 1:
			self.portRoyal.destroy()