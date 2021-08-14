import pygame,random,time,pickle,copy,math
pygame.init()

display=pygame.display.set_mode((0,0))
width,height=display.get_rect()[2],display.get_rect()[3]
# width=1280
# height=720
print(width,height)


screen=pygame.Surface((1536,864))
screenwidth=screen.get_width()
screenheight=screen.get_height()

vec=pygame.math.Vector2

scroll=[0,0]
# cloudx=400


sprite1=[pygame.image.load('assets/red1.png').convert_alpha(),pygame.image.load('assets/red2.png').convert_alpha()]
sprite1run=[pygame.image.load('assets/redrun1.png').convert_alpha(),pygame.image.load('assets/redrun2.png').convert_alpha()]
sprite1jump=pygame.image.load('assets/redjump.png').convert_alpha()
sprite1squish=pygame.image.load('assets/redsquish.png').convert_alpha()
sprite1score=pygame.image.load('assets/redscore.png').convert_alpha()
# sprite1=pygame.transform.scale(sprite1,(50,50))
# sprite1=pygame.transform.scale2x(sprite1)
sprite2=[pygame.image.load('assets/green1.png').convert_alpha(),pygame.image.load('assets/green2.png').convert_alpha()]
sprite2run=[pygame.image.load('assets/greenrun1.png').convert_alpha(),pygame.image.load('assets/greenrun2.png').convert_alpha()]
sprite2jump=pygame.image.load('assets/greenjump.png').convert_alpha()
sprite2squish=pygame.image.load('assets/greensquish.png').convert_alpha()
sprite2score=pygame.image.load('assets/greenscore.png').convert_alpha()
# sprite2=pygame.transform.scale(sprite2,(50,50))

# hitframe=pygame.image.load('assets/hitframe.png').convert_alpha()
# hitframe=pygame.transform.scale(hitframe,(50,50))
# sprite2=pygame.transform.scale2x(sprite2)
background1=pygame.image.load('assets/FIRbackground1.png').convert()
background2=pygame.image.load('assets/FIRbackground2.png').convert()
background2.set_colorkey((0,0,0),pygame.RLEACCEL)
# background3=pygame.image.load('FIRbackground3.png').convert()
# background3.set_colorkey((0,0,0),pygame.RLEACCEL)

# clouds1=pygame.image.load('clouds1.png').convert_alpha()
# clouds2=pygame.image.load('clouds2.png').convert_alpha()

# background=background.convert_alpha()
# sf=pygame.image.load('sf.png').convert()
# background=pygame.transform.scale2x(background)
# background=pygame.transform.scale2x(background)
minigun_b=pygame.image.load('assets/minigun-b.png').convert_alpha()
minigun=pygame.image.load('assets/minigun.png').convert_alpha()
sniper=pygame.image.load('assets/sniper.png').convert_alpha()
# sniper=pygame.transform.scale(sniper,(126,30))
sniper=pygame.transform.scale2x(sniper)
rocket=pygame.image.load('assets/rocket.png').convert_alpha()
bazooka=pygame.image.load('assets/bazooka.png').convert_alpha()
pistol_b=pygame.image.load('assets/pistol_b.png').convert_alpha()
deagle=pygame.image.load('assets/deagle.png').convert_alpha()
blue_laser=pygame.image.load('assets/blue_laser.png').convert_alpha()
blaster=pygame.image.load('assets/blaster.png').convert_alpha()
flames=[pygame.image.load('assets/flame'+str(x)+'.png').convert_alpha() for x in range(1,12)]
flamethrower=pygame.image.load('assets/flamethrower.png').convert_alpha()
shotgun=pygame.image.load('assets/shotgun.png').convert_alpha()
# flamethrower=pygame.transform.scale(flamethrower,(int(flamethrower.get_width()*0.8),int(flamethrower.get_height()*0.8)))
screenshake=False


play_button=pygame.image.load('assets/play_button.png').convert_alpha()
play_button_selected=pygame.image.load('assets/play_button_selected.png').convert_alpha()
play_button_pressed=pygame.image.load('assets/play_button_pressed.png').convert_alpha()
options_button=pygame.image.load('assets/options_button.png').convert_alpha()
options_button_selected=pygame.image.load('assets/options_button_selected.png').convert_alpha()
options_button_pressed=pygame.image.load('assets/options_button_pressed.png').convert_alpha()
continue_button=pygame.image.load('assets/continue_button.png').convert_alpha()
continue_button_selected=pygame.image.load('assets/continue_button_selected.png').convert_alpha()
continue_button_pressed=pygame.image.load('assets/continue_button_pressed.png').convert_alpha()
exit_button=pygame.image.load('assets/exit_button.png').convert_alpha()
exit_button_selected=pygame.image.load('assets/exit_button_selected.png').convert_alpha()
exit_button_pressed=pygame.image.load('assets/exit_button_pressed.png').convert_alpha()
particle_button_on=pygame.image.load('assets/particle_button_on.png').convert_alpha()
particle_button_off=pygame.image.load('assets/particle_button_off.png').convert_alpha()
trails_button_on=pygame.image.load('assets/trails_button_on.png').convert_alpha()
trails_button_off=pygame.image.load('assets/trails_button_off.png').convert_alpha()

particlecheck=True
trailcheck=True

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
	def __init__(self,xpos,ypos,idlesprites,runsprites,jumpsprite,squishsprite,scoresprite,scoreboard,color,controls='',weapon=False,weapon_sprite=False,face=False,\
					righthit=False,lefthit=False):

		self.idlesprites=idlesprites
		self.runsprites=runsprites
		self.jumpsprite=jumpsprite
		self.squishsprite=squishsprite
		self.scoresprite=scoresprite
		self.frame=0
		self.sprite=False
		self.rect=pygame.Rect(xpos,ypos,int(self.idlesprites[0].get_width()),(self.idlesprites[0].get_height()))
		
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
		self.controls=controls

		self.weapon=weapon
		self.weapon_sprite=weapon_sprite
		self.face=face
		self.bullets=[]
		self.righthit=righthit
		self.lefthit=lefthit
		self.knockback=0
		self.reloadtimes={"ROCKETLAUNCHER":[1,0],"MINIGUN":[0.2,0],"PISTOL":[0.5,0],"SNIPER":[1.5,0],"SHOTGUN":[0.9,0]}
		self.recoil=0

		self.particles=[]
		self.alive=True
		self.alivetime=0
		self.state=False
		self.color=color
		self.score=0
		self.scoreboard=scoreboard

	def update(self):
		global scrollcheck,weapons,avail_weapons,pause
		# if weapons:
		# 	print(weapons)
		
		keys=pygame.key.get_pressed()
		self.xc,self.yc=0,0
		drift=False


		# self.rect.width=self.sprite.get_width()
		# self.rect.height=self.sprite.get_height()

		

		if self.lefthit:
			self.xc=self.knockback

		elif self.righthit:
			self.xc=-self.knockback

		else:
			if not pause:
				if keys[self.controls[0]]:
					if self.acc<0:
						drift=True
					self.acc+=1
					if self.acc>9:
						self.acc=9
					self.xc=self.acc+self.recoil
					self.face="RIGHT"
					# self.sprite=self.sr
					self.flip=False
					scrollcheck=True
					
				elif keys[self.controls[1]]:
					if self.acc>0:
						drift=True
					self.acc-=1
					if self.acc<-9:
						self.acc=-9
					self.xc=self.acc+self.recoil
					self.face="LEFT"
					# self.sprite=self.sl
					self.flip=True
					scrollcheck=True

				else:
					self.xc=self.recoil
				if keys[self.controls[2]]:
					scrollcheck=True
					if not self.jump and time.monotonic()-self.coyote<0.14:
						self.jumptime=time.monotonic()
						self.state="JUMP"
						self.jump=True
						self.jumpv=37
						self.squishtime=False
				elif keys[self.controls[3]]:
					self.dash=True
					self.jumpv=0
					self.fall=True
					self.jump=False
					self.fallv+=8


					# print(weapons)

		if not self.xc:
			# self.sprite=self.idlesprites[0]

			if self.acc>0:
				self.acc-=1.6
				if self.acc<0:
					self.acc=0
			if self.acc<0:
				self.acc+=1.6
				if self.acc>0:
					self.acc=0
			self.xc=self.acc

			

		self.fall=True

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
			# if self.fallv>35:
			# 	self.jumptime=time.monotonic()
			if self.xc:
				if self.fallv>25:
					self.jumptime=time.monotonic()
			else:					
				if self.fallv>35:
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
			self.xc-=self.recoil
		collisionlist=detect_collisions(self.rect,world,"rect")

		for ob in collisionlist:
			if ob=="COLLIDER":		
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

		if self.rect[0]<-700 or self.rect[0]>2200 or self.rect[1]>screenwidth+300:
			self.opp.score+=1
			self.alive=False
			self.deathtime=time.monotonic()
			self.knockback=0

		collisionlist=detect_collisions(self.rect,world,"rect")

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
						for k in range(self.rect[0],self.rect[0]+self.rect[2],10):
							for o in world:
								if o.state in ('COLLIDER',"PLATFORM"):
									r=pygame.Rect(int(o.ix),int(o.iy),int(o.iw),int(o.ih))
									if r.collidepoint((k,self.rect[1]+self.rect[3])):
										self.particles.append(Trail(self.rect,k,False,"BOTTOM",self.color))

				self.fallv=0
				self.jumpv=37
				self.jump=False
				self.coyote=time.monotonic()
				self.fall=False
				self.state="GROUNDED"
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
							for o in world:
								if o.state in ('COLLIDER',"PLATFORM"):
									r=pygame.Rect(int(o.ix),int(o.iy),int(o.iw),int(o.ih))
									if r.collidepoint((k,self.rect[1]+self.rect[3])):
										self.particles.append(Trail(self.rect,k,False,"BOTTOM",self.color))

			elif self.yc<0 and ob!='PLATFORM':
				self.rect.top=collisionlist[ob].bottom
				self.jumpv=0
				self.fall=True

				if particlecheck:
					self.particles.append(Particle(self.rect,"TOP",False))


				# self.righthit=False
				# self.lefthit=False

		
		if self.recoil>0:
			self.recoil-=0.5
			if self.recoil<0:
				self.recoil=0
		elif self.recoil<0:
			self.recoil+=0.5
			if self.recoil>0:
				self.recoil=0

		if not self.weapon:
			for ob in weapons:
				if weapons[ob][1].colliderect(self.rect):
					self.weapon=ob
					self.weapon_sprite=weapons[ob][0]
					self.currentweapon=weapons[ob]
					# print(self.currentweapon)
			if self.weapon:
			# 	# print(weapons)
				weapons.pop(self.weapon)
				# del thisdict["model"]
		else:
			weaponswap=False
			for ob in weapons:
				if weapons[ob][1].colliderect(self.rect):
					if keys[self.controls[3]]:

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
			if keys[self.controls[4]]:
				if self.weapon=="ROCKETLAUNCHER":
					
					if time.monotonic()-self.reloadtimes["ROCKETLAUNCHER"][1]>self.reloadtimes["ROCKETLAUNCHER"][0]:
						self.acc=0

						if self.face=="RIGHT":
							self.bullets.append(RocketLauncher(pygame.Rect(self.rect[0]+45+10,self.rect[1]-10,rocket.get_width(),rocket.get_height())))
						else:
							self.bullets.append(RocketLauncher(pygame.Rect(self.rect[0]-30,self.rect[1]-10,rocket.get_width(),rocket.get_height())))					

						if self.rect[0]>self.opp.rect[0]:
							if self.xc:
								self.recoil=11
							else:
								self.recoil=8
						else:
							if self.xc:
								self.recoil=-11
							else:
								self.recoil=-8
						self.reloadtimes["ROCKETLAUNCHER"][1]=time.monotonic()

				elif self.weapon=="MINIGUN":
					
					if time.monotonic()-self.reloadtimes["MINIGUN"][1]>self.reloadtimes["MINIGUN"][0]:
						self.acc=0
						ry=random.choice([x for x in range(0,10,2)])

						if self.face=="RIGHT":
							self.bullets.append(Minigun(pygame.Rect(self.rect.center[0]+127,self.rect.center[1]-12+ry,minigun_b.get_width(),minigun_b.get_height()),sprite=minigun_b,rand=(3,5),side="RIGHT"))
							if self.xc:
								self.recoil=-6
							else:
								self.recoil=-4
						else:
							self.bullets.append(Minigun(pygame.Rect(self.rect.center[0]-127,self.rect.center[1]-12+ry,minigun_b.get_width(),minigun_b.get_height()),sprite=minigun_b,rand=(3,5),side="LEFT"))
							if self.xc:
								self.recoil=6
							else:
								self.recoil=4

						self.reloadtimes["MINIGUN"][1]=time.monotonic()


				elif self.weapon=='PISTOL':
					
					if time.monotonic()-self.reloadtimes["PISTOL"][1]>self.reloadtimes["PISTOL"][0]:
						self.acc=0
						if self.face=="RIGHT":
							self.bullets.append(Minigun(pygame.Rect(self.rect[0]+45+10,self.rect[1]+10,pistol_b.get_width(),pistol_b.get_height()),sprite=pistol_b,rand=(1,3),side="RIGHT"))
							if self.xc:
								self.recoil=-8
							else:
								self.recoil=-4
						else:
							self.bullets.append(Minigun(pygame.Rect(self.rect[0]-30,self.rect[1]+10,pistol_b.get_width(),pistol_b.get_height()),sprite=pistol_b,rand=(1,3),side="LEFT"))
							if self.xc:
								self.recoil=8
							else:
								self.recoil=4

						self.reloadtimes["PISTOL"][1]=time.monotonic()

				elif self.weapon=='SHOTGUN':
					
					if time.monotonic()-self.reloadtimes["SHOTGUN"][1]>self.reloadtimes["SHOTGUN"][0]:
						self.acc=0
						if self.face=="RIGHT":
							for k in range(4):
								self.bullets.append(Minigun(pygame.Rect(self.rect[0]+45+10+random.choice([-4,0,4]),self.rect[1]+10+k*2,pistol_b.get_width(),pistol_b.get_height()),sprite=pistol_b,rand=(2,13),side="RIGHT"))
							if self.xc:
								self.recoil=-12
							else:
								self.recoil=-7
						else:
							for k in range(4):
								self.bullets.append(Minigun(pygame.Rect(self.rect[0]-30+random.choice([-4,0,4]),self.rect[1]+10+k*2,pistol_b.get_width(),pistol_b.get_height()),sprite=pistol_b,rand=(2,13),side="LEFT"))
							if self.xc:
								self.recoil=12
							else:
								self.recoil=7

						self.reloadtimes["SHOTGUN"][1]=time.monotonic()


				elif self.weapon=='BLASTER':
					
					if time.monotonic()-self.reloadtimes["PISTOL"][1]>self.reloadtimes["PISTOL"][0]:
						self.acc=0
						if self.face=="RIGHT":
							self.bullets.append(Minigun(pygame.Rect(self.rect[0]+45+10,self.rect[1]+10,blue_laser.get_width(),blue_laser.get_height()),sprite=blue_laser,rand=(1,3),side="RIGHT"))
							if self.xc:
								self.recoil=-8
							else:
								self.recoil=-4
						else:
							self.bullets.append(Minigun(pygame.Rect(self.rect[0]-30,self.rect[1]+10,blue_laser.get_width(),blue_laser.get_height()),sprite=blue_laser,rand=(1,3),side="LEFT"))
							if self.xc:
								self.recoil=8
							else:
								self.recoil=4

						self.reloadtimes["PISTOL"][1]=time.monotonic()


				elif self.weapon=="SNIPER":
					
					if time.monotonic()-self.reloadtimes["SNIPER"][1]>self.reloadtimes["SNIPER"][0]:
						self.acc=0
						if self.face=="RIGHT":
							self.bullets.append(Sniper(pygame.Rect(self.rect[0]+45+10,self.rect[1]-10,minigun_b.get_width(),minigun_b.get_height()),self.opp.rect,minigun_b))
						else:
							self.bullets.append(Sniper(pygame.Rect(self.rect[0]-30,self.rect[1]-10,minigun_b.get_width(),minigun_b.get_height()),self.opp.rect,minigun_b))

						
						if self.rect[0]>self.opp.rect[0]:
							if self.xc:
								self.recoil=12
							else:
								self.recoil=7
						else:
							if self.xc:
								self.recoil=-12
							else:
								self.recoil=-7
						self.reloadtimes["SNIPER"][1]=time.monotonic()


				elif self.weapon=="FLAMETHROWER":
					# self.acc=0
					
					if self.face=="RIGHT":
						for k in range(4):
							self.particles.append(Flame(self.rect[0]+132,self.rect.center[1]-12,self.face))
						self.recoil=-1.3
					else:
						for k in range(4):
							self.particles.append(Flame(self.rect[0]-96,self.rect.center[1]-12,self.face))
						self.recoil=1.3





		# if click:
		# 	if self.weapon=='ROCKETLAUNCHER':
		# 		self.bullets.append([rocket,pygame.Rect(self.rect[0]+10+45,self.rect[1]+10+45,rocket.get_width(),rocket.get_height()),time.monotonic(),time.monotonic(),self.face])
		# follow=self.opp[0]
		######## BULLET ANIMATION AND DISPLAY ##########

		if self.bullets:

			for bullet in self.bullets:
				bullet.update(self.opp)

			self.bullets=[b for b in self.bullets if not b.rect.colliderect(self.opp.rect) and not detect_collisions(b.rect,world,'mask',b.mask)\
					and b.rect[0]<2500 and b.rect[0]>-1000]


		######## CHARACTER ANIMATION & DISPLAY ##########

		self.frame+=0.06
		if self.frame>2:
			self.frame=0

		if pause:
			self.sprite=self.idlesprites[0]
		elif self.state=="GROUNDED":
			self.offsety=0
			if self.squishtime and time.monotonic()-self.squishtime<0.16 and time.monotonic()-self.squishtime>0.02:
				self.sprite=self.squishsprite
				self.offsetx=4
			elif self.xc in (-9,9):
				self.sprite=self.runsprites[int(self.frame)]
				self.offsetx=0
			else:
				self.sprite=self.idlesprites[int(self.frame)]
				self.offsetx=0
		else:
			if time.monotonic()-self.jumptime<0.2:
				self.sprite=self.jumpsprite
				self.offsety=0
			else:
				self.sprite=self.idlesprites[0]
				self.offsety=0
				self.offsetx=0

		screen.blit(pygame.transform.flip(self.sprite,self.flip,False),(self.rect[0]-self.offsetx-scroll[0],self.rect[1]-self.offsety-scroll[1]))


		######## WEAPON ANIMATION & DISPLAY #############

		if self.weapon_sprite:
			if self.weapon_sprite==bazooka or self.weapon_sprite==sniper:

				if self.rect[0]>self.opp.rect[0]:
					self.new=pygame.transform.flip(self.weapon_sprite,True,False)

					angle=math.atan2(-( self.rect.center[1]-(self.opp.rect.center[1]) ),( self.rect.center[0]-(self.opp.rect.center[0]) ))
					angle=math.degrees(angle)
					self.new=pygame.transform.rotate(self.new,angle)

					screen.blit(self.new,(self.rect.center[0]-scroll[0]-self.new.get_width()//2,self.rect.center[1]-scroll[1]+5-self.new.get_height()//2))
					
				else:
					angle=math.atan2(-( self.opp.rect.center[1]-(self.rect.center[1]) ),( self.opp.rect.center[0]-(self.rect.center[0]) ))
					angle=math.degrees(angle)
				
					self.new=pygame.transform.rotate(self.weapon_sprite,angle)

					screen.blit(self.new,(self.rect.center[0]-scroll[0]-self.new.get_width()//2,self.rect.center[1]-scroll[1]+5-self.new.get_height()//2))

			else:
				if self.face=="RIGHT":
					screen.blit(self.weapon_sprite,(self.rect[0]+self.rect[2]-scroll[0]-self.weapon_sprite.get_width()//2,self.rect.center[1]-scroll[1]+10-self.weapon_sprite.get_height()//2))
				else:
					screen.blit(pygame.transform.flip(self.weapon_sprite,True,False),(self.rect[0]-scroll[0]-self.weapon_sprite.get_width()//2,self.rect.center[1]-scroll[1]+10-self.weapon_sprite.get_height()//2))
				

		######## PARTICLE ANIMATION AND DISPLAY #########

		if self.particles:

			for part in self.particles:
				part.update(self.opp)
			self.particles=[p for p in self.particles if p.size>1]





# play1copy=copy.deepcopy(play1)
# play2copy=copy.deepcopy(play2)

############################################################################################################################################
############################################################################################################################################

class RocketLauncher:
	def __init__(self,rect,sprite=rocket,mask=pygame.mask.from_surface(rocket)):

		self.sprite=sprite
		self.mask=mask
		self.rect=rect
		self.pos=vec(self.rect.center)
		self.vel = vec(0,0)
		self.acc = vec(0, 0)
		self.rand=(random.randint(4+4,6+4)*random.choice([0.1,-0.1]),random.randint(4+4,6+4)*random.choice([0.1,-0.1]))

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

			angle=math.atan2(-(opp.rect[1]-self.rect[1]),(opp.rect[0]-self.rect[0]))

			angle=math.degrees(angle)-90
			self.rot_sprite=pygame.transform.rotate(self.sprite,angle)
			self.rect=self.rot_sprite.get_rect(center=self.pos)
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
					

			if detect_collisions(self.rect,world,'mask',self.mask):
				if self.vel[0]>0:
					for x in range(30):
						opp.particles.append(Particle(self.rect,'RIGHT',dx=[x for x in range(1,-8-2)]))
				elif self.vel[0]<0:
					for x in range(30):
						opp.particles.append(Particle(self.rect,'LEFT',dx=[x for x in range(-1,8,2)]))

		screen.blit(self.rot_sprite,(self.rect[0]-scroll[0],self.rect[1]-scroll[1]))

############################################################################################################################################
############################################################################################################################################

class Minigun:
	def __init__(self,rect,sprite,side=False,rand=False):

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
		self.rect=self.sprite.get_rect(center=self.pos)
		# self.rect[1]+=random.randint(1,8)*random.choice([-1,1])
		self.mask=pygame.mask.from_surface(self.sprite)

		self.rand=(random.randint(4,6)*random.choice([0.1,-0.1]),random.randint(4,6)*random.choice([0.1,-0.1]))

	def update(self,opp):
		global screenshake
		if not pause:
			self.pos += self.vel

			self.rect.center = self.pos

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

			if detect_collisions(self.rect,world,'mask',self.mask):
				if self.vel[0]>0:
					for x in range(10):
						opp.particles.append(Particle(self.rect,'RIGHT',[x for x in range(-90,-100-2)],decay=0.2))
				elif self.vel[0]<0:
					for x in range(10):
						opp.particles.append(Particle(self.rect,'LEFT',[x for x in range(-1,6,2)],decay=0.2))

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
		self.rect=self.sprite.get_rect(center=self.pos)
		self.mask=pygame.mask.from_surface(self.sprite)


	def update(self,opp):
		global screenshake
		if not pause:
			self.pos += self.vel

			self.rect.center = self.pos

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

			if detect_collisions(self.rect,world,'mask',self.mask):
				if self.vel[0]>0:
					for x in range(10):
						opp.particles.append(Particle(self.rect,'RIGHT',dx=[x for x in range(1,-6-2)]))
				elif self.vel[0]<0:
					for x in range(10):
						opp.particles.append(Particle(self.rect,'LEFT',dx=[x for x in range(-1,6,2)]))

		screen.blit(self.sprite,(self.rect[0]-scroll[0],self.rect[1]-scroll[1]))

############################################################################################################################################
############################################################################################################################################

class Flame:
	def __init__(self,x,y,side):
		if side=="RIGHT":
			self.side=1
		else:
			self.side=-1
		self.size=random.randint(5,6)
		self.rect=pygame.Rect(x,y,self.size,self.size)
		self.distance=0
		self.lifetime=random.choice([0.5,1,1.5,2])
		self.decay=time.monotonic()

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
						for x in range(30):
							opp.particles.append(Blood(opp.rect,'LEFT',opp.color))
						screenshake=("hit",time.monotonic())
				elif self.side==-1:
					if not opp.righthit:
						opp.righthit=True
						for x in range(30):
							opp.particles.append(Blood(opp.rect,'RIGHT',opp.color))
						screenshake=("hit",time.monotonic())
				opp.jump=True
				opp.jumpv=40
				opp.knockback=10
				opp.fallv=0
			
			if self.size<=1:
				self.size=1
			# self.rect.size=(int(self.size),int(self.size))
			self.color=pygame.transform.scale(self.color,(int(self.size)*4,int(self.size)*4))

		self.copy=self.rect.copy()
		self.copy[0]-=scroll[0]
		self.copy[1]-=scroll[1]

		# pygame.draw.rect(screen,self.color,self.copy)
		self.color.set_colorkey((0,0,0),pygame.RLEACCEL)
		# screen.blit(self.color,self.copy)
		# self.color.set_colorkey((255,255,255))
		# surf.set_colorkey((0, 0, 0))
		screen.blit(self.color,self.copy,special_flags=pygame.BLEND_RGB_ADD)



############################################################################################################################################
############################################################################################################################################


class Particle:
	def __init__(self,t,side,dx,decay=0.25,rand=(1,2),size=False,color=False):
		if size:
			self.size=size
		else:
			self.size=random.randint(5,8)
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

	def update(self,opp):
		if not pause:
		
			self.rect[1]+=self.vel
			self.rect[0]+=random.choice(self.dx)
			self.vel+=0.3
			self.size=self.size-self.decay
			if self.size<=1:
				self.size=1
			self.rect.size=(int(self.size),int(self.size))

		pygame.draw.rect(screen,self.color,self.rect)

class Blood:
	def __init__(self,t,side,color,decay=0.008,rand=(2,7)):

		self.radius=random.randint(4,6)
		self.size=self.radius*2
		self.decay=decay

		if side=='RIGHT':
			# self.rect=pygame.Rect( random.randint(t[0]-1,t[0]+1) , random.randint(t[1]-1, t[1]+t[3]+1)   ,self.size,self.size)
			self.center=[ random.randint(t[0]-1,t[0]+1) , random.randint(t[1]-1, t[1]+t[3]+1)]

			self.dx=[x for x in range(3,11,2)]


		elif side=="LEFT":
			# self.rect=pygame.Rect( random.randint(t[0]+t[2]-1,t[0]+t[2]+1) , random.randint(t[1]-1, t[1]+t[3]+1)   ,self.size,self.size)
			self.center=[ random.randint(t[0]+t[2]-1,t[0]+t[2]+1) , random.randint(t[1]-1, t[1]+t[3]+1)]

			self.dx=[x for x in range(-3,-11,-2)]


		self.vel=random.randint(rand[0],rand[1])*-1
		self.yvel=True
		
		self.color=color
	def update(self,opp):
		if not pause:
			if self.yvel:
				self.center[1]+=self.vel
			if self.dx:
				self.center[0]+=random.choice(self.dx)

			self.vel+=0.3
			self.size=self.size-self.decay
			# if self.size<5:
			# 		self.decay=random.choice([x for x in range(5,7)])/10
			if self.size<=1:
				self.size=1
			# self.rect.size=(int(self.size),int(self.size))
			self.radius=int(self.size)/2

			# collisionlist=detect_collisions(pygame.Rect(),world,"rect")


			for ob in world:
				r=pygame.Rect(ob.ix,ob.iy,ob.iw,ob.ih)
				if r.collidepoint(self.center):
					if self.center[1]-self.radius>r.top:
						self.center[1]=r.top+self.radius
						self.dx=0
						self.decay=0.02
						self.yvel=False


		# self.copy=self.rect.copy()
		# self.copy[0]-=scroll[0]
		# self.copy[1]-=scroll[1]
		# pygame.draw.rect(screen,self.color,self.copy)

		self.copy=(self.center[0]-scroll[0],self.center[1]-scroll[1])

		
		pygame.draw.circle(screen,self.color,self.copy,self.radius)


############################################################################################################################################
############################################################################################################################################


class Snow:
	def __init__(self,position,extend,y=False):

		if extend:
			if extend==1:
				self.x=random.randint(-500,screenwidth)
				# self.x=random.randint(100,101)
			else:
				self.x=random.randint(0,screenwidth+500)
				# self.x=random.randint(1000,1001)
		else:
			self.x=random.randint(-200,screenwidth+200)
		if not y:
			if self.x>screenwidth or self.x<0:
				self.y=random.randrange(50,screenheight//2)
			else:
				self.y=-50
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

		self.offset=random.choice([1,1.1,1.2,0.9,0.8])
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
			self.rect[0]+=random.choice(self.speed)

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
	def __init__(self,player,x,y,side,color):
		self.side=side
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
		

		self.copy=(self.center[0]-scroll[0],self.center[1]-scroll[1])

		
		pygame.draw.circle(screen,self.color,self.copy,self.radius)





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


	
def detect_collisions(rect,objects,check,mask=False):
	collisionlist={}
	if check=='rect':
		for o in objects:
			if o.state in ("COLLIDER","PLATFORM"):
				r=pygame.Rect(int(o.ix),int(o.iy),int(o.iw),int(o.ih))
				if rect.colliderect(r):
					collisionlist[o.state]=r
					break

	else:
		for o in objects:
			if o.state=="COLLIDER":
				r=pygame.Rect(int(o.ix),int(o.iy),int(o.iw),int(o.ih))
				if rect.colliderect(r):
					offset=(r[0]-rect[0],r[1]-rect[1])
					if mask.overlap(worldmasks[o.name],offset):
						return True

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

def screen_shake(weapon=False):
	if weapon:
		return random.choice([-1,1]),random.choice([-1,1])
	else:
		return random.choice([x for x in range(-11,11,3)]),random.choice([x for x in range(-11,11,3)])



clock=pygame.time.Clock()

def MainMenu():
	global particlecheck,trailcheck,pause

	play_button_rect=play_button.get_rect(center=(screenwidth/2,screenheight/2))
	options_button_rect=options_button.get_rect(centerx=screenwidth/2,top=play_button_rect.bottom+20)
	exit_button_rect=exit_button.get_rect(centerx=screenwidth/2,top=options_button_rect.bottom+20)
	particle_button_rect=particle_button_on.get_rect(center=(screenwidth/2,screenheight/2))
	trails_button_rect=trails_button_on.get_rect(top=particle_button_rect.bottom+20,left=particle_button_rect.left)

	selected = "PLAY"
	running=True
	click=False
	enter=False
	optionscreen=False
	pause=False
	snow=[]
	snowy=-200




	snowtime=time.monotonic()
	snowduration=[1,2,4,6,7]
	snowcurrentduration=random.choice(snowduration)
	snowdirection=[-1,1]
	snowcurrentdirection=random.choice(snowdirection)
	snowacc=[0.01,0.08,0.03]
	snowcurrentacc=random.choice(snowacc)



	for x in range(80):
		snow.append(Snow(random.choice(['FRONT',"MID","BACK"]),False,snowy))
		snowy+=screenheight/60
	while running:
		clock.tick(60)
		mousepos=list(pygame.mouse.get_pos())
		mousepos[0]*=1536/width
		mousepos[1]*=864/height

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False

			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					optionscreen=False

			elif event.type==pygame.MOUSEBUTTONDOWN:
				if event.button==1:
					for k in [play_button_rect,options_button_rect,exit_button_rect,particle_button_rect,trails_button_rect]:
						if k.collidepoint(mousepos):
							click=True
			elif event.type==pygame.MOUSEBUTTONUP:
				if event.button==1:
					if click:
						click=False
						if selected=="PLAY":
							Game()
							return
						elif selected=="EXIT":
							running=False
						elif selected=="OPTIONS":
							optionscreen=True
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


					else:
						enter=False



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

			# for x in snow:
			# 	x.update()

		snow=[x for x in snow if x.rect[1]<screenheight+100]

		# if play_button_rect.collidepoint(mousepos):
		# 	selected="PLAY"
		# elif options_button_rect.collidepoint(mousepos):
		# 	selected="OPTIONS"
		# elif exit_button_rect.collidepoint(mousepos):
		# 	selected="EXIT"
		# if particle_button_rect.collidepoint(mousepos):
		# 	selected="PARTICLES"
		# elif trails_button_rect.collidepoint(mousepos):
		# 	selected="TRAILS"

		if not optionscreen:
			if play_button_rect.collidepoint(mousepos):
				selected="PLAY"
			elif options_button_rect.collidepoint(mousepos):
				selected="OPTIONS"
			elif exit_button_rect.collidepoint(mousepos):
				selected="EXIT"
			
			if selected=="PLAY":
				if click:
					screen.blit(play_button_pressed,(play_button_rect))

						
				else:
					screen.blit(play_button_selected,(play_button_rect))
				
			else:
				screen.blit(play_button,(play_button_rect))

			if selected=="OPTIONS":
				if click:
					screen.blit(options_button_pressed,(options_button_rect))
				else:
					screen.blit(options_button_selected,(options_button_rect))

			else:
				screen.blit(options_button,(options_button_rect))

			if selected=="EXIT":
				if click:
					screen.blit(exit_button_pressed,(exit_button_rect))
				else:
					screen.blit(exit_button_selected,(exit_button_rect))


			else:
				screen.blit(exit_button,(exit_button_rect))

		else:
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

		new_screen=pygame.transform.scale(screen,(width,height))
		display.blit(new_screen,(0,0))
		pygame.display.update()
		
	pygame.quit()

def Game():

	global scroll,world,screenshake,weapons,avail_weapons,pause,particlecheck,trailcheck
	snow=[]
	snowy=-200
	avail_weapons=[["MINIGUN",minigun,False],['SNIPER',sniper,False],['ROCKETLAUNCHER',bazooka,False],["PISTOL",deagle,False],['BLASTER',blaster,False],["FLAMETHROWER",flamethrower,False],["SHOTGUN",shotgun,False]]
	weapon_time=time.monotonic()
	weapon_spawn=5
	weapons={}
	weaponx=[x for x in range(-200,1900,300)]
	running=True
	pause=False
	win=False
	win_alpha=0
	wintime=False

	youwin=pygame.image.load('assets/youwin.png').convert_alpha()
	pink_scoreboard=pygame.image.load('assets/pink_scoreboard.png').convert_alpha()
	pink_scoreboard.set_alpha(180)
	pink_scoreboard_rect=pink_scoreboard.get_rect(topleft=(30+20,50))
	green_scoreboard=pygame.image.load('assets/green_scoreboard.png').convert_alpha()
	green_scoreboard.set_alpha(180)
	green_scoreboard_rect=green_scoreboard.get_rect(topleft=(screenwidth-green_scoreboard.get_width()-30+20,50))
	pink_score,green_score=0,0
	pink_score_x=200
	green_score_x=screenwidth-300

	play1=Player(450,-150,controls=[pygame.K_d,pygame.K_a,pygame.K_w,pygame.K_s,1073742049],idlesprites=sprite1,runsprites=sprite1run,jumpsprite=sprite1jump,squishsprite=sprite1squish,scoresprite=sprite1score,face="RIGHT",color=(229,58,255),scoreboard=[sprite1[0].get_rect(topleft=(x,58)) for x in range(66,325,64)])
	play2=Player(930,-150,controls=[1073741918,1073741916,1073741920,1073741917,1073741912],idlesprites=sprite2,runsprites=sprite2run,jumpsprite=sprite2jump,squishsprite=sprite2squish,scoresprite=sprite2score,face="LEFT",color=(46,255,108),scoreboard=[sprite1[0].get_rect(topleft=(x,58)) for x in range(66+screenwidth-400,325+screenwidth-400,64)])

	play1.opp=play2
	play2.opp=play1

	snowtime=time.monotonic()
	snowduration=[1,2,4,6,7]
	snowcurrentduration=random.choice(snowduration)
	snowdirection=[-1,1]
	snowcurrentdirection=random.choice(snowdirection)
	snowacc=[0.01,0.09,0.05]
	snowcurrentacc=random.choice(snowacc)

	# menu=pygame.Surface()
	for x in range(80):
		snow.append(Snow(random.choice(['FRONT',"MID","BACK"]),False,snowy))
		snowy+=screenheight/60
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
				# print(event.key)
				if event.key==pygame.K_l:
					with open("FIRleveleditor.dat",'wb') as f1:
						pickle.dump(world,f1)
				elif event.key==pygame.K_RETURN:
					scrollcheck=True
					play1.rect[0]=int(450)
					play1.rect[1]=int(-150)
					play2.rect[0]=int(930)
					play2.rect[1]=int(-150)
					play1.alive=True
					play2.alive=True
				elif event.key==pygame.K_ESCAPE:
					pause=True
					continue_button_rect=continue_button.get_rect(center=(screenwidth/2+20,screenheight/2-80))
					options_button_rect=options_button.get_rect(centerx=screenwidth/2+20,top=continue_button_rect.bottom+20)
					exit_button_rect=exit_button.get_rect(centerx=screenwidth/2+20,top=options_button_rect.bottom+20)
					particle_button_rect=particle_button_on.get_rect(center=(screenwidth/2+20,screenheight/2+20))
					trails_button_rect=trails_button_on.get_rect(top=particle_button_rect.bottom+20,left=particle_button_rect.left)

					selected = "CONTINUE"
					running=True
					click=False
					enter=False
					optionscreen=False
					while pause:
						for event in pygame.event.get():



							if event.type==pygame.QUIT:
								running=False

							elif event.type==pygame.KEYDOWN:
								if event.key==pygame.K_ESCAPE:
									pause=False


							elif event.type==pygame.MOUSEBUTTONDOWN:
								if event.button==1:
									for k in [continue_button_rect,options_button_rect,exit_button_rect,particle_button_rect,trails_button_rect]:
										if k.collidepoint(mousepos):
											click=True
									# click=True
							elif event.type==pygame.MOUSEBUTTONUP:
								if event.button==1:
									if click:
										click=False
										if selected=="CONTINUE":
											pause=False
										elif selected=="EXIT":
											running=False
											pause=False
										elif selected=="OPTIONS":
											optionscreen=True
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
									else:
										enter=False

						screen.blit(background1,(-250-(scroll[0]/11),-370+50-(scroll[1]/20)))
						screen.blit(background2,(-200-(scroll[0]/5),-200-(scroll[1]/7)))

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

						mousepos=list(pygame.mouse.get_pos())
						mousepos[0]*=1536/width
						mousepos[1]*=864/height

						if not optionscreen:
							if continue_button_rect.collidepoint(mousepos):
								selected="CONTINUE"
							elif options_button_rect.collidepoint(mousepos):
								selected="OPTIONS"
							elif exit_button_rect.collidepoint(mousepos):
								selected="EXIT"
							
							if selected=="CONTINUE":
								if click:
									screen.blit(continue_button_pressed,(continue_button_rect))
										
								else:
									screen.blit(continue_button_selected,(continue_button_rect))
								
							else:
								screen.blit(continue_button,(continue_button_rect))

							if selected=="OPTIONS":
								if click:
									screen.blit(options_button_pressed,(options_button_rect))
								else:
									screen.blit(options_button_selected,(options_button_rect))

							else:
								screen.blit(options_button,(options_button_rect))

							if selected=="EXIT":
								if click:
									screen.blit(exit_button_pressed,(exit_button_rect))
								else:
									screen.blit(exit_button_selected,(exit_button_rect))

							else:
								screen.blit(exit_button,(exit_button_rect))

						else:
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

						new_screen=pygame.transform.scale(screen,(width,height))
						display.blit(new_screen,(0,0))
						pygame.display.update()







				elif event.key==pygame.K_SPACE:
					print(clock.get_fps())
					print(play1.score)
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
				scroll[0]+=(((play1.rect[0]+play2.rect[0])//2)-scroll[0]-(screenwidth/2))/40
				scroll[1]+=(((play1.rect[1]+play2.rect[1])//2-70)-scroll[1]-(screenheight/2))/40

			else:

				scroll[0]+=(((play1.rect[0]+play2.rect[0])//2+20)-scroll[0]-(screenwidth/2))/15
				scroll[1]+=(((play1.rect[1]+play2.rect[1])//2-70)-scroll[1]-(screenheight/2))/20
			if scroll[0]<-300:
				scroll[0]=-300
			elif scroll[0]>340:
				scroll[0]=340
			
			if scroll[1]<-120:
				scroll[1]=-120
		elif play1.alive:
			scroll[0]+=((play1.rect[0])-scroll[0]-(screenwidth/2))/50
			scroll[1]+=((play1.rect[1]+20)-scroll[1]-(screenheight/2))/50
		elif play2.alive:
			scroll[0]+=((play2.rect[0])-scroll[0]-(screenwidth/2))/50
			scroll[1]+=((play2.rect[1]+20)-scroll[1]-(screenheight/2))/50

			
		# keys=pygame.key.get_pressed()
		# mice=pygame.mouse.get_pressed()
		
		# cloudx-=0.1
		screen.blit(background1,(-250-(scroll[0]/11),-370+50-(scroll[1]/20)))
		screen.blit(background2,(-200-(scroll[0]/5),-200-(scroll[1]/7)))
		# screen.blit(background3,(-200-(scroll[0]/5),-250+20-(scroll[1]/5)))
		# screen.blit(clouds1,(-350-(scroll[0]/9)+cloudx,-200-(scroll[1]/17)))
		# screen.blit(clouds2,(-650-(scroll[0]/8)+cloudx*2.2,-200-(scroll[1]/16)))




		for ob in world:

			screen.blit(assetnames[ob.name],(int((ob.ix-scroll[0])),int((ob.iy-scroll[1]))))
		for ob in worldextra:

			screen.blit(assetnames[ob.name],(int((ob.ix-scroll[0])),int((ob.iy-scroll[1]))))

		if win:
			if time.monotonic()-wintime>2:
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
							win.particles.append(Flame(r[0]+r[2]+x+scroll[0],y+scroll[1],"LEFT"))
							x-=10
				else:
					return MainMenu()


		if play1.alive:
			play1.update()
		else:
			if time.monotonic()-play1.deathtime>2:
				if play2.score<5:
					play1.rect.topleft=(play1.xpos,play1.ypos)
					play1.alive=True
					play1.alivetime=time.monotonic()
				else:
					if not win:
						win=play2
						wintime=time.monotonic()

		if play2.alive:
			play2.update()
		else:
			if time.monotonic()-play2.deathtime>2:
				if play1.score<5:
					play2.rect.topleft=(play2.xpos,play2.ypos)
					play2.alive=True
					play2.alivetime=time.monotonic()
				else:
					if not win:
						win=play1
						wintime=time.monotonic()

		screen.blit(pink_scoreboard,pink_scoreboard_rect)
		screen.blit(green_scoreboard,green_scoreboard_rect)

		

		if play1.score:
			for k in range(play1.score):
				screen.blit(play1.scoresprite,play1.scoreboard[k])
		if play2.score:
			for k in range(play2.score):
				screen.blit(play2.scoresprite,play2.scoreboard[k]) 
		if weapon_spawn:
			if time.monotonic()-weapon_time>weapon_spawn:
				weapon_time=time.monotonic()
				if weapon_spawn==5:
					weapon_spawn=4					
				else:
					weapon_spawn=random.randrange(15,20)
				w=random.choice(avail_weapons)
				if len(avail_weapons)==1:
					weapon_spawn=False
				avail_weapons.remove(w)

				if weaponx:
					x=random.choice(weaponx)
					weaponx.remove(x)
				else:
					while True:
						x=random.randrange(-200,1900,350)+70
						xlist=[weapons[ob][1].center[0] for ob in weapons]
						if x in xlist:
							continue					
						break

				
				w[2]=w[1].get_rect(center=(x+70,-300))
				weapons[w[0]]=[w[1],w[2]]

		# print(weapons)
		for wp in weapons.values():
			wp[1][1]+=3
			collisionlist=detect_collisions(wp[1],world,'rect')
			for ob in collisionlist:
				wp[1].bottom=collisionlist[ob].top

			screen.blit(wp[0],(wp[1][0]-scroll[0],wp[1][1]-scroll[1]))





		snowfall=random.choice([1,2,3,4,4,4,4,4,4,4,4,4])
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
				if time.monotonic()-screenshake[1]<0.2:
					dx,dy=screen_shake()
				else:
					screenshake=False
			else:
				if time.monotonic()-screenshake[1]<0.2:
					dx,dy=screen_shake(True)
				else:
					screenshake=False
		# if width!=1536:
		new_screen=pygame.transform.scale(screen,(width,height))
		# else:
		# 	new_screen=screen
		display.blit(new_screen,(dx,dy))
		pygame.display.update()
		pygame.display.set_caption(str(clock.get_fps()))
		clock.tick(60)
	pygame.quit()

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################


MainMenu()
