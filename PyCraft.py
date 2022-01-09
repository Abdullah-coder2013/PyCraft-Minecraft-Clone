from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
import random
import sys

app = Ursina()
grass_texture = load_texture('assets/grass_block.jpg')
stone_texture = load_texture('assets/stone_block.jpg')
brick_texture = load_texture('assets/brick.jpg')
dirt_texture  = load_texture('assets/dirt_block.jpg')
sky_texture   = load_texture('assets/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')
sand_texture = load_texture('assets/sand.jpg')
gravel_texture = load_texture('assets/gravel.jpg')
obsidian_texture = load_texture('assets/obsidian.jpg')
snow_texture = load_texture('assets/snow_block.jpg')
wood_texture = load_texture('assets/woodblock.jpg')
plank_texture = load_texture('assets/woodplanks.jpg')
water_texture = load_texture('assets/water.jpg')
lava_texture = load_texture('assets/lava.jpg')
table_texture = load_texture('block images/planks.png')
sofa_texture = load_texture('block images/sofa.png')
punch_sound   = Audio('assets/punch_sound',loop = False, autoplay = False)
block_pick = 1

window.fps_counter.enabled = False
window.exit_button.visible = True
window.fullscreen = True

def update():
	global block_pick

	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()
	else:
		hand.passive()

	if held_keys['1']: block_pick = 1
	if held_keys['2']: block_pick = 2
	if held_keys['3']: block_pick = 3
	if held_keys['4']: block_pick = 4
	if held_keys['5']: block_pick = 5
	if held_keys['6']: block_pick = 6
	if held_keys['7']: block_pick = 7
	if held_keys['8']: block_pick = 8
	if held_keys['9']: block_pick = 9
	if held_keys['0']: block_pick = 10
	if held_keys['k']: block_pick = 11
	if held_keys['l']: block_pick = 12
	if held_keys['t']: block_pick = 13
	if held_keys['y']: block_pick = 14
	if held_keys['escape']: sys.exit()

class Table(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
		parent = scene,
		model = 'assets/table',
		position = position,
		origin_y = 0.75,
		color = color.color(0,0,random.uniform(0.9,1)),
		texture = table_texture
		)
	def input(self, key):
		if self.hovered and key == 'left mouse down':
			punch_sound.play()
			destroy(self)

class Sofa(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
		parent = scene,
		model = 'assets/sofa',
		position = position,
		origin_y = 0.75,
		color = color.color(0,0,random.uniform(0.9,1)),
		texture = sofa_texture
		)
	def input(self, key):
		if self.hovered and key == 'left mouse down':
			punch_sound.play()
			destroy(self)

class Voxel(Button):
	def __init__(self, position = (0,0,0), texture = grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)

	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				punch_sound.play()
				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
				if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
				if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
				if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
				if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = sand_texture)
				if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = obsidian_texture)
				if block_pick == 7: voxel = Voxel(position = self.position + mouse.normal, texture = snow_texture)
				if block_pick == 8: voxel = Voxel(position = self.position + mouse.normal, texture = gravel_texture)
				if block_pick == 9: voxel = Voxel(position = self.position + mouse.normal, texture = wood_texture)
				if block_pick == 10: voxel = Voxel(position = self.position + mouse.normal, texture = plank_texture)
				if block_pick == 11: voxel = Voxel(position = self.position + mouse.normal, texture = water_texture)
				if block_pick == 12: voxel = Voxel(position = self.position + mouse.normal, texture = lava_texture)
				if block_pick == 13: table = Table(position = self.position + mouse.normal)
				if block_pick == 14: sofa = Sofa(position = self.position + mouse.normal)

			if key == 'left mouse down':
				punch_sound.play()
				destroy(self)

class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)



noise = PerlinNoise(octaves=3,seed=random.randint(1,1000000))

for z in range(-40,40):
	for x in range(-40,40):
	    y = noise([x * .02,z * .02])
	    y = math.floor(y * 7.5)
	    voxel = Voxel(position=(x,y,z))


player = FirstPersonController()
player.gravity = 0.3
sky = Sky()
hand = Hand()

app.run()
