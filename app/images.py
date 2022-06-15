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