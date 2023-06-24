from pygame import*
window = display.set_mode((900,700))
display.set_caption("Unicorn running")
background = transform.scale(image.load("bg.jpg"),(900,700))


font.init()
font1 = font.Font(None, 50)
win = font1.render("ГРА ЗАВЕРШЕНА!", True, (232, 251, 200))



mixer.init()#підключаємо музтку в пайгейм
mixer.music.load("musfon.mp3")#завантажуєм пісню
mixer.music.set_volume(0.5)#визначаємо гучність
mixer.music.play()#вмикаємо звук

score = 0 


class Player(sprite.Sprite):
    def __init__ (self,player_image,player_x,player_y,width,height,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()# створити рамку навколо картинки  спрайта
        self.rect.x = player_x
        self.rect.y = player_y
        self.vel_y = 0
    def reset(self):# фнукція для того щоб намалювати спрайт на екрані
        window.blit(self.image,(self.rect.x, self.rect.y))


class Hero(Player):
    def update(self):
      dy = 0
  
      keys = key.get_pressed()
      self.vel_y +=1 #швидкість падіння донизу
      dy += self.vel_y
      if self.vel_y>5:
        self.vel_y = 5
      self.rect.y += dy
      if self.rect.y>550:
        self.rect.y = 550
        dy = 0
      if Rect.colliderect(self.rect,w1.rect):
        dy = 0
        self.rect.y = w1.rect.y-80
      if Rect.colliderect(self.rect,w2.rect):
        dy = 0
        self.rect.y = w2.rect.y-80 
      if Rect.colliderect(self.rect,w3.rect):
        dy = 0
        self.rect.y = w3.rect.y-80
      if Rect.colliderect(self.rect,w4.rect):
        dy = 0
        self.rect.y = w4.rect.y-80
      if Rect.colliderect(self.rect,w5.rect):
        dy = 0
        self.rect.y = w5.rect.y-80
      if Rect.colliderect(self.rect,w7.rect):
        dy = 0
        self.rect.y = w7.rect.y-80
      if Rect.colliderect(self.rect,w9.rect):
        dy = 0
        self.rect.y = w9.rect.y-80
      if Rect.colliderect(self.rect,w11.rect):
        dy = 0
        self.rect.y = w11.rect.y-80
      if Rect.colliderect(self.rect,w12.rect):
        dy = 0
        self.rect.y = w12.rect.y-80
      if Rect.colliderect(self.rect,w13.rect):
        dy = 0
        self.rect.y = w13.rect.y-80
      if Rect.colliderect(self.rect,w14.rect):
        dy = 0
        self.rect.y = w14.rect.y-80
      if Rect.colliderect(self.rect,w15.rect):
        dy = 0
        self.rect.y = w15.rect.y-80
      if Rect.colliderect(self.rect,w16.rect):
        dy = 0
        self.rect.y = w16.rect.y-80
       
      if keys [K_UP] and self.rect.y >= 0:
        self.rect.y -= 20
      elif keys [K_DOWN] and self.rect.y <= 650:
        self.rect.y += self.speed
      elif keys [K_LEFT] and self.rect.x >= 0 :
        self.rect.x -= self.speed
      elif keys [K_RIGHT] and self.rect.x <= 850:
        self.rect.x += self.speed
        #______ ПИСАТИ ТУТ_____
      if keys [K_1]:
        self.image = transform.scale(image.load("unicorn.png"),(90,90))
      if keys [K_2]:
        self.image = transform.scale(image.load("unicorn2.png"),(90,90))
      if keys [K_3]:
        self.image = transform.scale(image.load("unicorn3.png"),(90,90))
      if keys [K_4]:
        self.image = transform.scale(image.load("unicorn4.png"),(90,90))


class Wall(sprite.Sprite):
    def __init__ (self,width,height,color,wall_x,wall_y):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.image = Surface((self.width,self.height))
        self.image.fill((color))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


w1 = Wall(150,20,(255,255,255),0,110)
w2 = Wall(250,20,(255,255,255),300,130)
w3 = Wall(150,20,(255,255,255),700,110)
w4 = Wall(200,20,(255,255,255),20,250)
w5 = Wall(100,20,(255,255,255),300,270)
w6 = Wall(20,100,(255,255,255),400,270)
w7 = Wall(100,20,(255,255,255),400,350)
w8 = Wall(20,100,(255,255,255),500,350)
w9 = Wall(100,20,(255,255,255),500,450)
w10 = Wall(20,100,(255,255,255),600,450)
w11 = Wall(100,20,(255,255,255),520,550)
w12 = Wall(250,20,(58,49,49),1000,1000)
w13 = Wall(150,20,(255,255,255),640,550)
w14 = Wall(150,20,(255,255,255),0,500)
w15 = Wall(400,20,(255,255,255),30,650)
w16 = Wall(380,20,(255,255,255),500,650)

hero = Hero("unicorn2.png",0,0,90,90,10)
book1 = Player("star.png",750,0,120,120,0)
book2 = Player("star.png",1000,1000,200,200,0)
book3 = Player("star.png",20,400,120,120,0)
end = Player("end.png",500,700,100,100,0)

book01 = Player("star.png",1000,1000,100,100,0)
book02 = Player("star.png",1000,1000,100,100,0)
book03 = Player("star.png",1000,1000,100,100,0)

game = True
finish = False
clock = time.Clock()
FPS = 55
while game:
  for e in event.get():
    if e.type == QUIT:
      game = False
  if finish!=True:
    if sprite.collide_rect(hero,w10):
       w10 = Wall(20,100,(255,255,255),1000,1000)
       w12 = Wall(250,20,(255,255,255),250,550)
       book2 = Player("star.png",400,460,120,120,0)
    if sprite.collide_rect(hero,book1):
       book1 = Player("star.png",1000,1000,100,100,0)
       book01 = Player("star.png",30,0,80,80,0)
       score = score + 1 
    if sprite.collide_rect(hero,book2):
       book2 = Player("star.png",1000,1000,50,50,0)
       book02 = Player("star.png",70,0,80,80,0)
       score = score + 1
    if sprite.collide_rect(hero,book3):
       book3 = Player("star.png",1000,1000,50,50,0)
       book03 = Player("star.png",110,0,80,80,0)
       end = Player("end.png",750,350,150,150,0)
       score = score + 1
    window.blit(background,(0,0))
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()
    w6.draw_wall()
    w7.draw_wall()
    w8.draw_wall()
    w9.draw_wall()
    w10.draw_wall()
    w11.draw_wall()
    w12.draw_wall()
    w13.draw_wall()
    w14.draw_wall()
    w15.draw_wall()
    w16.draw_wall()
    hero.update()
    hero.reset()
    end.update()
    end.reset()
    book1.update()
    book1.reset()
    book2.update()
    book2.reset()
    book3.update()
    book3.reset()
    book01.update()
    book01.reset()
    book02.update()
    book02.reset()
    book03.update()
    book03.reset()
    if sprite.collide_rect(hero,end) and score==3:
      window.blit(win,(300,200))
      finish = True
   


  display.update()
  clock.tick(FPS)
