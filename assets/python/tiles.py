import turtle as t

screen_width = 640
screen_height = 360

tile_data = []

def addTile(x,y,type):
    tile_data.data.append([x,y,type])

def drawTile():
    t.shape("square")

def renderTiles():
    x = -screen_width/2
    y = screen_height/2
    for tile in tile_data:
        if (abs(tile[0]) <= screen_width/2 and abs(tile[1]) <= screen_height/2):
            t.goto(tile[0],tile[1])
            drawTile()



