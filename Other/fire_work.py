import pygame,sys,random,math
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
FPS = 60
SIZE = 4.5 # kích thước viên đạn nổ ra 
SPEED_CHANGE_SIZE = 0.05 # tốc độ nhỏ lại của viên đạn nổ ra 
CHANGE_SPEED  = 0.07 # tốc độ chậm lại của viên đạn
RAD = math.pi/180 # đổi từ radian sang độ 
A_FALL = 1.5 #gia tốc rơi tự do
NUM_BULLET = 50 #số đạn nổ ra trong một quả pháo 
SPEED_MIN = 2 # Tốc độ nhỏ nhất của một viên đạn 
SPEED_MAX = 4 # tốc độ lớn nhất của một viên đạn
TIME_CHEAT_FW = 3 # số lượng pháo lớn nhất bắn lên 
NUM_FIREWORKS_MAX = 3 # số lượng pháo lớn nhất bắn lên 
NUM_FIREWORKS_MIN = 1 # số lượng pháo nhỏ nhất bắn lên 
SPEED_FLY_UP_MAX = 12 # Tốc độ lớn nhất của viên đạn bay lên (trước khi nổ)
SPEED_FLY_UP_MIN = 8 # tốc độ nhỏ nhất của viên đạn bay lên(trước khi nổ)

class Dot(): # những cấm theo sau của mỗi viên đạn
    def __init__(self,x,y,size,color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    def update(self):
        # Giảm kích thước chấm
        if self.size > 0:
            self.size -= SPEED_CHANGE_SIZE*5
        else:
            self.size = 0
    def draw(self): # Vẽ một chấm
        if self.size > 0:
            pygame.draw.circle(DISPLAYSURF, self.color,(int(self.x)),int(self.y),int(self.size))

class BulletFlyUp(): # Viên đạn bay lên trước khi nổ 
    def __int__(self,speed,x):
        self.speed = speed
        self.x = x
        self.y = WINDOWHEIGHT
        self.dots = []  # Một list các chấm theo sau
        self.size = SIZE/2
        self.color = (255,255,100)            
    def update(self):
        self.dots.append(Dot(self.x,self.y,self.size,self.color)) 
        # mỗi lần đạn đi qua sẽ có một chấm thêm vào 
        # xác định lại ví trí viên đạn
        self.y -= self.speed
        self.speed -= A_FALL*0.1
        # update từng chấm
        for i in range(len(self.dots)):
            self.dots[i].update()
            # xoá những chấm có kích thước <= 0
        i = 0
        while i < len(self.dots):
            if self.dots[i].size <= 0:
                self.dots.pop(i)
            else:
                i += 1
    
    def draw(self):
        pygame.draw.circle(DISPLAYSURF, self.color,(int(self.x)),int(self.y),int(self.size))
        # vẽ hình viên đạn
        # vẽ từng chấm
        for i in range(len(self.dots)):
            self.dots[i].draw()


class Bullet(): #viên đạn sau khi nổ
    def __init__(self,x,y,speed,angle,color):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle # góc hợp bởi viên đạn và phương ngang 
        self.size = SIZE
        self.color = color 

    def update(self):
        # xác định tốc độ theo 2 phương 
        speedX = self.speed * math.cos(self.angle*RAD)
        speedY = self.speed * math.sin(self.angle*RAD)
        # xác định lại vị trí viên đạn 
        self.x += speedX
        self.y += speedY
        self.y += A_FALL
        #giảm tốc độ đạn 
        if self.size > 0:
            self.size -= SPEED_CHANGE_SIZE
        else:
            self.size = 0
        # giảm kích thước đạn
        if self.speed > 0:
            self.speed -= CHANGE_SPEED
        else:
            self.speed = 0
    def draw(self):
        if self.size > 0:
            pygame.draw.circle(DISPLAYSURF, self.color,(int(self.x)),int(self.y),int(self.size))


class Firework(): # quả pháo hoa
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dots = []  # list các chấm theo sau mỗi viên đạn

        def creatBullets(): #Tạo list các viên đạn
            bullets = []
            color = random.color()
            for i in range(NUM_BULLET):
                angle = (360/NUM_BULLET)* i
                speed = random.uniform(SPEED_MIN,SPEED_MAX)
                bullets.append(Bullet(self.x,self.y,speed,angle,color))
            return bullets
        self.bullets = creatBullets();
    
    def update(self):
        for i in range(len(self.bullets)):#updatetừng viên đạn
            self.bullets[i].update()
            self.dots.append(Dot(self.bullets[i].x,self.bullets[i].y,self.bullets[i].size,self.bullets[i].color,))
        for i in range(len(self.dots)):
            self.dots[i].update()
        # xoá những chấm có kích thước <= 0
        i = 0
        while i < len(self.dots):
            if self.dots[i].size <= 0:
                self.dots.pop(i)
            else:
                i += 1


    def draw(self):
        for i in range(len(self.bullets)): # vẽ từng viên đạn
            self.bullets[i].draw()
        for i in range(len(self.dots)): # vẽ từng chấm
            self.dots[i].draw()

class Random():
    def __init__(self):
        pass

    def color(): #tạo màu ngẫu nhiên (màu sáng)
        color1 = random.randint(0,255)
        color2 = random.randint(0,255)
        if color1 + color2 >= 255:
            color3 = random.randint(0,255)
        else:
            color3 = random.randint(255 - color1 - color2, 255)
        colorList = [color1,color2,color3]
        random.shuffle(colorList)
        return colorList
    def num_firework(): #số pháo hoa mỗi lần bắn
        return random.randint(NUM_FIREWORKS_MIN,NUM_FIREWORKS_MAX)
    def randomBulletFlyUp_speed(): #tốc độ viên đạn bay lên
        speed = random.uniform(SPEED_FLY_UP_MIN,SPEED_FLY_UP_MAX)
        return speed
    def randomBulletFlyUp_x():
        x = random.randint(int(WINDOWWIDTH*0.2),int(WINDOWHEIGHT*0.8))
        return x


def main():
    global FPSCLOCK,DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    fireWorks = []
    time  = TIME_CHEAT_FW
    bulletFlyUps = []

    while True:
        DISPLAYSURF.fill((0,0,0)) # xoá nền
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        if time == TIME_CHEAT_FW: # tạo những viên đạn bay lên sau khoảng thời gian xác định
            for i in range(Random.num_firework()):
                bulletFlyUps.append(BulletFlyUp(Random.randomBulletFlyUp_speed(),Random.randomBulletFlyUp_x()))

        for i in range(len(bulletFlyUps)):
            bulletFlyUps[i].draw()
            bulletFlyUps[i].update()

        for i in range(len(fireWorks)):
            fireWorks[i].draw()
            fireWorks[i].update()

        i = 0
        while i < len(bulletFlyUps):
            if bulletFlyUps[i].speed <=0:
                fireWorks.append(Firework(bulletFlyUps[i].x,bulletFlyUps[i].y))
                # tạo ví trí viên đạn
                bulletFlyUps.pop(i) 
                # xoá viên đạn đó 
            else:
                i += 1    


        # đếm khoảng thời gian bắn 

        if time <= TIME_CHEAT_FW:
            time += 1
        else:
            time = 0
        pygame.display.update()
        FPSCLOCK.tick(FPS)



if __name__ == '__main__':
    main()
