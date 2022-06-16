import time
import images
import visualization

def main():

    start_time = time.time()
    picture_handler = images.Images()
    picture_handler.scan_directory()
    picture_handler.scan_image()
    print("[Finished running in " + str(round(- start_time + time.time(), 3)) + " seconds]")
    vis = visualization.Visualization((400, 400))
    while True:
        vis.update(picture_handler.imgnames[0])

main()
