from PIL import Image, ImageFont, ImageDraw, ImageFilter
from matplotlib import font_manager
import random
import sys
from blendmodes.blend import blendLayers, BlendType

system_fonts = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
not_viable = ['mathjax', 'noto', 'symbol', 'icon', 'ding', 'emoji', 'emote', 'picture', 'awesome', 'material']
viable_fonts = [font for font in system_fonts if not any(nonviable in font.casefold() for nonviable in not_viable)]
print(f"filtered out {len(system_fonts) - len(viable_fonts)} fonts")

name = sys.argv[1] if len(sys.argv) > 1 else 'LOKI'
grow = True if len(sys.argv) > 2 and sys.argv[2] == '-grow' else False
widthfactor = 150 if grow else 100
width = widthfactor * len(name) + 200
height = width // 16 * 9

#get chromatic aberration offset
def gco():
    return random.randrange(-2, 2)

channels = [(255,0,0,255), (0,255,0,255), (0,0,255,255)]

baseframe = Image.new('RGBA', (width, height), (0,0,0,255))
frames = []
for j in range(25):
    frame = baseframe.copy()
    font_add = j*5 if grow else random.randrange(5, 26)
    pos_add = j if grow else -20 + random.randrange(-15, 15)
    for i in range(len(name)):
        random.shuffle(channels)
        letter1 = Image.new('RGBA', baseframe.size, (0,0,0,0))
        letter2 = Image.new('RGBA', baseframe.size, (0,0,0,0))
        letter3 = Image.new('RGBA', baseframe.size, (0,0,0,0))
        fnt = ImageFont.truetype(random.choice(viable_fonts), font_add + 70)
        # ImageDraw.Draw(letter).text(((i+1)*widthfactor - pos_add, widthfactor - pos_add), name[i], font=fnt, fill=(255,255,255,random.randrange(128, 256)))
        # letter = letter.filter(ImageFilter.BoxBlur(20))
        ImageDraw.Draw(letter1).text(((i+1)*widthfactor - pos_add + gco(), widthfactor - pos_add + gco()), name[i], font=fnt, fill=channels[0])
        ImageDraw.Draw(letter2).text(((i+1)*widthfactor - pos_add + gco(), widthfactor - pos_add + gco()), name[i], font=fnt, fill=channels[1])
        ImageDraw.Draw(letter3).text(((i+1)*widthfactor - pos_add - gco(), widthfactor - pos_add - gco()), name[i], font=fnt, fill=channels[2])
        letter = blendLayers(letter1, letter2, BlendType.DIFFERENCE)
        letter = blendLayers(letter, letter3, BlendType.DIFFERENCE)
        # ImageDraw.Draw(letter).text(((i+1)*widthfactor - pos_add, widthfactor - pos_add), name[i], font=fnt, fill=(255,255,255,random.randrange(225, 256)))
        frame = Image.alpha_composite(frame, letter)
    frames.append(frame)

frames[0].save('out.gif', save_all=True, append_images=frames[1:], duration=300, loop=0)