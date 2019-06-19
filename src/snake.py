import random

import arcade

RESOURCES_ROOT = "../resources/"
ORIGINAL_TILE_SIZE = 128
TILE_SCALING = 0.5
TILE_SIZE = int(ORIGINAL_TILE_SIZE * TILE_SCALING)
HALF_TILE_SIZE = int(TILE_SIZE / 2)
SCREEN_WIDTH = TILE_SIZE * 11
SCREEN_HEIGHT = TILE_SIZE * 11
SCREEN_TITLE = "Snake"


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
        elif self.moving_down:
            self.head.bottom -= TILE_SIZE
        elif self.moving_left:
            self.head.left -= TILE_SIZE
        elif self.moving_right:
            self.head.left += TILE_SIZE
        for body in self.body:
            temp_x = body.left
            temp_y = body.bottom
            body.left = x
            body.bottom = y
            x = temp_x
            y = temp_y

    def exists_at_coordinates(self, x, y):
        if self.head.left == x and self.head.bottom == y:
            return True
        for body in self.body:
            if body.left == x and body.bottom == y:
                return True
        return False

    def is_off_screen(self):
        if self.head.left < 0 or self.head.left >= SCREEN_WIDTH:
            return True
        if self.head.bottom < 0 or self.head.bottom >= SCREEN_HEIGHT:
            return True
        return False

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


class SnakeBody(arcade.Sprite):

    def __init__(self):
        super().__init__()

        texture = arcade.load_texture(f"{RESOURCES_ROOT}/images/snake/body.png", scale=0.7)
        self.append_texture(texture)
        self.set_texture(0)


class Food(arcade.Sprite):

    def __init__(self):
        super().__init__()

        texture = arcade.load_texture(f"{RESOURCES_ROOT}/images/snake/food.png", scale=TILE_SCALING)
        self.append_texture(texture)
        self.set_texture(0)


class SnakeHead(arcade.Sprite):

    def __init__(self):
        super().__init__()

        texture = arcade.load_texture(f"{RESOURCES_ROOT}/images/snake/head.png", scale=0.73)
        self.append_texture(texture)
        self.set_texture(0)


class SnakeGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.set_update_rate(1.0)

        self.wall_list = None
        self.snake = None
        self.food = None
        self.score = 0

    def setup(self):
        self.wall_list = arcade.SpriteList()
        self.snake = Snake()
        self.food = Food()
        self.score = 0

        self.setup_wall()
        self.snake.setup()
        self.setup_food()

    def setup_wall(self):
        for x in range(0, SCREEN_WIDTH, TILE_SIZE):
            for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
                wall = arcade.Sprite(f"{RESOURCES_ROOT}/images/tiles/grassCenter.png", TILE_SCALING)
                wall.left = x
                wall.bottom = y
                self.wall_list.append(wall)

    def setup_food(self):
        while True:
            x = random.randrange(0, SCREEN_WIDTH, TILE_SIZE)
            y = random.randrange(0, SCREEN_HEIGHT, TILE_SIZE)
            if not self.snake.exists_at_coordinates(x, y):
                break
        self.food.left = x
        self.food.bottom = y

    def on_draw(self):
        self.snake.move()
        self.wall_list.draw()
        if self.snake.exists_at_coordinates(self.food.left, self.food.bottom):
            self.setup_food()
            self.score += 1
        if self.snake.is_off_screen():
            self.draw_game_over()
        else:
            self.snake.draw()
            self.food.draw()
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, 10, arcade.csscolor.WHITE, 18)

    @staticmethod
    def draw_game_over():
        arcade.draw_text("Game Over", TILE_SIZE, SCREEN_HEIGHT / 2, arcade.color.WHITE, 54)

    def on_key_press(self, key, modifiers):
        if (key == arcade.key.UP or key == arcade.key.W) and not self.snake.moving_down:
            self.snake.set_moving_up()
        elif (key == arcade.key.DOWN or key == arcade.key.S) and not self.snake.moving_up:
            self.snake.set_moving_down()
        elif (key == arcade.key.LEFT or key == arcade.key.A) and not self.snake.moving_right:
            self.snake.set_moving_left()
        elif (key == arcade.key.RIGHT or key == arcade.key.D) and not self.snake.moving_left:
            self.snake.set_moving_right()


def main():
    window = SnakeGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
