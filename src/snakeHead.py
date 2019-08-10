import arcade

from helpers import get_texture


class SnakeHead(arcade.Sprite):
    TEXTURE_UP = 0
    TEXTURE_DOWN = 1
    TEXTURE_LEFT = 2
    TEXTURE_RIGHT = 3

    def __init__(self):
        super().__init__()

        up_texture = arcade.load_texture(get_texture("images/snake/headUp.png"), scale=0.73)
        self.append_texture(up_texture)
        down_texture = arcade.load_texture(get_texture("images/snake/headDown.png"), scale=0.73)
        self.append_texture(down_texture)
        left_texture = arcade.load_texture(get_texture("images/snake/headLeft.png"), scale=0.73)
        self.append_texture(left_texture)
        right_texture = arcade.load_texture(get_texture("images/snake/headRight.png"), scale=0.73)
        self.append_texture(right_texture)

        self.set_texture(self.TEXTURE_UP)

    def set_texture_up(self):
        self.set_texture(self.TEXTURE_UP)

    def set_texture_down(self):
        self.set_texture(self.TEXTURE_DOWN)

    def set_texture_left(self):
        self.set_texture(self.TEXTURE_LEFT)

    def set_texture_right(self):
        self.set_texture(self.TEXTURE_RIGHT)
