#!/usr/bin/env python
import sys, pygame, random
from square import Square
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

class sliding:
    def __init__(self):
        self.screen_size = (600,600)
        self.dimensions = (rows,columns) = (4,4)
        self.FPS = 60
        self.black = (0,0,0)
        #colors taken from https://yeun.github.io/open-color/
        self.colors = [(134,142,150),(250,82,82),(230,73,128),(190,75,219),(121,80,242),(76,110,245),(34,138,230),(21,170,191),(18,184,134),(64,192,87),(130,201,30),(250,176,5),(253,126,20),(233,236,239),(255,236,153),(163,218,255)]
        self.shuffle = 5000
        self.columns = 4
        self.rows = 4
        self.simulatedclick = (0, 0)


    def calculate_xy(self,pos,puzzle):
        ''' calculates which square is the target '''
        w = 600 / self.columns
        h = 600 / self.rows
        to_return = (int(pos[0]//w),int(pos[1]//h))
        return to_return

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode(self.screen_size)
        font = pygame.font.SysFont("arial",64)
        clock = pygame.time.Clock()

        puzzle = []
        (w,h) = (self.screen_size[0]/self.columns,self.screen_size[1]/self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                position = j*self.rows + i
                color = self.colors[position]
                puzzle.append(Square(i,j,str(position+1),w,h,color,font))

        puzzle[15].color = (0,0,0)
        square16 = puzzle[15]



        for s in range(self.shuffle):
            simulatedclick = (random.randrange(600),random.randrange(600))
            simulatedmove = self.calculate_xy(simulatedclick, puzzle)
            for p in puzzle:
                if p.position == simulatedmove:
                    if square16.check_proximity(simulatedmove):
                        p.position = square16.position
                        square16.position = simulatedmove


        while True:
            clock.tick(self.FPS)

            screen.fill(self.black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    move = self.calculate_xy(pos, puzzle)

                    for a in puzzle:
                        if(a.position == move):
                            if (square16.check_proximity(move)):
                                a.position = square16.position
                                square16.position = move

            for p in puzzle:
                p.draw_square(pygame.draw,screen)


            pygame.display.flip()

if __name__ == '__main__':
    sliding = sliding()
    sliding.main()