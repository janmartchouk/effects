import sys, getopt
import random
import argparse

import cv2
import numpy
from blendmodes.blend import blendLayers, BlendType
from PIL import Image

from oil import process

parser = argparse.ArgumentParser(description='Generate a sparkly gif from a still image.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('input', help='file path of the input image')
parser.add_argument('-o', help='file path of the output image', dest='output', default='out')
parser.add_argument('-w', help='width of the output image', dest='width', default=500, type=int)
parser.add_argument('-b', help='brush size. increases the dots on the output. only even numbers', dest='brush', default=4, type=int)
parser.add_argument('-c', help='whether to cut off resulting black edges', dest='cut', default=False, type=bool)
args = parser.parse_args()

input_path = args.input
output_path = args.output
width = args.width
brush = args.brush
cut = args.cut

print(cut)

def image_resize(input_im, width):
    wpercent = (width/float(input_im.size[0]))
    hsize = int((float(input_im.size[1])*float(wpercent)))
    return hsize, input_im.resize((width,hsize), Image.LANCZOS)

def crossfade(in_arr):
    out_arr = []

    for i in range(len(in_arr) - 1):
        item = in_arr[i]
        next_item = in_arr[in_arr.index(item) + 1]
        inbetween_item = Image.blend(item, next_item, .25)
        second_inbetween_item = Image.blend(item, next_item, .50)
        third_inbetween_item = Image.blend(item, next_item, .75)
        out_arr.extend((item, inbetween_item, second_inbetween_item, third_inbetween_item))

    out_arr.append(Image.blend(in_arr[0], in_arr[-1], .5))

    return out_arr

frames = []

gold = Image.open(f'gold{random.randrange(1, 5)}.png').convert('RGBA')
input = Image.open(input_path).convert('RGBA')

height, input = image_resize(input, width)
gold = gold.resize(input.size)

input = blendLayers(input, gold, BlendType.HARDLIGHT)
input = cv2.cvtColor(numpy.array(input), cv2.COLOR_RGBA2BGRA) #convert to cv2 format

if input.ndim < 3:
    sys.exit('Only RGB or RGBA images supported.')
elif input.ndim == 4:
    input = input[:, :, :3]

for i in range(1, 21):
    if (i % 2) == 0:
        frame, duration = process(input, brush, 1.5)
        if cut:
            frame = frame[(brush*3):(height-(brush*3)), (brush*3):(width-(brush*3))]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGBA)
        frame = Image.fromarray(frame)
        frames.append(frame)

frames = crossfade(frames)

frames[0].save(f"{output_path}.gif", save_all=True, append_images=frames[1:], loop=0, duration=200)