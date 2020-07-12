# sprite classes for platfrom game
import pygame as pg
from settings import *
#from main import Game
vec = pg.math.Vector2
import pdb
PLAYER_W = 30
PLAYER_H = 40
class Player(pg.sprite.Sprite,):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((PLAYER_W,PLAYER_H))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.pos = vec(WIDTH/2,HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.game = game


    def check_colision_left(self):
        self.pos.x -= 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.pos.x += 1
        if hits:
            # pdb.set_trace()
            if self.rect.collidepoint(hits[0].rect.midright) or self.rect.collidepoint(
                    hits[0].rect.topright) or self.rect.collidepoint(hits[0].rect.bottomright):
                print(self.rect.left)
                self.pos.x = hits[0].rect.right + PLAYER_W / 2
                print(self.rect.left)
                self.vel.x = 0

    def update(self):
        self.acc = vec(0,GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_DOWN]:
            self.acc.y = PLAYER_ACC
        if keys[pg.K_SPACE]:
            self.jump()

        self.acc += self.vel*PLAYER_FRICTION
        #self.acc.x +=self.vel.x*PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel
        #take care of wrap around
        self.pos.x = self.pos.x%WIDTH

        self.rect.midbottom = self.pos
        self.check_colision_left()

    def jump(self):
        self.pos.y +=1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.pos.y -= 1
        if hits:
             self.vel.y -=JUMP_VEL





class Platfrom(pg.sprite.Sprite):

    def __init__(self,x,y,w,h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

