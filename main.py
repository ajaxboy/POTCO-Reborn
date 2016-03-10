import time

import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from pandac.PandaModules import CardMaker
from pandac.PandaModules import NodePath
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject

from direct.task import Task
from direct.actor.Actor import Actor
from direct.showbase import DirectObject
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker

from panda3d.core import *

import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
import random

class plySetup:
	'Default player class setup'
	
	def __init__(self):
		global Player
		#Binding animations to actor
		Player = Actor("phase_2/models/char/mp_2000.bam",
			{"running-jump-idle":"phase_2/models/char/mp_jump.bam",
			"walk":"phase_2/models/char/mp_walk.bam",
			"turnLeft1":"phase_2/models/char/mp_spin_left.bam",
			"turnRight2":"phase_2/models/char/mp_spin_right.bam",
			"neutral":"phase_2/models/char/mp_idle_centered.bam",
			"run":"phase_2/models/char/mp_run.bam"})
		
		#Setting camera offset variable
		cameraOffset = 3.2375

		base.camera.reparentTo(Player)
		base.camera.setPos(0, -12.0 - cameraOffset, cameraOffset)
		base.disableMouse()
		
		#Hiding clothing layers
		Player.reparentTo(render)
		Player.findAllMatches("**/clothing_layer1*").hide() 
		Player.findAllMatches("**/clothing_layer2*").hide() 
		Player.findAllMatches("**/clothing_layer3*").hide() 
		Player.findAllMatches("**/hair*").hide()
		Player.findAllMatches("**/acc*").hide() 
		Player.findAllMatches("**/beard*").hide() 
		Player.findAllMatches("**/mustache*").hide() 
		Player.findAllMatches("**/gh_master_face*").hide()
		Player.findAllMatches("**/body_armpit*").hide()
		Player.findAllMatches("**/body_forearm*").hide()
		Player.findAllMatches("**/body_foot*").hide()
		Player.findAllMatches("**/body_shoulder*").hide()
		Player.findAllMatches("**/body_torso*").hide()
		Player.findAllMatches("**/body_waist*").hide()
		Player.findAllMatches("**/body_knee*").hide()
		Player.findAllMatches('**/body_belt').hide()
			
	def plyHideClothingLayer(self, layerID):
		layerID = layerID
		
		if layerID == 1:
			#Showing barbossa clothing layers
			Player.findAllMatches('**/clothing_layer1_hat_barbossa').show()
			Player.findAllMatches('**/clothing_layer1_hat_barbossa_feather').show()
			Player.findAllMatches('**/clothing_layer2_vest_long_closed_legs_front').show()
			Player.findAllMatches('**/clothing_layer2_vest_long_closed_torso_front').show()
			Player.findAllMatches('**/clothing_layer3_coat_long_torso').show()
			Player.findAllMatches('**/clothing_layer3_coat_long_legs').show()
			Player.findAllMatches('**/clothing_layer1_pant_tucked_base').show()
			Player.findAllMatches('**/clothing_layer2_belt_square').show()
			Player.findAllMatches('**/clothing_layer2_belt_buckle_square').show()
			Player.findAllMatches('**/clothing_layer1_shoe_boot_tall_left').show()
			Player.findAllMatches('**/clothing_layer1_shoe_boot_tall_right').show()
			Player.findAllMatches('**/').show()
			
		else:
			print "Error: A valid layerID was not recieved"
			
	def plySetNameRank(self, name, rank):
		#Setting up text node, setting the text, scaling the text, reparenting the text and assigning a font
		text = TextNode('node name')
		text.setText(name)
		textNodePath = aspect2d.attachNewNode(text)
		textNodePath.setScale(.5)
		textNodePath.reparentTo(Player)
		textNodePath.setPos(-1.5, 0, 7.1)
		Impress = loader.loadFont('phase_2/models/fonts/BriosoPro_chipped_outline.bam')
		text.setTextColor(0.9, 0.3, 0.9, 1)
		text.setCardColor(0.8, 0.8, 0.8, 0.001)
		text.setCardAsMargin(.1, .2, .2, .1)
		text.setCardDecal(True)
		#Preloading symbols
		GM = loader.loadModel("phase_2/models/gui/gmLogo_tflip.bam")
		founder = loader.loadModel("phase_2/models/gui/toplevel_gui_founder.bam")
		if rank == 3:
			GM.reparentTo(Player)
			GM.setScale(1)
			GM.setPos(0, 0, 8.15)
			
		elif rank == 2:
			founder.reparentTo(aspect2d)
			switch = founder.find("**/+SwitchNode")
			switch.node().setVisibleChild(70)
			founder.reparentTo(Player)
			founder.setScale(1.5)
			founder.setPos(-1.75, 0, 7.25)
			
		elif rank == 1:
			return
			
		else:
			print "Error: A valid RankID was not recieved"

class worldInitialize:

	def __init__(self):
		global TortugaMusic_Main
		global TortugaMusic_Secondary
		global TortugaMusic_Third
		global tortugaBase
		global tortugaBuildings
		self.LoadingImage(1)
		#Initialzing the Tortuga base
		tortugaBase = loader.loadModel('phase_5/models/islands/pir_m_are_isl_tortuga.bam')
		#Initializing the Tortuga buildings
		tortugaBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_tortuga.bam')
		
		#Preloading Music
		TortugaMusic_Main = base.loader.loadSfx("phase_2/audio/will_and_elizabeth.mp3")
		TortugaMusic_Secondary = base.loader.loadSfx("phase_4/audio/music_ballad_of_a_buccaneer.mp3")
		TortugaMusic_Third = base.loader.loadSfx("phase_4/audio/he_is_a_pirate.mp3")
		
		#Sand running walk preload
		sandRun = loader.loadSfx('phase_2/audio/sfx_avatar_run_sandx2.mp3')
		self.renderPortRoyal()
		
	def LoadingImage(self, State):
		global loadingImage
		global loadingImage1
		if State == 1:
			#Loading and rendering loading screen
			loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_tortuga.jpg', pos = (0, 20, .3), parent=render2d)
			loadingImage1.setScale(.7)
			loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
			loadingImage.reparentTo(aspect2d)      
			loadingImage.setPos(0, 0, 0.0)
			loadingImage.setScale(.21)
			base.graphicsEngine.renderFrame()
			base.graphicsEngine.renderFrame()
		elif State == 2:
			loadingImage1.removeNode()
			loadingImage.removeNode()
		
	def renderPortRoyal(self):
		#Playing one of 3 random songs
		scenemusic = random.randint(1,3)
		if(scenemusic == 1):
			TortugaMusic_Main.setVolume(0.20)
			TortugaMusic_Main.setLoopCount(0)
			TortugaMusic_Main.play()
		elif(scenemusic == 2):
			TortugaMusic_Secondary.setVolume(0.20)
			TortugaMusic_Secondary.setLoopCount(0)
			TortugaMusic_Secondary.play()
		elif(scenemusic == 3):
			TortugaMusic_Third.setVolume(0.20)
			TortugaMusic_Third.setLoopCount(0)
			TortugaMusic_Third.play()
		#Rendering Tortuga base
		tortugaBase.reparentTo(render)
		#Rendering Tortuga buildings
		tortugaBuildings.reparentTo(render)
		#Spawning player at pos
		Player.setY(-597.64)
		Player.setX(23.68)
		Player.setZ(4.21)
		Player.setH(368.84)
		self.HolidayCheck()
		
	def HolidayCheck(self):
		#Hiding holiday decorations if it's not a holiday
		if(time.strftime("%d/%m") == "25/12"):
			tortugaBuildings.findAllMatches("**/holiday").hide()
			tortugaBuildings.findAllMatches("**/extraData").hide()
			print("It's Christmas!")
		if(time.strftime("%d/%m") == "18/02"):
			tortugaBuildings.findAllMatches("**/extraData").hide()
			tortugaBuildings.findAllMatches("**/WinterFestival").hide()
			print("It's a test holiday!")
		else:
			print("It's not a holiday")
			tortugaBuildings.findAllMatches("**/holiday").hide()
			tortugaBuildings.findAllMatches("**/extraData").hide()
			tortugaBuildings.findAllMatches("**/WinterFestival").hide()
		self.LoadingImage(2)

def StartGame():
	def Rank():
		plyRank = raw_input("What's your rank?: ")
		if plyRank == "1":
			plyChar.plySetNameRank(plyName, 1)
			return
		if plyRank == "2":
			plyChar.plySetNameRank(plyName, 2)
			return
		if plyRank == "3":
			plyChar.plySetNameRank(plyName, 3)
			return
		else:
			print "You entered an incorrect value! Try again!"
			Rank()
	
	def ClothingPreset():
		plyClothes = raw_input("What clothing preset would you like?: ")
		if plyClothes == "1":
			plyChar.plyHideClothingLayer(1)
			return
		else:
			print "You entered an incorrect value! Try again!"
			ClothingPreset()

	#Setting defauly values
	print "Welcome to POTCO Reborn!"
	time.sleep(1)
	plyName = raw_input("What's your name?: ")
	time.sleep(1)
	print "That's a fine name,",plyName
	time.sleep(1)
	print "There are three ranks 1.Player, 2.Founder and 3.Game Master (Choose 1-3)"
	time.sleep(1)
	Rank()
	time.sleep(1)
	print "There is currently only one clothing preset, 1.Barbossa (Choose 1)"
	ClothingPreset()
	time.sleep(1)
	print "Enjoy your game!"
	#Starting game initializing
	World = worldInitialize()

plyChar = plySetup()
StartGame()
#Final hiding and running
camera.hide()
base.oobe()
base.run()
