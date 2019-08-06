import arcade

from helpers import get_texture, TILE_SCALING


class Food(arcade.Sprite):

    def __init__(self):
        super().__init__()

        texture = arcade.load_texture(get_texture("images/snake/food.png"), scale=TILE_SCALING)
        self.append_texture(texture)
        self.set_texture(0)
