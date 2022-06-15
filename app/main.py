import time
import images

def main():
    start_time = time.time()
    picture_handler = images.Images()
    picture_handler.scan_directory()
    picture_handler.scan_image()
    print("[Finished running in " + str(round(- start_time + time.time(), 3)) + " seconds]")

main()
