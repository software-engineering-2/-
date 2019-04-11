import pygame
import time
import random
from plane_sprites import *

pygame.init()

SCREEN_RECT = pygame.Rect(0,0,340,573)

    #1.创建窗口
screen = pygame.display.set_mode(SCREEN_RECT.size)
clock = pygame.time.Clock()
    #2 创建一个背景图片

bg = pygame.image.load('./images/bg2.png')
screen.blit(bg,(0,0))

game_over = pygame.image.load('./images/game_over.png')


#创建飞机
# hero = pygame.image.load('./images/plane1.png')
# screen.blit(hero,(150,350))
# pygame.display.update()
# hero_rect = pygame.Rect(128,411,83,84)


enemies1 = pygame.sprite.Group()
enemy1_down_group = pygame.sprite.Group()

hero_group = pygame.sprite.Group()
hero = Hero()
hero_group = pygame.sprite.Group(hero)

#创建精灵
# enemy = GameSprite('./images/enemy.png')
# enemy1 = GameSprite('./images/enemy2.png')
# enemy_group = pygame.sprite.Group(enemy,enemy1)

#创建精灵组
enemy_group = pygame.sprite.Group()
enemy = Enemy()
enemy_group.add(enemy)

#背景精灵
# bg1 = Background('./images/bg2.png')
# bg2 = Background('./images/bg2.png')
# bg2.rect.y = -bg2.rect.height
# bg_group = pygame.sprite.Group(bg1,bg2)

pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
pygame.time.set_timer(HERO_FIRE_EVENT,500)



count = 0
score = 0
while True:
    count += 1
     #3 显示到屏幕
    clock.tick(60)
    screen.blit(bg, (0, 0))
     #判断飞机位置
    hero_group.update()
    hero_group.draw(screen)

    #精灵组调用
    enemy_group.update()
    enemy_group.draw(screen)

    #子弹
    hero.bullet.update()
    hero.bullet.draw(screen)

    #敌方子弹
    enemy.bullet1.update()
    enemy.bullet1.draw(screen)

    #小消失
    # enemy_group.update()
    # enemy_group.draw(screen)
     # #精灵背景
    # bg_group.update()
    # bg_group.draw(screen)
    #
    # pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏。。。")
            pygame.quit()
            exit()

        elif event.type == CREATE_ENEMY_EVENT:
            print("敌机出场")
            enemy = Enemy()
            enemy_group.add(enemy)
        elif event.type == HERO_FIRE_EVENT:
            hero.fire()
            enemy.fire()
        # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        #     print("向右移动。。。")

         #键盘模块
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT]:
        hero.speed = 3
    elif keys_pressed[pygame.K_LEFT]:
        hero.speed = -3
    elif keys_pressed[pygame.K_UP]:
        hero.speed1 = -3
    elif keys_pressed[pygame.K_DOWN]:
        hero.speed1 = 3
    else:
        hero.speed = 0
        hero.speed1 = 0

    #子弹摧毁敌机
    enemy_down=pygame.sprite.groupcollide(hero.bullet, enemy_group, True, True)
    enemy1_down_group.add(enemy_down)
    #战绩摧毁
    enemies = pygame.sprite.spritecollide(hero,enemy_group,True)
    enemies1.add(enemies)


    for enemy1_down in enemy1_down_group:
        for i in (0,1,2,3,4,5,6):
            screen.blit(enemy1_down_surface[i],enemy1_down.rect)
        # if count % 5 == 0:
        #     enemy1_down.down_index += 1
        #     if enemy1_down.down_index == 3:
            #     # pygame.mixer.music.load("./baozha.ogg")
            #      # pygame.mixer.music.play()
        enemy1_down_group.remove(enemy1_down)
        score += 100
        print(score)


    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render('score: ' + str(score), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(score_text, text_rect)




    if len(enemies) > 0:
        hero.kill()

        font = pygame.font.Font(None, 64)
        text = font.render('Final Score: ' + str(score), True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.centery = screen.get_rect().centery + 24
        screen.blit(game_over, (0, 0))
        screen.blit(text, text_rect)



    pygame.display.update()


