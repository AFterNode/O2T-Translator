from PIL import ImageGrab
import os

def print_screen(top_left_x: int,
                 top_left_y: int,
                 bottom_right_x: int,
                 bottom_right_y: int,
                 save_path):
    im = ImageGrab.grab(bbox=(top_left_x, top_left_y, bottom_right_x, bottom_right_y))
    im.save(save_path)
