from pirates.world.worldGlobals import worldGlobals

class worldCreator:

	def __init__(self):
		self.sceneRendered = 0

	def renderScene(self, sceneID):
		self.sceneID = sceneID
		self.sceneRendered = 0
		if self.sceneRendered == 0:
			self.RenderScene = worldGlobals(self.sceneID, 0)
			self.sceneRendered = 1
		elif self.sceneRendered == 1:
			self.RenderScene = worldGlobals(self.sceneID, 1)
			self.sceneRendered = 0

	def renderOther(self):
		#Stub
		pass