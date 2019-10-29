import arcade


WIDTH = 640
HEIGHT = 480

window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")

current_screen = "menu"

def setup():
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    pass


@window.event
def on_draw():
    global current_screen
    arcade.start_render()

    if current_screen == "menu":
        draw_menu()


@window.event
def on_key_press(key, modifiers):
    global current_screen
    if current_screen == "menu":
        if key == arcade.key.P:
            current_screen = "play"
    elif current_screen == "play":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
    elif current_screen == "instructions":
        
@window.event
def on_key_release(key, modifiers):
    pass


@window.event
def on_mouse_press(x, y, button, modifiers):
    pass

def draw_menu():
    arcade.set_background_color(arcade.color.ASH_GREY)
    arcade.draw_circle_filled(100, 100, 25, arcade.color.BLUE)
def draw_instructions():
    arcade.set_background_color(arcade.color.BLACK
    start_y = HEIGHT-100
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
def draw_play():
    arcade.set_background_color(arcade.color.BLACK)


if __name__ == '__main__':
    setup()
