import arcade

from helpers import get_texture
from snakeSprite import SnakeSprite


class SnakeBody(SnakeSprite):

    def __init__(self):
        super().__init__()

        up_texture = arcade.load_texture(get_texture("images/snake/bodyUp.png"), scale=0.73)
        self.append_texture(up_texture)
        down_texture = arcade.load_texture(get_texture("images/snake/bodyDown.png"), scale=0.73)
        self.append_texture(down_texture)
        left_texture = arcade.load_texture(get_texture("images/snake/bodyLeft.png"), scale=0.73)
        self.append_texture(left_texture)
        right_texture = arcade.load_texture(get_texture("images/snake/bodyRight.png"), scale=0.73)
        self.append_texture(right_texture)

        self.set_texture(self.TEXTURE_UP)
