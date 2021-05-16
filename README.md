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

## sparkle.py

Creates a sparkly GIF from a still image. Uses [juanlao7/oilify](https://github.com/juanlao7/oilify/blob/master/oilify.py) for some transformations.
Example:
INPUT: `python ./sparkle.py ./sparkle_in_2.jpg -b 15` | OUTPUT
------|--------
![Sparkle Example Input #1](https://github.com/realnajan/effects/blob/master/examples/sparkle_in_1.jpg) | ![Sparkle Example Output #1](https://github.com/realnajan/effects/blob/master/examples/sparkle_out_1.gif)
INPUT: `python .\sparkle.py .\sparkle_in_2.jpg -b 15 -c true` | OUTPUT
![Sparkle Example Input #2](https://github.com/realnajan/effects/blob/master/examples/sparkle_in_2.jpg) | ![Sparkle Example Output #2](https://github.com/realnajan/effects/blob/master/examples/sparkle_out_2.gif)
