import time
import images
import visualization

def main(size):

    start_time = time.time()
    picture_handler = images.Images()
    picture_handler.scan_directory()
    picture_handler.scan_image(size)
    print("[Finished running in " + str(round(- start_time + time.time(), 3)) + " seconds]")
    vis = visualization.Visualization(size)
    while True:
        vis.update(picture_handler.imgnames[0], picture_handler.calculate_rect_bounds())

main((400, 400))
