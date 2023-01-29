import pygame
import random
import time
pygame.init()

class Snakegame:
    screen_height=600
    screen_width=1000
    #colours
    white=(255,255,255)
    black=(0,0,0)
    light_green=(200,250,210)
    red=(255,0,0)
    purple=(48,25,52)
    brown=(150,75,0)
    snakecolour=black


    #------------------

    exit_game=False
    
    gamename='Eating Fruit'
    window_colour=light_green
    
    clock=pygame.time.Clock()
    fps=60
    fontgameover=pygame.font.Font("fonts\gameover.ttf",100)
    fontscore=pygame.font.Font("fonts\score.ttf",40)
    fontbutton=pygame.font.SysFont(None,30)
    


    def __init__(self):
        self.window=pygame.display.set_mode((self.screen_width,self.screen_height))

        pygame.display.set_caption(self.gamename)
        

    def textonscreen(self,texts,font,colour,x,y):
        fonts=font
        text=fonts.render(texts,True,colour)
        self.window.blit(text,[x,y])

    def button(self,text,buttonx,buttony,buttonwidth=80,buttonheight=40,addingx=15,addingy=11,text_colour=purple,buttoncolour=black):
        pygame.draw.rect(self.window,buttoncolour,[buttonx,buttony,buttonwidth,buttonheight],4)
        x=self.fontbutton.render(text,True,text_colour)
        self.window.blit(x,[buttonx+addingx,buttony+addingy]) #877,12 --> x,y




    def buttonpressed(self,buttonx,buttony,buttonwidth=80,buttonheight=40):
        mouseposition=pygame.mouse.get_pos()
        mouse_x=mouseposition[0]
        mouse_y=mouseposition[1]
        if mouse_x>buttonx and mouse_x<(buttonwidth+buttonx-4) and mouse_y<(buttonheight+buttony-7) and mouse_y>buttony:
            return True
        else:
            return False



        '''    .......button press......

        e.g menu botton

        buttonwidth=80 
        buttonheight=40
        buttonx=877
        buttony=12
        if mouse_x>877 and mouse_x<953 and mouse_y<45 and mouse_y>12: ---> it is found experimentally
        '''




    def menuoptionsscreen(self):


        exit_menuoptionsscreen=False


        while not exit_menuoptionsscreen:
            self.window.fill(self.brown)
            self.button('Snake Colour',450,280,buttonwidth=150,addingx=11,addingy=9,text_colour=self.light_green,buttoncolour=self.white)

            for events in pygame.event.get():
                if events.type==pygame.QUIT:
                    pygame.quit()
                    quit()

                if events.type==pygame.MOUSEBUTTONDOWN:
                    if self.buttonpressed(450,280,buttonwidth=150):
                        self.changecolourscreen()
                        exit_menuoptionsscreen=True

            pygame.display.update()

    def changecolourscreen(self):
        exitchangecolourscreen=False
        while not exitchangecolourscreen:
            self.window.fill(self.brown)

            self.button('RED',67,289,text_colour=self.light_green,buttoncolour=self.white)
            self.button('BLACK',250,289,text_colour=self.light_green,buttoncolour=self.white,buttonwidth=85,addingx=8)

            for events in pygame.event.get():
                if events.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if events.type==pygame.MOUSEBUTTONDOWN:
                    if self.buttonpressed(67,289):
                        self.snakecolour=self.red
                        exitchangecolourscreen=True
                    if self.buttonpressed(250,289,buttonwidth=85):
                        self.snakecolour=self.black
                        exitchangecolourscreen=True


                        
        
            pygame.display.update()



    def gameoverscreen(self):
        exitgameoverscreen=False    
        while not exitgameoverscreen:
            self.window.fill(self.white)
            self.textonscreen('Game Over',self.fontgameover,self.purple,295,250)
            smallfontgameover=pygame.font.Font("fonts\gameover.ttf",40)

            self.textonscreen('Press Space to play again',smallfontgameover,self.purple,295,350)



            for events in pygame.event.get():
                if events.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if events.type==pygame.KEYDOWN:
                    if events.key==pygame.K_SPACE:
                        exitgameoverscreen=True


            pygame.display.update()
            
        self.gameplaying()



    def gameplaying(self):
        self.score=0

        self.snake_x=54
        self.snake_y=90
        self.velocity_x=0
        self.velocity_y=0
        self.food_x=random.randint(30,950)
        self.food_y=random.randint(60,530)
        
        
        

        self.exit_game=False
        
        while not self.exit_game:
            #variables 
            
            
            self.snake_size=25

            
            
            self.init_snake_velocity=5
            
            self.snake_x+=self.velocity_x
            self.snake_y+=self.velocity_y

            #-------------------------------


            
            self.window.fill(self.window_colour)
            self.textonscreen(f'Score: {self.score}',self.fontscore,self.purple,12,12)
            pygame.draw.rect(self.window,self.black,[25,60,950,530],5) #x,y ,width,height

            pygame.draw.rect(self.window,self.black,[self.food_x,self.food_y,20,20])

            pygame.draw.rect(self.window,self.snakecolour,[self.snake_x,self.snake_y,self.snake_size,self.snake_size])
            self.button('Menu',877,12)


            for events in pygame.event.get():
                if events.type==pygame.MOUSEBUTTONDOWN:
                        if events.button==1:
                            if self.buttonpressed(877,12) :

                                self.menuoptionsscreen()


                if events.type==pygame.QUIT:


                    pygame.quit()
                    quit()
                if events.type==pygame.KEYDOWN:
                    if events.key==pygame.K_RIGHT:
                        self.velocity_x=self.init_snake_velocity
                        self.velocity_y=0
                    if events.key==pygame.K_LEFT:
                        self.velocity_x=-self.init_snake_velocity
                        self.velocity_y=0
                    if events.key==pygame.K_UP:
                        self.velocity_y=-self.init_snake_velocity
                        self.velocity_x=0
                    if events.key==pygame.K_DOWN:
                        self.velocity_y=self.init_snake_velocity
                        self.velocity_x=0

            
            # game end
            if self.snake_x <30 or self.snake_x > 948 or self.snake_y<65 or self.snake_y>555:
                self.gameover_snake_x=self.snake_x
                self.gameover_snake_y=self.snake_y

                self.exit_game=True

            # eating food

            if abs(self.snake_x-self.food_x)<10 and abs(self.snake_y-self.food_y)<10:
                self.food_x=random.randint(30,950)
                self.food_y=random.randint(60,530)
                self.score+=10
            # print(pygame.mouse.get_pos())
            pygame.display.update()
            
            




            self.clock.tick(self.fps)

        self.gameoverscreen()

            
    
    

if __name__=='__main__':
                    

        

    Window1=Snakegame()
    Window1.gameplaying()










   
    