import os

import pygame.display
from PIL import Image


class Images:
    def __init__(self):
        self.imgs = []
        self.imgnames = []
        self.rgbas = []
        self.rect_pos = (0,0,0,0)
        self.pixel_bounds = []

    def scan_directory(self):
        with os.scandir('pictures/') as entries:
            for entry in entries:
                if entry.name.endswith(".png"):
                    img = Image.open("pictures/" + entry.name)
                    self.imgnames.append(entry.name)
                    self.imgs.append(img)

    def scan_image(self, size):
        for img in self.imgs:
            color_values = []
            for y in range(img.size[1]):
                for x in range(img.size[0]):
                    color_values.append(img.getpixel((x, y)))
            self.rgbas.append(color_values)
        self.find_colors(size)

    def find_colors(self, size):
        self.pixel_bounds = []
        for x, col in enumerate(self.rgbas[0]):
            if self.check_value(1, 255, 1, 255, 1, 255, col):
                x_v = x % self.imgs[0].size[1]
                y_v = x // self.imgs[0].size[1]
                x_v *= size[0] / self.imgs[1].size[0]
                y_v *= size[1] / self.imgs[1].size[1]
                print(f"x: {x_v}, y: {y_v}, color: {col}")
                self.pixel_bounds.append((x_v, y_v))


    def check_value(self, minr, maxr, ming, maxg, minb, maxb, rgb):
        return minr <= rgb[0] <= maxr and ming <= rgb[1] <= maxg and minb <= rgb[2] <= maxb

    def calculate_rect_bounds(self):
        if not self.pixel_bounds: return (0,0,0,0)
        tlx = min(item[0] for item in self.pixel_bounds)
        tly = min(item[1] for item in self.pixel_bounds)
        brx = max(item[0] for item in self.pixel_bounds)
        bry = max(item[1] for item in self.pixel_bounds)
        return (tlx, tly, brx, bry)