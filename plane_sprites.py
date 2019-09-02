import random
import pygame
#屏幕大小
SCREEN_RECT = pygame.Rect(0,0,480,700)
#刷新的帧率
FRAME_PER_SEC = 60
#创建敌机的定时器常量
CREAT_ENEMY_EVENT = pygame.USEREVENT
#发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT+1

class GameSprite(pygame.sprite.Sprite):

    def __init__(self,image_name,speed=1):

        #调用父类的初始化方法
        super().__init__()

        #定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 在屏幕垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):
    '''游戏背景'''

    def __init__(self,is_alt=False):
        #1.调用父类方法实现精灵创建(image/rect/speed)
        super().__init__('./images/background.png')

        #2.判断是否是交替图像
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        #1.调用父类方法实现
        super().update()

        #2。判断是否溢出屏幕，如果True，将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):


    def __init__(self):
        #1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__('./images/enemy1.png')
        #2。指定敌机的初始速度 1~3
        self.speed = random.randint(10,30)
        #3。指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        #1。调用父类方法，保持垂直方向飞行
        super().update()

        #2。判断是否飞出屏幕。从精灵组中删除
        if self.rect.y >= SCREEN_RECT.height:
            #kill方法可以将精灵从所有精灵组中移除,同时在内存中进行销毁
            self.kill()

    def __del__(self):
        # print('敌机挂了')
        pass


class Hero(GameSprite):

    def __init__(self):
        #1.调用父类方法，设置image&speed
        super().__init__('./images/me1.png',0)

        #2.设置英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        #3。创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed

        #控制英雄不能离开屏幕
        if self.rect.x < 0 :
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (0,1,2):
            #1.创建精灵
            bullet = Bullet()
            #2。设置精灵位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            #3。将精灵添加到精灵组
            self.bullets.add(bullet)

class Bullet(GameSprite):


    def __init__(self):
        #调用父类方法，设置图片，速度
        super().__init__('./images/bullet1.png',-10)

    def update(self):
        #调用父类方法，让子弹垂直飞行
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass