import arcade
import random

WIDTH = 640
HEIGHT = 480

left_pressed = False
right_pressed = False

window = arcade.open_window(WIDTH, HEIGHT, "Halloween Candy Drop Game")

background = arcade.Sprite('sprites/background.png', center_x=320, center_y=240, scale=1)

candy = arcade.Sprite('sprites/candy.png', center_x=random.randint(1, 610), center_y=HEIGHT, scale=0.4)
candy.change_y = -7

basket = arcade.Sprite('sprites/basket.png', center_x=WIDTH / 2, center_y=128, scale=0.7)

score = 0
start_y = 220
start_x = 300


def setup():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(update, 1 / 60)
    arcade.run()


def update(delta_time, ):
    global score, hit
    hit = arcade.check_for_collision(basket, candy)
    candy.update()
    if candy.center_y == 130:
        candy.center_y = HEIGHT
        candy.center_x = random.randint(1, 610)
    if left_pressed:
        basket.center_x -= 12
    if right_pressed:
        basket.center_x += 12
    if basket.center_x > 600:
        basket.center_x -= 20
    if basket.center_x < 50:
        basket.center_x += 20
    if hit:
        candy.center_y = HEIGHT
        candy.center_x = random.randint(1, 610)
        score += 1
        


@window.event
def on_draw():
    background.draw()
    candy.draw()
    basket.draw()
    arcade.draw_text(f"Score : {score}", 250, 35, arcade.color.BLACK, 25, )


@window.event
def on_key_press(key, modifiers):
    global left_pressed, right_pressed
    if key == arcade.key.D:
        right_pressed = True

    if key == arcade.key.A:
        left_pressed = True


@window.event
def on_key_release(key, modifiers):
    global left_pressed, right_pressed

    if key == arcade.key.D:
        right_pressed = False

    if key == arcade.key.A:
        left_pressed = False


@window.event
def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
