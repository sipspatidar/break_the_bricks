import pygame
import timeit
import time

screen_width = 600
screen_height = 600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
pygame.init()
gameDisplay = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("tiles_broken")
clock = pygame.time.Clock()

sound = pygame.mixer.Sound("break3.wav")
leve_bg_img = pygame.image.load("level_bg.png")
def crash():
	pygame.quit()
	quit()
	
	
def display_message(size,text,color,x,y):
	font = pygame.font.Font("freesansbold.ttf",size)
	text = font.render(str(text),True,color)
	text_rect = text.get_rect()
	text_rect.center = (x,y)
	gameDisplay.blit(text,text_rect)

def complete():
	time.sleep(5)
	crash()

class Levels:
	level_1 = "wwwww@wwwww"
	level_2 = "wwwww@wsssw@wwwww"
	level_3 = "wwwww@wdddw@wwwww"
	level_4 = "dwwwd@dsssd@dwwwd"
	level_5 = "ddddd@ddddd@ddddd"
	level_6 = "wwwww@wsssw@wwwww"
	level_7 = "wwwww@wsssw@wwwww"
	level_8 = "wwwww@wsssw@wwwww"
	level_9 = "wwwww@wsssw@wwwww"
	level_10 = "wwwww@wsssw@wwwww"

class Front:

	def __init__(self):
	
		self.intro_img = pygame.image.load("intro.png").convert_alpha() 
		self.start_img = pygame.image.load("play.png").convert_alpha() 
		self.level_img = pygame.image.load("level.png").convert_alpha() 
		self.exit_img = pygame.image.load("exit.png").convert_alpha() 
		self.bg_img = pygame.image.load("background.jpeg").convert_alpha() 
		self.name_img = pygame.image.load("name.png").convert_alpha() 
		self.intro_rect = self.intro_img.get_rect()
		self.start_rect = self.start_img.get_rect()
		self.level_rect = self.level_img.get_rect()
		self.exit_rect = self.exit_img.get_rect()
		self.bg_rect = self.bg_img.get_rect()
		self.name_rect = self.name_img.get_rect()
		self.intro_rect.center = (300,300)
		self.start_rect.center = (300,300)
		self.level_rect.center = (300,400)
		self.exit_rect.center = (300,500)
		self.bg_rect.center = (300,300)
		self.name_rect.center = (300,150)
		clock.tick(30)
		gameDisplay.blit(self.intro_img,self.intro_rect)
		pygame.display.update()
		
		time.sleep(3)
			
	def draw_levels(self):
		level = pygame.image.load("level_img.png")
		
		while True:
			for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						quit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_KP_ENTER:
							intro = False
			gameDisplay.fill(white)
			display_message(50,"Levels",red,screen_width/2,50)
			
			a = 100
			b = 200
			pygame.draw.rect(gameDisplay,red,(50,100,500,450))
			for x in range(0,2):
				for y in range(0,3):
					gameDisplay.blit(level,(a,b,100,90))
					display_message(50,str(int(y+1)+(x*3)),red,a+50,b+40)
					a += 150
				a = 100
				b += 200
				
			pygame.display.update()
			clock.tick(50)
		
		
	
	def page(self):
		intro = True
		while intro:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_KP_ENTER:
						intro = False
			
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
		
		
			if self.start_rect.x < mouse[0] < self.start_rect.x+100 and self.start_rect.y < mouse[1] < self.start_rect.y+50:
				if click[0] == 1:
					intro = False
			if self.level_rect.x < mouse[0] < self.level_rect.x+100 and self.level_rect.y < mouse[1] < self.level_rect.y+50:
				if click[0] == 1:
					self.draw_levels()
			if self.exit_rect.x < mouse[0] < self.exit_rect.x+100 and self.exit_rect.y < mouse[1] < self.exit_rect.y+50:
				if click[0] == 1:
					pygame.quit()
					quit()
			
			gameDisplay.fill(black)
			gameDisplay.blit(self.bg_img,self.bg_rect)
			gameDisplay.blit(self.name_img,self.name_rect)
			
			
			gameDisplay.blit(self.start_img,self.start_rect)
			gameDisplay.blit(self.level_img,self.level_rect)
			gameDisplay.blit(self.exit_img,self.exit_rect)
			pygame.display.update()
			clock.tick(50)
		
		
class Player:
	
	speed = 50
	width = 100
	height = 10
	def __init__(self):
		self.rect = pygame.Rect((screen_width/2)-(Player.width/2),screen_height-20,Player.width,Player.height)
		self.player_img = pygame.image.load("paddel.png")
	def draw_player(self):
		gameDisplay.blit(self.player_img,self.rect)
	def move_left(self):
		if not self.check_left():
			self.rect.left -= Player.speed 
	def move_right(self):
		if not self.check_right():
			self.rect.right += Player.speed 
	def check_left(self):
		if self.rect.x <= 0:
			return True
		else:
			return False
	def check_right(self):
		if self.rect.x+Player.width >= screen_width:
			return True
		else:
			return False
	def reset(self):
		self.rect.x = (screen_width/2)-(Player.width/2)
		self.rect.y = screen_height-20
		
		
		
class Ball:
	width = 10
	height = 10
	def __init__(self):
		self.rect = pygame.Rect((screen_width/2)-(Ball.width/2),screen_height-30,Ball.width,Ball.height)
		self.speed_x = 1
		self.speed_y = 2
		self.ball_img = pygame.image.load("ball1.png")
	def draw_ball(self):
		gameDisplay.blit(self.ball_img,self.rect)
	def move(self):
		self.rect.x -= self.speed_x
		self.rect.y -= self.speed_y
	def change_dir_x(self):
		self.speed_x = - self.speed_x
	def change_dir_y(self):
		self.speed_y = - self.speed_y

	def check(self):
		if ball.rect.colliderect(player.rect):
			self.speed_y = - self.speed_y
		if self.rect.x <= 0 or self.rect.x+Ball.width >= screen_width:
			self.speed_x = - self.speed_x
		if self.rect.y <= 45:
			self.speed_y = - self.speed_y
		if self.rect.y+Ball.height >= screen_height:
			crash()
	
	def reset(self):
		self.rect.x = screen_width/2
		self.rect.y = screen_height-30
		self.speed_x = 1
		self.speed_y = 2
			
	
	
class Bricks:
	pos_x = 50
	pos_y = 100
	
	def __init__(self):
		self.width = 90
		self.height = 30
		self.space = 10
		self.brick_no = 10
		self.rect = pygame.Rect(Bricks.pos_x,Bricks.pos_y,self.width,self.height)
		self.brick_value = [[1 for a in range(0,5)],[1 for a in range(0,5)]]
		self.rect_map = [[],[]]
		self.brick_img = pygame.image.load("brick.png")
		self.brick_img2 = pygame.image.load("cement.png")
		
	def set_map(self):
		x = 50
		y = 100
		self.rect = pygame.Rect(x,y,self.width,self.height)
		for m in range(0,len(self.brick_value)):
			for n in range(0,len(self.brick_value[m])):
				self.rect = pygame.Rect(x,y,self.width,self.height)
				self.rect_map[m].append(self.rect)
				x += self.width+self.space 				
			y += self.height+self.space
			x = Bricks.pos_x
		self.rect = pygame.Rect(Bricks.pos_x,Bricks.pos_y,self.width,self.height)		
	
	
	
	def draw(self):
		for x in range(0,len(self.brick_value)):
			for y in range(0,len(self.brick_value[x])):
				if self.brick_value[x][y] == 1:
					gameDisplay.blit(self.brick_img,self.rect)
				if self.brick_value[x][y] == 2:
					gameDisplay.blit(self.brick_img2,self.rect)
				self.rect.x += self.width+self.space
			self.rect.y += self.height+self.space
			self.rect.x = Bricks.pos_x
		self.rect.x = Bricks.pos_x
		self.rect.y = Bricks.pos_y
		
		
		
	def change_level(self,level):
		level += 1 
		a = []
		b = []
		c = []
		self.brick_no = 0
		level_lines = []
		if level == 2:
			level_lines = Levels.level_2.split('@')
			print(level_lines)
		elif level == 3:
			level_lines = Levels.level_3.split('@')
			print(level_lines)
		elif level == 4:
			level_lines = Levels.level_4.split('@')
			print(level_lines)
		elif level == 5:
			level_lines = Levels.level_5.split('@')
			print(level_lines)
		elif level == 6:
			level_lines = Levels.level_6.split('@')
			print(level_lines)
		elif level == 7:
			level_lines = Levels.level_7.split('@')
			print(level_lines)
		elif level == 8:
			level_lines = Levels.level_8.split('@')
			print(level_lines)
		elif level == 9:
			level_lines = Levels.level_9.split('@')
			print(level_lines)
		elif level == 10:
			level_lines = Levels.level_10.split('@')
			print(level_lines)
		
		for text in level_lines:
		
			if len(text)-1 > 5:
				self.width = ((screen_width-100)/(len(text)-1))-self.space
				self.brick_img = pygame.transform.scale(self.brick_img, (int(((screen_width-100)/(len(text)-1))-self.space),30))
				self.brick_img2 = pygame.transform.scale(self.brick_img2, (int(((screen_width-100)/(len(text)-1))-self.space),30))
					
			for x in range(len(text)):
				if text[x]=='w':
					a.append(1)
					self.brick_no += 1
				elif text[x]=='d':
					a.append(2)
					self.brick_no += 1
				elif text[x]=='s':
					a.append(-1)
				
			b.append(a)
			a = []
			c.append([])
		self.brick_value = b
		self.rect_map = c
			
		self.set_map()
		return level
player = Player()
ball = Ball()
bricks = Bricks()
bricks.set_map()

def gameloop():
	start = False
	gameover = False
	level = 1
	
	change_speed = False
	count = 0
	speed = 100
	#gameDisplay.blit(leve_bg_img,(0,0))
	timer = 0
	temp = 0
	while not gameover:

		if int(time.clock())>temp:
			print(temp)
		temp = int(time.clock())
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					if not start and ball.rect.left >= 100:
						ball.rect.left -= 50 
					player.move_left()
				if event.key == pygame.K_RIGHT:
					if not start and ball.rect.right <= 550:
						ball.rect.right += 50 
					player.move_right()
				if event.key == pygame.K_UP:
					start = True

		for m in range(0,len(bricks.rect_map)):
			for n in range(0,len(bricks.rect_map[m])):
				if bricks.brick_value[m][n] >= 1:
					if ball.rect.colliderect(bricks.rect_map[m][n]):
						sound.play()
						ball.change_dir_y()
						bricks.brick_value[m][n] -= 1 
						if bricks.brick_value[m][n] == 0:
							count += 1
							if count%int(bricks.brick_no/3) == 0:
								change_speed = True
							
				
				
		#Change Speed			
		if change_speed:		
			change_speed = False
			speed += 25
			print(speed,"change speed on ",count)
		#gameDisplay.fill((255,102,0))	
		gameDisplay.fill((102, 255, 255))	
		display_message(20,"Time : "+str(temp),black,60,25)
		display_message(30,"Level : "+str(level),black,screen_width/2,25)
		
		#level complete
		if count == bricks.brick_no:
			score = temp
			display_message(50,"level completed",black,screen_width/2,screen_height/2)
			display_message(25,"Score : "+str(score),black,screen_width/2,(screen_height/2)+50)
			
			
		pygame.draw.rect(gameDisplay,black,(0,45,screen_width,5))
		player.draw_player()
		ball.draw_ball()
		bricks.draw()
		pygame.display.update()
		
		clock.tick(speed)
		
		#After Level Completion
		if count == bricks.brick_no:
			
			speed = 100
			start = False
			time.sleep(2)
			count = 0
			ball.reset()
			player.reset()
			level= bricks.change_level(level)
			
		if start:
			ball.move()
		ball.check()
front = Front()
front.page()

gameloop()

#this is not yet completed there are many changes required to improve this game