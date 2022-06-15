import os
from PIL import Image


class Images:
    def __init__(self):
        self.imgs = []
        self.rgbas = []

    def scan_directory(self):
        with os.scandir('pictures/') as entries:
            for entry in entries:
                if entry.name.endswith(".png"):
                    img = Image.open("pictures/" + entry.name)
                    self.imgs.append(img)

    def scan_image(self):
        for img in self.imgs:
            color_values = []
            for y in range(img.size[1]):
                for x in range(img.size[0]):
                    color_values.append(img.getpixel((x, y)))
            self.rgbas.append(color_values)
        self.find_colors()

    def find_colors(self):
        for x, col in enumerate(self.rgbas[0]):
            if self.check_value(0, 255, 160, 165, 0, 30, col):
                print(f"x: {x % self.imgs[0].size[1]}, y: {x // self.imgs[0].size[1]}, color: {col}")

    def check_value(self, minr, maxr, ming, maxg, minb, maxb, rgb):
        return minr <= rgb[0] <= maxr and ming <= rgb[1] <= maxg and minb <= rgb[2] <= maxb

