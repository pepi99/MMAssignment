class Cell:
    # Cell class for storing color information
    def __init__(self, color):
        self.color = color
        self.next_color = None

    def set_next_color(self, next_color):
        # Next color setter
        self.next_color = next_color

    def get_color(self):
        # Color getter
        return self.color

    def color_cell(self):
        # Set current color to the next color, if such exists
        if self.next_color is not None:
            self.color = self.next_color
            self.next_color = None


