import pygame,random,time,pickle,copy,math,glob
pygame.mixer.pre_init(44100, -16, 2, 256)
pygame.mixer.init()
pygame.init()
pygame.mixer.set_num_channels(64)

display=pygame.display.set_mode((0,0))
width,height=display.get_rect()[2],display.get_rect()[3]
# width=1280
# height=720
# print(width,height)


screen=pygame.Surface((1536,864),pygame.SRCALPHA)
screenrect=pygame.Rect(-400,-100,2320,1080)
screenwidth=screen.get_width()
screenheight=screen.get_height()

vec=pygame.math.Vector2
scroll=[0,0]
win=False
wintime=False


# cloudx=400


sprite1=[pygame.image.load('charactersprites/red1.png').convert_alpha(),pygame.image.load('charactersprites/red2.png').convert_alpha()]
sprite1run=[pygame.image.load('charactersprites/redrun1.png').convert_alpha(),pygame.image.load('charactersprites/redrun2.png').convert_alpha()]
sprite1jump=pygame.image.load('charactersprites/redjump.png').convert_alpha()
sprite1squish=pygame.image.load('charactersprites/redsquish.png').convert_alpha()
sprite1score=pygame.image.load('charactersprites/redscore.png').convert_alpha()
sprite1hurt=pygame.image.load('charactersprites/redhurt.png').convert_alpha()
# sprite1=pygame.transform.scale(sprite1,(50,50))
# sprite1=pygame.transform.scale2x(sprite1)
sprite2=[pygame.image.load('charactersprites/green1.png').convert_alpha(),pygame.image.load('charactersprites/green2.png').convert_alpha()]
sprite2run=[pygame.image.load('charactersprites/greenrun1.png').convert_alpha(),pygame.image.load('charactersprites/greenrun2.png').convert_alpha()]
sprite2jump=pygame.image.load('charactersprites/greenjump.png').convert_alpha()
sprite2squish=pygame.image.load('charactersprites/greensquish.png').convert_alpha()
sprite2score=pygame.image.load('charactersprites/greenscore.png').convert_alpha()
sprite2hurt=pygame.image.load('charactersprites/greenhurt.png').convert_alpha()
# sprite2=pygame.transform.scale(sprite2,(50,50))

# hitframe=pygame.image.load('assets/hitframe.png').convert_alpha()
# hitframe=pygame.transform.scale(hitframe,(50,50))
# sprite2=pygame.transform.scale2x(sprite2)
background1=pygame.image.load('levelassets/FIRbackground1-export.png').convert()
background2=pygame.image.load('levelassets/FIRbackground2.png').convert()
background2.set_colorkey((0,0,0),pygame.RLEACCEL)
backgroundblur1=pygame.image.load('levelassets/backgroundblur1.png').convert_alpha()
backgroundblur2=pygame.image.load('levelassets/backgroundblur2.png').convert_alpha()
backgroundblur=pygame.image.load('levelassets/backgroundblur.png').convert_alpha()
fade=pygame.image.load('levelassets/fade.png').convert_alpha()
gooey=pygame.image.load('ui/gooey.png').convert_alpha()
gooey_glow=pygame.image.load('ui/gooey_glow.png').convert_alpha()
warfare=pygame.image.load('ui/warfare.png').convert_alpha()
warfare_glow=pygame.image.load('ui/warfare_glow.png').convert_alpha()
# background3=pygame.image.load('FIRbackground3.png').convert()
# background3.set_colorkey((0,0,0),pygame.RLEACCEL)

# clouds1=pygame.image.load('clouds1.png').convert_alpha()
# clouds2=pygame.image.load('clouds2.png').convert_alpha()

# background=background.convert_alpha()
# sf=pygame.image.load('sf.png').convert()
# background=pygame.transform.scale2x(background)
# background=pygame.transform.scale2x(background)
minigun_b=pygame.image.load('weaponsprites/minigun-b.png').convert_alpha()
minigun_b_glow=pygame.image.load('weaponsprites/minigun-b_glow.png').convert_alpha()
sniper_b_glow=pygame.image.load('weaponsprites/sniper-b_glow.png').convert_alpha()
minigun=pygame.image.load('weaponsprites/minigun.png').convert_alpha()
sniper=pygame.image.load('weaponsprites/sniper.png').convert_alpha()
# sniper=pygame.transform.scale(sniper,(126,30))
sniper=pygame.transform.scale2x(sniper)
rocket=[pygame.transform.smoothscale(pygame.image.load('weaponsprites/missile'+str(x)+'.png').convert_alpha(),(int(22*1.3),int(52*1.3))) for x in range(1,11)]
rocket_glow=pygame.image.load('weaponsprites/rocket_glow.png').convert_alpha()
bazooka=pygame.image.load('weaponsprites/bazooka.png').convert_alpha()
pistol_b=pygame.image.load('weaponsprites/pistol_b.png').convert_alpha()
deagle=pygame.image.load('weaponsprites/deagle.png').convert_alpha()
invertedpistol=pygame.image.load('weaponsprites/invertedpistol.png').convert_alpha()
blue_laser=pygame.image.load('weaponsprites/blue_laser.png').convert_alpha()
blue_laser_glow=pygame.image.load('weaponsprites/blue_laser_glow.png').convert_alpha()
lasergun=pygame.image.load('weaponsprites/lasergun.png').convert_alpha()
laser_beam=pygame.image.load('weaponsprites/laserbeam.png').convert_alpha()
laser_ball=pygame.image.load('weaponsprites/laserball.png').convert_alpha()
blaster=pygame.image.load('weaponsprites/blaster.png').convert_alpha()
flames=[pygame.image.load('weaponsprites/flame'+str(x)+'.png').convert_alpha() for x in range(1,12)]
flamethrower=pygame.image.load('weaponsprites/flamethrower.png').convert_alpha()
shotgun=pygame.image.load('weaponsprites/shotgun.png').convert_alpha()
explosion=[[pygame.image.load('weaponsprites/explosion'+str(x)+'.png').convert_alpha() for x in range(1,10)],[pygame.image.load('weaponsprites/explosion_a'+str(x)+'.png').convert_alpha() for x in range(1,10)]]
minigun_flashes=[[pygame.image.load('muzzleflashes/minigun_flash_a'+str(x)+'.png').convert_alpha() for x in range(1,6)],
					[pygame.image.load('muzzleflashes/minigun_flash_b'+str(x)+'.png').convert_alpha() for x in range(1,6)]]
shotgun_flashes=[[pygame.image.load('muzzleflashes/shotgun_flash_a'+str(x)+'.png').convert_alpha() for x in range(1,7)]]
pistol_flashes=[[pygame.image.load('muzzleflashes/pistol_flash_a'+str(x)+'.png').convert_alpha() for x in range(1,7)]]
inverted_pistol_flashes=[[pygame.image.load('muzzleflashes/inverted_pistol_flash_a'+str(x)+'.png').convert_alpha() for x in range(1,6)]]
sniper_flashes=[[pygame.image.load('muzzleflashes/sniper_flash_a'+str(x)+'.png').convert_alpha() for x in range(1,7)]]
# minigun_flashes=[[x,x.get_rect()] for x in minigun_flashes]
# flamethrower=pygame.transform.scale(flamethrower,(int(flamethrower.get_width()*0.8),int(flamethrower.get_height()*0.8)))
screenshake=False


play_button=pygame.image.load('ui/play_button.png').convert_alpha()
play_button_selected=pygame.image.load('ui/play_button_selected.png').convert_alpha()
play_button_pressed=pygame.image.load('ui/play_button_pressed.png').convert_alpha()
settings_button=pygame.image.load('ui/settings_button.png').convert_alpha()
settings_button_selected=pygame.image.load('ui/settings_button_selected.png').convert_alpha()
settings_button_pressed=pygame.image.load('ui/settings_button_pressed.png').convert_alpha()
continue_button=pygame.image.load('ui/continue_button.png').convert_alpha()
continue_button_selected=pygame.image.load('ui/continue_button_selected.png').convert_alpha()
continue_button_pressed=pygame.image.load('ui/continue_button_pressed.png').convert_alpha()
quit_button=pygame.image.load('ui/quit_button.png').convert_alpha()
quit_button_selected=pygame.image.load('ui/quit_button_selected.png').convert_alpha()
quit_button_pressed=pygame.image.load('ui/quit_button_pressed.png').convert_alpha()
particle_button_on=pygame.image.load('ui/particle_button_on.png').convert_alpha()
particle_button_off=pygame.image.load('ui/particle_button_off.png').convert_alpha()
trails_button_on=pygame.image.load('ui/trails_button_on.png').convert_alpha()
trails_button_off=pygame.image.load('ui/trails_button_off.png').convert_alpha()
video_button=pygame.image.load('ui/video_button.png').convert_alpha()
video_button_selected=pygame.image.load('ui/video_button_selected.png').convert_alpha()
video_button_pressed=pygame.image.load('ui/video_button_pressed.png').convert_alpha()
controls_button=pygame.image.load('ui/controls_button.png').convert_alpha()
controls_button_selected=pygame.image.load('ui/controls_button_selected.png').convert_alpha()
controls_button_pressed=pygame.image.load('ui/controls_button_pressed.png').convert_alpha()
controls_menu=pygame.image.load('ui/controls_menu.png').convert_alpha()
restart_button=pygame.image.load('ui/restart_button.png').convert_alpha()
restart_button_selected=pygame.image.load('ui/restart_button_selected.png').convert_alpha()
restart_button_pressed=pygame.image.load('ui/restart_button_pressed.png').convert_alpha()
escape_button=pygame.image.load('ui/escape_button.png').convert_alpha()
escape_button_selected=pygame.image.load('ui/escape_button_selected.png').convert_alpha()
escape_button_pressed=pygame.image.load('ui/escape_button_pressed.png').convert_alpha()
showdown_button=pygame.image.load('ui/showdown_button.png').convert_alpha()
showdown_button_selected=pygame.image.load('ui/showdown_button_selected.png').convert_alpha()
showdown_button_pressed=pygame.image.load('ui/showdown_button_pressed.png').convert_alpha()
deathmatch_button=pygame.image.load('ui/deathmatch_button.png').convert_alpha()
deathmatch_button_selected=pygame.image.load('ui/deathmatch_button_selected.png').convert_alpha()
deathmatch_button_pressed=pygame.image.load('ui/deathmatch_button_pressed.png').convert_alpha()

pink_scoreboard=pygame.image.load('ui/pink_scoreboard.png').convert_alpha()
green_scoreboard=pygame.image.load('ui/green_scoreboard.png').convert_alpha()

flamethrower_sounds=[pygame.mixer.Sound('sounds/flamethrower_start.wav'),pygame.mixer.Sound('sounds/flamethrower_spray.wav')]
flamethrower_sounds=[[x,x.get_length(),0] for x in flamethrower_sounds]
jumping_sounds=[pygame.mixer.Sound('sounds/landing1.wav'),pygame.mixer.Sound('sounds/landing2.wav')]
for k in jumping_sounds:
	k.set_volume(0.3)
landing_sounds=[pygame.mixer.Sound('sounds/landing3.wav'),pygame.mixer.Sound('sounds/landing3.wav'),pygame.mixer.Sound('sounds/landing3.wav')]
landing_sounds[0].set_volume(0.35)
landing_sounds[1].set_volume(0.2)
landing_sounds[2].set_volume(0.4)
shotgun_sound=pygame.mixer.Sound('sounds/sshotgun.wav')
shotgun_sound.set_volume(0.35)
minigun_sound=pygame.mixer.Sound('sounds/minigunnew.wav')
minigun_sound.set_volume(0.35)
pistol_sound=pygame.mixer.Sound('sounds/pistol.wav')
pistol_sound.set_volume(0.35)
laser_sound=[pygame.mixer.Sound('sounds/laser2.wav')]
sniper_sound=pygame.mixer.Sound('sounds/sniper.wav')
sniper_sound.set_volume(0.35)
swap_sound=pygame.mixer.Sound('sounds/swap.wav')

jumpchannel=pygame.mixer.Channel(63)
swapchannel=pygame.mixer.Channel(62)

particlecheck=True
trailcheck=True

font={}
for image in glob.glob('font/*.png'):
	font[str(image[5:-4])]=pygame.image.load(image).convert_alpha()
	
	# im=pygame.image.load('D:/LevelEditorAssets/'+image[21:]).convert_alpha()
# print(font)

class Asset():
	def __init__(self,image=False,name=False,ix=0,iy=0,state='UNDEFINED'):
		if image:
			self.image=image
			self.rect=image.get_rect()
			if iy:
				self.rect[1]=iy
			if ix:
				self.rect[0]=ix
			self.xpos=self.rect[0]
			self.ypos=self.rect[1]


		self.state=state
		
		if name:
			self.name=name
			self.ix=ix
			self.iy=iy
class Player:
	def __init__(self,xpos,ypos,idlesprites,runsprites,jumpsprite,squishsprite,scoresprite,hurtsprite,scoreboard,color,collision_map,controls='',weapon=False,weapon_sprite=False,face=False,\
					righthit=False,lefthit=False):

		self.idlesprites=idlesprites
		self.runsprites=runsprites
		self.jumpsprite=jumpsprite
		self.squishsprite=squishsprite
		self.scoresprite=scoresprite
		self.hurtsprites=[hurtsprite,self.idlesprites[0]]
		self.frame=0
		self.sprite=False
		self.rect=pygame.Rect(xpos,ypos,int(self.idlesprites[0].get_width()),(self.idlesprites[0].get_height()))
		self.collision_map=collision_map
		
		self.flip=False
		# self.sr=sprite
		# self.sl=pygame.transform.flip(sprite,True,False)
		self.xpos=xpos
		self.ypos=ypos
		self.acc=0
		self.jump=False
		self.fall=False
		self.jumpv=37
		self.fallv=0
		self.gravity=3
		self.dash=False
		self.coyote=0
		self.jumptime=0
		self.squishtime=0
		self.hurt_time=False
		self.hurtframe=0
		self.controls=controls
		self.wallhit=False
		self.stay=False

		self.weapon=weapon
		self.weapon_sprite=weapon_sprite
		self.weaponswaptime=0
		self.recoilangle=0
		self.face=face
		self.bullets=[]
		self.righthit=righthit
		self.lefthit=lefthit
		self.knockback=0
		self.reloadtimes={"ROCKETLAUNCHER":[1,0],"MINIGUN":[0.22,0],"PISTOL":[0.5,0],"SNIPER":[1.5,0],"SHOTGUN":[0.9,0]}
		self.recoil=[0,0]
		self.flame=False
		self.laser=False
		self.angle=0

		self.particles=[]
		self.alive=True
		self.alivetime=0
		self.state=False
		self.color=color
		self.score=0
		self.scoreboard=scoreboard
		self.name=False

	def update(self,auto=False,autoright=False,autoleft=False,autojump=False,autofire=False):
		global scrollcheck,weapons,avail_weapons,pause,screenshake,win,wintime
		# if weapons:
		# 	print(weapons)
		
		keys=pygame.key.get_pressed()
		self.xc,self.yc=0,0
		drift=False


		# self.rect.width=self.sprite.get_width()
		# self.rect.height=self.sprite.get_height()

		

		if self.lefthit:
			self.xc=self.knockback
			if not self.hurt_time:
				self.hurt_time=time.monotonic()

		elif self.righthit:
			self.xc=-self.knockback
			if not self.hurt_time:
				self.hurt_time=time.monotonic()

		else:
			if not pause:
				if keys[self.controls[1]] and not self.stay or autoright:
					if self.acc<0:
						drift=True
					self.acc+=1
					if self.acc>9:
						self.acc=9
					self.xc=self.acc+self.recoil[0]
					self.face="RIGHT"
					# self.sprite=self.sr
					self.flip=False
					scrollcheck=True
					
				elif keys[self.controls[0]] and not self.stay or autoleft:
					if self.acc>0:
						drift=True
					self.acc-=1
					if self.acc<-9:
						self.acc=-9
					self.xc=self.acc+self.recoil[0]
					self.face="LEFT"
					# self.sprite=self.sl
					self.flip=True
					scrollcheck=True

				else:
					self.xc=self.recoil[0]
				if keys[self.controls[2]] and not self.stay or autojump:
					scrollcheck=True
					if not self.jump and time.monotonic()-self.coyote<0.14:
						if not jumpchannel.get_busy():

							jumpchannel.play(random.choice(jumping_sounds))
						self.jumptime=time.monotonic()
						self.state="JUMP"
						self.jump=True
						self.jumpv=37
						self.squishtime=False
						self.weaponswaptime=0
				elif keys[self.controls[4]]:
					self.dash=True
					self.jumpv=0
					self.fall=True
					self.jump=False
					self.fallv+=8


					# print(weapons)

		if not self.xc:
			if self.stay:
				dec=0.3
			else:
				dec=1.4
			# self.sprite=self.idlesprites[0]

			if self.acc>0:
				self.acc-=dec
				if self.acc<0:
					self.acc=0
			elif self.acc<0:
				self.acc+=dec
				if self.acc>0:
					self.acc=0
			self.xc=self.acc

			

		self.fall=True

		self.yc+=self.recoil[1]

		if self.jump:
			self.yc-=self.jumpv/self.gravity
			self.jumpv-=2.8
			if self.jumpv<0:
				self.jumpv=0
				self.fall=True
				self.jump=False
			
		if self.fall and not self.jump and not pause:			
			self.yc+=self.fallv/self.gravity
			self.fallv+=2.8

			if self.recoil[1]>0:
				self.recoil[1]-=0.5
				if self.recoil[1]<0:
					self.recoil[1]=0
			elif self.recoil[1]<0:
				self.recoil[1]+=0.5
				if self.recoil[1]>0:
					self.recoil[1]=0




			# if self.fallv>35:
			# 	self.jumptime=time.monotonic()
			if self.xc:
				if self.fallv>25:
					if self.state!="JUMP":
						self.state="FALL"
					self.jumptime=time.monotonic()
			else:					
				if self.fallv>35:
					if self.state!="JUMP":
						self.state="FALL"
					self.jumptime=time.monotonic()
			if self.dash:
				if self.fallv>80:
					self.fallv=80
			else:
				
				if self.fallv>50:
					self.fallv=50

				# self.lefthit=False
				# self.righthit=False

		if self.xc:
			self.rect[0]+=self.xc
			# self.xc-=self.recoil

		if not auto:
			collisionlist=detect_collisions(self.rect,world,"rect")
		else:
			collisionlist=detect_collisions(self.rect,self.collision_map,"rect",defaultrect=True)


		for ob in collisionlist:
			if self.acc>7 or self.acc<-7:
				landing_sounds[2].play()

			self.acc=0
			if self.xc>0:
				self.rect.right=collisionlist[ob].left

				if particlecheck:
					self.particles.append(Particle(self.rect,'RIGHT',False,color=self.color))
				if trailcheck:
					for k in range(self.rect[1]+10,self.rect[1]+self.rect[3]-10,10):
						for o in world:
							if o.state in ('COLLIDER',"PLATFORM"):
								r=pygame.Rect(int(o.ix),int(o.iy),int(o.iw),int(o.ih))
								if r.collidepoint((self.rect[0]+self.rect[2],k)):
									self.particles.append(Trail(self.rect,False,k,"RIGHT",self.color))
				if self.knockback>0:
					self.knockback-=0.7
				elif self.knockback<0:
					self.knockback+=0.7


			elif self.xc<0:
				self.rect.left=collisionlist[ob].right
				if particlecheck:
					self.particles.append(Particle(self.rect,'LEFT',False,color=self.color))
				if trailcheck:
					for k in range(self.rect[1]+10,self.rect[1]+self.rect[3]-10,10):
						for o in world:
							if o.state in ('COLLIDER',"PLATFORM"):
								r=pygame.Rect(int(o.ix),int(o.iy),int(o.iw),int(o.ih))
								if r.collidepoint((self.rect[0]-1,k)):
									self.particles.append(Trail(self.rect,False,k,"LEFT",self.color))
				if self.knockback>0:
					self.knockback-=0.7
				elif self.knockback<0:
					self.knockback+=0.7


		self.rect[1]+=self.yc

		if self.rect[0]<-700 or self.rect[0]>2200 or self.rect[1]>screenheight+200:
			screenshake=("weapon",time.monotonic(),5)
			
			# if self.opp.score<4:
			# 	if win:
			# 		print("WINNNNNN")
			# 	if not win:
			self.opp.score+=1
			# else:
			# 	print("WONNNN")
			# 	win=self.opp
			# 	wintime=time.monotonic()
			self.alive=False
			self.deathtime=time.monotonic()
			self.knockback=0
			if self.rect[0]<-700:
				if not auto:
					for k in range(30):
						# t,side,color,radius,decay=0.008,rand=(2,7))
						self.particles.append(Blood(self.rect,"RIGHT",self.color,random.randrange(5,12),rand=(6,15)))
				else:
					for k in range(30):
						self.particles.append(Blood(self.rect,"RIGHT",self.color,random.randrange(5,12),rand=(6,15),collision_map=self.collision_map))
			elif self.rect[0]>2200:
				if not auto:
					for k in range(30):
						# t,side,color,radius,decay=0.008,rand=(2,7))
						self.particles.append(Blood(self.rect,"LEFT",self.color,random.randrange(5,12),rand=(6,15)))
				else:
					for k in range(30):
						self.particles.append(Blood(self.rect,"LEFT",self.color,random.randrange(5,12),rand=(6,15),collision_map=self.collision_map))
			elif self.rect[1]>screenheight+200:
				if not auto:
					for k in range(30):
						# t,side,color,radius,decay=0.008,rand=(2,7))
						self.particles.append(Blood(self.rect,"UP",self.color,random.randrange(5,12),rand=(3,9)))
				else:
					for k in range(30):
						self.particles.append(Blood(self.rect,"UP",self.color,random.randrange(5,12),rand=(3,9),collision_map=self.collision_map))
			# self.bullets=[]

		if not auto:
			collisionlist=detect_collisions(self.rect,world,"rect")
		else:
			collisionlist=detect_collisions(self.rect,self.collision_map,"rect",defaultrect=True)

		if self.dash:
			if self.state=="JUMP":
				if not self.opp.lefthit and not self.opp.righthit:
					if self.rect.colliderect(self.opp.rect):
						if self.rect.bottom>self.opp.rect.top:
							if self.rect.center[0]>self.opp.rect.center[0]:
								self.opp.righthit=True
							else:
								self.opp.lefthit=True
							self.opp.jump=True
							self.opp.jumpv=40
							self.opp.knockback=10
							self.opp.fallv=0

		for ob in collisionlist:

			if self.yc>0:
				if self.yc>13:
					drop=True
					
				else:
					drop=False

				self.rect.bottom=collisionlist[ob].top
				if drop:
					
					if particlecheck:
						if self.dash:
							for x in range(20):
								self.particles.append(Particle(self.rect,"BOTTOM",False,decay=0.15,rand=(1,4),color=self.color))
						else:
							for x in range(10):
								self.particles.append(Particle(self.rect,"BOTTOM",False,decay=0.2,rand=(2,3),color=self.color))
					if trailcheck:
						for k in range(self.rect[0]-5,self.rect[0]+self.rect[2]+5,10):
							for o in world:
								if o.state in ('COLLIDER',"PLATFORM"):
									r=pygame.Rect(int(o.ix),int(o.iy),int(o.iw),int(o.ih))
									if r.collidepoint((k,self.rect[1]+self.rect[3])):
										self.particles.append(Trail(self.rect,k,False,"BOTTOM",self.color,(8,13)))

				self.fallv=0
				self.jumpv=37
				self.jump=False
				self.coyote=time.monotonic()
				self.fall=False
				if self.state!="GROUNDED":
					if self.yc>10:						
						landing_sounds[0].play()
					else:
						landing_sounds[1].play()
				self.state="GROUNDED"
				if not self.weaponswaptime:
					self.weaponswaptime=time.monotonic()
				self.dash=False
				if not self.squishtime:
					if self.yc>13:
						self.squishtime=time.monotonic()

				self.righthit=False
				self.lefthit=False
				self.knockback=0

				if self.xc>4 or self.xc<-4:
					if particlecheck:
						for k in range(2):
							self.particles.append(Particle(self.rect,"BOTTOM",False,color=self.color))
					
						if drift:
							if self.xc>5.5:
								for k in range(12):
									self.particles.append(Particle(self.rect,'BOTTOM',rand=(2,4),decay=0.15,dx=[x for x in range(2,7,2)],color=self.color))
							else:
								for k in range(12):
									self.particles.append(Particle(self.rect,'BOTTOM',rand=(2,4),decay=0.15,dx=[x for x in range(-2,-7,-2)],color=self.color))
					if trailcheck:
						for k in range(self.rect[0]+10,self.rect[0]+self.rect[2]-10,10):
							if not auto:
								for o in world:
									if o.state in ('COLLIDER',"PLATFORM"):
										r=pygame.Rect(int(o.ix),int(o.iy),int(o.iw),int(o.ih))
										if r.collidepoint((k,self.rect[1]+self.rect[3])):
											self.particles.append(Trail(self.rect,k,False,"BOTTOM",self.color))
							else:
								for o in self.collision_map:
									if o.collidepoint((k,self.rect[1]+self.rect[3])):
										self.particles.append(Trail(self.rect,k,False,"BOTTOM",self.color))


			elif self.yc<0 and ob!='PLATFORM':
				self.rect.top=collisionlist[ob].bottom
				self.jumpv=0
				self.fall=True

				if particlecheck:
					self.particles.append(Particle(self.rect,"TOP",False))


				# self.righthit=False
				# self.lefthit=False

		if not auto:
			if self.recoil[0]>0:
				self.recoil[0]-=0.5
				if self.recoil[0]<0:
					self.recoil[0]=0
			elif self.recoil[0]<0:
				self.recoil[0]+=0.5
				if self.recoil[0]>0:
					self.recoil[0]=0

			if not self.weapon:
				for ob in weapons:
					if self.rect.center[0]>weapons[ob][1].center[0]-200 and self.rect.center[0]<weapons[ob][1].center[0]+200:
						name=ob
						if ob[-1]=='1':
							name=name[:len(name)-1]
						render_text(name,(weapons[ob][1].center[0]-scroll[0],weapons[ob][1][1]-10-scroll[1]),0.3)	
						if weapons[ob][1].colliderect(self.rect):
							self.weapon=ob
							self.weapon_sprite=weapons[ob][0]
							self.currentweapon=weapons[ob]
							# print(self.currentweapon)
				if self.weapon:
					swap_sound.play()
				# 	# print(weapons)
					weapons.pop(self.weapon)
					# del thisdict["model"]
			else:
				weaponswap=False
				for ob in weapons:
					if self.rect.center[0]>weapons[ob][1].center[0]-200 and self.rect.center[0]<weapons[ob][1].center[0]+200:
						name=ob
						if ob[-1]=='1':
							name=name[:len(name)-1]
						render_text(name,(weapons[ob][1].center[0]-scroll[0],weapons[ob][1][1]-10-scroll[1]),0.3)
						if weapons[ob][1].colliderect(self.rect):
							if self.state=="GROUNDED" and keys[self.controls[4]]:							
								if time.monotonic()-self.weaponswaptime>0.1:

									weaponswap=[self.weapon,self.weapon_sprite]

									self.weapon_sprite=weapons[ob][0]
									# weaponswap=[self.weapon,self.currentweapon]

									self.weapon=ob

									self.currentweapon=weapons[ob]
									
									# print(self.weapon in weapons)
							
				if self.weapon in weapons:
				# 	# print(weapons)
					weapons.pop(self.weapon)

				if weaponswap:
					# if not swapchannel.get_busy():
					# 	swapchannel.play(swap_sound)
					swap_sound.play()
					# while True:
					# 	x=random.randrange(-200,1900,350)+70
					# 	xlist=[weapons[ob][1].center[0] for ob in weapons]
					# 	if x in xlist:
					# 		continue					
					# 	break
							
					# weaponswap[1][1].center=(x,-300)
					# weapons[weaponswap[0]]=weaponswap[1]
					avail_weapons.append([weaponswap[0],weaponswap[1],False])

					# ["MINIGUN",minigun,False]
				# else:
				# 	weapons[self.weapon]=self.currentweapon

				
		if not pause:
			if keys[self.controls[3]] or autofire:
				if self.weapon in ("ROCKETLAUNCHER","ROCKETLAUNCHER1"):
					
					if time.monotonic()-self.reloadtimes["ROCKETLAUNCHER"][1]>self.reloadtimes["ROCKETLAUNCHER"][0]:
						if not screenshake:
							screenshake=("weapon",time.monotonic(),3)
						self.acc=0

						if self.face=="RIGHT":
							self.bullets.append(RocketLauncher(pygame.Rect(self.rect[0]+45+10,self.rect[1]-10,rocket[0].get_width(),rocket[0].get_height())))
						else:
							self.bullets.append(RocketLauncher(pygame.Rect(self.rect[0]-30,self.rect[1]-10,rocket[0].get_width(),rocket[0].get_height())))					

						if self.rect[0]>self.opp.rect[0]:
							angle=math.atan2(-( self.rect.center[1]-(self.opp.rect.center[1]) ),( self.rect.center[0]-(self.opp.rect.center[0]) ))
							self.recoilangle=math.degrees(angle)
							if self.xc or self.state in ("JUMP","FALL"):
								self.recoil=vec(9,0).rotate(self.recoilangle*-1)
								self.recoil[0]=12
							else:
								self.recoil=vec(9,0).rotate(self.recoilangle*-1)
								self.recoil[0]=8

						else:
							angle=math.atan2(-( self.opp.rect.center[1]-(self.rect.center[1]) ),( self.opp.rect.center[0]-(self.rect.center[0]) ))
							self.recoilangle=math.degrees(angle)
							if self.xc or self.state in ("JUMP","FALL"):
								self.recoil=vec(-9,0).rotate(self.recoilangle*-1)
								self.recoil[0]=-12
							else:
								self.recoil=vec(-9,0).rotate(self.recoilangle*-1)
								self.recoil[0]=-8

						self.reloadtimes["ROCKETLAUNCHER"][1]=time.monotonic()

				elif self.weapon in ("MINIGUN","MINIGUN1"):

					
					if time.monotonic()-self.reloadtimes["MINIGUN"][1]>self.reloadtimes["MINIGUN"][0]:
						# random.choice(minigun_sound).play()
						minigun_sound.play()
						flash=random.choice(minigun_flashes)
						# render_text('sabor',(self.rect.center[0]+110-scroll[0],self.rect.center[1]-13-scroll[1]))
						# (self,t,side,dx,decay=0.25,rand=(1,2),size=False,color=False)					
						if not screenshake:
							screenshake=("weapon",time.monotonic(),2)
						self.acc/=2.3
						ry=random.choice([x for x in range(0,10,2)])

						if self.face=="RIGHT":
							for k in range(5):
								self.particles.append(Particle(pygame.Rect(self.rect.center[0]+95,self.rect.center[1]+ry,3,3),"BOTTOM",dx=[x for x in range(-1,2,1)],decay=0.5,rand=(3,5),size=10,color=(194,167,55),smoke=True))
							self.particles.append(MuzzleFlash(minigun_flashes,self.rect.center[0]+100,self.rect.center[1]+15+ry))
							self.bullets.append(Minigun(pygame.Rect(self.rect.center[0]+110,self.rect.center[1]-13+ry,minigun_b.get_width(),minigun_b.get_height()),sprite=minigun_b,glow=minigun_b_glow,rand=(3,5),side="RIGHT"))
							# screen.blit(flash,flash.get_rect(left=self.rect.center[0]+100-scroll[0],centery=self.rect.center[1]+15-scroll[1]))
							if self.xc:
								self.recoil[0]=-7
							else:
								self.recoil[0]=-4
						else:
							self.particles.append(MuzzleFlash(minigun_flashes,self.rect.center[0]-100,self.rect.center[1]+15+ry,xflip=True))
							self.bullets.append(Minigun(pygame.Rect(self.rect.center[0]-110,self.rect.center[1]-13+ry,minigun_b.get_width(),minigun_b.get_height()),sprite=minigun_b,glow=minigun_b_glow,rand=(3,5),side="LEFT"))
							# screen.blit(pygame.transform.flip(flash,True,False),flash.get_rect(left=self.rect.center[0]-100-scroll[0]-flash.get_width(),centery=self.rect.center[1]+15-scroll[1]))
							if self.xc:
								self.recoil[0]=7
							else:
								self.recoil[0]=4

						self.reloadtimes["MINIGUN"][1]=time.monotonic()


				elif self.weapon in ('PISTOL','PISTOL1'):
					
					if time.monotonic()-self.reloadtimes["PISTOL"][1]>self.reloadtimes["PISTOL"][0]:
						if not screenshake:
							screenshake=("weapon",time.monotonic(),2)
						pistol_sound.play()
						self.acc/=3
						if self.face=="RIGHT":
							self.particles.append(MuzzleFlash(pistol_flashes,self.rect[0]+80,self.rect[1]+25))
							self.bullets.append(Minigun(pygame.Rect(self.rect[0]+80,self.rect[1]+15,pistol_b.get_width(),pistol_b.get_height()),sprite=pistol_b,rand=(1,3),side="RIGHT"))
							if self.state=="JUMP":
								self.recoil[0]=-9
							else:
								self.recoil[0]=-5
						else:
							self.particles.append(MuzzleFlash(pistol_flashes,self.rect[0]-25,self.rect[1]+25,xflip=True))
							self.bullets.append(Minigun(pygame.Rect(self.rect[0]-25,self.rect[1]+15,pistol_b.get_width(),pistol_b.get_height()),sprite=pistol_b,rand=(1,3),side="LEFT"))
							if self.state=="JUMP":
								self.recoil[0]=9
							else:
								self.recoil[0]=5

						self.reloadtimes["PISTOL"][1]=time.monotonic()

				elif self.weapon in ('SHOTGUN','SHOTGUN1'):
					
					
					if time.monotonic()-self.reloadtimes["SHOTGUN"][1]>self.reloadtimes["SHOTGUN"][0]:
						if not screenshake:
							screenshake=("weapon",time.monotonic(),3)
						shotgun_sound.play()
						self.acc=0
						if self.face=="RIGHT":
							self.particles.append(MuzzleFlash(shotgun_flashes,self.rect[0]+45+10+25,self.rect.center[1]+15))
							for k in range(4):
								self.bullets.append(Minigun(pygame.Rect(self.rect[0]+45+10+25+random.choice([-4,0,4]),self.rect[1]+15+k*2,pistol_b.get_width(),pistol_b.get_height()),sprite=pistol_b,glow=minigun_b_glow,rand=(2,13),side="RIGHT",gun="SHOTGUN"))
							if self.xc or self.state=="JUMP":
								self.recoil[0]=-12							
							else:
								self.recoil[0]=-8
						else:
							self.particles.append(MuzzleFlash(shotgun_flashes,self.rect[0]-30,self.rect.center[1]+15,xflip=True))
							for k in range(4):
								self.bullets.append(Minigun(pygame.Rect(self.rect[0]-30+random.choice([-4,0,4]),self.rect[1]+15+k*2,pistol_b.get_width(),pistol_b.get_height()),sprite=pistol_b,glow=minigun_b_glow,rand=(2,13),side="LEFT",gun="SHOTGUN"))
							if self.xc or self.state=="JUMP":
								self.recoil[0]=12
							else:
								self.recoil[0]=8

						self.reloadtimes["SHOTGUN"][1]=time.monotonic()


				elif self.weapon in ('BLASTER','BLASTER1'):
					
					if time.monotonic()-self.reloadtimes["PISTOL"][1]>self.reloadtimes["PISTOL"][0]:
						if not screenshake:
							screenshake=("weapon",time.monotonic(),2)
						random.choice(laser_sound).play()
						self.acc/=3
						if self.face=="RIGHT":
							self.bullets.append(Minigun(pygame.Rect(self.rect[0]+45+10-10,self.rect[1]+15,blue_laser.get_width(),blue_laser.get_height()),sprite=blue_laser,glow=blue_laser_glow,rand=(1,3),side="RIGHT"))
							if self.state=="JUMP":
								self.recoil[0]=-9
							else:
								self.recoil[0]=-5
						else:
							self.bullets.append(Minigun(pygame.Rect(self.rect[0]-30-10,self.rect[1]+15,blue_laser.get_width(),blue_laser.get_height()),sprite=blue_laser,glow=blue_laser_glow,rand=(1,3),side="LEFT"))
							if self.state=="JUMP":
								self.recoil[0]=9
							else:
								self.recoil[0]=5

						self.reloadtimes["PISTOL"][1]=time.monotonic()


				elif self.weapon in ("SNIPER","SNIPER1"):
					
					if time.monotonic()-self.reloadtimes["SNIPER"][1]>self.reloadtimes["SNIPER"][0]:
						if not screenshake:
							screenshake=("weapon",time.monotonic(),3)
						sniper_sound.play()
						self.acc=0

						
						if self.rect[0]>self.opp.rect[0]:
							angle=math.atan2(-( self.rect.center[1]-(self.opp.rect.center[1]) ),( self.rect.center[0]-(self.opp.rect.center[0]) ))
							self.recoilangle=math.degrees(angle)
							self.particles.append(MuzzleFlash(sniper_flashes,self.rect.center[0],self.rect.center[1],angle=[self.recoilangle-180]))
							if self.xc or self.state in ("JUMP","FALL"):
								self.recoil=vec(11,0).rotate(self.recoilangle*-1)
								# self.recoil[0]=12
							else:
								self.recoil=vec(11,0).rotate(self.recoilangle*-1)
								# self.recoil[0]=8

						else:
							angle=math.atan2(-( self.opp.rect.center[1]-(self.rect.center[1]) ),( self.opp.rect.center[0]-(self.rect.center[0]) ))
							self.recoilangle=math.degrees(angle)
							self.particles.append(MuzzleFlash(sniper_flashes,self.rect.center[0],self.rect.center[1],angle=[self.recoilangle]))
							if self.xc or self.state in ("JUMP","FALL"):
								self.recoil=vec(-11,0).rotate(self.recoilangle*-1)
								# self.recoil[0]=-12
							else:
								self.recoil=vec(-11,0).rotate(self.recoilangle*-1)
								# self.recoil[0]=-8

						# if self.face=="RIGHT":
						# 	self.bullets.append(Sniper(pygame.Rect(self.rect[0]+45+10,self.rect[1]-10,minigun_b.get_width(),minigun_b.get_height()),self.opp.rect,minigun_b))
						# else:
						# 	self.bullets.append(Sniper(pygame.Rect(self.rect[0]-30,self.rect[1]-10,minigun_b.get_width(),minigun_b.get_height()),self.opp.rect,minigun_b))
						self.bullets.append(Sniper(pygame.Rect(self.rect.center[0],self.rect.center[1],minigun_b.get_width(),minigun_b.get_height()),self.opp.rect,minigun_b))

						self.reloadtimes["SNIPER"][1]=time.monotonic()


				elif self.weapon in ("FLAMETHROWER","FLAMETHROWER1"):
					if not self.flame:
						# flamethrower_sounds[0][0].play()
						flamethrower_sounds[1][2]=time.monotonic()
						self.flame=True
					if self.flame:
						if time.monotonic()-flamethrower_sounds[1][2]>flamethrower_sounds[1][1]:
							# flamethrower_sounds[1][0].play()
							flamethrower_sounds[1][2]=time.monotonic()
					# self.acc=0
					
					if self.face=="RIGHT":
						for k in range(3):
							self.particles.append(Flame(self.rect[0]+132,self.rect.center[1]-12,self.face))
						if self.xc:
							self.recoil[0]=-2.3
						else:
							self.recoil[0]=-1.7
					else:
						for k in range(3):
							self.particles.append(Flame(self.rect[0]-96,self.rect.center[1]-12,self.face))
						if self.xc:
							self.recoil[0]=2.3
						else:
							self.recoil[0]=1.7


				elif self.weapon in ("LASER","LASER1"):
					if self.laser:
						self.stay=self.laser.update(self.rect,self.opp)
						if not screenshake and self.laser.charged:
							screenshake=("weapon",time.monotonic(),1)
						if time.monotonic()-self.laser.time>4:
							self.laser=False

					else:
						self.laser=Laser_Beam(self.rect,self.opp)

				elif self.weapon in ("INVERTEDPISTOL","INVERTEDPISTOL1"):
					if time.monotonic()-self.reloadtimes["PISTOL"][1]>self.reloadtimes["PISTOL"][0]:
						if self.rect[0]>self.opp.rect[0]:
							angle=math.atan2(-( self.rect.center[1]-(self.opp.rect.center[1]) ),( self.rect.center[0]-(self.opp.rect.center[0]) ))
							self.recoilangle=math.degrees(angle)

						else:
							angle=math.atan2(-( self.opp.rect.center[1]-(self.rect.center[1]) ),( self.opp.rect.center[0]-(self.rect.center[0]) ))
							self.recoilangle=math.degrees(angle)

						self.bullets.append(InvertedPistol(self.opp.rect,self))



						self.reloadtimes["PISTOL"][1]=time.monotonic()

			else:
				self.flame=False
				self.laser=False
				self.stay=False





		# if click:
		# 	if self.weapon=='ROCKETLAUNCHER':
		# 		self.bullets.append([rocket,pygame.Rect(self.rect[0]+10+45,self.rect[1]+10+45,rocket.get_width(),rocket.get_height()),time.monotonic(),time.monotonic(),self.face])
		# follow=self.opp[0]


		

	##############################################################################################################################################################################

			######## CHARACTER ANIMATION & DISPLAY ##########

		self.frame+=0.06
		if self.frame>2:
			self.frame=0

		if self.hurt_time:
			if time.monotonic()-self.hurt_time<0.01:
				if self.righthit or self.lefthit:
					self.state="HURT"
			else:
				self.hurt_time=False
				self.hurtframe=0

		if pause:
			self.sprite=self.idlesprites[0]
		elif self.state=="GROUNDED":
			self.offsety=0
			if self.squishtime and time.monotonic()-self.squishtime<0.16 and time.monotonic()-self.squishtime>0.02:
				self.sprite=self.squishsprite
				self.offsetx=4
			elif self.acc in (-9,9):
				self.sprite=self.runsprites[int(self.frame)]
				self.offsetx=0
			else:
				self.sprite=self.idlesprites[int(self.frame)]
				self.offsetx=0

		elif self.state=="HURT":
			self.hurtframe+=0.12
			self.sprite=self.hurtsprites[int(self.hurtframe)]
			# if int(self.hurtframe)%2==0:
			# 	self.sprite=self.idlesprites[0]
			# 	self.offsetx=0
			# else:
			# 	self.sprite=self.hurtsprite
			# 	self.offsetx=0


		else:
			if time.monotonic()-self.jumptime<0.2:
				self.sprite=self.jumpsprite
				self.offsety=0
			else:
				self.sprite=self.idlesprites[0]
				self.offsety=0
				self.offsetx=0

		screen.blit(pygame.transform.flip(self.sprite,self.flip,False),(self.rect[0]-self.offsetx-scroll[0],self.rect[1]-self.offsety-scroll[1]))
		render_text(self.name,(self.rect.center[0]-scroll[0],self.rect[1]-10-scroll[1]),0.5)

		######## WEAPON ANIMATION & DISPLAY #############

		if self.weapon_sprite:
			if self.weapon_sprite in (sniper,bazooka,lasergun,invertedpistol):

				if self.rect[0]>self.opp.rect[0]:
					self.new=pygame.transform.flip(self.weapon_sprite,True,False)

					angle=math.atan2(-( self.rect.center[1]-(self.opp.rect.center[1]) ),( self.rect.center[0]-(self.opp.rect.center[0]) ))
					self.angle=math.degrees(angle)
					if self.laser:
						self.angle=self.laser.Beam_Angle()-180
					self.new=pygame.transform.rotate(self.new,self.angle)

					screen.blit(self.new,(self.rect.center[0]-scroll[0]-self.new.get_width()//2,self.rect.center[1]-scroll[1]+5-self.new.get_height()//2))
					
				else:
					angle=math.atan2(-( self.opp.rect.center[1]-(self.rect.center[1]) ),( self.opp.rect.center[0]-(self.rect.center[0]) ))
					self.angle=math.degrees(angle)
					if self.laser:
						self.angle=self.laser.Beam_Angle()
				
					self.new=pygame.transform.rotate(self.weapon_sprite,self.angle)

					screen.blit(self.new,(self.rect.center[0]-scroll[0]-self.new.get_width()//2,self.rect.center[1]-scroll[1]+5-self.new.get_height()//2))

				

			else:
				if self.face=="RIGHT":
					screen.blit(self.weapon_sprite,(self.rect[0]+self.rect[2]-scroll[0]-self.weapon_sprite.get_width()//2,self.rect.center[1]-scroll[1]+10-self.weapon_sprite.get_height()//2))
				else:
					screen.blit(pygame.transform.flip(self.weapon_sprite,True,False),(self.rect[0]-scroll[0]-self.weapon_sprite.get_width()//2,self.rect.center[1]-scroll[1]+10-self.weapon_sprite.get_height()//2))
				
	##############################################################################################################################################################################
		
	def update_bullets(self):
		######## BULLET ANIMATION AND DISPLAY ##########

		if self.bullets:

			for bullet in self.bullets:
				bullet.update(self.opp)

			self.bullets=[b for b in self.bullets if b.alive]

	##############################################################################################################################################################################

	def update_particles(self):
		######## PARTICLE ANIMATION AND DISPLAY #########

		if self.particles:

			for part in self.particles:
				part.update(self.opp)
			self.particles=[p for p in self.particles if p.alive]






# play1copy=copy.deepcopy(play1)
# play2copy=copy.deepcopy(play2)

############################################################################################################################################
############################################################################################################################################

class RocketLauncher:
	def __init__(self,rect,sprite=rocket,glow=rocket_glow,mask=pygame.mask.from_surface(rocket[0])):

		self.sprite=sprite
		self.glow=glow
		self.mask=mask
		self.rect=rect
		self.pos=vec(self.rect.center)
		self.glow_rect=glow.get_rect(center=self.rect.center)
		self.vel = vec(0,0)
		self.acc = vec(0, 0)
		self.rand=(random.randint(4+4,6+4)*random.choice([0.1,-0.1]),random.randint(4+4,6+4)*random.choice([0.1,-0.1]))
		self.alive=True
		self.frame=0
		self.time=time.monotonic()

	def update(self,opp):
		global screenshake
		if not pause:
			self.target=((opp.rect.center - self.pos).normalize() * 9.5) + self.rand
			self.acc=(self.target - self.vel)
			if self.acc.length() > 0.4:
				self.acc.scale_to_length(0.4)

			self.vel += self.acc
			if self.vel.length() > 9.5:
				self.vel.scale_to_length(9.5)
			self.pos += self.vel

			self.rect.center = self.pos
			self.glow_rect = self.pos

			if self.rect[0]>2500 or self.rect[0]<-1000:
				self.alive=False

			angle=math.atan2(-(opp.rect[1]-self.rect[1]),(opp.rect[0]-self.rect[0]))

			angle=math.degrees(angle)-90

			# if time.monotonic()-self.time>0.2:
			# 	self.frame=random.randrange(len(self.sprite))
			# 	self.time=time.monotonic()
			self.frame+=0.15
			if self.frame>9:
				self.frame=0

			sprite=self.sprite[int(self.frame)]
			self.rot_sprite=pygame.transform.rotate(sprite,angle)
			self.rot_glow=pygame.transform.rotate(self.glow,angle)
			self.rect=self.rot_sprite.get_rect(center=self.pos)
			self.glow_rect=self.rot_glow.get_rect(center=self.pos)
			self.mask=pygame.mask.from_surface(self.rot_sprite)
			if self.rect.colliderect(opp.rect):
				if self.vel[0]>0:
					screenshake=("hit",time.monotonic())				
					opp.lefthit=True
					for x in range(30):
						opp.particles.append(Blood(opp.rect,'LEFT',opp.color))
					
				elif self.vel[0]<0:
					screenshake=("hit",time.monotonic())
					opp.righthit=True
					for x in range(30):
						opp.particles.append(Blood(opp.rect,'RIGHT',opp.color))
				
				opp.jump=True
				opp.jumpv=40
				opp.knockback=11
				opp.fallv=0

				self.alive=False
					

			elif detect_collisions(self.rect,world,'mask',self.mask):
				if self.vel[0]>0:
					for x in range(30):
						opp.particles.append(Particle(self.rect,'RIGHT',dx=[x for x in range(1,-8-2)],color=(194,167,55)))
					for x in range(4):
						opp.particles.append(Explosion((self.rect[0]+self.rect[2]+random.choice([x for x in range(-7,7,2)]),random.randrange(self.rect[1]+10,self.rect[1]+self.rect[3]-10)),True,size="ROCKETLAUNCHER"))
				elif self.vel[0]<0:
					for x in range(30):
						opp.particles.append(Particle(self.rect,'LEFT',dx=[x for x in range(-1,8,2)],color=(194,167,55)))
					for x in range(4):
						opp.particles.append(Explosion((self.rect[0]+random.choice([x for x in range(-7,7,2)]),random.randrange(self.rect[1]+10,self.rect[1]+self.rect[3]-10)),True,size="ROCKETLAUNCHER"))

				self.alive=False

		screen.blit(self.rot_glow,(self.glow_rect[0]-scroll[0],self.glow_rect[1]-scroll[1]))
		screen.blit(self.rot_sprite,(self.rect[0]-scroll[0],self.rect[1]-scroll[1]))

############################################################################################################################################
############################################################################################################################################

class Minigun:
	def __init__(self,rect,sprite,glow=False,side=False,rand=False,gun=False):

		self.pos=vec(rect.center)
		self.side=side
		self.rand=rand
		if side=='RIGHT':
			self.vel = vec(16, random.randint(rand[0],rand[1])*random.choice([-0.1,0.1]) )
		else:
			self.vel = vec(-16, random.randint(rand[0],rand[1])*random.choice([-0.1,0.1]) )
		self.angle=math.atan2(-( self.pos[1]-(self.pos[1]+self.vel[1]) ),( self.pos[0]-(self.pos[0]+self.vel[0]) ))
		self.angle=math.degrees(self.angle)-90-180
		self.sprite=pygame.transform.rotate(sprite,self.angle)
		if glow:
			self.glow=pygame.transform.rotate(glow,self.angle)
			self.glow_rect=self.glow.get_rect(center=self.pos)
		else:
			self.glow=False
			self.glow_rect=False
		self.rect=self.sprite.get_rect(center=self.pos)		
		# self.rect[1]+=random.randint(1,8)*random.choice([-1,1])
		self.mask=pygame.mask.from_surface(self.sprite)

		self.rand=(random.randint(4,6)*random.choice([0.1,-0.1]),random.randint(4,6)*random.choice([0.1,-0.1]))
		if gun=="SHOTGUN":
			self.blood=10
		else:
			self.blood=30
		self.alive=True

	def update(self,opp):
		global screenshake
		if not pause:
			self.pos += self.vel

			self.rect.center = self.pos
			if self.glow_rect:
				self.glow_rect.center = self.pos

			if self.rect[0]>2500 or self.rect[0]<-1000:
				self.alive=False

			if self.rect.colliderect(opp.rect):
				if self.vel[0]>0:
					opp.lefthit=True
					for x in range(self.blood):
						opp.particles.append(Blood(opp.rect,'LEFT',opp.color))
					screenshake=("hit",time.monotonic())
				elif self.vel[0]<0:
					opp.righthit=True
					for x in range(self.blood):
						opp.particles.append(Blood(opp.rect,'RIGHT',opp.color))
					screenshake=("hit",time.monotonic())
				opp.jump=True
				opp.jumpv=40
				opp.knockback=10
				opp.fallv=0

				self.alive=False

			elif detect_collisions(self.rect,world,'mask',self.mask):
				if self.vel[0]>0:
					for x in range(10):
						opp.particles.append(Particle(self.rect,'RIGHT',[x for x in range(-90,-100-2)],decay=0.2,color=(194,167,55)))
					opp.particles.append(Explosion((self.rect[0]+self.rect[2]+random.choice([x for x in range(-3,3)]),random.randrange(self.rect[1],self.rect[1]+self.rect[3])),size="MINIGUN"))
				elif self.vel[0]<0:
					for x in range(10):
						opp.particles.append(Particle(self.rect,'LEFT',[x for x in range(-1,6,2)],decay=0.2,color=(194,167,55)))
					opp.particles.append(Explosion((self.rect[0]+random.choice([x for x in range(-3,3)]),random.randrange(self.rect[1],self.rect[1]+self.rect[3])),size="MINIGUN"))

				self.alive=False

		if self.glow:
			screen.blit(self.glow,(self.glow_rect[0]-scroll[0],self.glow_rect[1]-scroll[1]))
		screen.blit(self.sprite,(self.rect[0]-scroll[0],self.rect[1]-scroll[1]))


############################################################################################################################################
############################################################################################################################################


class Sniper:
	def __init__(self,rect,target,sprite):
		self.rect=rect
		self.pos=vec(rect.center)
		self.target=vec(target.center)
		self.target[0]+=random.choice([-6,-4,4,6])
		self.target[1]+=random.choice([-6,-4,4,6])
		self.vel=(self.target-self.pos).normalize()*30
		# self.angle=self.pos.angle_to(self.target)-90

		self.angle=math.atan2(-(self.target[1]-self.rect[1]),(self.target[0]-self.rect[0]))

		self.angle=math.degrees(self.angle)-90
		self.sprite=pygame.transform.rotate(sprite,self.angle)
		self.glow=pygame.transform.rotate(sniper_b_glow,self.angle)
		self.rect=self.sprite.get_rect(center=self.pos)
		self.glow_rect=self.glow.get_rect(center=self.pos)
		self.mask=pygame.mask.from_surface(self.sprite)
		self.alive=True


	def update(self,opp):
		global screenshake
		if not pause:
			self.pos += self.vel

			self.rect.center = self.pos
			self.glow_rect.center = self.pos

			if self.rect[0]>2500 or self.rect[0]<-1000:
				self.alive=False

			if self.rect.colliderect(opp.rect):
				if self.vel[0]>0:
					opp.lefthit=True
					for x in range(30):
						opp.particles.append(Blood(opp.rect,'LEFT',opp.color))
					screenshake=("hit",time.monotonic())
				elif self.vel[0]<0:
					opp.righthit=True
					for x in range(30):
						opp.particles.append(Blood(opp.rect,'RIGHT',opp.color))
					screenshake=("hit",time.monotonic())
				opp.jump=True
				opp.jumpv=40
				opp.knockback=10
				opp.fallv=0

				self.alive=False

			elif detect_collisions(self.rect,world,'mask',self.mask):
				if self.vel[0]>0:
					for x in range(10):
						opp.particles.append(Particle(self.rect,'RIGHT',dx=[x for x in range(1,-6-2)],color=(194,167,55)))
					opp.particles.append(Explosion((self.rect[0]+self.rect[2]+random.choice([x for x in range(-3,3)]),random.randrange(self.rect[1],self.rect[1]+self.rect[3])),size="SNIPER"))
				elif self.vel[0]<0:
					for x in range(10):
						opp.particles.append(Particle(self.rect,'LEFT',dx=[x for x in range(-1,6,2)],color=(194,167,55)))
					opp.particles.append(Explosion((self.rect[0]+random.choice([x for x in range(-3,3)]),random.randrange(self.rect[1],self.rect[1]+self.rect[3])),size="SNIPER"))

				self.alive=False
		screen.blit(self.glow,(self.glow_rect[0]-scroll[0],self.glow_rect[1]-scroll[1]))
		screen.blit(self.sprite,(self.rect[0]-scroll[0],self.rect[1]-scroll[1]))


############################################################################################################################################
############################################################################################################################################


class InvertedPistol:
	def __init__(self,target,player):
		self.player=player
		self.rect=player.rect
		# self.pos=vec(rect.center)
		# self.target=vec(target.center)
		# self.target[0]+=random.choice([-6,-4,4,6])
		# self.target[1]+=random.choice([-6,-4,4,6])
		# self.vel=(self.target-self.pos).normalize()*20
		# self.angle=self.pos.angle_to(self.target)-90

		self.angle=math.atan2(-(target[1]-player.rect[1]),(target[0]-player.rect[0]))
		self.angle=math.degrees(self.angle)+random.choice([-6,-4,-2,2,4,6])

		self.pos=self.rect.center+vec(1600,0).rotate(self.angle*-1)
		# self.vel=vec(20,0).rotate(self.angle-180)
		self.vel=(self.rect.center-self.pos).normalize()*20

		self.sprite=pygame.transform.rotate(minigun_b,self.angle-90)
		self.glow=pygame.transform.rotate(minigun_b_glow,self.angle-90)
		self.rect=self.sprite.get_rect(center=self.pos)
		self.glow_rect=self.glow.get_rect(center=self.pos)
		self.mask=pygame.mask.from_surface(self.sprite)
		self.alive=True


	def update(self,opp):
		global screenshake
		if not pause:
			self.pos += self.vel

			self.rect.center = self.pos
			self.glow_rect.center = self.pos

			if self.rect[0]>3000 or self.rect[0]<-1500:
				self.alive=False

			if self.rect.colliderect(opp.rect):
				if self.vel[0]>0:
					opp.righthit=True
					for x in range(30):
						opp.particles.append(Blood(opp.rect,'RIGHT',opp.color))
					screenshake=("hit",time.monotonic())
				elif self.vel[0]<0:
					opp.lefthit=True
					for x in range(30):
						opp.particles.append(Blood(opp.rect,'LEFT',opp.color))
					screenshake=("hit",time.monotonic())
				opp.jump=True
				opp.jumpv=40
				opp.knockback=10
				opp.fallv=0

			elif self.rect.colliderect(self.player.rect):
				if self.player.rect[0]>opp.rect[0]:
					self.player.particles.append(MuzzleFlash(inverted_pistol_flashes,self.player.rect.center[0],self.player.rect.center[1],angle=[self.player.recoilangle-180]))
				else:
					self.player.particles.append(MuzzleFlash(inverted_pistol_flashes,self.player.rect.center[0],self.player.rect.center[1],angle=[self.player.recoilangle]))

				self.alive=False

		screen.blit(self.glow,(self.glow_rect[0]-scroll[0],self.glow_rect[1]-scroll[1]))
		screen.blit(self.sprite,(self.rect[0]-scroll[0],self.rect[1]-scroll[1]))


############################################################################################################################################
############################################################################################################################################

class Laser_Beam:
	def __init__(self,player,opp):
		self.player=player
		self.opp=opp
		self.angle=math.atan2(-(self.player[1]-self.opp.rect[1]),(self.player[0]-self.opp.rect[0]))
		self.angle=math.degrees(self.angle)*-1
		distance=math.sqrt((self.player[0]-self.opp.rect[0])*(self.player[0]-self.opp.rect[0]) + (self.player[1]-self.opp.rect[1])*(self.player[1]-self.opp.rect[1])    ) *0.1
		self.aim=vec(self.opp.rect.center)
		self.aim=random.choice([self.aim+vec(distance,0).rotate(self.angle+90),self.aim+vec(distance,0).rotate(self.angle-90)])
		self.laser=laser_beam
		self.ball=laser_ball
		self.rect=laser_beam.get_rect(center=player.center)
		self.ball_rect=laser_ball.get_rect()
		self.time=time.monotonic()
		self.width=[1,5]
		self.hit=False
		self.charged=False

	def update(self,player,opp):
		self.angle=math.atan2(-(self.aim[1]-player.center[1]),(self.aim[0]-player.center[0]))
		self.angle=math.degrees(self.angle)
		# print(self.angle)
		self.vel=opp.rect.center - self.aim
		if self.vel.length():
			# self.vel=self.vel.normalize()*3
			self.vel.scale_to_length(3)
		self.aim+=self.vel

		distance=vec(10,0)
		# nline=distance.rotate(self.angle*-1)
		# pygame.draw.line(screen,(255,0,0),(player.center[0]-scroll[0],player.center[1]-scroll[1]),(player.center[0]-scroll[0]+nline[0],player.center[1]-scroll[1]+nline[1]))
		while True:
			nline=distance.rotate(self.angle*-1)			
			
			# print(self.angle)
			if detect_collisions(((player.center+nline)[0],(player.center+nline)[1]),world,"point")\
				or not screenrect.collidepoint(((player.center+nline)[0],(player.center+nline)[1])):
				break
			if opp.rect.collidepoint(((player.center+nline)[0],(player.center+nline)[1])):
				self.hit=True
				break
			else:
				self.hit=False
			if distance[0]>1600:
				break

			distance[0]+=40



		if time.monotonic()-self.time>1.9:
			pygame.draw.line(screen,(3,172,244),(player.center[0]-scroll[0],player.center[1]-scroll[1]),(player.center[0]-scroll[0]+nline[0],player.center[1]-scroll[1]+nline[1]),width=int(self.width[1]))
			ball_copy=pygame.transform.scale(laser_ball,(int(self.width[1])*7,int(self.width[1])*7))
			
			screen.blit(ball_copy,ball_copy.get_rect(center=(player.center[0]-scroll[0]+nline[0],player.center[1]-scroll[1]+nline[1])))
			self.width[1]-=0.3
			if self.width[1]<0:
				self.width[1]=0
			stay=False
			self.charged=False
		elif time.monotonic()-self.time>0.8:
			newimage=pygame.Surface((distance[0]*2,60),pygame.SRCALPHA)
			newimage.blit(self.laser,(0,0),(1656-distance[0],0,distance[0]*2,60))
			# newimage.set_colorkey((0,0,0),pygame.RLEACCEL)
			sprite=pygame.transform.rotate(newimage,self.angle)
			copy=sprite.get_rect(center=player.center)
			rx=random.randrange(-2,3,2)
			ry=random.randrange(-2,3,2)
			copy[0]-=scroll[0]+rx
			copy[1]-=scroll[1]+ry

			screen.blit(sprite,copy)
			# pygame.draw.circle(screen,(3,172,244),(player.center[0]-scroll[0]+nline[0],player.center[1]-scroll[1]+nline[1]),30)
			self.ball_rect.center=(player.center[0]-scroll[0]+nline[0]-rx,player.center[1]-scroll[1]+nline[1]-ry)
			screen.blit(laser_ball,self.ball_rect)

			if self.hit:
				# if self.ball_rect.colliderect(opp.rect):
				if self.player.center[0]<self.opp.rect.center[0]:
					screenshake=("hit",time.monotonic())				
					opp.lefthit=True
					for x in range(10):
						opp.particles.append(Blood(opp.rect,'LEFT',opp.color,decay=0.1))
					
				elif self.player.center[0]>self.opp.rect.center[0]:
					screenshake=("hit",time.monotonic())
					opp.righthit=True
					for x in range(10):
						opp.particles.append(Blood(opp.rect,'RIGHT',opp.color,decay=0.1))
				
				opp.jump=True
				opp.jumpv=40
				opp.knockback=11
				opp.fallv=0

			stay=True
			self.charged=True
		
		else:
			pygame.draw.line(screen,(3,172,244),(player.center[0]-scroll[0],player.center[1]-scroll[1]),(player.center[0]-scroll[0]+nline[0],player.center[1]-scroll[1]+nline[1]),width=int(self.width[0]))
			ball_copy=pygame.transform.scale(laser_ball,(int(self.width[0])*7,int(self.width[0])*7))
			
			screen.blit(ball_copy,ball_copy.get_rect(center=(player.center[0]-scroll[0]+nline[0],player.center[1]-scroll[1]+nline[1])))
			self.width[0]+=0.2
			stay=False
			self.charged=False

		return stay

	def Beam_Angle(self):
		return self.angle





############################################################################################################################################
############################################################################################################################################

class Flame:
	def __init__(self,x,y,side):
		self.name="FLAME"
		if side=="RIGHT":
			self.side=1
		else:
			self.side=-1
		self.size=random.randint(5,6)
		self.rect=pygame.Rect(x,y,self.size,self.size)
		self.distance=0
		self.lifetime=random.choice([0.5,1,1.5,2])
		self.decay=time.monotonic()
		self.alive=True

	def update(self,opp):
		global screenshake
		hit=False
		if not pause:
			if self.distance>random.randint(75,250):
				x=random.choice([x for x in range(-1,1)])
				self.rect[0]+=x*self.side*-1
				self.distance+=x
				self.rect[1]+=random.choice([x for x in range(-8,8)])
			else:
				x=random.randint(8,9)
				self.rect[0]+=x*self.side
				self.distance+=x
				self.rect[1]+=random.choice([x for x in range(-5,5)])

			if self.distance<random.randint(25,50):
				if self.rect.colliderect(opp.rect):
					hit=True
				# self.color=random.choice([(250,247,155),(246,250,197)])
				self.color=random.choice(flames[0:3])
			elif self.distance<random.randint(90,190):
				if self.rect.colliderect(opp.rect):
					hit=True
				# self.color=random.choice([(250,155,30),(250,212,60)])
				self.color=random.choice(flames[3:7])
			elif self.distance<random.randint(210,240):
				# self.color=random.choice([(250,108,0),(250,56,8)])
				self.color=random.choice(flames[7:11])
			else:
				self.size=self.size-1
				# self.color=pygame.transform.scale(self.color,(self.size,self.size))

			if hit:
				if self.side==1:
					if not opp.lefthit:
						opp.lefthit=True
						opp.jump=True
						opp.jumpv=40
						opp.knockback=10
						opp.fallv=0					
						for x in range(30):
							opp.particles.append(Blood(opp.rect,'LEFT',opp.color))
						screenshake=("hit",time.monotonic())
				elif self.side==-1:
					if not opp.righthit:
						opp.righthit=True
						opp.jump=True
						opp.jumpv=40
						opp.knockback=10
						opp.fallv=0	
						for x in range(30):
							opp.particles.append(Blood(opp.rect,'RIGHT',opp.color))
						screenshake=("hit",time.monotonic())
				
			
			if self.size<=1:
				self.alive=False
			# self.rect.size=(int(self.size),int(self.size))
			self.color=pygame.transform.scale(self.color,(int(self.size)*4,int(self.size)*4))

		self.copy=self.rect.copy()
		self.copy[0]-=scroll[0]
		self.copy[1]-=scroll[1]

		# pygame.draw.rect(screen,self.color,self.copy)
		# self.color.set_colorkey((0,0,0),pygame.RLEACCEL)
		# screen.blit(self.color,self.copy)
		# self.color.set_colorkey((255,255,255))
		# surf.set_colorkey((0, 0, 0))
		screen.blit(self.color,self.copy,special_flags=pygame.BLEND_RGBA_ADD)



############################################################################################################################################
############################################################################################################################################


class Particle:
	def __init__(self,t,side,dx,decay=0.25,rand=(1,2),size=False,color=False,smoke=False):
		self.name="PARTICLE"
		if size:
			self.size=size
		else:
			self.size=random.randint(6,8)
		self.decay=decay
		if side=='BOTTOM':
			self.rect=pygame.Rect( random.randint(t[0]-1,t[0]+t[2]+1)-scroll[0] , random.randint(t[1]+t[3]-5, t[1]+t[3]-3)-scroll[1]   ,self.size,self.size)
			if dx:
				self.dx=dx
			else:
				self.dx=[x for x in range(-5,5,2)]

		elif side=="RIGHT":
			self.rect=pygame.Rect( random.randint(t[0]+t[2]-1,t[0]+t[2]+1)-scroll[0] , random.randint(t[1]-1, t[1]+t[3]+1)-scroll[1]   ,self.size,self.size)
			if dx:
				self.dx=dx
			else:
				self.dx=[x for x in range(-2,2,2)]

		elif side=='LEFT':
			self.rect=pygame.Rect( random.randint(t[0]-1,t[0]+1)-scroll[0] , random.randint(t[1]-1, t[1]+t[3]+1)-scroll[1]   ,self.size,self.size)
			if dx:
				self.dx=dx
			else:
				self.dx=[x for x in range(-2,3,2)]

		
		elif side=="TOP":
			self.rect=pygame.Rect( random.randint(t[0]-1,t[0]+t[2]+1)-scroll[0] , random.randint(t[1]-2, t[1]+1)-scroll[1]   ,self.size,self.size)
			if dx:
				self.dx=dx
			else:
				self.dx=[x for x in range(-5,5,2)]

		self.vel=random.randint(rand[0],rand[1])*-1
		
		
		self.color=[(255,255,255)]
		if color:
			self.color.append(color)
			self.color.append(color)
			self.color.append(color)
		self.color=random.choice(self.color)
		self.smoke=smoke
		self.alive=True

	def update(self,opp):
		if not pause:
		
			self.rect[1]+=self.vel
			self.rect[0]+=random.choice(self.dx)
			if self.smoke:
				self.vel=-1.001
			else:
				self.vel+=0.3
			self.size=self.size-self.decay
			if self.size<=1:
				self.alive=False
			self.rect.size=(int(self.size),int(self.size))

		pygame.draw.rect(screen,self.color,self.rect)

class Blood:
	def __init__(self,t,side,color,radius=False,decay=0.008,rand=(2,7),collision_map=False):
		self.name="BLOOD"
		if radius:
			self.radius=radius
		else:
			self.radius=random.randint(4,7)
		self.size=self.radius*2
		self.decay=decay
		self.vel=random.randint(rand[0],rand[1])*-1

		if side=='RIGHT':
			# self.rect=pygame.Rect( random.randint(t[0]-1,t[0]+1) , random.randint(t[1]-1, t[1]+t[3]+1)   ,self.size,self.size)
			self.center=[ random.randint(t[0]-1,t[0]+1) , random.randint(t[1]-1, t[1]+t[3]+1)]
			if radius:
				self.dx=[x for x in range(6,13)]
			else:
				self.dx=[x for x in range(3,11,2)]


		elif side=="LEFT":
			# self.rect=pygame.Rect( random.randint(t[0]+t[2]-1,t[0]+t[2]+1) , random.randint(t[1]-1, t[1]+t[3]+1)   ,self.size,self.size)
			self.center=[ random.randint(t[0]+t[2]-1,t[0]+t[2]+1) , random.randint(t[1]-1, t[1]+t[3]+1)]
			if radius:
				self.dx=[x for x in range(-6,-13,-1)]


			else:
				self.dx=[x for x in range(-3,-11,-2)]

		elif side=="UP":
			self.center=[ random.randint(t[0]-1,t[0]+t[2]+1) , random.randint(t[1]-1, t[1]+1)]
			if radius:
				self.dx=random.choice([[x for x in range(-3,1,1)],[x for x in range(0,4,1)]])

			else:
				self.dx=[x for x in range(-2,3,1)]

			self.vel=random.randint(rand[0]+8,rand[1]+8)*-1


		
		self.yvel=True		
		self.color=color
		self.map=collision_map
		self.alive=True

	def update(self,opp):
		if not pause:
			if self.yvel:
				self.center[1]+=self.vel*random.choice([1,0.9,1.1,0.85,1.15])
			if self.dx:
				self.center[0]+=random.choice(self.dx)

			self.vel+=0.3
			self.size=self.size-self.decay
			# if self.size<5:
			# 		self.decay=random.choice([x for x in range(5,7)])/10
			if self.size<=1:
				self.alive=False
			if self.center[1]>1300:
				self.alive=False
			# self.rect.size=(int(self.size),int(self.size))
			self.radius=int(self.size)/2

			# collisionlist=detect_collisions(pygame.Rect(),world,"rect")

			if self.map:
				for ob in self.map:
					if ob.collidepoint(self.center):
						if self.center[1]-self.radius>ob.top:
							self.center[1]=ob.top+self.radius
							self.dx=0
							self.decay=0.08
							self.yvel=False

			else:
				for ob in world:
					if ob.state in ('COLLIDER',"PLATFORM"):
						r=pygame.Rect(ob.ix,ob.iy,ob.iw,ob.ih)
						if r.collidepoint(self.center):
							if self.vel>0:
								if self.center[1]-self.radius>r.top:
									self.center[1]=r.top+self.radius
									self.dx=0
									self.decay=0.08
									self.yvel=False
							elif self.vel<0:
								if self.center[1]+self.radius<r.bottom:
									self.center[1]=r.bottom-self.radius
									self.dx=0
									self.decay=0.3
									self.yvel=False


		# self.copy=self.rect.copy()
		# self.copy[0]-=scroll[0]
		# self.copy[1]-=scroll[1]
		# pygame.draw.rect(screen,self.color,self.copy)

		self.copy=(self.center[0]-scroll[0],self.center[1]-scroll[1])

		
		pygame.draw.circle(screen,self.color,self.copy,self.radius)

############################################################################################################################################
############################################################################################################################################

class Explosion:
	def __init__(self,center,delay=False,size=False):
		self.center=center
		if size=="MINIGUN":
			self.size=random.choice([0.8,0.9])
		elif size=="SNIPER":
			self.size=random.choice([0.8,0.9,1])
		elif size=="ROCKETLAUNCHER":
			self.size=random.choice([1.2,1.4,1.6])
		else:
			self.size=random.choice([1,1.2,1.4,1.6,1.8,2,2.2])

		self.spritesheet=random.choice(explosion)
		if self.size!=1:
			self.spritesheet=[]
			for x in range(len(random.choice(explosion))):
				self.spritesheet.append(pygame.transform.smoothscale(random.choice(explosion)[x].copy(),(int(random.choice(explosion)[x].get_width()*self.size),int(random.choice(explosion)[x].get_height()*self.size))))
		self.frame=0
		self.alive=True
		self.sprite=self.spritesheet[0]
		self.rect=self.sprite.get_rect(center=self.center)
		if delay:
			self.delay=time.monotonic()
			self.delaytime=random.randrange(0,3)*0.1
		else:
			self.delay=False

	def update(self,opp):
		if self.delay and time.monotonic()-self.delay>self.delaytime or not self.delay:

			if not pause:
				self.frame+=0.3
				if self.frame>8:
					self.alive=False

				self.sprite=self.spritesheet[int(self.frame)]

			self.copy=(self.rect[0]-scroll[0],self.rect[1]-scroll[1])

			screen.blit(self.sprite,self.copy)


############################################################################################################################################
############################################################################################################################################


class MuzzleFlash:
	def __init__(self,spritesheet,x,y,xflip=False,angle=False):

		self.spritesheet=random.choice(spritesheet)

		self.xflip=xflip
		self.frame=0
		self.angle=angle
		if angle:
			self.spritesheet=[pygame.transform.rotate(x,self.angle[0]) for x in self.spritesheet]
			self.rect=self.spritesheet[0].get_rect(left=x,top=y)			
		else:
			if self.xflip:
				self.spritesheet=[pygame.transform.flip(x,True,False) for x in self.spritesheet]
			self.rect=self.spritesheet[0].get_rect(left=x,centery=y)
		self.sprite=self.spritesheet[0]
		self.width=self.sprite.get_width()
		self.height=self.sprite.get_height()
		if self.xflip:
			self.rect[0]-=self.width
		self.alive=True

	def update(self,opp):
		if not pause:
			if int(self.frame)>1:
				self.frame+=0.15
			else:
				self.frame+=0.2
			if self.frame>len(self.spritesheet):
				self.alive=False

			if self.frame>len(self.spritesheet)-1:
				# if self.angle or self.angle==0:
				self.sprite=self.spritesheet[int(len(self.spritesheet)-1)]
				# else:
				# 	self.sprite=pygame.transform.flip(self.spritesheet[int(len(self.spritesheet)-1)],self.xflip,False)
			else:
				# if self.angle or self.angle==0:
				self.sprite=self.spritesheet[int(self.frame)]
				# else:
				# 	self.sprite=pygame.transform.flip(self.spritesheet[int(self.frame)],self.xflip,False)

		# if self.xflip:
		# 	self.copy=(self.rect[0]-self.width-scroll[0],self.rect[1]-scroll[1])
		# else:
		if self.angle:
			self.copy=(self.rect[0]-scroll[0]-self.width//2,self.rect[1]-scroll[1]-self.height//2)
		else:
			self.copy=(self.rect[0]-scroll[0],self.rect[1]-scroll[1])

		screen.blit(self.sprite,self.copy)


############################################################################################################################################
############################################################################################################################################


class Snow:
	def __init__(self,position,extend,y=False):

		if extend:
			if extend==1:
				self.x=random.randrange(-1000,screenwidth,30)
				# self.x=random.randint(100,101)
			else:
				self.x=random.randrange(0,screenwidth+1000,30)
				# self.x=random.randint(1000,1001)
		else:
			self.x=random.randint(-200,screenwidth+200)
		if not y:
			if self.x>screenwidth or self.x<0:
				self.y=random.randrange(50,screenheight//2)
			else:
				self.y=random.randrange(-100,-50)
		else:
			self.y=y

		if position=="FRONT":
			self.rect=pygame.Rect(self.x,self.y,4,4)
			self.color=(229,58,255)
			self.speed=[x for x in range(-4,5,2)]
			self.yspeed=random.choice([3+1,4+1])
		elif position=='MID':
			self.rect=pygame.Rect(self.x,self.y,3,3)
			self.color=(250,250,250)
			self.speed=[x for x in range(-2,3,2)]
			self.yspeed=random.choice([2+1,3+1])
		elif position=="BACK":
			self.rect=pygame.Rect(self.x,self.y,2,2)
			self.color=(46,255,108)
			self.speed=[x for x in range(-3,2,2)]
			self.yspeed=random.choice([2+1,3+1])

		self.offset=random.choice([1,1.1,1.2,1.3,0.9,0.8,0.7])
		self.acc=[0.01,0.08,0.3,0.1]
		self.currentacc=random.choice(self.acc)
		self.vel=0
		self.time=time.monotonic()
		self.duration=[5,6,7,8]
		self.currentduration=random.choice(self.duration)

	def update(self,currentacc,direction,switch):
		if not pause:
			# if time.monotonic()-snowtime<snowcurrentduration:
			self.vel+=currentacc*direction
			self.rect[0]+=self.vel*self.offset
			self.rect[0]+=random.choice([1,-1,2,-2])

			if switch:
				self.currentacc=random.choice(self.acc)
			# else:
				# self.snowtime=time.monotonic()
				# snowcurrentacc=random.choice(self.acc)*direction
				# self.snowcurrentduration=random.choice(self.duration)
				

			# self.rect[0]+=random.choice(self.speed)
			self.rect[1]+=self.yspeed

			self.copy=self.rect.copy()
			self.copy[0]-=scroll[0]//2
			self.copy[1]-=scroll[1]//2
			# self.copy[1]-=scroll[1]
		pygame.draw.rect(screen,self.color,self.copy)


class Trail:
	def __init__(self,player,x,y,side,color,radius=False):
		self.side=side
		if radius:
			self.radius=random.randrange(radius[0],radius[1])
		else:
			self.radius=random.randrange(6,11)
		self.size=self.radius*2
		if side=='BOTTOM':
			self.center=[x,player[1]+player[3]+self.radius]
		elif side=='TOP':
			self.center=[x,player[1]-self.radius]
		elif side=="LEFT":
			self.center=[player[0]-self.radius,y]
		elif side=="RIGHT":
			self.center=[player[0]+player[2]+self.radius,y]

		self.decay=0.09
		self.color=color
		self.alive=True

	def update(self,s):

		if not pause:

			if self.side=='BOTTOM':
				self.center[1]-=self.radius
				self.size=self.size-self.decay
				if self.size<10:
					self.decay=random.choice([x for x in range(5,7)])/10
				

				self.radius=int(self.size)/1.6

				self.center[1]+=self.radius
			elif self.side=='TOP':
				self.center[1]+=self.radius
				self.size=self.size-self.decay
				if self.size<10:
					self.decay=random.choice([x for x in range(5,7)])/10
				

				self.radius=int(self.size)/1.6

				self.center[1]-=self.radius
			elif self.side=="LEFT":
				self.center[0]+=self.radius
				self.size=self.size-self.decay
				if self.size<10:
					self.decay=random.choice([x for x in range(5,7)])/10
				

				self.radius=int(self.size)/1.6

				self.center[0]-=self.radius
			elif self.side=="RIGHT":
				self.center[0]-=self.radius
				self.size=self.size-self.decay
				if self.size<10:
					self.decay=random.choice([x for x in range(5,7)])/10
				
				self.radius=int(self.size)/1.6

				self.center[0]+=self.radius

			if self.size<=1:
				self.alive=False

		self.copy=(self.center[0]-scroll[0],self.center[1]-scroll[1])

		
		pygame.draw.circle(screen,self.color,self.copy,self.radius)

class Transition:
	def __init__(self,direction,color=(0,0,0)):
		self.direction=direction
		self.color=color
		if self.direction=="IN":
			self.slides=[pygame.Rect(0-screenwidth-20*20,0,screenwidth,90),pygame.Rect(screenwidth+10*20,90,screenwidth,220),pygame.Rect(0-screenwidth,310,screenwidth,180),pygame.Rect(screenwidth+20*20,490,screenwidth,120),\
							pygame.Rect(0-screenwidth-10*20,610,screenwidth,80),pygame.Rect(screenwidth,690,screenwidth,174)]
		else:
			self.slides=[pygame.Rect(0,0,screenwidth+10*20,90),pygame.Rect(0-300,90,screenwidth+300,220),pygame.Rect(0,310,screenwidth+300,180),pygame.Rect(0,490,screenwidth,120),\
							pygame.Rect(0,610,screenwidth+100,80),pygame.Rect(0-150,690,screenwidth+150,174)]
		self.time=time.monotonic()
		self.complete=False

	def update(self):
		for x in range(len(self.slides)):
			pygame.draw.rect(screen,self.color,self.slides[x])

			if self.direction=="IN":
				if x%2==0:
					self.slides[x][0]+=50
					if self.slides[x][0]>0:
						self.slides[x][0]=0
				else:
					self.slides[x][0]-=50
					if self.slides[x][0]<0:
						self.slides[x][0]=0
						# self.complete=True
				if time.monotonic()-self.time>1.4:
					self.complete=True

			else:
				if x%2==0:
					self.slides[x][0]-=50
				else:
					self.slides[x][0]+=50
				if time.monotonic()-self.time>1.4:
					self.complete=True

		# if time.monotonic()-self.time>5:
		# 	self.complete=True





class Object:
	def __init__(self,xpos,ypos,width,height):
		self.rect=pygame.Rect(xpos,ypos,width,height)
# try:
# 	with open("FIRleveleditor.dat",'rb') as f1:
# 		world=pickle.load(f1)
# eself.xcept:
# 	with open("FIRleveleditor.dat",'wb') as f1:
# 		pickle.dump([],f1)

# worldcopy=copy.deepcopy(world)
with open("levelassets/ToxicMountains.dat",'rb') as f2:
	world=pickle.load(f2)
	
	worldextra=[x for x in world if x.state=="FOREGROUND"]
	world=[x for x in world if x.state!="FOREGROUND"]
	assetnames=pickle.load(f2)
	assetnames={name:pygame.image.load(name).convert_alpha() for name in assetnames}
	worldmasks={name:pygame.mask.from_surface(assetnames[name]) for name in assetnames}


	
def detect_collisions(rect,objects,check,mask=False,defaultrect=False):
	collisionlist={}
	if not defaultrect:
		if check=='rect':
			for o in objects:
				if o.state in ("COLLIDER","PLATFORM"):
					r=pygame.Rect(int(o.ix),int(o.iy),int(o.iw),int(o.ih))
					if rect.colliderect(r):
						collisionlist[o.state]=r
						break

		elif check=='point':
			for o in objects:
				if o.state in ("COLLIDER","PLATFORM"):
					r=pygame.Rect(int(o.ix),int(o.iy),int(o.iw),int(o.ih))
					if r.collidepoint(rect):
						collisionlist[o.state]=r
						return True

		elif check=='line':
			for o in objects:
				if o.state in ("COLLIDER","PLATFORM"):
					r=pygame.Rect(int(o.ix),int(o.iy),int(o.iw),int(o.ih))
					collide=r.clipline(rect)
					if collide:
						return collide

		else:
			for o in objects:
				if o.state=="COLLIDER":
					r=pygame.Rect(int(o.ix),int(o.iy),int(o.iw),int(o.ih))
					if rect.colliderect(r):
						offset=(r[0]-rect[0],r[1]-rect[1])
						if mask.overlap(worldmasks[o.name],offset):
							return True
	else:
		for o in objects:
			if rect.colliderect(o):
				collisionlist["COLLIDER"]=o
				break

	return collisionlist 

# def detect_mask_collisions(rect,mask,objects):
# 	for o in objects:
# 		r=pygame.Rect(int(o.ix),int(o.iy),int(o.iw),int(o.ih))
# 		if rect.colliderect(r):
# 			offset=(r[0]-rect[0],r[1]-rect[1])
# 			if mask.overlap(worldmasks[o.name],offset):
# 				# print(mask.overlap(worldmasks[o.name],offset))
# 				return True
# 	return False

def add_coordinates(original,value):
	original[0]+=value[0]
	original[1]+=value[1]
	return original

def screen_shake(weapon=False,size=False):
	if weapon:
		return random.choice([-size,size]),random.choice([-size,size])
	else:
		return random.choice([x for x in range(-15,15,3)]),random.choice([x for x in range(-15,15,3)])

def render_text(text,pos,size=1):
	if len(text)>5:
		if 'right' in text:
			text='r'+'-'+text.split()[-1]
		elif 'left' in text:
			text='r'+'-'+text.split()[-1]
	elif len(text)==3:
		if '[' in text:
			text=text[1]


	width=0
	height=0
	for letter in text:
		letter=letter.lower()
		if letter==' ':
			# if size=="DOUBLE":
			# 	width+=32
			# elif size=="HALF":
			# 	width+=8
			# else:
			# 	width+=16
			width+=int(16*size)
		else:
			# if size=="DOUBLE":
			# 	width+=font[letter].get_width()*2
			# 	if font[letter].get_height()*2>height:
			# 		height=font[letter].get_height()*2
			# elif size=="HALF":
			# 	width+=font[letter].get_width()/2
			# 	if font[letter].get_height()/2>height:
			# 		height=font[letter].get_height()/2
			# else:
			# 	width+=font[letter].get_width()
			# 	if font[letter].get_height()>height:
			# 		height=font[letter].get_height()

			width+=int(font[letter].get_width()*size)
			if int(font[letter].get_height()*size)>height:
					height=int(font[letter].get_height()*size)
	rect=pygame.Rect(0,0,width+5,height+5)
	rect.center=pos
	rect[0]-=5
	rect[1]-=5
	width=5
	for letter in text:
		letter=letter.lower()
		if letter==' ':
			# if size=="DOUBLE":
			# 	width+=32
			# elif size=="HALF":
			# 	width+=8
			# else:
			# 	width+=16
			width+=int(16*size)
		else:
			# if size=="DOUBLE":
			# 	screen.blit(pygame.transform.scale2x(font[letter]),(rect[0]+width,rect[1]+5))
			# 	width+=font[letter].get_width()*2
			# elif size=="HALF":
			# 	screen.blit(pygame.transform.smoothscale(font[letter],(font[letter].get_width()//2,font[letter].get_height()//2)),(rect[0]+width,rect[1]+5))
			# 	width+=font[letter].get_width()/2
			# else:
			# 	screen.blit(font[letter],(rect[0]+width,rect[1]+5))
			# 	width+=font[letter].get_width()
			screen.blit(pygame.transform.smoothscale(font[letter],( int(font[letter].get_width()*size) , int(font[letter].get_height()*size) )),(rect[0]+width,rect[1]+5))
			width+=font[letter].get_width()*size
	return rect





clock=pygame.time.Clock()

def MainMenu(transout=False):
	global particlecheck,trailcheck,pause,play1controls,play2controls,scroll

	gooey_rect=gooey.get_rect(centerx=screenwidth/2,top=100)
	gooey_glow_rect=gooey_glow.get_rect(center=gooey_rect.center)
	warfare_rect=warfare.get_rect(centerx=screenwidth/2,top=gooey_rect.bottom+30)
	warfare_glow_rect=warfare_glow.get_rect(center=warfare_rect.center)

	play_button_rect=play_button.get_rect(center=(screenwidth/2,(screenheight/2)+100))
	settings_button_rect=settings_button.get_rect(centerx=screenwidth/2,top=play_button_rect.bottom+20)
	quit_button_rect=quit_button.get_rect(centerx=screenwidth/2,top=settings_button_rect.bottom+20)
	video_button_rect=video_button.get_rect(center=(screenwidth/2,screenheight/2))
	controls_button_rect=controls_button.get_rect(centerx=screenwidth/2,top=video_button_rect.bottom+20)
	particle_button_rect=particle_button_on.get_rect(center=(screenwidth/2,screenheight/2))
	trails_button_rect=trails_button_on.get_rect(top=particle_button_rect.bottom+20,left=particle_button_rect.left)
	deathmatch_button_rect=deathmatch_button.get_rect(center=(screenwidth/2,screenheight/2))
	showdown_button_rect=showdown_button.get_rect(centerx=screenwidth/2,top=deathmatch_button_rect.bottom+20)
	controls_menu_rect=controls_menu.get_rect(center=(screenwidth/2,screenheight/2))
	escape_button_rect=escape_button.get_rect(right=screenwidth-100,bottom=screenheight-50)
	play1control_rect=pygame.Rect(controls_menu_rect[0]+330,controls_menu_rect[1]+40,265,330)
	play2control_rect=pygame.Rect(play1control_rect[0]+play1control_rect[2],play1control_rect[1],265,330)

	buttons=[gooey_rect,warfare_rect]
	
	with open('controls.dat','rb') as f1:
		play1controls=pickle.load(f1)
		play2controls=pickle.load(f1)

	currentkey=False

	selected = "PLAY"
	running=True
	click=False
	enter=False
	settingscreen=False
	videoscreen=False
	modescreen=False
	controlscreen=False
	pause=False
	snow=[]
	snowy=-200
	text=False
	scroll=[0,0]

	cclick=False
	controlswap=False

	snowtime=time.monotonic()
	snowduration=[1,2,4,6]
	snowcurrentduration=2
	snowdirection=[-1,1]
	snowcurrentdirection=random.choice(snowdirection)
	snowacc=[0.03,0.1,0.08,0.06]
	snowcurrentacc=0.1

	title_alpha=0
	glow_alpha=0
	menu_alpha=0
	menu_time=0
	screen_alpha=255
	brighten=True

	for x in range(80):
		snow.append(Snow(random.choice(['FRONT',"MID","BACK"]),False,snowy))
		snowy+=screenheight/60
	pink_scoreboard_rect=pink_scoreboard.get_rect(topleft=(40,50))
	green_scoreboard_rect=green_scoreboard.get_rect(topleft=(screenwidth-green_scoreboard.get_width()-40,50))

	weapon_names={'MINIGUN':minigun,"SHOTGUN":shotgun,"BLASTER":blaster,"ROCKETLAUNCHER":bazooka,"SNIPER":sniper,"PISTOL":deagle,"FLAMETHROWER":flamethrower}

	play1=Player(400,-70,controls=play1controls,idlesprites=sprite1,runsprites=sprite1run,jumpsprite=sprite1jump,squishsprite=sprite1squish,scoresprite=sprite1score,hurtsprite=sprite1hurt,face="RIGHT",color=(229,58,255),scoreboard=[sprite1[0].get_rect(topleft=(x,58)) for x in range(pink_scoreboard_rect[0]+16,325,64)],collision_map=buttons)
	play2=Player(screenwidth-450,-70,controls=play2controls,idlesprites=sprite2,runsprites=sprite2run,jumpsprite=sprite2jump,squishsprite=sprite2squish,scoresprite=sprite2score,hurtsprite=sprite2hurt,face="LEFT",color=(46,255,108),scoreboard=[sprite1[0].get_rect(topleft=(x,58)) for x in range(green_scoreboard_rect[0]+16,325+screenwidth-400,64)],collision_map=buttons)
	play1.opp=play2
	play2.opp=play1
	play1.name="austin"
	play2.name="sabor"
	if random.randrange(3)==0:
		wpn,wp= random.choice(list(weapon_names.items()))
	else:
		wpn,wp= "",False
	play1.weapon=wpn
	play1.weapon_sprite=wp

	if random.randrange(3)==0:
		wpn,wp= random.choice(list(weapon_names.items()))
	else:
		wpn,wp= "",False
	play2.weapon=wpn
	play2.weapon_sprite=wp


	play1event=time.monotonic()
	play2event=time.monotonic()
	play1right=True
	play1left=False
	play1jump=False
	play1fire=random.choice([True,False])

	play2right=False
	play2left=True	
	play2jump=False
	play2fire=random.choice([True,False])

	transitionin=False
	while running:
		# if controlswap:
		# 	print(controlswap[1])
		clock.tick(60)
		mousepos=list(pygame.mouse.get_pos())
		mousepos[0]*=1536/width
		mousepos[1]*=864/height

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False

			elif event.type==pygame.KEYDOWN:
				transition1=Transition("IN")
				transition2=Transition("OUT")
				if controlswap:
					currentkey=event.key
					keyname=pygame.key.name(currentkey)
					if len(keyname)>5:
						if 'right' in keyname:
							keyname='r'+'-'+keyname.split()[-1]
						elif 'left' in keyname:
							keyname='r'+'-'+keyname.split()[-1]
					elif len(keyname)==3:
						if '[' in keyname:
							keyname=keyname[1]
					# if currentkey:
					if keyname[0] in font.keys() and keyname!='escape':
						# if controlswap[0]==play1controls:
						# 	if currentkey not in play2controls:
						# 		controlswap[0][controlswap[1]]=currentkey
						# elif controlswap[0]==play2controls:
						# 	if currentkey not in play1controls:
						# 		controlswap[0][controlswap[1]]=currentkey
						if currentkey not in play1controls and currentkey not in play2controls:
							controlswap[0][controlswap[1]]=currentkey
					# if currentkey:
					# if pygame.key.name(currentkey)[0] in font.keys():
						# print("IN IT")
						# play1controls[count]=currentkey
						

				if event.key==pygame.K_ESCAPE:
					
					if videoscreen:
						videoscreen=False
					elif modescreen:
						modescreen=False
					elif controlscreen:
						controlscreen=False
						with open('controls.dat','wb') as f1:
							pickle.dump(play1controls,f1)
							pickle.dump(play2controls,f1)

					elif settingscreen:
						settingscreen=False

			elif event.type==pygame.MOUSEBUTTONDOWN:
				cclick=True
				if event.button==1:
					for k in [play_button_rect,settings_button_rect,quit_button_rect,particle_button_rect,trails_button_rect,\
							escape_button_rect,showdown_button_rect,deathmatch_button_rect]:
						if k.collidepoint(mousepos):
							click=True
			elif event.type==pygame.MOUSEBUTTONUP:
				cclick=False
				if event.button==1:
					if click:
						click=False
						if selected=="PLAY":
							modescreen=True
						elif selected=="EXIT":
							running=False
						elif selected=="settings":
							settingscreen=True
						elif selected=="VIDEO":
							videoscreen=True
						elif selected=="CONTROLS":
							controlscreen=True
						elif selected=="DEATHMATCH" or selected=="SHOWDOWN":
							transitionin=Transition("IN")
						elif selected=="PARTICLES":
							if particlecheck:
								particlecheck=False
							else:
								particlecheck=True
						elif selected=="TRAILS":
							if trailcheck:
								trailcheck=False
							else:
								trailcheck=True
						elif selected=="ESCAPE":
							if videoscreen:
								videoscreen=False
							elif modescreen:
								modescreen=False
							elif controlscreen:
								controlscreen=False
								with open('controls.dat','wb') as f1:
									pickle.dump(play1controls,f1)
									pickle.dump(play2controls,f1)

							elif settingscreen:
								settingscreen=False



					else:
						enter=False


		# if settingscreen:
		# 	screen.blit(b1,(-250,-370+50))
		# 	screen.blit(b2,(-200,-200))
		# else:

		screen.blit(background1,(-250,-370+50))
		screen.blit(background2,(-200,-200))



		snowfall=random.choice([1,2,3,4,4,4,4,4,4,4])
		if snowfall==1:
			if snowcurrentduration==1:
				snow.append(Snow('FRONT',snowcurrentdirection))
				snow.append(Snow('FRONT',snowcurrentdirection))
			else:
				snow.append(Snow('FRONT',snowcurrentdirection))
		elif snowfall==2:
			if snowcurrentduration==1:
				snow.append(Snow('MID',snowcurrentdirection))
				snow.append(Snow('MID',snowcurrentdirection))
			else:
				snow.append(Snow('MID',snowcurrentdirection))
		elif snowfall==3:
			if snowcurrentduration==1:
				snow.append(Snow('BACK',snowcurrentdirection))
				snow.append(Snow('BACK',snowcurrentdirection))
			else:
				snow.append(Snow('BACK',snowcurrentdirection))


		if snow:
			if time.monotonic()-snowtime<snowcurrentduration:
				for x in snow:
					x.update(snowcurrentacc,snowcurrentdirection,False)
			else:
				snowtime=time.monotonic()
				snowcurrentduration=random.choice(snowduration)
				snowcurrentdirection=random.choice(snowdirection)
				if snowcurrentduration==1:
					snowcurrentacc=0.5
				else:
					snowcurrentacc=random.choice(snowacc)
				for x in snow:
					x.update(snowcurrentacc,snowcurrentdirection,True)

		if videoscreen or controlscreen:
			screen.blit(backgroundblur2,(0,0))
		elif settingscreen or modescreen:
			screen.blit(backgroundblur1,(0,0))
		
			# for x in snow:
			# 	x.update()

		snow=[x for x in snow if x.rect[1]<screenheight+100]

		# if play_button_rect.collidepoint(mousepos):
		# 	selected="PLAY"
		# elif settings_button_rect.collidepoint(mousepos):
		# 	selected="settings"
		# elif quit_button_rect.collidepoint(mousepos):
		# 	selected="EXIT"
		# if particle_button_rect.collidepoint(mousepos):
		# 	selected="PARTICLES"
		# elif trails_button_rect.collidepoint(mousepos):
		# 	selected="TRAILS"

		escapescreen=True

		if not settingscreen and not modescreen:
			gooey_glow.set_alpha(glow_alpha)
			gooey.set_alpha(title_alpha)
			warfare_glow.set_alpha(glow_alpha)
			warfare.set_alpha(title_alpha)

			if screen_alpha<50:
				if title_alpha>150:
					title_alpha+=8

					if title_alpha>255:
						title_alpha=255
						if not menu_time:
							menu_time=time.monotonic()
				else:
					title_alpha+=3

				if brighten:
					if glow_alpha<255:
						glow_alpha+=3
					else:
						brighten=False
				else:
					if glow_alpha>110:
						glow_alpha-=3
					else:
						brighten=True

				screen.blit(gooey_glow,gooey_glow_rect)
				screen.blit(gooey,gooey_rect)
				screen.blit(warfare_glow,warfare_glow_rect)
				screen.blit(warfare,warfare_rect)

			if menu_time and time.monotonic()-menu_time>0.5:
				play_button.set_alpha(menu_alpha)
				settings_button.set_alpha(menu_alpha)
				quit_button.set_alpha(menu_alpha)

				menu_alpha+=15
				if menu_alpha>255:
					menu_alpha=255
			
				if play_button_rect.collidepoint(mousepos):
					selected="PLAY"
				elif settings_button_rect.collidepoint(mousepos):
					selected="settings"
				elif quit_button_rect.collidepoint(mousepos):
					selected="EXIT"
				
				if selected=="PLAY":
					if click:
						screen.blit(play_button_pressed,(play_button_rect))

							
					else:
						screen.blit(play_button_selected,(play_button_rect))
					
				else:
					screen.blit(play_button,(play_button_rect))

				if selected=="settings":
					if click:
						screen.blit(settings_button_pressed,(settings_button_rect))
					else:
						screen.blit(settings_button_selected,(settings_button_rect))

				else:
					screen.blit(settings_button,(settings_button_rect))

				if selected=="EXIT":
					if click:
						screen.blit(quit_button_pressed,(quit_button_rect))
					else:
						screen.blit(quit_button_selected,(quit_button_rect))


				else:
					screen.blit(quit_button,(quit_button_rect))
				

				if play1.alive:
					if time.monotonic()-play1event>random.randint(1,3):
						play1event=time.monotonic()
						play1right=random.choice([True,False])
						play1left= not play1right
						play1jump=random.choice([True,False])
					play1.update(auto=True,autoright=play1right,autoleft=play1left,autojump=play1jump)
					if play1jump:
						play1jump=False
				else:
					if time.monotonic()-play1.deathtime>1.7:
						if random.randrange(2)==0:
							wpn,wp= random.choice(list(weapon_names.items()))
						else:
							wpn,wp= "",False
						play1.weapon=wpn
						play1.weapon_sprite=wp
						play1.rect.topleft=(random.randint(250,screenwidth-250),-70)
						play1.alive=True
				play1.update_particles()
				if play2.alive:
					if time.monotonic()-play2event>random.randint(1,3):
						play2event=time.monotonic()
						play2right=random.choice([True,False])
						play2left= not play2right
						play2jump=random.choice([True,False])
					play2.update(auto=True,autoright=play2right,autoleft=play2left,autojump=play2jump)
					if play2jump:
						play2jump=False
				else:
					if time.monotonic()-play2.deathtime>1.7:
						if random.randrange(2)==0:
							wpn,wp= random.choice(list(weapon_names.items()))
						else:
							wpn,wp= "",False
						play2.weapon=wpn
						play2.weapon_sprite=wp
						play2.rect.topleft=(random.randint(250,screenwidth-250),-70)
						play2.alive=True
				play2.update_particles()
			escapescreen=False

		elif modescreen:
			render_text("game modes",(screenwidth/2+8,80),2)
			if deathmatch_button_rect.collidepoint(mousepos):
				selected="DEATHMATCH"
			elif showdown_button_rect.collidepoint(mousepos):
				selected="SHOWDOWN"

			if selected=="DEATHMATCH":
				if click:
					screen.blit(deathmatch_button_pressed,(deathmatch_button_rect))

						
				else:
					screen.blit(deathmatch_button_selected,(deathmatch_button_rect))
				
			else:
				screen.blit(deathmatch_button,(deathmatch_button_rect))

			if selected=="SHOWDOWN":
				if click:
					screen.blit(showdown_button_pressed,(showdown_button_rect))

						
				else:
					screen.blit(showdown_button_selected,(showdown_button_rect))
				
			else:
				screen.blit(showdown_button,(showdown_button_rect))


		elif videoscreen:
			render_text("video settings",(screenwidth/2+8,80),2)
			if particle_button_rect.collidepoint(mousepos):
				selected="PARTICLES"
			elif trails_button_rect.collidepoint(mousepos):
				selected="TRAILS"
			if particlecheck:
				screen.blit(particle_button_on,particle_button_rect)
			else:
				screen.blit(particle_button_off,particle_button_rect)

			if trailcheck:
				screen.blit(trails_button_on,trails_button_rect)
			else:
				screen.blit(trails_button_off,trails_button_rect)

			# print(render_text('right alt',(particle_button_rect.center[0],particle_button_rect[1]-200)))
			# print(particle_button_rect.center)

		elif controlscreen:
			render_text("controls",(screenwidth/2+8,80),2)
			screen.blit(controls_menu,controls_menu_rect)
			count=0
			for x in range(controls_menu_rect[1]+118,controls_menu_rect[1]+369,56):
				rect=render_text(pygame.key.name(play1controls[count]),(825,x))
				count+=1
			count=0
			for x in range(controls_menu_rect[1]+118,controls_menu_rect[1]+369,56):
				rect=render_text(pygame.key.name(play2controls[count]),(1070,x))
				count+=1

			if play1control_rect.collidepoint(mousepos):
				count=0
				for x in range(controls_menu_rect[1]+118,controls_menu_rect[1]+369,56):
					rect=render_text(pygame.key.name(play1controls[count]),(825,x))
					
					if rect.collidepoint(mousepos):
						pygame.draw.rect(screen,(255,255,255),rect,width=1)
					if cclick:
						if rect.collidepoint(mousepos):
							controlswap=[play1controls,count]
							break
						else:
							controlswap=False
					count+=1

			elif play2control_rect.collidepoint(mousepos):
				count=0
				for x in range(controls_menu_rect[1]+118,controls_menu_rect[1]+369,56):
					rect=render_text(pygame.key.name(play2controls[count]),(1070,x))
					
					if rect.collidepoint(mousepos):
						pygame.draw.rect(screen,(255,255,255),rect,width=1)
					if cclick:
						if rect.collidepoint(mousepos):
							controlswap=[play2controls,count]
							break
						else:
							controlswap=False
					count+=1



		elif settingscreen:
			render_text("settings",(screenwidth/2+8,80),2)
			if video_button_rect.collidepoint(mousepos):
				selected="VIDEO"
			elif controls_button_rect.collidepoint(mousepos):
				selected="CONTROLS"

			if selected=="VIDEO":
				if click:
					screen.blit(video_button_pressed,(video_button_rect))
				else:
					screen.blit(video_button_selected,(video_button_rect))

			else:
				screen.blit(video_button,(video_button_rect))

			if selected=="CONTROLS":
				if click:
					screen.blit(controls_button_pressed,(controls_button_rect))
				else:
					screen.blit(controls_button_selected,(controls_button_rect))

			else:
				screen.blit(controls_button,(controls_button_rect))

		if escapescreen:				
			if escape_button_rect.collidepoint(mousepos):
				selected="ESCAPE"
				if click:
					screen.blit(escape_button_pressed,(escape_button_rect))
				else:
					screen.blit(escape_button_selected,(escape_button_rect))

			else:
				screen.blit(escape_button,(escape_button_rect))

			pygame.draw.line(screen,(245-30,250-30,246-30),(70,140),(screenwidth-70,140),width=2)
			pygame.draw.line(screen,(245-30,250-30,246-30),(70,screenheight-110),(screenwidth-70,screenheight-110),width=2)
		# if controlswap:
		# 	print(controlswap[1])

		if screen_alpha>=0:
			screen.blit(fade,(0,0))
			screen_alpha-=15
			fade.set_alpha(screen_alpha)

		if transitionin:	
			if transitionin.complete:
				transitionin=False
				return Game(selected)				
			else:
				transitionin.update()
		if transout:
			if not transout.complete:
				transout.update()

		new_screen=pygame.transform.scale(screen,(width,height))
		display.blit(new_screen,(0,0))
		pygame.display.update()
		
	pygame.quit()

def Game(gamemode):

	global world,screenshake,weapons,avail_weapons,pause,particlecheck,trailcheck,play1controls,play2controls,win,wintime
	snow=[]
	snowy=-200
	avail_weapons=[["MINIGUN",minigun,False],['SNIPER',sniper,False],['ROCKETLAUNCHER',bazooka,False],["PISTOL",deagle,False],\
		['BLASTER',blaster,False],["FLAMETHROWER",flamethrower,False],["SHOTGUN",shotgun,False],["LASER",lasergun,False],["INVERTEDPISTOL",invertedpistol,False]]
	used_weapons=[]
	if gamemode=="DEATHMATCH":
		for x in range(len(avail_weapons)):
			new_wep=list(avail_weapons[x])
			new_wep[0]+='1'
			# if x<1:
			avail_weapons.append(new_wep)
	weapon_time=time.monotonic()
	weapon_spawn=5
	weapons={}
	# weaponx=[x+60 for x in range(-200,1900,300)]
	weaponx=[-130, 190, 460, 750, 1050, 1380, 1660]
	# print(weaponx)
	running=True
	pause=False
	win_alpha=0

	youwin=pygame.image.load('ui/youwin.png').convert_alpha()
	pink_scoreboard.set_alpha(180)
	pink_scoreboard_rect=pink_scoreboard.get_rect(topleft=(40,50))
	green_scoreboard.set_alpha(180)
	green_scoreboard_rect=green_scoreboard.get_rect(topleft=(screenwidth-green_scoreboard.get_width()-40,50))
	pink_score,green_score=0,0
	pink_score_x=200
	green_score_x=screenwidth-300

	play1=Player(450,-150,controls=play1controls,idlesprites=sprite1,runsprites=sprite1run,jumpsprite=sprite1jump,squishsprite=sprite1squish,scoresprite=sprite1score,hurtsprite=sprite1hurt,face="RIGHT",color=(229,58,255),scoreboard=[sprite1[0].get_rect(topleft=(x,58)) for x in range(pink_scoreboard_rect[0]+16,325,64)],collision_map=False)
	play2=Player(930,-150,controls=play2controls,idlesprites=sprite2,runsprites=sprite2run,jumpsprite=sprite2jump,squishsprite=sprite2squish,scoresprite=sprite2score,hurtsprite=sprite2hurt,face="LEFT",color=(46,255,108),scoreboard=[sprite1[0].get_rect(topleft=(x,58)) for x in range(green_scoreboard_rect[0]+16,325+screenwidth-400,64)],collision_map=False)

	play1.opp=play2
	play2.opp=play1
	play1.name="girish"
	play2.name="numa"

	if gamemode=="SHOWDOWN":
		wpn=random.choice(avail_weapons)
		play1.weapon=wpn[0]
		play2.weapon=wpn[0]
		play1.weapon_sprite=wpn[1]
		play2.weapon_sprite=wpn[1]

	snowtime=time.monotonic()
	snowduration=[1,2,4,6]
	snowcurrentduration=2
	snowdirection=[-1,1]
	snowcurrentdirection=random.choice(snowdirection)
	snowacc=[0.03,0.1,0.08,0.06]
	snowcurrentacc=0.1

	currentkey=False
	cclick=False
	controlswap=False

	win=False
	wintime=False

	# menu=pygame.Surface()
	for x in range(80):
		snow.append(Snow(random.choice(['FRONT',"MID","BACK"]),False,snowy))
		snowy+=screenheight/60

	transitionout=Transition("OUT")
	transitionin=False
	modename=True
	modenamecenter=[-300,150]

	while running:
		# if clock.get_fps()<45:
		# 	print("LOW FPS")
		dx,dy=0,0
		# screen.fill((255,255,255))
		# display.fill((255,255,255))
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False

			elif event.type==pygame.KEYDOWN:
				# print(pygame.key.name(event.key))
				if event.key==pygame.K_l:
					with open("FIRleveleditor.dat",'wb') as f1:
						pickle.dump(world,f1)
				# elif event.key==pygame.K_RETURN:
				# 	scrollcheck=True
				# 	play1.rect[0]=int(450)
				# 	play1.rect[1]=int(-150)
				# 	play2.rect[0]=int(930)
				# 	play2.rect[1]=int(-150)
				# 	play1.alive=True
				# 	play2.alive=True
				elif event.key==pygame.K_ESCAPE:
					pause=True
					continue_button_rect=continue_button.get_rect(center=(screenwidth/2+20,screenheight/2-80))
					restart_button_rect=restart_button.get_rect(centerx=screenwidth/2+20,top=continue_button_rect.bottom+20)
					settings_button_rect=settings_button.get_rect(centerx=screenwidth/2+20,top=restart_button_rect.bottom+20)
					quit_button_rect=quit_button.get_rect(centerx=screenwidth/2+20,top=settings_button_rect.bottom+20)
					particle_button_rect=particle_button_on.get_rect(center=(screenwidth/2+20,screenheight/2+20))
					trails_button_rect=trails_button_on.get_rect(top=particle_button_rect.bottom+20,left=particle_button_rect.left)
					video_button_rect=video_button.get_rect(center=(screenwidth/2,screenheight/2))
					controls_button_rect=controls_button.get_rect(centerx=screenwidth/2,top=video_button_rect.bottom+20)
					controls_menu_rect=controls_menu.get_rect(center=(screenwidth/2,screenheight/2))
					escape_button_rect=escape_button.get_rect(right=screenwidth-100,bottom=screenheight-50)
					play1control_rect=pygame.Rect(controls_menu_rect[0]+330,controls_menu_rect[1]+40,265,330)
					play2control_rect=pygame.Rect(play1control_rect[0]+play1control_rect[2],play1control_rect[1],265,330)

					selected = "CONTINUE"
					running=True
					click=False
					enter=False
					settingscreen=False
					videoscreen=False
					controlscreen=False
					while pause:
						for event in pygame.event.get():



							if event.type==pygame.QUIT:
								running=False

							elif event.type==pygame.KEYDOWN:
								if controlswap:
									currentkey=event.key
									keyname=pygame.key.name(currentkey)
									if len(keyname)>5:
										if 'right' in keyname:
											keyname='r'+'-'+keyname.split()[-1]
										elif 'left' in keyname:
											keyname='r'+'-'+keyname.split()[-1]
									elif len(keyname)==3:
										if '[' in keyname:
											keyname=keyname[1]
									# if currentkey:
									if keyname[0] in font.keys() and keyname!='escape':
										if controlswap[0]==play1controls:
											if currentkey not in play2controls:
												controlswap[0][controlswap[1]]=currentkey
										elif controlswap[0]==play2controls:
											if currentkey not in play1controls:
												controlswap[0][controlswap[1]]=currentkey


								if event.key==pygame.K_ESCAPE:
									if event.key==pygame.K_ESCAPE:					
										if videoscreen:
											videoscreen=False
										elif controlscreen:
											controlscreen=False
											with open('controls.dat','wb') as f1:
												pickle.dump(play1controls,f1)
												pickle.dump(play2controls,f1)

										elif settingscreen:
											settingscreen=False
										elif pause:
											pause=False


							elif event.type==pygame.MOUSEBUTTONDOWN:
								cclick=True
								if event.button==1:
									for k in [continue_button_rect,settings_button_rect,quit_button_rect,particle_button_rect,trails_button_rect,escape_button_rect]:
										if k.collidepoint(mousepos):
											click=True
									# click=True
							elif event.type==pygame.MOUSEBUTTONUP:
								cclick=False
								if event.button==1:
									if click:
										click=False
										if selected=="CONTINUE":
											pause=False
										elif selected=="EXIT":
											pause=False
											transitionin=Transition("IN")											
										elif selected=="RESTART":
											return Game(gamemode)
										elif selected=="settings":
											settingscreen=True
										elif selected=="VIDEO":
											videoscreen=True
										elif selected=="CONTROLS":
											controlscreen=True
										elif selected=="PARTICLES":
											if particlecheck:
												particlecheck=False
											else:
												particlecheck=True
										elif selected=="TRAILS":
											if trailcheck:
												trailcheck=False
											else:
												trailcheck=True
										elif selected=="ESCAPE":
											if videoscreen:
												videoscreen=False
											elif controlscreen:
												controlscreen=False
												with open('controls.dat','wb') as f1:
													pickle.dump(play1controls,f1)
													pickle.dump(play2controls,f1)

											elif settingscreen:
												settingscreen=False
											elif pause:
												pause=False
									else:
										enter=False

						screen.blit(background1,(-270-(scroll[0]/11),-380+50-(scroll[1]/20)))
						screen.blit(background2,(-220-(scroll[0]/5),-210-(scroll[1]/10)))

						for ob in world:
							screen.blit(assetnames[ob.name],(int((ob.ix-scroll[0])),int((ob.iy-scroll[1]))))

						if play1.alive:
							play1.update()
						# screen.blit(play1.runsprites[0],(play1.rect[0]-scroll[0],play1.rect[1]-scroll[1]))
						# screen.blit(play2.runsprites[0],(play2.rect[0]-scroll[0],play2.rect[1]-scroll[1]))
						if play2.alive:
							play2.update()

						for ob in worldextra:

							screen.blit(assetnames[ob.name],(int((ob.ix-scroll[0])),int((ob.iy-scroll[1]))))
						for x in snow:
							x.update(snowcurrentacc,snowcurrentdirection,False)

						if videoscreen or controlscreen:
							screen.blit(backgroundblur2,(0,0))
						elif settingscreen:
							screen.blit(backgroundblur1,(0,0))
						else:
							screen.blit(backgroundblur,(0,0))
							render_text("paused",(screenwidth/2+8,80),2)

						mousepos=list(pygame.mouse.get_pos())
						mousepos[0]*=1536/width
						mousepos[1]*=864/height

						escapescreen=True

						if not settingscreen:
						
							if continue_button_rect.collidepoint(mousepos):
								selected="CONTINUE"
							elif restart_button_rect.collidepoint(mousepos):
								selected="RESTART"
							elif settings_button_rect.collidepoint(mousepos):
								selected="settings"
							elif quit_button_rect.collidepoint(mousepos):
								selected="EXIT"
							
							if selected=="CONTINUE":
								if click:
									screen.blit(continue_button_pressed,(continue_button_rect))
										
								else:
									screen.blit(continue_button_selected,(continue_button_rect))
								
							else:
								screen.blit(continue_button,(continue_button_rect))

							if selected=="RESTART":
								if click:
									screen.blit(restart_button_pressed,(restart_button_rect))
										
								else:
									screen.blit(restart_button_selected,(restart_button_rect))
								
							else:
								screen.blit(restart_button,(restart_button_rect))

							if selected=="settings":
								if click:
									screen.blit(settings_button_pressed,(settings_button_rect))
								else:
									screen.blit(settings_button_selected,(settings_button_rect))

							else:
								screen.blit(settings_button,(settings_button_rect))

							if selected=="EXIT":
								if click:
									screen.blit(quit_button_pressed,(quit_button_rect))
								else:
									screen.blit(quit_button_selected,(quit_button_rect))

							else:
								screen.blit(quit_button,(quit_button_rect))

						elif videoscreen:
							render_text("video settings",(screenwidth/2+8,80),2)
							if particle_button_rect.collidepoint(mousepos):
								selected="PARTICLES"
							elif trails_button_rect.collidepoint(mousepos):
								selected="TRAILS"
							if particlecheck:
								screen.blit(particle_button_on,particle_button_rect)
							else:
								screen.blit(particle_button_off,particle_button_rect)

							if trailcheck:
								screen.blit(trails_button_on,trails_button_rect)
							else:
								screen.blit(trails_button_off,trails_button_rect)
						elif controlscreen:
							render_text("controls",(screenwidth/2+8,80),2)
							screen.blit(controls_menu,controls_menu_rect)
							count=0
							for x in range(controls_menu_rect[1]+118,controls_menu_rect[1]+369,56):
								rect=render_text(pygame.key.name(play1controls[count]),(825,x))
								count+=1
							count=0
							for x in range(controls_menu_rect[1]+118,controls_menu_rect[1]+369,56):
								rect=render_text(pygame.key.name(play2controls[count]),(1070,x))
								count+=1

							

							if play1control_rect.collidepoint(mousepos):
								count=0
								for x in range(controls_menu_rect[1]+118,controls_menu_rect[1]+369,56):
									rect=render_text(pygame.key.name(play1controls[count]),(825,x))
									
									if rect.collidepoint(mousepos):
										pygame.draw.rect(screen,(255,255,255),rect,width=1)
									if cclick:
										if rect.collidepoint(mousepos):
											controlswap=[play1controls,count]
											break
										else:
											controlswap=False
									count+=1
								
							elif play2control_rect.collidepoint(mousepos):
								count=0
								for x in range(controls_menu_rect[1]+118,controls_menu_rect[1]+369,56):
									rect=render_text(pygame.key.name(play2controls[count]),(1070,x))
									
									if rect.collidepoint(mousepos):
										pygame.draw.rect(screen,(255,255,255),rect,width=1)
									if cclick:
										if rect.collidepoint(mousepos):
											controlswap=[play2controls,count]
											break
										else:
											controlswap=False
									count+=1

						elif settingscreen:
							render_text("settings",(screenwidth/2+8,80),2)
							if video_button_rect.collidepoint(mousepos):
								selected="VIDEO"
							elif controls_button_rect.collidepoint(mousepos):
								selected="CONTROLS"

							if selected=="VIDEO":
								if click:
									screen.blit(video_button_pressed,(video_button_rect))
								else:
									screen.blit(video_button_selected,(video_button_rect))

							else:
								screen.blit(video_button,(video_button_rect))

							if selected=="CONTROLS":
								if click:
									screen.blit(controls_button_pressed,(controls_button_rect))
								else:
									screen.blit(controls_button_selected,(controls_button_rect))

							else:
								screen.blit(controls_button,(controls_button_rect))

						if escapescreen:				
							if escape_button_rect.collidepoint(mousepos):
								selected="ESCAPE"
								if click:
									screen.blit(escape_button_pressed,(escape_button_rect))
								else:
									screen.blit(escape_button_selected,(escape_button_rect))

							else:
								screen.blit(escape_button,(escape_button_rect))
							pygame.draw.line(screen,(245-30,250-30,246-30),(70,140),(screenwidth-70,140),width=2)
							pygame.draw.line(screen,(245-30,250-30,246-30),(70,screenheight-110),(screenwidth-70,screenheight-110),width=2)

						new_screen=pygame.transform.scale(screen,(width,height))
						display.blit(new_screen,(0,0))
						pygame.display.update()

				elif event.key==pygame.K_SPACE:
					print(clock.get_fps())
					print(len(snow))
			# elif event.type==pygame.KEYUP:
			# 	if event.key in [pygame.K_d,pygame.K_a,1073741918,1073741916]:
			# 		play1.acc=0
			# 		play2.acc=0
				# elif event.key==pygame.K_b:
				# 	drag=False
				

		

		# if drag:
		# 	curpos=pygame.mouse.get_pos()
		# 	if curpos==framepos:
		# 		startpos=framepos
		# 	xdist=(curpos[0]-startpos[0])/10
		# 	ydist=(curpos[1]-startpos[1])/10

		# 	scroll[0]-=xdist
		# 	scroll[1]-=ydist
		# 	framepos=curpos
		# if scrollcheck:
		if play1.alive and play2.alive:
			if time.monotonic()-play1.alivetime <0.1 or time.monotonic()-play2.alivetime <0.1:
				scroll[0]+=(((play1.rect.center[0]+play2.rect.center[0])//2)-scroll[0]-(screenwidth/2))/40
				scroll[1]+=(((play1.rect.center[1]+play2.rect.center[1])//2-70)-scroll[1]-(screenheight/2))/40

			else:

				scroll[0]+=(((play1.rect.center[0]+play2.rect.center[0])//2+11)-scroll[0]-(screenwidth/2))/15
				scroll[1]+=(((play1.rect.center[1]+play2.rect.center[1])//2-70)-scroll[1]-(screenheight/2))/20
			if scroll[0]<-300:
				scroll[0]=-300
			elif scroll[0]>350:
				scroll[0]=350
			
			if scroll[1]<-100:
				scroll[1]=-100
			elif scroll[1]>50:
				scroll[1]=50
		elif play1.alive:
			scroll[0]+=((play1.rect.center[0])-scroll[0]-(screenwidth/2))/50
			scroll[1]+=((play1.rect.center[1]-40)-scroll[1]-(screenheight/2))/50
		elif play2.alive:
			scroll[0]+=((play2.rect.center[0])-scroll[0]-(screenwidth/2))/50
			scroll[1]+=((play2.rect.center[1]-40)-scroll[1]-(screenheight/2))/50

			
		# keys=pygame.key.get_pressed()
		# mice=pygame.mouse.get_pressed()
		
		# cloudx-=0.1
		screen.blit(background1,(-270-(scroll[0]/11),-380+50-(scroll[1]/20)))
		screen.blit(background2,(-220-(scroll[0]/5),-210-(scroll[1]/10)))
		# screen.blit(background3,(-200-(scroll[0]/5),-250+20-(scroll[1]/5)))
		# screen.blit(clouds1,(-350-(scroll[0]/9)+cloudx,-200-(scroll[1]/17)))
		# screen.blit(clouds2,(-650-(scroll[0]/8)+cloudx*2.2,-200-(scroll[1]/16)))




		for ob in world:

			screen.blit(assetnames[ob.name],(int((ob.ix-scroll[0])),int((ob.iy-scroll[1]))))
		for ob in worldextra:

			screen.blit(assetnames[ob.name],(int((ob.ix-scroll[0])),int((ob.iy-scroll[1]))))

		if win:
			print("WONNNN")
			if time.monotonic()-wintime>1.5:
				if time.monotonic()-wintime<10:
					youwin.set_alpha(win_alpha)
					r=youwin.get_rect(center=(screenwidth/2,screenheight/2-150))
					screen.blit(youwin,r)
					if win_alpha<100:
						win_alpha+=2
					else:
						win_alpha+=3
					if time.monotonic()-wintime>4 and time.monotonic()-wintime<7:
						# self.particles.append(Flame(self.rect[0]+132,self.rect.center[1]-12,self.face))
						x=95
						for y in range(r[1]+20,r[1]+r[3]-20,50):
							win.particles.append(Flame(r[0]-x+scroll[0],y+scroll[1],"RIGHT"))
							# win.particles.append(Explosion((r[0]-x+scroll[0],y+scroll[1]),True))
							win.particles.append(Flame(r[0]+r[2]+x+scroll[0],y+scroll[1],"LEFT"))
							# win.particles.append(Explosion((r[0]+r[2]+x+scroll[0],y+scroll[1]),True))
							x-=10
						if random.choice([1,2])==1:
							win.particles.append(Explosion((  random.randrange(r[0]-300,r[0]+r[2]+300)+scroll[0] ,  random.randrange(r[1]-300,r[1]+r[3]+300)+scroll[1]   ),True))
				else:
					if not transitionin:
						transitionin=Transition("IN")

		play2.update_bullets()
		if play2.alive:
			play2.update()			
		else:
			if gamemode=="SHOWDOWN" and not win:
				
				wpn=random.choice(avail_weapons)

				play1.weapon_sprite=wpn[1]
				play2.weapon_sprite=wpn[1]

			if time.monotonic()-play2.deathtime>1.7:
					
				if play1.score<5:
					if gamemode=="SHOWDOWN":
						while True:
							wpn=random.choice(avail_weapons)
							wpnname=wpn[0]
							if wpnname[-1]=='1':
								wpnname=wpnname[:len(wpnname)-1]
							playerwpnname=play2.weapon
							if playerwpnname[-1]=='1':
								playerwpnname=playerwpnname[:len(playerwpnname)-1]
							if wpnname!=playerwpnname and wpn not in used_weapons:
								used_weapons.append(wpn)
								play1.weapon=wpn[0]
								play2.weapon=wpn[0]
								play1.weapon_sprite=wpn[1]
								play2.weapon_sprite=wpn[1]
								break

					play2.rect.topleft=(play2.xpos,play2.ypos)
					play2.alive=True
				else:
					if not win:
						win=play1
						wintime=time.monotonic()


		
		play2.update_particles()


		play1.update_bullets()
		if play1.alive:
			play1.update()
		else:
			if gamemode=="SHOWDOWN" and not win:
				
				wpn=random.choice(avail_weapons)
				play1.weapon_sprite=wpn[1]
				play2.weapon_sprite=wpn[1]

			if time.monotonic()-play1.deathtime>1.7:
					
				if play2.score<5:
					if gamemode=="SHOWDOWN":
						while True:
							wpn=random.choice(avail_weapons)
							wpnname=wpn[0]
							if wpnname[-1]=='1':
								wpnname=wpnname[:len(wpnname)-1]
							playerwpnname=play1.weapon
							if playerwpnname[-1]=='1':
								playerwpnname=playerwpnname[:len(playerwpnname)-1]
							if wpnname!=playerwpnname and wpn not in used_weapons:
								used_weapons.append(wpn)
								play1.weapon=wpn[0]
								play2.weapon=wpn[0]
								play1.weapon_sprite=wpn[1]
								play2.weapon_sprite=wpn[1]
								break

					play1.rect.topleft=(play1.xpos,play1.ypos)
					play1.alive=True
				else:
					if not win:
						win=play2
						wintime=time.monotonic()

	
		play1.update_particles()


		screen.blit(pink_scoreboard,pink_scoreboard_rect)
		screen.blit(green_scoreboard,green_scoreboard_rect)

		

		if play1.score:
			for k in range(play1.score):
				screen.blit(play1.scoresprite,play1.scoreboard[k])
		if play2.score:
			for k in range(play2.score):
				screen.blit(play2.scoresprite,play2.scoreboard[k]) 

		if gamemode=="DEATHMATCH":
			if weapon_spawn:
				if time.monotonic()-weapon_time>weapon_spawn:
					weapon_time=time.monotonic()
					if weapon_spawn==5:
						weapon_spawn=4					
					else:
						weapon_spawn=random.randint(1,2)
					w=random.choice(avail_weapons)
					if len(avail_weapons)<=1:
						weapon_spawn=False				
					avail_weapons.remove(w)			

					if weaponx:
						x=random.choice(weaponx)
						weaponx.remove(x)
						w[2]=w[1].get_rect(center=(x,-300))
						weapons[w[0]]=[w[1],w[2]]
					else:
						# print('weaponx')
						if len(weapons)<7:
							xxrange=[-130, 190, 460, 750, 1050, 1380, 1660]
							xlist=[weapons[ob][1].center[0] for ob in weapons]
							xxrange=[x for x in xxrange if x not in xlist]
							x=random.choice(xxrange)

							w[2]=w[1].get_rect(center=(x,-300))
							weapons[w[0]]=[w[1],w[2]]				
					
					
			else:
				if len(avail_weapons)>=1:
					weapon_spawn=random.randrange(15,20)

			# print(weapons)
			for wp in weapons.values():
				wp[1][1]+=3
				collisionlist=detect_collisions(wp[1],world,'rect')
				for ob in collisionlist:
					wp[1].bottom=collisionlist[ob].top

				screen.blit(wp[0],(wp[1][0]-scroll[0],wp[1][1]-scroll[1]))





		snowfall=random.choice([1,2,3,4,4,4,4,4,4,4])
		if snowfall==1:
			if snowcurrentduration==1:
				
				snow.append(Snow('FRONT',snowcurrentdirection))
				snow.append(Snow('FRONT',snowcurrentdirection))
			else:
				
				snow.append(Snow('FRONT',snowcurrentdirection))
		elif snowfall==2:
			if snowcurrentduration==1:
				
				snow.append(Snow('MID',snowcurrentdirection))
				snow.append(Snow('MID',snowcurrentdirection))
			else:
				
				snow.append(Snow('MID',snowcurrentdirection))
		elif snowfall==3:
			if snowcurrentduration==1:
				
				snow.append(Snow('BACK',snowcurrentdirection))
				snow.append(Snow('BACK',snowcurrentdirection))
			else:
				
				snow.append(Snow('BACK',snowcurrentdirection))


		if snow:
			if time.monotonic()-snowtime<snowcurrentduration:
				for x in snow:
					x.update(snowcurrentacc,snowcurrentdirection,False)
			else:
				snowtime=time.monotonic()
				snowcurrentduration=random.choice(snowduration)
				snowcurrentdirection=random.choice(snowdirection)
				if snowcurrentduration==1:
					snowcurrentacc=0.5
				else:
					snowcurrentacc=random.choice(snowacc)
				for x in snow:
					x.update(snowcurrentacc,snowcurrentdirection,True)

		snow=[x for x in snow if x.rect[1]<screenheight+100]

		


		if screenshake:
			if screenshake[0]=="hit":
				if time.monotonic()-screenshake[1]<0.25:
					dx,dy=screen_shake()
				else:
					screenshake=False
			else:
				if time.monotonic()-screenshake[1]<0.1:
					dx,dy=screen_shake(True,screenshake[2])
				else:
					screenshake=False

		if modename:
			render_text(gamemode,modenamecenter,2)
			if modenamecenter[0]>screenwidth//2-80:
				if modenamecenter[0]>screenwidth//2+80:
					if modenamecenter[0]>screenwidth+150:
						modename=False
					else:
						modenamecenter[0]+=40
				else:
					modenamecenter[0]+=1
			else:
				modenamecenter[0]+=70

		if not transitionout.complete:
			transitionout.update()
		if transitionin:
			if not transitionin.complete:
				transitionin.update()
			else:
				return MainMenu(Transition("OUT"))

		# if width!=1536:
		new_screen=pygame.transform.scale(screen,(width,height))
		# else:
		# 	new_screen=screen
		display.blit(new_screen,(dx,dy))
		pygame.display.update()
		pygame.display.set_caption(str(clock.get_fps()))
		clock.tick(60)
	

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

	
MainMenu()
