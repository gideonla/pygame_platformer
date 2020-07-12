import random
import pdb
import pygame as pg
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        #pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        self.all_sprites =pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        p1 = Platfrom(0,HEIGHT-50,WIDTH,100)
        p2 = Platfrom(0, HEIGHT - 300, WIDTH*3/4, 100)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        self.all_sprites.add(p2)
        self.platforms.add(p2)

    def run(self):
        self.clock.tick(FPS)
        self.playing  = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.updates()
            self.draw()


    def updates(self):
        # Game Loop  - update
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            #print (self.player.pos.y)
            #print(self.player.vel)
            #pdb.set_trace()
            if self.player.vel.y>0.001 : # I have to add delta due to rounding error
                #pdb.set_trace()
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        self.all_sprites.update()


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        # show game over screen
        pass


g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.run()
    g.show_go_screen()

pg.quite()
