class Spot:
    """
    Spot class
    """
    def __init__(self, x, y, stone_color, stone_size):
        """
        Initialize x, y ,color and size
        Number, Number, Number, Number --> Spot
        """
        self.x = x
        self.y = y
        self.stone_color = stone_color
        self.stone_size = stone_size

    def display(self):
        """
        Display Stone
        """
        fill(self.stone_color)
        ellipse(self.x, self.y, self.stone_size, self.stone_size)
        strokeWeight(self.stone_size // 10)
