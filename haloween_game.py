import arcade
import random

WIDTH = 640
HEIGHT = 480

up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False
window = arcade.open_window(WIDTH, HEIGHT, "Halloween Candy Drop Game")
background = arcade.Sprite('sprites/background.png', center_x= 320
                     , center_y= 240, scale=1)
candy = arcade.Sprite('sprites/candy.png', center_x=random.randint(1, 640)
                     , center_y=HEIGHT, scale=0.4)
candy.change_y = -5
basket = arcade.Sprite('sprites/basket.png', center_x=random.randint(1, 640)
                     , center_y=HEIGHT, scale=0.1)
score = 0
start_y = 220
start_x = 300


def setup():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time,):
    global score
    candy.update()
    hit = arcade.check_for_collision(basket, candy)
    if hit == True:
        score += 1



@window.event
def on_draw():
    backround.draw()
    candy.draw()
    if candy.center_y == 130:
        candy.center_y += HEIGHT
        candy.center_x = random.randint(1, 640)




def draw_game():
    pass



@window.event
def on_key_press(key, modifiers):
    pass


@window.event
def on_key_release(key, modifiers):
    pass


@window.event
def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()


