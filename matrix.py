import os
import random
import sys

import pygame as pg


WORK_PATH = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
MATRIX_FONT = os.path.join(WORK_PATH, 'MS Mincho.ttf')


class MatrixLetters:
    def __init__(self, app):
        self.app = app

        self.letters = [chr(int('0x30a0', 16) + i) for i in range(1, 95)]
        self.font_size = 10
        self.font = pg.font.Font(MATRIX_FONT, self.font_size, bold=True)

        self.columns = app.WIDTH // self.font_size
        self.drops = [1 for i in range(0, self.columns)]

    def draw(self):
        for i in range(0, len(self.drops)):
            char = random.choice(self.letters)
            char_render = self.font.render(char, False, (0, 255, 0))
            pos = i * self.font_size, (self.drops[i] - 1) * self.font_size
            self.app.surface.blit(char_render, pos)
            if self.drops[i] * self.font_size > app.HEIGHT and random.uniform(0, 1) > 0.975:
                self.drops[i] = 0
            self.drops[i] = self.drops[i] + 1

    def run(self):
        self.draw()


class MatrixApp:
    def __init__(self):
        self.RES = self.WIDTH, self.HEIGHT = 1920, 1080
        pg.init()
        self.screen = pg.display.set_mode(self.RES)
        self.surface = pg.Surface(self.RES, pg.SRCALPHA)
        self.clock = pg.time.Clock()
        self.matrixLetters = MatrixLetters(self)

    def draw(self):
        self.surface.fill((0, 0, 0, 10))
        self.matrixLetters.run()
        self.screen.blit(self.surface, (0, 0))

    def run(self):
        while True:
            self.draw()
            pg.display.flip()
            self.clock.tick(50)

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        sys.exit()


if __name__ == '__main__':
    app = MatrixApp()
    app.run()
