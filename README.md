# realnajan/effects
Sick image &amp; gif effects

## Usage

Clone repo:
```
git clone git@github.com:realnajan/effects.git
```
Select effect (i.e. sparkle), cd into it:
```
cd effects/sparkle
```
Install requirements:
```
pip install -r requirements.txt
```
View help:
```
python sparkle.py -h
```

## loki.py & loki_glitch.py

Creates a loki intro mock from given text.
Example:
INPUT: `python ./loki.py LOKI` | INPUT: `python ./loki_glitch.py FUCK`
------|--------
![Sparkle Example Input #1](https://github.com/realnajan/effects/blob/master/loki/out_normal.gif) | ![Sparkle Example Input #2](https://github.com/realnajan/effects/blob/master/loki/out_glitch.gif)

## sparkle.py

Creates a sparkly GIF from a still image. Uses [juanlao7/oilify](https://github.com/juanlao7/oilify/blob/master/oilify.py) for some transformations.
Example:
INPUT: `python ./sparkle.py ./sparkle_in_2.jpg -b 15` | OUTPUT
------|--------
![Sparkle Example Input #1](https://github.com/realnajan/effects/blob/master/examples/sparkle_in_1.jpg) | ![Sparkle Example Output #1](https://github.com/realnajan/effects/blob/master/examples/sparkle_out_1.gif)
INPUT: `python ./sparkle.py ./sparkle_in_2.jpg -b 15 -c true` | OUTPUT
![Sparkle Example Input #2](https://github.com/realnajan/effects/blob/master/examples/sparkle_in_2.jpg) | ![Sparkle Example Output #2](https://github.com/realnajan/effects/blob/master/examples/sparkle_out_2.gif)

## holotone.py

Creates a GIF that interestingly transitions between three duo-tone versions of a still image. **Requires [carloe/duotone](https://github.com/carloe/duotone-py.git)**.

INPUT: `python ./holotone.py ./holo_in_1.jpg -t 1 -o holo_out_1` | OUTPUT
---------------|---------------
![Holo Example Input #1](https://github.com/realnajan/effects/blob/master/examples/holo_in_1.jpg) | ![Holo Example Output #1](https://github.com/realnajan/effects/blob/master/examples/holo_out_1.gif)

