import pygame
import time
import random
from plane_sprites import *

game_over = pygame.image.load('./images/game_over.png')

global n1
global n2
n1 = True
n2 = True
class Plane_main(object):

    def __init__(self):
        print('游戏初始化')
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()

        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
        pygame.time.set_timer(ENEMY_FIRE_EVENT, 800)
        self.count = 0
        self.score = 0

    def __create_sprites(self):
        # 背景组
        self.back_group = pygame.sprite.Group()
        bg1 = BackGround()
        bg2 = BackGround(True)
        # pygame.mixer.init()
        # pygame.mixer.music.load("./Capo Productions - Journey 00_00_00-00_00_59.ogg")
        # pygame.mixer.music.play(-1)

        self.back_group.add(bg1,bg2)


        self.enemy_group = pygame.sprite.Group()
        self.enemy = Enemy()
        self.enemy_group = pygame.sprite.Group(self.enemy)
        self.enemies1 = pygame.sprite.Group()

        # 敌机组
        self.enemy_group = pygame.sprite.Group()
        #敌级销毁组
        self.enemy1_down_group=pygame.sprite.Group()
        # 英雄组
        self.hero_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group.add(self.hero)


    # def mainScene(self):
    #     screen = pygame.display.set_mode(SCREEN_RECT.size)
    #     clock = pygame.time.Clock()
    #     # 2 创建一个背景图片
    #     bg = pygame.image.load('./images/bg2.png')
    #     screen.blit(bg, (0, 0))
    #     pygame.display.update()
    #     pass


    def run1(self):
        self.count += 1
        # 1. 设置刷新帧率
        self.clock.tick(60)
        self.star()
        self.__update_sprites1()
        pygame.display.update()
        # score_font = pygame.font.Font("C:/Windows/Fonts/STHUPO.TTF", 25)
        # score_text = score_font.render("按H开始游戏 ", True, (128, 128, 128))
        # text_rect = score_text.get_rect()
        # text_rect.topleft = [105, 420]
        # self.screen.blit(score_text, text_rect)
        # pygame.display.update()


    def start_game1(self):

        pygame.init()
        print("开始游戏...")
        pygame.mixer.init()
        pygame.mixer.music.load("./zhan.ogg")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        gameIcon = pygame.image.load("./images/bullet.png")
        pygame.display.set_icon(gameIcon)
        n1 = True
        while n1:
            self.run1()


    def start_game2(self):

        pygame.init()
        print("开始游戏...")
        pygame.mixer.init()
        pygame.mixer.music.load("./zhan.ogg")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        gameIcon = pygame.image.load("./images/bullet.png")
        pygame.display.set_icon(gameIcon)
        n2 = True
        while n2:
            self.run2()



    def run2(self):
        self.count += 1
        # 1. 设置刷新帧率
        self.clock.tick(60)
        # 2. 事件监听
        self.__event_handler()

        # 3. 碰撞检测
        self.__check_collide()
        # 4. 更新精灵组
        self.__update_sprites()
        # 5. 更新屏幕显示
        pygame.display.update()

    # def __event_handler1(self):
    #     """事件监听"""
    #     for event in pygame.event.get():
    #         self.clock.tick(60)
    #         if event.type == pygame.QUIT:
    #             print("退出游戏。。。")
    #
    #
    #         Plane_main.__game_over(self)
    #         buttons = pygame.mouse.get_pressed()
    #         x1, y1 = pygame.mouse.get_pos()
    #         if x1 >= 227 and x1 <= 555 and y1 >= 261 and y1 <= 327:
    #
    #                 if buttons[0]:
    #                     n1 = False
    #
    #         print("敌机出场")
    #         exit()

    def __event_handler(self):
        """事件监听"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                print("退出游戏。。。")
                Plane_main.__game_over1(self)
                exit()

            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场")
                self.enemy_group.add(Enemy())
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            elif event.type == ENEMY_FIRE_EVENT:
                for self.enemy in self.enemy_group:
                    self.enemy.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动。。。")

             #键盘模块
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = 3
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -3
            elif keys_pressed[pygame.K_UP]:
                self.hero.speed1 = -3
            elif keys_pressed[pygame.K_DOWN]:
                self.hero.speed1 = 3
            else:
                self.hero.speed = 0
                self.hero.speed1 = 0

    def __check_collide(self):
          # 子弹摧毁敌机
          enemy_down = pygame.sprite.groupcollide(self.hero.bullet, self.enemy_group, True, True, pygame.sprite.collide_mask)
          enemy1_down_group.add(enemy_down)
          # 战绩摧毁
          enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True, pygame.sprite.collide_mask)
          self.enemies1.add(enemies)
          pygame.sprite.groupcollide(self.enemy.bullet1, self.hero.bullet, True, True, pygame.sprite.collide_mask)
          enemies2 = pygame.sprite.spritecollide(self.hero, self.enemy.bullet1, True, pygame.sprite.collide_mask)
          self.enemies1.add(enemies2)
          for enemy1_down in enemy1_down_group:
              self.screen.blit(enemy1_down_surface[enemy1_down.down_index], enemy1_down.rect)
              if self.count % 5 == 0:
                  enemy1_down.down_index += 1
              if enemy1_down.down_index == 3:

                  bomb_sound = pygame.mixer.Sound("./bomb.ogg")
                  bomb_sound.play()
                  bomb_sound.set_volume(0.2)
                  self.score += 100
                  enemy1_down_group.remove(enemy1_down)
                  print(self.score)


          if len(self.enemies1) > 0:
                self.hero.kill()
            # 结束游戏
                Plane_main.__game_over(self)
                font = pygame.font.Font(None, 40)
                text = font.render('Final Score: ' + str(self.score), True, (255, 0, 0))
                text_rect = text.get_rect()
                text_rect.centerx = self.screen.get_rect().centerx
                text_rect.centery = self.screen.get_rect().centery + 24
                self.screen.blit(game_over, (0, 0))
                self.screen.blit(text, text_rect)

    def __update_sprites1(self):
        font = pygame.font.Font(None, 40)
        text = font.render('Best Score: ' + str(self.score), True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = self.screen.get_rect().centerx
        text_rect.centery = self.screen.get_rect().centery + 24
        self.screen.blit(text, text_rect)

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        # 精灵组调用
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        # 子弹
        self.hero.bullet.update()
        self.hero.bullet.draw(self.screen)

        # 敌方子弹
        self.enemy.bullet1.update()
        self.enemy.bullet1.draw(self.screen)

        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render('score: ' + str(self.score), True, (128, 128, 128))
        text_rect = score_text.get_rect()
        text_rect.topleft = [10, 10]
        self.screen.blit(score_text, text_rect)

        for enemy1_down in enemy1_down_group:
            self.screen.blit(enemy1_down_surface[enemy1_down.down_index], enemy1_down.rect)
            if self.count % 5 == 0:
                enemy1_down.down_index += 1
            if enemy1_down.down_index == 3:
                self.score += 5
                enemy1_down_group.remove(enemy1_down)
                print(self.score)


    def __game_over(self):
        """游戏结束"""
        print("游戏结束")
        n1 = True
        n2 = False
        self.start_game1()
        exit()


    def star(self):
        ck = pygame.display.set_mode(SCREEN_RECT.size)

        # 2 创建一个背景图片
        # ck = pygame.display.set_mode((340, 573))
        clock = pygame.time.Clock()
        bg4 = pygame.image.load('./images/bg4.png')
        ck.blit(bg4, (0, 0))
                    # 充当第一关的画布界面暂时占位（可以理解为游戏开始了）

        for event in pygame.event.get():
            self.clock.tick(60)
            if event.type == pygame.QUIT:
                print("退出游戏。。。")
                Plane_main.__game_over1(self)

        buttons = pygame.mouse.get_pressed()
        x1, y1 = pygame.mouse.get_pos()
        if x1 >= 103 and x1 <= 237 and y1 >= 400 and y1 <= 425:
            # bg4.blit(i11, (200, 240))
            if buttons[0]:
                n1 = False
                self.start_game2()
                print("敌机出场")
        elif x1 >= 103 and x1 <= 237 and y1 >= 460 and y1 <= 490:
            # start_ck.blit(i21, (200, 360))
            if buttons[0]:
                pygame.quit()
                exit()
        ck.blit(bg4, (0, 0))
        pygame.display.update()
        # bg = pygame.image.load('./images/bg3.jpg')
        # screen.blit(bg, (0, 0))
        # pygame.display.update()

    def __game_over1(self):
        """游戏结束"""
        print("游戏结束")
        pygame.quit()
        exit()
if __name__ == '__main__':
    game = Plane_main()

    n1 = True
    n2 = True
    # game.mainScene()
    while True:
        if n1 == True:
            game.start_game1()
        else:
            game.start_game2()

