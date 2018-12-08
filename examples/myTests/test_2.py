from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

# get inky display variable
inky_display = InkyPHAT("yellow")

# set inky display border (YELLOW/BLACK/WHITE)
inky_display.set_border(inky_display.YELLOW)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

# decide font and size
font = ImageFont.truetype(FredokaOne, 30)

# message to write
message = "Hello, World!"

x = y = 0

# draw message at a starting point, with decided font and colour
draw.text((x, y), message, inky_display.YELLOW, font)

inky_display.set_image(img)
inky_display.show()
