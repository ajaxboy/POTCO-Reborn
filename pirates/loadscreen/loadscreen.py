from pirates.loadscreen.loadscreenGlobals import loadscreenGlobals
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task

class loadscreen:

	def __init__(self, name, sceneID):
		self.name = name
		self.sceneID = sceneID

		self.LoadingImage = loadscreenGlobals()
		if sceneID != 1:
			# Location load screen
			self.BackGround = base.loader.loadModel("phase_2/models/gui/loading_screen.bam")
			self.BackGround.setPos(0, 0, 0.0)
			self.BackGround.setScale(.21)
		else:
			# Start load screen
			self.BackGround = base.loader.loadModel("phase_2/models/gui/loading_screen.bam")
			self.BackGround.find('**/title_bg').hide()
			self.BackGround.find('**/title_frame').hide()
			self.BackGround.setPos(0, 0, 0.0)
			self.BackGround.setScale(.21)
		
		self.LocationImage = OnscreenImage(image = self.LoadingImage.getLoadImage(self.sceneID), pos = (0, 0.1, 0.2), scale=(0.9,0.8,0.5), parent=aspect2d)
		self.BackGround.reparentTo(aspect2d)
		self.LoadingText = OnscreenText(text = self.name, pos = (0, -0.314), scale = 0.07, fg=(1, 0.90000000000000002, 0.69999999999999996, 1), shadow=(0, 0, 0, 1), font=loader.loadFont('phase_2/models/fonts/BriosoPro_chipped_outline.bam'))
		self.LoadingCircle = self.BackGround.find('**/red_wheel')
		taskMgr.add(self.tick, 'LoadCircleTask')
		
	def tick(self, task):
		self.LoadingCircle.setR(self.LoadingCircle, 3)
		return task.cont

	def destroy(self):
		taskMgr.remove('LoadCircleTask')
		self.LocationImage.destroy()
		self.BackGround.removeNode()
		self.LoadingText.destroy()