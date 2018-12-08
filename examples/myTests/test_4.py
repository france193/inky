from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

# get inky display variable
inky_display = InkyPHAT("yellow")

# set inky display border (YELLOW/BLACK/WHITE)
inky_display.set_border(inky_display.YELLOW)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

text = "29.5"
font = ImageFont.truetype(FredokaOne, 22)

# Get the width/height of the text if it were rendered with our chosen font
text_w, text_h = font.getsize(text)

# Create a 1bit mask canvas to fit the text
text_mask = Image.new("1", (text_w, text_h))

# Set up ImageDraw
mask_draw = ImageDraw.Draw(text_mask)

# Write the text, using colour 1 (on) as this is an on/off 1bit canvas
mask_draw.text((0, 0), text, 1, font)

# Using the mask to guide which pixels should be set,
# this is where we pick the text colour.
draw.paste(InkyPHAT.BLACK, (0, 0), text_mask.rotate(90))
