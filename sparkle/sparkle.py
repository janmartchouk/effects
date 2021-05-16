import sys, getopt
import random
import argparse

import cv2
import numpy
from blendmodes.blend import blendLayers, BlendType
from PIL import Image
from tqdm import tqdm

from oil import process

parser = argparse.ArgumentParser(description='Generate a sparkly gif from a still image.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('input', help='file path of the input image')
parser.add_argument('-o', help='file path of the output image', dest='output', default='out')
parser.add_argument('-w', help='width of the output image', dest='width', type=int)
parser.add_argument('-b', help='brush size. increases the dots on the output', dest='brush', default=4, type=int)
parser.add_argument('-c', help='whether to cut off resulting black edges', dest='cut', default=False, type=bool)
args = parser.parse_args()

input_path = args.input
output_path = args.output
brush = args.brush
cut = args.cut

def image_resize(input_im, width):
    wpercent = (width/float(input_im.size[0]))
    hsize = int((float(input_im.size[1])*float(wpercent)))
    return hsize, input_im.resize((width,hsize), Image.LANCZOS)

def crossfade(in_arr):
    print("Crossfading frames...")
    out_arr = []

    for i in tqdm(range(len(in_arr) - 1)):
        item = in_arr[i]
        next_item = in_arr[in_arr.index(item) + 1]
        to_extend = []
        for i in range(11):
            to_extend.append(Image.blend(item, next_item, (i/10)))
        # inbetween_item = Image.blend(item, next_item, .10)
        # second_inbetween_item = Image.blend(item, next_item, .50)
        # third_inbetween_item = Image.blend(item, next_item, .75)
        out_arr.extend(to_extend)

    out_arr.append(Image.blend(in_arr[0], in_arr[-1], .5))

    return out_arr

frames = []

gold = Image.open(f'gold{random.randrange(1, 5)}.png').convert('RGBA')
input = Image.open(input_path).convert('RGBA')

if args.width:
    width = args.width
else:
    width = input.size[0]

height, input = image_resize(input, width)
gold = gold.resize(input.size)

input = blendLayers(input, gold, BlendType.HARDLIGHT)
input = cv2.cvtColor(numpy.array(input), cv2.COLOR_RGBA2BGRA) #convert to cv2 format

if input.ndim < 3:
    sys.exit('Only RGB or RGBA images supported.')
elif input.ndim == 4:
    input = input[:, :, :3]

print("Generating frames...")
for i in tqdm(range(1, 21)):
    if (i % 2) == 0:
        frame, duration = process(input, brush, 2)
        if cut:
            frame = frame[(brush*4):(height-(brush*4)), (brush*4):(width-(brush*4))]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGBA)
        frame = Image.fromarray(frame)
        frames.append(frame)

frames = crossfade(frames)

print("Saving...")
frames[0].save(f"{output_path}.gif", save_all=True, append_images=frames[1:], loop=0, duration=200)
print("Done!")