from turtle import *
import random

screen = Screen()
screen.setup(width=1.0, height=1.0)

SPEED = 8
MAX_SIZE = 125
MIN_SIZE = 5
MIN_DISTANCE = 30
MAX_DISTANCE = 100
COUNT_BEFORE_BG_COLOR_ALLOWED = 125
PALETTES = [
    ["#FAE7EB", "#E0D4E7", "#dbeef7", "#bdd2e4", "#eeceda", "#ccdceb"], #Cotton Candy Cloud
    ["#f8edeb", "#fec89a", "#fcd5ce", "#ffdab9", "#f49595", "#f1cebe"], #Mango Smoothie
    ["#a9cdd7", "#d0edef", "#a9e4de", "#e1f6f2", "#f3d17c", "#83b8c6"], #Florida Keys
    ["#d8e2dc", "#f8edeb", "#FAE1DD", "#ded6ce", "#fec5bb", "#f5ebe0"], #Embroidery
    ["#fff5ed", "#fae0d8", "#f0f4bf", "#dfe1be", "#f1deee", "#c4b7bb"], #Spring Kiss
    ["#e1d3f8", "#b0b5ed", "#eeecf4", "#e4f4e3", "#f7f5ff", "#c5dbc4"], #Lavender Fields
    ["#f1efeb", "#f6f6f6", "#e8e1d5", "#ddd5d5", "#ededed", "#d3dce8"], #Organic Cotton
    ["#dadbdd", "#fcd5ce", "#ffcad4", "#fadde1", "#fff1f5", "#f6eee9"], #Ballerina
    ["#faedcb", "#c9e4de", "#c6def1", "#dbcdf0", "#f2c6de", "#f7d9c4"], #Pastel Rainbow
    ["#e5f8f8", "#eef6f2", "#d6dfe8", "#c2ebef", "#a8cad6", "#d5e3e4"], #Waterfall - pretty
    ["#fcfdaf", "#fdf8e1", "#f8dfc1", "#eec18e", "#f9ed85", "#fcefb4"], #Rubber Duck
    ["#dfe4d6", "#e9e2ee", "#a99abd", "#e5D0e3", "#d6d6e9", "#cfd7cf"], #Lilac
    ["#ccd5ae", "#e9edc9", "#e7f1dc", "#fefae0", "#e3e7a0", "#b5c1b2"], #Herb Garden
    ["#ffdfc8", "#d8e2dc", "#fec5bb", "#e8e8e4", "#ffe5d9", "#faf7f0"], #Canvas Tote
    ["#ffcae9", "#ffede4", "#fa9bcf", "#f4dbe9", "#c4c7e2", "#fff0f1"], #Barbie
    ["#ffadad", "#ffd6a5", "#fdffb6", "#e4f1ee", "#d9edf8", "#dedaf4"], #Technicolor
    ["#eac7c7", "#d5e3e8", "#e8a2a2", "#f7f5eb", "#a0c3d2", "#eae0da"], #Faded Glory
    ["#f7d9c4", "#ffdca9", "#f8c8c8", "#fcf9be", "#f8edeb", "#f8dfc1"], #Sherbert Dream
    ["#c0e5e8", "#efece6", "#daf4ef", "#deebeb", "#9edce1", "#efe4cb"], #Sandy Beach
    ["#97ecf1", "#dffdff", "#bdb2ff", "#fad1fa", "#fec868", "#f1f7b5"], #90s Kid
    ["#fd8a8a", "#ffcbcb", "#9ea1d4", "#f1f7b5", "#a8d1d1", "#dfebeb"], #New Kicks
    ["#f5fbfb", "#d9e2de", "#f0e9df", "#507882", "#edd7c8", "#e1eff0"], #Emerald Sands
    ["#ede2ff", "#f7d59c", "#fff5c1", "#afb3ce", "#fae4cb", "#dbcdf0"], #Golden Girls
    ["#f7e5ec", "#eebec6", "#d28a8c", "#ffd8cc", "#fdba90", "#f9d4b2"], #Peach Rose
    ["#d6f0e2", "#ffeab8", "#bfdbc8", "#ffe8a4", "#e4eeeb", "#fff6db"], #Citrus Mint
    ["#ece9f2", "#bfbde2", "#e1bde3", "#f4e2dc", "#e9eafb", "#ccc6d9"], #Lavendar Haze
    ["#fad4d9", "#fce9b2", "#f8d7c6", "#ffedf3", "#e0eed5", "#f2cce3"], #Kawaii
    ["#c4d7e0", "#e5f4f4", "#879ba6", "#a3bccb", "#dae7eb", "#e8ebcf"], #Summer Storm
    ["#d2c8d9", "#eedbe6", "#f1ebf9", "#c3cfde", "#eaf6fb", "#dfe6f2"], #Enchanted Twilight
    ['#faf1c8', '#badfdb', '#4dc8c0', '#ffc2aa', '#f78558'], #Aesthetic Summer
]
PALETTE_NAMES = ["Cotton Candy Cloud", "Mango Smoothie", "Florida Keys", "Embroidery", "Spring Kiss", "Lavender Fields", "Organic Cotton", "Ballerina", "Pastel Rainbow", "Waterfall", "Rubber Duck", "Lilac", "Herb Garden", "Canvas Tote", "Barbie", "Technicolor", "Faded Glory", "Sherbert Dream", "Sandy Beach", "90s Kid", "New Kicks", "Emerald Sands", "Golden Girls", "Peach Rose", "Citrus Mint", "Lavendar Haze", "Kawaii", "Summer Storm", "Enchanted Twilight", "Aesthetic Summer"]

CHOSEN_PALETTE_INDEX = random.randint(0, len(PALETTES) - 1)
CHOSEN_PALETTE_NANE = PALETTE_NAMES[CHOSEN_PALETTE_INDEX]
COLORS = PALETTES[CHOSEN_PALETTE_INDEX]
BG_COLOR = random.choice(COLORS)

shapeCount = 0

screen.title(CHOSEN_PALETTE_NANE)

def getRandomSize():
    return random.randrange(MIN_SIZE, MAX_SIZE)

def getRandomColor():
    chosenColor = random.choice(COLORS)
    while shapeCount < COUNT_BEFORE_BG_COLOR_ALLOWED and chosenColor == BG_COLOR:
        chosenColor = random.choice(COLORS)
    return chosenColor

def moveRandom():
    setheading(0)
    penup()
    goto(0, 0)

    directionChoices = ["upLeft", "upRight", "downLeft", "downRight"]

    halfWidth = screen.window_width() / 2
    halfHeight = screen.window_height() / 2
    x, y = pos()
    direction = random.choice(directionChoices)

    maxUp = int(halfHeight - y)
    maxDown = int(halfHeight + y)
    maxRight = int(halfWidth - x)
    maxLeft = int(halfWidth + x)

    if direction == "upLeft":
        left(90)
        forward(random.randrange(0, maxUp))
        left(90)
        forward(random.randrange(0, maxLeft))
    elif direction == "upRight":
        left(90)
        forward(random.randrange(0, maxUp))
        right(90)
        forward(random.randrange(0, maxRight))
    elif direction == "downLeft":
        right(90)
        forward(random.randrange(0, maxDown))
        right(90)
        forward(random.randrange(0, maxLeft))
    else:
        right(90)
        forward(random.randrange(0, maxDown))
        left(90)
        forward(random.randrange(0, maxRight))

    setheading(0)
    pendown()

def star(shapeSize=20, shapeColor="black"):
    color(shapeColor)
    begin_fill()
    for i in range(5):
        forward(shapeSize)
        left(72)
        forward(shapeSize)
        right(144)
    end_fill()

def heart(shapeSize=20, shapeColor="black"):
    headingAtStart = heading()
    adjustedSize = shapeSize * .75# / 2
    newLength = adjustedSize * 113 / 56.5
    color(shapeColor)
    begin_fill()
    left(140)
    forward(newLength)
    circle(adjustedSize * -1, 200)
    setheading(60 + headingAtStart)
    circle(adjustedSize * -1, 200)
    forward(newLength)
    end_fill()

def drawRandomShape():
    choiceNames = ["star", "heart"]
    choices = {
        "star": star,
        "heart": heart
    }

    chosenFunction = choices[random.choice(choiceNames)]

    setheading(random.randrange(0, 361))
    startX, startY = pos()
    chosenFunction(getRandomSize(), getRandomColor())
    penup()
    goto(startX, startY)
    setheading(0)
    pendown()

speed(SPEED)
bgcolor(BG_COLOR)

def changePalette():
    global CHOSEN_PALETTE_INDEX
    CHOSEN_PALETTE_INDEX = random.randint(0, len(PALETTES) - 1)
    global CHOSEN_PALETTE_NAME
    CHOSEN_PALETTE_NAME = PALETTE_NAMES[CHOSEN_PALETTE_INDEX]
    global COLORS
    COLORS = PALETTES[CHOSEN_PALETTE_INDEX]
    global BG_COLOR
    BG_COLOR = random.choice(COLORS)

    global shapeCount
    shapeCount = 0

    clear()
    screen.title(CHOSEN_PALETTE_NAME)
    bgcolor(BG_COLOR)
    

#test new shape
# testStartHeading = random.randrange(0, 361)
# setheading(testStartHeading)
# shapeColor = "black"
# shapeSize = MAX_SIZE
# color(shapeColor)
# begin_fill()
# end_fill()
# done()


screen.onkey(changePalette, "Return")
screen.listen()

while True:    
    moveRandom()
    drawRandomShape()
    shapeCount += 1
    