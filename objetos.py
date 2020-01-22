# -*- coding: utf-8 -*-
from Tkinter import PhotoImage
from random import choice

class Bola(object):
    def __init__(self, tela, raio, pos, vel, cor):
        self.tela = tela
        self.raio = raio
        self.pos  = pos
        self.vel = vel
        self.cor = cor
        self.buraco = None
        self.fig  = tela.create_oval(
            pos.x - raio, pos.y - raio,
            pos.x + raio, pos.y + raio,
            fill=self.cor, outline='black')
            
    def atualizar(self, dt):
        constante = 10
        if self.buraco==None:
            dp = self.vel * dt
            self.pos += dp
            if abs(self.vel) >= constante:
                self.vel+=-constante*self.vel/abs(self.vel)
            if abs(self.vel) < constante:
                self.vel = 0*self.vel
            if not (128 <= self.pos.x < 1145):
                self.vel.x *= -1
            if not (28 <= self.pos.y < 600):
                self.vel.y *= -1
            if 199 <= self.pos.x <= 606 and self.pos.y <= 80:
                self.vel.y *= -0.90
                self.pos.y=80
            if 674 <= self.pos.x <= 1079 and self.pos.y <= 80:
                self.vel.y *= -0.90
                self.pos.y=80
            if 199 <= self.pos.x <= 606 and self.pos.y >= 560:
                self.vel.y *= -0.90
                self.pos.y=560
            if 674 <= self.pos.x <= 1079 and self.pos.y >= 560:
                self.vel.y *= -0.90
                self.pos.y=560
            if 169 >= self.pos.x and 92 <= self.pos.y <= 547:
                self.vel.x *= -0.90
                self.pos.x=169
            if 1111 <= self.pos.x and 92 <= self.pos.y <= 547:
                self.vel.x *= -0.90
                self.pos.x=1111
            
        else:
            self.vel = 20*(self.buraco.pos-self.pos)
            dp = self.vel * dt
            self.pos += dp
            self.tela.move(self.fig, dp.x, dp.y)
        self.tela.delete(self.fig)
        self.fig  = self.tela.create_oval(
            self.pos.x - self.raio, self.pos.y - self.raio,
            self.pos.x + self.raio, self.pos.y + self.raio,
            fill=self.cor, outline='black')
            
            

class Cacapa(object):
    def __init__(self, tela, raio, pos):
        self.tela = tela
        self.raio = raio
        self.pos  = pos
        
        self.fig  = tela.create_oval(
            pos.x - raio, pos.y - raio,
            pos.x + raio, pos.y + raio,
            fill='black', outline='black')

class Canto(object):
    def __init__(self, tela, raio, pos):
        self.tela = tela
        self.raio = raio
        self.pos  = pos

class Bolabranca(object):
    def __init__(self, tela, raio, pos, vel,cor):
        self.tela = tela
        self.raio = raio
        self.pos  = pos
        self.vel  = vel
        self.cor=cor
        self.buraco = True
        self.fig  = tela.create_oval(
            pos.x - raio, pos.y - raio,
            pos.x + raio, pos.y + raio,
            fill=self.cor, outline='black')

    def atualizar(self, dt):
        constante = 10
        if self.buraco==True:
            dp = self.vel * dt
            self.pos += dp
            if abs(self.vel) >= constante:
                self.vel+=-constante*self.vel/abs(self.vel)
            if abs(self.vel) < constante:
                self.vel = 0*self.vel
            if not (128 <= self.pos.x < 1145):
                self.vel.x *= -1
            if not (28 <= self.pos.y < 600):
                self.vel.y *= -1
            if 199 <= self.pos.x <= 606 and self.pos.y <= 80:
                self.vel.y *= -0.90
                self.pos.y=80
            if 674 <= self.pos.x <= 1079 and self.pos.y <= 80:
                self.vel.y *= -0.90
                self.pos.y=80
            if 199 <= self.pos.x <= 606 and self.pos.y >= 560:
                self.vel.y *= -0.90
                self.pos.y=560
            if 674 <= self.pos.x <= 1079 and self.pos.y >= 560:
                self.vel.y *= -0.90
                self.pos.y=560
            if 92 <= self.pos.y <= 547 and 169 >= self.pos.x:
                self.vel.x *= -0.90
                self.pos.x=169
            if 92 <= self.pos.y <= 547 and 1111 <= self.pos.x:
                self.vel.x *= -0.90
                self.pos.x=1111
            
        else:
            self.vel = 20*(self.buraco.pos-self.pos)
            dp = self.vel * dt
            self.pos += dp
            self.tela.move(self.fig, dp.x, dp.y)
        self.tela.delete(self.fig)
        self.fig  = self.tela.create_oval(
            self.pos.x - self.raio, self.pos.y - self.raio,
            self.pos.x + self.raio, self.pos.y + self.raio,
            fill=self.cor, outline='black')
