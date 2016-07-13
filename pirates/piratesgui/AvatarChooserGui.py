from direct.gui.DirectGui import *

class AvatarChooserGui:

	def __init__(self):
		self.Click1 = base.loader.loadSfx("phase_2/audio/sfx_gui_click_08.mp3")
		self.Click2 = base.loader.loadSfx("phase_2/audio/sfx_gui_click_22.mp3")

		self.FrameModel = base.loader.loadModel("phase_2/models/gui/avatar_chooser_rope.bam")

		self.highlightFrame = DirectFrame(parent = base.a2dBottomCenter, relief = None,
										  image = self.FrameModel.find('**/avatar_c_B_frame'), image_scale = 0.37,
										  pos = (0, 0, 0.25), scale = 0.90000000000000002)
		#self.highlightFrame.hide()

		self.PlayButton = DirectButton(parent = self.highlightFrame, relief = None, text_scale = 0.050000000000000003,
									   text_fg = (1, 0.90000000000000002, 0.69999999999999996, 1),
									   text_shadow = (0, 0, 0, 1),
									   text_font=loader.loadFont('phase_2/models/fonts/BriosoPro_chipped_outline.bam'),
									   text = 'Play',
									   image = (self.FrameModel.find('**/avatar_c_B_bottom'),
									   		    self.FrameModel.find('**/avatar_c_B_bottom'),
									   			self.FrameModel.find('**/avatar_c_B_bottom_over')),
									   image_scale = 0.37, text_pos = (0, -0.014999999999999999), pos = (0, 0, -0.080000000000000002),
									   scale = 1.7,
									   rolloverSound=self.Click1, clickSound=self.Click2, command = self.PlayGame)

	def PlayGame(self):
		print "Playing Game"

	def destroy(self):
		pass