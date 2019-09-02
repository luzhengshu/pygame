import pygame

pygame.init()

#创建游戏窗口
screen = pygame.display.set_mode((480,700))

# 绘制背景图像
# 1> 加载图像
bg = pygame.image.load("./images/background.png")
# 2> 绘制在屏幕
screen.blit(bg, (0, 0))
# # 3> 更新显示
# pygame.display.update()

#绘制飞机
hero = pygame.image.load('./images/me1.png')
screen.blit(hero,(150,500))

#可以在所有绘制工作完成后，统一调用
pygame.display.update()
#创建时钟对象
clock = pygame.time.Clock()

#1。定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150,500,102,126)

#游戏循环 ->游戏开始了
while True:
    pygame.event.get()
    #可以执行循环体内部执行的频率
    clock.tick(60)
    #捕获事件
    event_list = pygame.event.get()
    if len(event_list) >0:
     print(event_list)

    #2.修改飞机的位置
    hero_rect.y -=5
    #判断飞机位置
    if hero_rect.y <= -126:
        hero_rect.y =700

    #3。调用blit方法绘制图像,绘制飞机前绘制游戏背景
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    #4。调用update方法更新显示
    pygame.display.update()

pygame.quit()