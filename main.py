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

#Offsetting camera
cameraOffset = 3.2375

#Binding animations to actor
Player = Actor("phase_2/models/char/mp_2000.bam",
											{"running-jump-idle":"phase_2/models/char/mp_jump.bam",
											"walk":"phase_2/models/char/mp_walk.bam",
											"turnLeft1":"phase_2/models/char/mp_spin_left.bam",
											"turnRight2":"phase_2/models/char/mp_spin_right.bam",
											"neutral":"phase_2/models/char/mp_idle_centered.bam",
											"run":"phase_2/models/char/mp_run.bam"})

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

#Initialzing the Tortuga base
tortugaBase = loader.loadModel('phase_5/models/islands/pir_m_are_isl_tortuga.bam')
#Initializing the Tortuga buildings
tortugaBuildings = loader.loadModel('phase_4/models/islands/pir_m_are_bui_tortuga.bam')

#Preloading Music
TortugaMusic_Main = base.loader.loadSfx("phase_2/audio/will_and_elizabeth.mp3")
TortugaMusic_Secondary = base.loader.loadSfx("phase_4/audio/music_ballad_of_a_buccaneer.mp3")
TortugaMusic_Third = base.loader.loadSfx("phase_4/audio/he_is_a_pirate.mp3")

#Setting up text node, setting the text, scaling the text, reparenting the text and assigning a font
text = TextNode('node name')
text.setText("Kyle")
textNodePath = aspect2d.attachNewNode(text)
textNodePath.setScale(.5)
textNodePath.reparentTo(Player)
textNodePath.setPos(-1.5, 0, 7.1)
Impress = loader.loadFont('phase_2/models/fonts/BriosoPro_chipped_outline.bam')
text.setTextColor(0.9, 0.3, 0.9, 1)
text.setCardColor(0.8, 0.8, 0.8, 0.001)
text.setCardAsMargin(.1, .2, .2, .1)
text.setCardDecal(True)

#Preloading, rendering and reparenting GM symbol to Player
GM = loader.loadModel("phase_2/models/gui/gmLogo_tflip.bam")
GM.reparentTo(Player)
GM.setScale(1)
GM.setPos(0, 0, 8.15)

#Preloading, rendering and reparenting Founder symbol to Player
founder = loader.loadModel("phase_2/models/gui/toplevel_gui_founder.bam")
founder.reparentTo(aspect2d)
switch = founder.find("**/+SwitchNode")
switch.node().setVisibleChild(70)
founder.reparentTo(Player)
founder.setScale(1.5)
founder.setPos(-1.75, 0, 7.25)

#Sand running walk preload
sandRun = loader.loadSfx('phase_2/audio/sfx_avatar_run_sandx2.mp3')

geom = Player.getGeomNode()
geom.getChild(0).setSx(1.0)
geom.getChild(0).setSy(1.0)
geom.getChild(0).setSz(1.0)
geom.getChild(0).setH(180)
 
base.camera.reparentTo(Player)
base.camera.setPos(0, -12.0 - cameraOffset, cameraOffset)
base.disableMouse()
wallBitmask = BitMask32(1)
floorBitmask = BitMask32(2)
base.cTrav = CollisionTraverser()

def getAirborneHeight():
    return cameraOffset + 0.025000000000000001

#Setting walk speed and collisions
walkControls = GravityWalker(legacyLifter=True)
walkControls.setWallBitMask(wallBitmask)
walkControls.setFloorBitMask(floorBitmask)
walkControls.setWalkSpeed(30.0, 30.0, 15.0, 80.0)
walkControls.initializeCollisions(base.cTrav, Player, floorOffset=0.025, reach=4.0)
walkControls.setAirborneHeightFunc(getAirborneHeight)
walkControls.enableAvatarControls()
Player.physControls = walkControls
 
def setWatchKey(key, input, keyMapName):
    def watchKey(active=True):
        if active == True:
            inputState.set(input, True)
            keyMap[keyMapName] = 1
        else:
            inputState.set(input, False)
            keyMap[keyMapName] = 0
    base.accept(key, watchKey, [True])
    base.accept(key+'-up', watchKey, [False])

#Setting up the Key Map	
keyMap = {'left':0, 'right':0, 'forward':0, 'backward':0, 'space':0}

#Setting Watch Keys
setWatchKey('w', 'forward', 'forward')
setWatchKey('s', 'reverse', 'backward')
setWatchKey('a', 'turnLeft', 'left')
setWatchKey('d', 'turnRight', 'right')
setWatchKey('space', 'jump', 'space')

movingNeutral, movingForward = (False, False)
movingRotation, movingBackward = (False, False)
movingJumping = False

#Changing variables depending on input
def setMovementAnimation(loopName, playRate=1.0):
    global movingNeutral
    global movingForward
    global movingRotation
    global movingBackward
    global movingJumping
    if 'jump' in loopName:
        movingJumping = True
        movingForward = False
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    elif loopName == 'run':
        movingJumping = False
        movingForward = True
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    elif loopName == 'walk':
        movingJumping = False
        movingForward = False
        movingNeutral = False
        if playRate == -1.0:
            movingBackward = True
            movingRotation = False
    elif loopName == 'turnLeft1':
		movingJumping = False
		movingForward = False
		movingNeutral = False
		movingRotation = True
		movingBackward = False
    elif loopName == 'turnRight2':
		movingJumping = False
		movingForward = False
		movingNeutral = False
		movingRotation = True
		movingBackward = False
    elif loopName == 'neutral':
        movingJumping = False
        movingForward = False
        movingNeutral = True
        movingRotation = False
        movingBackward = False
    else:
        movingJumping = False
        movingForward = False
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    ActorInterval(Player, loopName, playRate=playRate).loop()
 

#Setting movement animation based on user input
def handleMovement(task):
	global movingNeutral, movingForward
	global movingRotation, movingBackward, movingJumping
	if keyMap['space'] == 1:
		if keyMap['forward'] or keyMap['backward'] or keyMap['left'] or keyMap['right']:
			if movingJumping == False:
				if Player.physControls.isAirborne:
					setMovementAnimation('running-jump-idle')
				else:
					if keyMap['forward']:
						if movingForward == False:
							setMovementAnimation('run')
					elif keyMap['backward']:
						if movingBackward == False:
							setMovementAnimation('walk', playRate=-1.0)
					elif keyMap['left']:
						if movingRotation == False:
							setMovementAnimation('turnLeft1', playRate=1.0)
					elif keyMap['right']:
						if movingRotation == False:
							setMovementAnimation('turnRight2', playRate=1.0)
			else:
				if not Player.physControls.isAirborne:
					if keyMap['forward']:
						if movingForward == False:
							setMovementAnimation('run')
					elif keyMap['backward']:
						if movingBackward == False:
							setMovementAnimation('walk', playRate=-1.0)
					elif keyMap['left']:
						if movingRotation == False:
							setMovementAnimation('turnLeft1', playRate=1.0)
					elif keyMap['right']:
						if movingRotation == False:
							setMovementAnimation('turnRight2', playRate=1.0)
		else:
			if movingJumping == False:
				if Player.physControls.isAirborne:
					setMovementAnimation('running-jump-idle')
				else:
					if movingNeutral == False:
						setMovementAnimation('neutral')
			else:
				if not Player.physControls.isAirborne:
					if movingNeutral == False:
						setMovementAnimation('neutral')
	elif keyMap['forward'] == 1:
		if movingForward == False:
			if not Player.physControls.isAirborne:
				setMovementAnimation('run')
				sandRun.setLoop(True)
				sandRun.play()
				sandRun.setVolume(0.125)
				
	elif keyMap['backward'] == 1:
		if movingBackward == False:
			if not Player.physControls.isAirborne:
				setMovementAnimation('walk', playRate=-1.0)
	elif keyMap['left']: 
		if movingRotation == False:
			if not Player.physControls.isAirborne:
				setMovementAnimation('turnLeft1', playRate=1.0)
	elif keyMap['right']:
		if movingRotation == False:
			if not Player.physControls.isAirborne:
				setMovementAnimation('turnRight2', playRate=1.0)
	else:
		if not Player.physControls.isAirborne:
			if movingNeutral == False:
				setMovementAnimation('neutral')
				sandRun.stop()
	return Task.cont

base.taskMgr.add(handleMovement, 'controlManager')

def RenderLoadingImage():
	global loadingImage
	global loadingImage1
	#Loading and rendering loading screen
	loadingImage1 = OnscreenImage(image = 'phase_2/maps/loadingscreen_tortuga.jpg', pos = (0, 20, .3), parent=render2d)
	loadingImage1.setScale(.7)
	loadingImage = loader.loadModel("phase_2/models/gui/loading_screen.bam")  
	loadingImage.reparentTo(aspect2d)      
	loadingImage.setPos(0, 0, 0.0)
	loadingImage.setScale(.21)
	base.graphicsEngine.renderFrame()
	base.graphicsEngine.renderFrame()
	baseSpawn()

def baseSpawn():
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
	HolidayCheck()
	#Once base is loaded un-render loading screen
	loadingImage1.removeNode()
	loadingImage.removeNode()
		
def HolidayCheck():
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
		
	
#Running EnvironmentRender functions
RenderLoadingImage()
#Final hiding and running
camera.hide()
base.oobe()
base.run()