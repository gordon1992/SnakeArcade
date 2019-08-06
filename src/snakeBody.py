import arcade

from helpers import get_texture


class SnakeBody(arcade.Sprite):

    def __init__(self):
        super().__init__()

        texture = arcade.load_texture(get_texture("images/snake/body.png"), scale=0.7)
        self.append_texture(texture)
        self.set_texture(0)
