import pygame
k = 0

class GUI:
    def __init__(self):
        self.elements = []
        
        
    def add_element(self, element):
        self.elements.append(element)
        
        
    def render(self, surface):
        for element in self.elements:
            render = getattr(element, 'render', None)
            if callable(render):
                element.render(surface)
    
    
    def update(self):
        for element in self.elements:
            update = getattr(element, 'update', None)
            if callable(update):
                element.update()     
                
                
    
    def get_event(self, event):
        for element in self.elements:
            get_event = getattr(element, 'get_event', None)
            if callable(get_event):
                element.get_event(event)      
 
class Label:
    def __init__(self, rect, text):
        self.Rect = pygame.Rect(rect)
        self.text = text
        self.bgcolor = pygame.Color('white')
        self.font_color = pygame.Color('purple')
        self.font = pygame.font.SysFont('arial', self.Rect.height - 18)
        self.rendered_text = None
        self.rendered_rect = None
        
        
    def render(self, surface):
        surface.fill(self.bgcolor, self.Rect)
        self.rendered_text = self.font.render(self.text, 1, self.font_color)
        self.rendered_rect = self.rendered_text.get_rect(x=self.Rect.x + 2, centery=self.Rect.centery)
        surface.blit(self.rendered_text, self.rendered_rect)
 
class Button(Label):
    def __init__(self, rect, text):
        super().__init__(rect, text)
        self.bgcolor = pygame.Color('blue')
        self.pressed = False
        
        
    def render(self, surface):
        global k
        surface.fill(self.bgcolor, self.Rect)
        self.rendered_text = self.font.render(self.text, 1, self.font_color)
        if not self.pressed:
            color1, color2 = pygame.Color('white'), pygame.Color('black')
            self.rendered_rect = self.rendered_text.get_rect(x=self.Rect.x + 2, centery=self.Rect.centery)
            k = 0
        else:
            color1, color2 = pygame.Color('black'), pygame.Color('white')
            self.rendered_rect = self.rendered_text.get_rect(x=self.Rect.x + 3, centery=self.Rect.centery - 2)
            k = 1
            
            
        # границы кнопки
        pygame.draw.rect(surface,color1, self.Rect, 2)
        pygame.draw.line(surface, color2, (self.Rect.right - 1, self.Rect.top),(self.Rect.right - 1, self.Rect.bottom), 2)
        pygame.draw.line(surface, color2, (self.Rect.left, self.Rect.bottom),(self.Rect.right, self.Rect.bottom-1), 2)
        surface.blit(self.rendered_text, self.rendered_rect)
        
        
        
    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.pressed = self.Rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:           
            self.pressed = False
            
def k():
    global k
    return k