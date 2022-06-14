import os

picture_names = []

with os.scandir('pictures/') as entries:
    for entry in entries:
        if entry.name.endswith(".png"):
            picture_names.append(entry.name)

print(picture_names)