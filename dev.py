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

current_screen = "menu"

def setup():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(update, 1 / 60)
    arcade.run()


def update(delta_time, ):
    global score, hit, current_screen
    if current_screen == "play":
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
    global current_screen
    if current_screen == "menu":
        draw_menu()
    elif current_screen == "instructions":
        draw_instructions()
    elif current_screen == "play":
        background.draw()
        candy.draw()
        basket.draw()
        arcade.draw_text(f"Score : {score}", 250, 35, arcade.color.BLACK, 25, )


@window.event
def on_key_press(key, modifiers):
    global left_pressed, right_pressed, current_screen
    if current_screen == "menu":
        if key == arcade.key.P:
            current_screen = "play"
        if key == arcade.key.I:
            current_screen = "instructions"
    elif current_screen == "instructions":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"

    elif current_screen == "play":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
        if key == arcade.key.D:
            right_pressed = True
        if key == arcade.key.A:
            left_pressed = True


@window.event
def on_key_release(key, modifiers):
    global left_pressed, right_pressed, current_screen
    if current_screen == "play":
        if key == arcade.key.D:
            right_pressed = False
        if key == arcade.key.A:
            left_pressed = False


@window.event
def on_mouse_press(x, y, button, modifiers):
    pass

def draw_menu():
    arcade.set_background_color(arcade.color.BLACK)
    start_y = HEIGHT - 100
    start_x = 0
    width = 200
    arcade.draw_text("CANDY DROP",
                     start_x, start_y, arcade.color.YELLOW, 75, width=WIDTH, align="center")
    start_x = 0
    start_y = HEIGHT*0.6
    arcade.draw_text("Press the 'P' key to play",
                     start_x, start_y, arcade.color.WHITE, 30, width=WIDTH, align="center")
    start_y = HEIGHT*0.4
    arcade.draw_text("Press the 'I' key to see instructions",
                     start_x, start_y, arcade.color.WHITE, 30, width=WIDTH, align="center")
    start_y = HEIGHT*0.2
    arcade.draw_text("ENJOY",
                     start_x, start_y, arcade.color.WHITE, 40, width=WIDTH, align="center")

def draw_instructions():
    arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)
    start_y = HEIGHT - 100
    start_x = 0
    width = 200
    arcade.draw_text("INSTRUCTIONS: ",
                     start_x, start_y, arcade.color.RED_DEVIL, 50, width=WIDTH, align="center")
    start_x = 0
    start_y = HEIGHT*0.6
    arcade.draw_text("1. Use the 'A' and 'D' keys to move your basket LEFT/RIGHT",
                     start_x, start_y, arcade.color.WHITE, 20, width=WIDTH, align="center")
    start_y = HEIGHT*0.5
    arcade.draw_text("2. Collect the candies but DON'T let any touch the ground",
                     start_x, start_y, arcade.color.WHITE, 20, width=WIDTH, align="center")
    start_y = HEIGHT*0.4
    arcade.draw_text("3. Press the 'esc' key to exit instructions",
                     start_x, start_y, arcade.color.WHITE, 20, width=WIDTH, align="center")

    start_y = HEIGHT*0.2
    arcade.draw_text("4. HAVE FUN :)",
                     start_x, start_y, arcade.color.WHITE, 40, width=WIDTH, align="center")


if __name__ == '__main__':
    setup()
