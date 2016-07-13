import random

class loadscreenGlobals:

	def __init__(self):
		self.StartLoad = ['phase_2/maps/loadingscreen_enterGame.jpg', 'phase_2/maps/loadingscreen_exitGame.jpg']
		self.Tutorial = ['phase_2/maps/loadingscreen_tutorial_aiming.jpg',
							'phase_2/maps/loadingscreen_tutorial_tab.jpg',
							'phase_2/maps/loadingscreen_tutorial_timing.jpg',
							'phase_2/maps/loadingscreen_tutorial_walk.jpg',
							'phase_2/maps/loadingscreen_tutorial_weapon.jpg']
		self.GlobalJail = 'phase_2/maps/loadingscreen_jail.jpg'
		self.PortRoyal = []

	def getLoadImage(self, sceneID):
		self.sceneID = sceneID
		if self.sceneID == 1:
			self.LoadImage = random.choice(self.StartLoad)
		elif self.sceneID == 2:
			self.LoadImage = random.choice(self.Tutorial)
		elif self.sceneID == 3:
			self.LoadImage = self.GlobalJail
		elif self.sceneID == 4:
			self.LoadImage = random.choice(self.PortRoyal)
		return self.LoadImage