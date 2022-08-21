from game_controller import GameController

# The proportion of boards changes accrodingly 
PIXEL_WIDTH = 1200
PIXEL_HEIGHT = 1200
BOARD_SIZE = 15

RECT_SIZE = PIXEL_WIDTH // BOARD_SIZE 
STONE_SIZE = RECT_SIZE - 25  
RECT_POS_X = RECT_SIZE // 2   
RECT_POS_Y = RECT_SIZE // 2   
BOARD_BOX_NUMBER = BOARD_SIZE - 1 

dot_position = set()
field = (PIXEL_WIDTH, PIXEL_HEIGHT)
# Creating nested list for 15X15 board
grid = [[0]*BOARD_BOX_NUMBER for n in range(BOARD_BOX_NUMBER)]
gc = GameController(field, dot_position, STONE_SIZE, RECT_SIZE)


def setup():
    """
    Set up the environment
    """
    # Set background
    size(*field)
    background(175,130,75)

    # Fill same color as background in the squares
    fill(175,130,75)

    # Set the board with squares
    # Add all the vertices of a square to dot_position
    strokeWeight(10)
    x,y = RECT_POS_X, RECT_POS_Y
    for row in grid:
        for col in row:
            square(x,y,RECT_SIZE)
            dot_position.add((x,y))
            dot_position.add((x, y + RECT_SIZE))
            x += RECT_SIZE
            dot_position.add((x,y))
            dot_position.add((x,y + RECT_SIZE))
        y += RECT_SIZE
        x = RECT_POS_X
    

def draw():
    """
    Update the environment
    """
    if gc.continue_game:
        if gc.playing == False:
            gc.end_text()
            print("Game is Over")
        elif mousePressed and gc.playing:
            gc.user_put_stone(mouseX, mouseY)
            gc.update()
