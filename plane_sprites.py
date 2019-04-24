import pygame
import random


SCREEN_RECT = pygame.Rect(0,0,340,573)
CREATE_ENEMY_EVENT = pygame.USEREVENT
#hero子弹
HERO_FIRE_EVENT = pygame.USEREVENT + 1
ENEMY_FIRE_EVENT = pygame.USEREVENT + 2

#爆炸销毁图片
bg1 = pygame.image.load('./images/z1.png')
bg2 = pygame.image.load('./images/z2.png')
bg3 = pygame.image.load('./images/z3.png')
bg4 = pygame.image.load('./images/z4.png')
bg5 = pygame.image.load('./images/z5.png')
bg6 = pygame.image.load('./images/z6.png')
bg7 = pygame.image.load('./images/z7.png')

#爆炸精灵组
enemy1_down_group = pygame.sprite.Group()
#把爆炸图片放到列表当中
enemy1_down_surface = []
enemy1_down_surface.append(bg1)
enemy1_down_surface.append(bg2)
enemy1_down_surface.append(bg3)
enemy1_down_surface.append(bg4)
enemy1_down_surface.append(bg5)
enemy1_down_surface.append(bg6)
enemy1_down_surface.append(bg7)




class GameSprite(pygame.sprite.Sprite):
    "精灵"
    def __init__(self,image_name,speed=1):
        #调用父类的初始化
        super().__init__()

        #对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        pass

class BackGround(GameSprite):
    def __init__(self,is_alt=False):
        super().__init__('./images/bg2.png')
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
    # 1. 调用父类的方法实现
        super().update()
    # 2. 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if  self.rect.y >= SCREEN_RECT.height:
            self.rect.y =- self.rect.height


class Enemy(GameSprite):


    def __init__(self):
        # 调用父类，制定敌机
        super().__init__('./images/enemy.png')
        #随机速度
        self.speed = random.randint(1,2)
        #随机位置
        self.down_index = 0
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)
        #创建子弹精灵族
        self.bullet1 = pygame.sprite.Group()



    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
        pass


    def fire(self):

        print("发射子弹22")


        # 1.创建子弹
        bullet = Bullet1()

        # 2.设置精灵位置
        bullet.rect.bottom = self.rect.y + 100
        bullet.rect.centerx = self.rect.centerx

        # 3.精灵添加到精灵组
        self.bullet1.add(bullet)

    def __del__(self):
        print("敌机挂了")


class Hero(GameSprite):

    def __init__(self):
        #1.调用父类方法设置 images&speed
        super().__init__('./images/plane1.png')
        self.speed1 = 0
        #2.hero初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        #3.zidan
        self.bullet = pygame.sprite.Group()


    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

        self.rect.y += self.speed1
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > 489:
            self.rect.y = 489

    def fire(self):
        print("发射子弹")

        for i in (0,1,2):

            #1.创建子弹
            bullet = Bullet()

            #2.设置精灵位置
            bullet.rect.bottom = self.rect.y -  20*i
            bullet.rect.centerx = self.rect.centerx

            #3.精灵添加到精灵组
            self.bullet.add(bullet)


class Bullet(GameSprite):
    """docstring for ClassName"""
    def __init__(self):
        super().__init__('./images/bullet.png',-10)
        self.down_index = 0
        pass

    def update(self):
        super().update()

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹销毁")

class Bullet1(GameSprite):
    """docstring for ClassName"""
    def __init__(self):
        super().__init__('./images/bullet3.png',-5)
        self.down_index = 0
        pass

    def update(self):
        self.rect.y -= self.speed
        if self.rect.height > SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print("子弹销毁222")