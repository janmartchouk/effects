#https://github.com/juanlao7/oilify/blob/master/oilify.py
import random
import time
from math import pi

import numpy as np
from matplotlib import pyplot as plt
from skimage import draw

MEASURE_MIN_TIME = False
BRUSHES = 50

def showImage(image):
    plt.imshow(image)
    plt.show()

def process(inputImage, brushSize, expressionLevel):
    start = time.time()
    
    brushSizeInt = int(brushSize)
    expressionSize = brushSize * expressionLevel
    margin = int(expressionSize * 2)
    halfBrushSizeInt = brushSizeInt // 2
    
    shape = ((inputImage.shape[0] - 2 * margin) // brushSizeInt, (inputImage.shape[1] - 2 * margin) // brushSizeInt)
    brushes = [draw.ellipse(halfBrushSizeInt, halfBrushSizeInt, brushSize, random.randint(brushSizeInt, expressionSize), rotation=random.random() * pi) for _ in range(BRUSHES)]

    result = np.zeros(inputImage.shape, dtype=np.uint8)

    for x in range(margin, inputImage.shape[0] - margin, brushSizeInt):
        for y in range(margin, inputImage.shape[1] - margin, brushSizeInt):
            ellipseXs, ellipseYs = random.choice(brushes)
            result[x + ellipseXs, y + ellipseYs] = inputImage[x, y]
    
    return result, time.time() - start