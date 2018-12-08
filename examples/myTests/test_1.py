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
font = ImageFont.truetype(FredokaOne, 22)

# message to write
message = "Hello, World!"

# get width and height of the message to write
w, h = font.getsize(message)

# The x and y variables will tell the draw.text() function where to place the top left corner of our text
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

# draw message at a starting point, with decided font and colour
draw.text((x, y), message, inky_display.YELLOW, font)

inky_display.set_image(img)
inky_display.show()
