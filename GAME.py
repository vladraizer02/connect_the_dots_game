import pygame
import os
import button_GAME
 
pygame.init()
size = width, height = 350, 500
screen = pygame.display.set_mode(size)
 
 
class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]            
        self.left = 35
        self.top = 115
        self.cell_size = 60
        # значения по умолчанию
        if width == 5:
            self.cell_size = 56
        elif width == 6:
            self.cell_size = 46
        elif width == 7:
            self.cell_size = 40  
        elif width == 8:
            self.cell_size = 35
        elif width == 9:
            self.cell_size = 31      
        self.radius = self.cell_size//2
        self.spisok_button_GAME = []
 
    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        
    def render(self):
        white = pygame.Color(255, 255, 255)
        spisok = []
        text_x = 120
        text_y = 10
        text_x2 = 140
        text_y2 = 60          
        for i in range(self.height):          
            for g in range(self.width):
                spisok.append('black')
                pygame.draw.rect(screen, white, (self.left+self.cell_size*g, self.top+self.cell_size*i, self.cell_size, self.cell_size), 1)
                if self.width == 5:
                    level = self.load_level("level1.txt")
                    if level[i][g] != '.':
                        pygame.draw.circle(screen, pygame.Color(level[i][g]), (self.left+(self.cell_size*(i+1)-self.radius), self.top+(self.cell_size*(g+1)-self.radius)), (self.radius)-4)
                    font = pygame.font.SysFont('arial', 50)
                    text = font.render("Level1", 1, (80, 255, 100))
                    text2 = font.render("5x5", 1, (80, 255, 100))
                    self.win_spisok = [['red', 'black', 'green', 'green', 'black'], ['red', 'green', 'green', 'blue', 'black'], ['red', 'green', 'black', 'blue', 'black'], ['black', 'green', 'yellow', 'black', 'yellow'], ['black', 'green', 'yellow', 'yellow', 'yellow']]
                elif self.width == 6:
                    level = self.load_level("level2.txt")
                    if level[i][g] != '.':
                        pygame.draw.circle(screen, pygame.Color(level[i][g]), (self.left+(self.cell_size*(i+1)-self.radius), self.top+(self.cell_size*(g+1)-self.radius)), (self.radius)-4)
                    font = pygame.font.SysFont("arial", 50)
                    text = font.render("Level2", 1, (255, 165, 0))
                    text2 = font.render("6x6", 1, (255, 165, 0))
                    self.win_spisok = [['orange', 'orange', 'orange', 'orange', 'orange', 'black'], ['orange', 'black', 'black', 'green', 'green', 'green'], ['orange', 'green', 'red', 'green', 'black', 'black'], ['orange', 'green', 'black', 'green', 'blue', 'black'], ['orange', 'green', 'green', 'green', 'black', 'yellow'], ['black', 'black', 'yellow', 'yellow', 'yellow', 'yellow']]
                elif self.width == 7:
                    level = self.load_level("level3.txt")
                    if level[i][g] != '.':
                        pygame.draw.circle(screen, pygame.Color(level[i][g]), (self.left+(self.cell_size*(i+1)-self.radius), self.top+(self.cell_size*(g+1)-self.radius)), (self.radius)-4)
                    font = pygame.font.SysFont("arial", 50)
                    text = font.render("Level3", 1, (139, 0, 255))
                    text2 = font.render("7x7", 1, (139, 0, 255))               
                    screen.blit(text, (text_x, text_y))
                    screen.blit(text2, (text_x2, text_y2))
                    self.win_spisok = [['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'black'], ['yellow', 'red', 'red', 'red', 'red', 'red', 'black'], ['yellow', 'red', 'cyan', 'cyan', 'cyan', 'cyan', 'black'], ['black', 'red', 'cyan', 'green', 'black', 'cyan', 'orange'], ['red', 'red', 'cyan', 'green', 'cyan', 'cyan', 'orange'], ['red', 'black', 'cyan', 'black', 'black', 'black', 'orange'], ['red', 'red', 'red', 'black', 'black', 'blue', 'black']]
                elif self.width == 8:
                    level = self.load_level("level4.txt")
                    if level[i][g] != '.':
                        pygame.draw.circle(screen, pygame.Color(level[i][g]), (self.left+(self.cell_size*(i+1)-self.radius), self.top+(self.cell_size*(g+1)-self.radius)), (self.radius)-4)
                    font = pygame.font.SysFont("arial", 50)
                    text = font.render("Level4", 1, (255, 0, 0))
                    text2 = font.render("8x8", 1, (255, 0, 0))
                    self.win_spisok = [['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green'], ['black', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'green'], ['blue', 'blue', 'red', 'red', 'red', 'red', 'black', 'green'], ['blue', 'red', 'red', 'yellow', 'black', 'red', 'red', 'black'], ['blue', 'red', 'black', 'yellow', 'black', 'orange', 'red', 'red'], ['blue', 'red', 'black', 'blue', 'blue', 'orange', 'black', 'red'], ['blue', 'red', 'red', 'black', 'blue', 'orange', 'cyan', 'red'], ['blue', 'blue', 'blue', 'blue', 'blue', 'black', 'black', 'black']]
                elif self.width == 9:
                    level = self.load_level("level5.txt")
                    if level[i][g] != '.':
                        pygame.draw.circle(screen, pygame.Color(level[i][g]), (self.left+(self.cell_size*(i+1)-self.radius), self.top+(self.cell_size*(g+1)-self.radius)), (self.radius)-4)
                    font = pygame.font.SysFont("arial", 50)
                    text = font.render("Level5", 1, (66, 170, 255))
                    text2 = font.render("9x9", 1, (66, 170, 255))
                    self.win_spisok = [['orange', 'orange', 'black', 'black', 'purple', 'purple', 'purple', 'purple', 'purple'], ['orange', 'black', 'blue', 'cyan', 'cyan', 'cyan', 'cyan', 'cyan', 'purple'], ['orange', 'black', 'blue', 'cyan', 'black', 'orange', 'orange', 'cyan', 'purple'], ['orange', 'yellow', 'blue', 'cyan', 'cyan', 'cyan', 'orange', 'cyan', 'purple'], ['orange', 'yellow', 'blue', 'blue', 'black', 'black', 'orange', 'cyan', 'purple'], ['orange', 'yellow', 'yellow', 'black', 'red', 'black', 'orange', 'cyan', 'purple'], ['orange', 'orange', 'yellow', 'black', 'orange', 'orange', 'orange', 'cyan', 'purple'], ['black', 'orange', 'orange', 'orange', 'orange', 'cyan', 'cyan', 'cyan', 'purple'], ['green', 'green', 'green', 'green', 'black', 'black', 'black', 'purple', 'purple']]
            self.spisok_button_GAME.append(spisok)
            spisok = []                                
            screen.blit(text, (text_x, text_y))
            screen.blit(text2, (text_x2, text_y2))
        
        
    def get_cell(self, mouse_pos):
        if mouse_pos[0] > self.left and mouse_pos[0] < self.left+self.cell_size*self.width and mouse_pos[1] > self.top and mouse_pos[1] < self.top+self.cell_size*self.height:
            for i in range(self.height):
                for g in range(self.width):
                    if mouse_pos[0] <= self.left+self.cell_size*g+self.cell_size and mouse_pos[1] <= self.top+self.cell_size*i + self.cell_size:    
                        return [g, i]                    
        else:
            return None
        
    def on_click(self, cell_coords):
        self.koord = cell_coords
        
        if self.width == 5:
            if self.koord[0] == 0 and self.koord[1] == 1 or self.koord[0] == 3 and self.koord[1] == 0:
                self.color = 'red'
            elif self.koord[0] == 4 and self.koord[1] == 0 or self.koord[0] == 0 and self.koord[1] == 4:
                self.color = 'green'
            elif self.koord[0] == 1 and self.koord[1] == 4 or self.koord[0] == 3 and self.koord[1] == 3:
                self.color = 'blue'
            elif self.koord[0] == 2 and self.koord[1] == 2 or self.koord[0] == 2 and self.koord[1] == 4:
                self.color = 'yellow'
            else:
                self.color = 'black'
        if self.width == 6:
            if self.koord[0] == 1 and self.koord[1] == 2 or self.koord[0] == 3 and self.koord[1] == 2:
                self.color = 'red'
            elif self.koord[0] == 1 and self.koord[1] == 1 or self.koord[0] == 2 and self.koord[1] == 5:
                self.color = 'green'
            elif self.koord[0] == 2 and self.koord[1] == 4 or self.koord[0] == 4 and self.koord[1] == 4:
                self.color = 'blue'
            elif self.koord[0] == 3 and self.koord[1] == 5 or self.koord[0] == 5 and self.koord[1] == 1:
                self.color = 'yellow'  
            elif self.koord[0] == 0 and self.koord[1] == 5 or self.koord[0] == 5 and self.koord[1] == 0:
                self.color = 'orange'
            else:
                self.color = 'black'
        if self.width == 7:            
            if self.koord[0] == 6 and self.koord[1] == 3 or self.koord[0] == 1 and self.koord[1] == 6:
                self.color = 'red'
            elif self.koord[0] == 5 and self.koord[1] == 3 or self.koord[0] == 3 and self.koord[1] == 4:
                self.color = 'green'
            elif self.koord[0] == 6 and self.koord[1] == 4 or self.koord[0] == 6 and self.koord[1] == 6:
                self.color = 'blue'
            elif self.koord[0] == 3 and self.koord[1] == 0 or self.koord[0] == 0 and self.koord[1] == 6:
                self.color = 'yellow'  
            elif self.koord[0] == 2 and self.koord[1] == 6 or self.koord[0] == 5 and self.koord[1] == 5:
                self.color = 'orange'
            elif self.koord[0] == 5 and self.koord[1] == 1 or self.koord[0] == 5 and self.koord[1] == 4:
                self.color = 'cyan'
            else:
                self.color = 'black'
        if self.width == 8:            
            if self.koord[0] == 6 and self.koord[1] == 3 or self.koord[0] == 7 and self.koord[1] == 7:
                self.color = 'red'
            elif self.koord[0] == 1 and self.koord[1] == 0 or self.koord[0] == 3 and self.koord[1] == 7:
                self.color = 'green'
            elif self.koord[0] == 2 and self.koord[1] == 6 or self.koord[0] == 5 and self.koord[1] == 2:
                self.color = 'blue'
            elif self.koord[0] == 4 and self.koord[1] == 2 or self.koord[0] == 3 and self.koord[1] == 4:
                self.color = 'yellow'  
            elif self.koord[0] == 7 and self.koord[1] == 5 or self.koord[0] == 4 and self.koord[1] == 4:
                self.color = 'orange'
            elif self.koord[0] == 5 and self.koord[1] == 6 or self.koord[0] == 7 and self.koord[1] == 6:
                self.color = 'cyan'
            else:
                self.color = 'black'
        if self.width == 9:            
            if self.koord[0] == 5 and self.koord[1] == 3 or self.koord[0] == 5 and self.koord[1] == 5:
                self.color = 'red'
            elif self.koord[0] == 7 and self.koord[1] == 0 or self.koord[0] == 8 and self.koord[1] == 4:
                self.color = 'green'
            elif self.koord[0] == 1 and self.koord[1] == 1 or self.koord[0] == 4 and self.koord[1] == 4:
                self.color = 'blue'
            elif self.koord[0] == 2 and self.koord[1] == 1 or self.koord[0] == 6 and self.koord[1] == 3:
                self.color = 'yellow'  
            elif self.koord[0] == 0 and self.koord[1] == 2 or self.koord[0] == 2 and self.koord[1] == 4:
                self.color = 'orange'
            elif self.koord[0] == 4 and self.koord[1] == 5 or self.koord[0] == 8 and self.koord[1] == 5:
                self.color = 'cyan'
            elif self.koord[0] == 0 and self.koord[1] == 3 or self.koord[0] == 8 and self.koord[1] == 6:
                self.color = 'purple'
            else:
                self.color = 'black'
            
    
    def get_click(self, mouse_pos):
        self.cell = self.get_cell(mouse_pos)
        if self.cell:
            self.on_click(self.cell)
            return self.cell
    
    def draw_linii(self, koord):
        global koord2
        #print(koord2)
        
        if (koord2[0] >= 0 and koord2[0] < self.width) and (koord2[1] >= 0 and koord2[1] < self.width):
            if self.width == 5:
                if not(koord2[0] == 0 and koord2[1] == 1) and not(koord2[0] == 3 and koord2[1] == 0) and not(koord2[0] == 4 and koord2[1] == 0) and not(koord2[0] == 0 and koord2[1] == 4) and not (koord2[0] == 1 and koord2[1] == 4) and not(koord2[0] == 3 and koord2[1] == 3) and not(koord2[0] == 2 and koord2[1] == 2) and not(koord2[0] == 2 and koord2[1] == 4):
                    pygame.draw.circle(screen, pygame.Color(self.color), (self.left+(self.cell_size*(1+koord2[0])-self.radius), self.top+(self.cell_size*(1+koord2[1])-self.radius)), (self.radius)-4)
                    self.spisok_button_GAME[koord[0]][koord[1]] = self.color
            if self.width == 6:
                if not(koord2[0] == 1 and koord2[1] == 2 ) and not( koord2[0] == 3 and koord2[1] == 2) and not ( koord2[0] == 1 and koord2[1] == 1 ) and not( koord2[0] == 2 and koord2[1] == 5) and not ( koord2[0] == 2 and koord2[1] == 4 ) and not( koord2[0] == 4 and koord2[1] == 4) and not ( koord2[0] == 3 and koord2[1] == 5 ) and not( koord2[0] == 5 and koord2[1] == 1) and not ( koord2[0] == 0 and koord2[1] == 5 ) and not( koord2[0] == 5 and koord2[1] == 0):         
                    pygame.draw.circle(screen, pygame.Color(self.color), (self.left+(self.cell_size*(1+koord2[0])-self.radius), self.top+(self.cell_size*(1+koord2[1])-self.radius)), (self.radius)-4)
                    self.spisok_button_GAME[koord[0]][koord[1]] = self.color
            if self.width == 7:
                if not(koord2[0] == 6 and koord2[1] == 3 ) and not( koord2[0] == 1 and koord2[1] == 6) and not( koord2[0] == 5 and koord2[1] == 3 ) and not( koord2[0] == 3 and koord2[1] == 4) and not( koord2[0] == 6 and koord2[1] == 4 ) and not( koord2[0] == 6 and koord2[1] == 6) and not( koord2[0] == 3 and koord2[1] == 0 ) and not( koord2[0] == 0 and koord2[1] == 6) and not( koord2[0] == 2 and koord2[1] == 6 ) and not( koord2[0] == 5 and koord2[1] == 5) and not( koord2[0] == 5 and koord2[1] == 1 ) and not( koord2[0] == 5 and koord2[1] == 4):
                    pygame.draw.circle(screen, pygame.Color(self.color), (self.left+(self.cell_size*(1+koord2[0])-self.radius), self.top+(self.cell_size*(1+koord2[1])-self.radius)), (self.radius)-4)
                    self.spisok_button_GAME[koord[0]][koord[1]] = self.color
            if self.width == 8:
                if not (koord2[0] == 6 and koord2[1] == 3 ) and not( koord2[0] == 7 and koord2[1] == 7) and not ( koord2[0] == 1 and koord2[1] == 0 ) and not( koord2[0] == 3 and koord2[1] == 7) and not ( koord2[0] == 2 and koord2[1] == 6 ) and not( koord2[0] == 5 and koord2[1] == 2) and not ( koord2[0] == 4 and koord2[1] == 2 ) and not( koord2[0] == 3 and koord2[1] == 4) and not ( koord2[0] == 7 and koord2[1] == 5 ) and not( koord2[0] == 4 and koord2[1] == 4) and not ( koord2[0] == 5 and koord2[1] == 6 ) and not( koord2[0] == 7 and koord2[1] == 6):
                    pygame.draw.circle(screen, pygame.Color(self.color), (self.left+(self.cell_size*(1+koord2[0])-self.radius), self.top+(self.cell_size*(1+koord2[1])-self.radius)), (self.radius)-4)
                    self.spisok_button_GAME[koord[0]][koord[1]] = self.color
            if self.width == 9:
                #print(self.spisok_button_GAME)            
                if not(koord2[0] == 5 and koord2[1] == 3 ) and not( koord2[0] == 5 and koord2[1] == 5) and not( koord2[0] == 7 and koord2[1] == 0 ) and not( koord2[0] == 8 and koord2[1] == 4)and not( koord2[0] == 1 and koord2[1] == 1 ) and not( koord2[0] == 4 and koord2[1] == 4) and not( koord2[0] == 2 and koord2[1] == 1 ) and not( koord2[0] == 6 and koord2[1] == 3) and not( koord2[0] == 0 and koord2[1] == 2 ) and not( koord2[0] == 2 and koord2[1] == 4) and not( koord2[0] == 4 and koord2[1] == 5 ) and not( koord2[0] == 8 and koord2[1] == 5) and not( koord2[0] == 0 and koord2[1] == 3 ) and not( koord2[0] == 8 and koord2[1] == 6):
                    pygame.draw.circle(screen, pygame.Color(self.color), (self.left+(self.cell_size*(1+koord2[0])-self.radius), self.top+(self.cell_size*(1+koord2[1])-self.radius)), (self.radius)-4)
                    self.spisok_button_GAME[koord[0]][koord[1]] = self.color                                                                                              
        else:
            if koord2[0] < 0:
                koord2[0] += 1
            if koord2[1] < 0:
                koord2[1] += 1            
            if koord2[0] >= self.width:
                koord2[0] -= 1
            if koord2[1] >= self.width:
                koord2[1] -= 1
    
    def win(self):
        if self.spisok_button_GAME == self.win_spisok:
            screen.fill((0, 0, 0))
            return True
    
    def load_level(self, filename):
        fullname = "data/" + filename
        levelFile = open(fullname, 'r')
        level_map = [line.strip().split() for line in levelFile]
        
        return level_map    
            
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as err:
        print('Cannot load file', name)
        raise SystemExit(err)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

    
running = True
gui = button_GAME.GUI()
gui.add_element(button_GAME.Button((130,230,60,60),"Да"))
k = 0
w_p = 5
h_p = 5
all_sprites = pygame.sprite.Group()

img = load_image('run.png')
img = pygame.transform.scale(img, (700, 365))
person = AnimatedSprite(img, 5, 2, 100, 100)           
    
clock = pygame.time.Clock()
running = True
while running:
    if k == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            gui.get_event(event)        
            
        screen.fill(pygame.Color('green'))
        gui.render(screen)
         
        gui.update()
 
        font = pygame.font.SysFont('arial', 29)
        text = font.render("Добро пожаловать в игру CTD!", 1, (0, 0, 255))
        text_x = 5
        text_y = 10               
        screen.blit(text, (text_x, text_y))
        font1 = pygame.font.SysFont('arial', 36)
        text1 = font1.render("Хотите начать игру?", 1, (0, 0, 255))
        text_x1 = 35
        text_y1 = 130               
        screen.blit(text1, (text_x1, text_y1))
        if button_GAME.k != 0:
            k = 1

    if k == 1:
        board = Board(w_p, h_p)
        koord2 = 0   
        screen.fill((0, 0, 0))
        board.render()
        k = 2
    if k == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                koord = board.get_click(event.pos)
                if koord:
                    koord2 = koord[:]
            elif event.type == pygame.KEYDOWN:
                if koord2:
                    if event.key == 273:                
                        koord2[1] -= 1                
                        board.draw_linii(koord2)                
                    elif event.key == 274:
                        koord2[1] += 1                
                        board.draw_linii(koord2)
                    elif event.key == 275:
                        koord2[0] += 1                
                        board.draw_linii(koord2)
                    elif event.key == 276:
                        koord2[0] -= 1                
                        board.draw_linii(koord2)  
    
        if board.win():
            if w_p != 9:
                w_p += 1
                h_p += 1
                board = Board(w_p, h_p)
                running = True
                koord2 = 0   
                screen.fill((0, 0, 0))
                board.render()
            else:
                k = 3
    
    if k == 3:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 50)
        text = font.render("Вы прошли игру!", 1, (0, 0, 255))
        text_x = 15
        text_y = 20               
        screen.blit(text, (text_x, text_y))    
        all_sprites.update()
        all_sprites.draw(screen)
        clock.tick(10)
        pygame.display.flip()        
 
    pygame.display.flip()