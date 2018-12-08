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
font = ImageFont.truetype(FredokaOne, 17)

# message to write
message1 = "ROW 1 - Hello, World! - :D"
message2 = "ROW 2 - Hello, World! - :)"
message3 = "ROW 3 - Hello, World! - :("
message4 = "ROW 4 - Hello, World! - D:"

y_interval = inky_display.HEIGHT / 4

# get width and height of the message to write
w, h = font.getsize(message1)

a = (y_interval - h) / 2
x = (inky_display.WIDTH / 2) - (w / 2)

y1 = (y_interval * 0) + a
y2 = (y_interval * 1) + a
y3 = (y_interval * 2) + a
y4 = (y_interval * 3) + a

# draw message at a starting point, with decided font and colour
draw.text((x, y1), message1, inky_display.YELLOW, font)
draw.text((x, y2), message2, inky_display.YELLOW, font)
draw.text((x, y3), message3, inky_display.YELLOW, font)
draw.text((x, y4), message4, inky_display.YELLOW, font)

inky_display.set_image(img)
inky_display.show()
