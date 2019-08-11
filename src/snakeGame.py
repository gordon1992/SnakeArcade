import random

import arcade

from food import Food
from helpers import get_texture, TILE_SCALING, TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from snake import Snake


class SnakeGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.set_update_rate(1.0)

        self.wall_list = None
        self.snake = None
        self.food = None
        self.score = 0
        self.should_wait_until_next_redraw = False

    def setup(self):
        self.wall_list = arcade.SpriteList()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.should_wait_until_next_redraw = False

        self.setup_wall()
        self.snake.setup()
        self.setup_food()

    def setup_wall(self):
        for x in range(0, SCREEN_WIDTH, TILE_SIZE):
            for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
                wall = arcade.Sprite(get_texture("images/tiles/grassCenter.png"), TILE_SCALING)
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
        self.should_wait_until_next_redraw = False
        self.snake.move()
        self.wall_list.draw()
        if self.snake.exists_at_coordinates(self.food.left, self.food.bottom):
            self.setup_food()
            self.score += 1
            self.snake.extend()
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
        # If multiple key presses handled between redraws, there is a risk that the snake can do
        # a 180 degree turn on the spot thus moving over itself. This flag prevents this.
        if self.should_wait_until_next_redraw:
            return
        else:
            self.should_wait_until_next_redraw = True
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
