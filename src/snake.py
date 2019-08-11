import arcade

from helpers import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from snakeBody import SnakeBody
from snakeHead import SnakeHead
from snakeSprite import set_sprite_texture


class Snake:

    def __init__(self):
        self.head = None
        self.body = None
        self.moving_up = True
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def setup(self):
        self.head = SnakeHead()
        self.body = arcade.SpriteList()
        self.moving_up = True
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        starting_x = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 2) % TILE_SIZE
        starting_y = (SCREEN_HEIGHT / 2) - (SCREEN_HEIGHT / 2) % TILE_SIZE
        self.head.left = starting_x
        self.head.bottom = starting_y
        for i in range(1, 3):
            body = SnakeBody()
            body.left = starting_x
            body.bottom = starting_y - (TILE_SIZE * i)
            self.body.append(body)

    def draw(self):
        self.head.draw()
        self.body.draw()

    def move(self):
        x = self.head.left
        y = self.head.bottom
        if self.moving_up:
            self.head.bottom += TILE_SIZE
            self.head.set_texture_up()
        elif self.moving_down:
            self.head.bottom -= TILE_SIZE
            self.head.set_texture_down()
        elif self.moving_left:
            self.head.left -= TILE_SIZE
            self.head.set_texture_left()
        elif self.moving_right:
            self.head.left += TILE_SIZE
            self.head.set_texture_right()
        for body in self.body:
            current_x = body.left
            current_y = body.bottom
            set_sprite_texture(body, current_x, current_y, x, y)
            body.left = x
            body.bottom = y
            x = current_x
            y = current_y

    def extend(self):
        body_before_current_tail = self.body[len(self.body) - 2]
        current_tail = self.body[len(self.body) - 1]
        new_tail = SnakeBody()
        set_sprite_texture(new_tail, current_tail.left, current_tail.bottom,
                           body_before_current_tail.left, body_before_current_tail.bottom)
        new_tail.left = current_tail.left
        new_tail.bottom = current_tail.bottom
        self.body.append(new_tail)

    def _head_exists_at_coordinates(self, x, y):
        return self.head.left == x and self.head.bottom == y

    def _body_exists_at_coordinates(self, x, y):
        for body in self.body:
            if body.left == x and body.bottom == y:
                return True
        return False

    def exists_at_coordinates(self, x, y):
        return self._head_exists_at_coordinates(x, y) or self._body_exists_at_coordinates(x, y)

    def is_off_screen(self):
        if self.head.left < 0 or self.head.left >= SCREEN_WIDTH:
            return True
        if self.head.bottom < 0 or self.head.bottom >= SCREEN_HEIGHT:
            return True
        return False

    def has_collided_with_self(self):
        return self._body_exists_at_coordinates(self.head.left, self.head.bottom)

    def _reset_movement(self):
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def set_moving_up(self):
        self._reset_movement()
        self.moving_up = True

    def set_moving_down(self):
        self._reset_movement()
        self.moving_down = True

    def set_moving_left(self):
        self._reset_movement()
        self.moving_left = True

    def set_moving_right(self):
        self._reset_movement()
        self.moving_right = True
