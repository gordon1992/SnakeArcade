from arcade import Sprite


class SnakeSprite(Sprite):
    TEXTURE_UP = 0
    TEXTURE_DOWN = 1
    TEXTURE_LEFT = 2
    TEXTURE_RIGHT = 3

    def set_texture_up(self):
        self.set_texture(self.TEXTURE_UP)

    def set_texture_down(self):
        self.set_texture(self.TEXTURE_DOWN)

    def set_texture_left(self):
        self.set_texture(self.TEXTURE_LEFT)

    def set_texture_right(self):
        self.set_texture(self.TEXTURE_RIGHT)


def set_sprite_texture(body, current_x, current_y, new_x, new_y):
    if new_y > current_y:
        body.set_texture_up()
    elif new_y < current_y:
        body.set_texture_down()
    elif new_x < current_x:
        body.set_texture_left()
    elif new_x > current_x:
        body.set_texture_right()
    body.left = new_x
    body.bottom = new_y
