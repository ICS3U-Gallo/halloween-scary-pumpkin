### post code here
###background screen for game in progress
#STILL need logic
#STILL need title screen
import arcade


WIDTH = 640
HEIGHT = 480

window = arcade.open_window(WIDTH, HEIGHT, "Haloween Candy Drop Game")


def setup():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    pass


@window.event
def on_draw():
    arcade.start_render()
    # GROUND
    arcade.draw_lrtb_rectangle_filled(0, WIDTH, 100, 0, arcade.color.DARK_SEA_GREEN)
    # MOON
    arcade.draw_circle_filled(WIDTH-100, HEIGHT-75, 30, arcade.color.WHITE_SMOKE)

    draw_pumkin(75, 50)
    draw_pumkin(300, 50)
    #PUMPKIN
def draw_pumkin(x: int, y: int):
    #BODY
    BODY_WIDTH = 70
    BODY_HEIGHT = 45
    arcade.draw_ellipse_filled(x, y, BODY_WIDTH, BODY_HEIGHT, arcade.color.ORANGE )
    #STUMP
    arcade.draw_rectangle_filled(x+BODY_WIDTH/20, y+30, 8, 15, arcade.color.GREEN)
    #EYE
    arcade.draw_triangle_filled(x+BODY_HEIGHT-30, y, x+BODY_WIDTH-45, y+10, x+BODY_WIDTH-40, y, arcade.color.BLACK)
    arcade.draw_triangle_filled(x+BODY_HEIGHT-70, y, x+BODY_WIDTH-90, y+10, x+BODY_WIDTH-80, y, arcade.color.BLACK)
    #MOUTH
    arcade.draw_ellipse_filled(x+BODY_WIDTH/20, y-10, 25, 15, arcade.color.BLACK)
    arcade.draw_ellipse_filled(x+BODY_WIDTH/20, y-4, 20, 15, arcade.color.ORANGE)
    arcade.draw_rectangle_filled(x+BODY_WIDTH-70, y-11, 5, 5, arcade.color.ORANGE)
    arcade.draw_rectangle_filled(x+BODY_WIDTH-62, y-15, 5, 5, arcade.color.ORANGE)
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
