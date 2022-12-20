import pygame,sys,random
from pygame.math import Vector2
pygame.init()

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(-1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            xpos = int(block.x*cell_size)
            ypos = int(block.y*cell_size)
            block_rect = pygame.Rect(xpos,ypos,cell_size,cell_size)
            pygame.draw.rect(screen,"dark blue",block_rect)

    def move_snake(self):
        if self.new_block == True:
            body2 = self.body[:]
            body2.insert(0, body2[0] + self.direction)
            self.body = body2
            self.new_block = False
        
        else:
            body2 = self.body[:-1]
            body2.insert(0, body2[0] + self.direction)
            self.body = body2
            
    def addblock(self):
        self.new_block = True

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit = pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        pygame.draw.ellipse(screen,pygame.Color("red") ,fruit)
    
    def randomize(self):
        self.x = random.randint(0,cell_num-1)
        self.y = random.randint(0,cell_num-1)
        self.pos = Vector2(self.x, self.y)

class MAIN:

    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.addblock()

    def check_fail(self):
        if not (0 <= self.snake.body[0].x < cell_num) or not (0 <= self.snake.body[0].y < cell_num):
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()
 
# Stuff in the game
cell_size = 40
cell_num = 20
screen = pygame.display.set_mode((cell_num*cell_size,cell_num*cell_size))
clock = pygame.time.Clock()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_game.snake.direction != Vector2(0,1):
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN and main_game.snake.direction != Vector2(0,-1):
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT and main_game.snake.direction != Vector2(-1,0):
                main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT and main_game.snake.direction != Vector2(1,0):
                main_game.snake.direction = Vector2(-1,0)
        
        screen.fill(pygame.Color("Gold"))
        main_game.draw_elements()
        main_game.check_fail()
        pygame.display.update()
        clock.tick(100)