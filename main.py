import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Tutoriel Arcade"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()


y = SCREEN_HEIGHT / 2 + 70
arcade.draw_triangle_filled(250, y + 80,
                           150, y - 200,
                           350, y - 200,
                           arcade.color.GRAY)
arcade.draw_triangle_filled(450, y + 60,
                           150, y - 200,
                           450, y - 300,
                           arcade.color.GRAY)

arcade.draw_triangle_filled(100, y + 30,
                           150, y - 200,
                           450, y - 300,
                           arcade.color.GRAY)
arcade.draw_rectangle_filled(621, SCREEN_HEIGHT /1.6, 10, 200, arcade.csscolor.BROWN)
arcade.draw_rectangle_filled(640, SCREEN_HEIGHT /1.6, 10, 200, arcade.csscolor.BROWN)
arcade.draw_triangle_filled(100, y + 30,
                           150, y - 200,
                           450, y - 300,
                           arcade.color.DARK_GRAY)
arcade.draw_triangle_filled(550, y + 30,
                           580, y - 200,
                           450, y - 300,
                           arcade.color.GRAY)
arcade.draw_triangle_filled(450, y + 45,
                           150, y - 200,
                           450, y - 300,
                           arcade.color.LIGHT_GRAY)
arcade.draw_triangle_filled(700, y + 150,
                           950, y - 400,
                           450, y - 300,
                           arcade.color.GRAY)
arcade.draw_triangle_filled(470, y + 20,
                           700, y - 400,
                           50, y - 500,
                           arcade.color.GRAY)
arcade.draw_triangle_filled(110, y + 10,
                           300, y - 400,
                           100, y - 100,
                           arcade.color.LIGHT_GRAY)
arcade.draw_line(SCREEN_WIDTH - 800, SCREEN_HEIGHT - 500, SCREEN_WIDTH - 400, SCREEN_HEIGHT - 275, arcade.color.BROWN, 10)
arcade.draw_arc_filled(390, SCREEN_HEIGHT / 2 + 20, 50, 80, arcade.csscolor.BLACK, 0, 180)
arcade.draw_triangle_filled(20, y + 0,
                           390, y - 370,
                           100, y - 400,
                           arcade.color.DARK_GRAY)
arcade.draw_triangle_filled(8, y + -40,
                           -40, y - 500,
                           250, y - 500,
                           arcade.color.GRAY)
arcade.draw_triangle_filled(60, y + -70,
                           -40, y - 500,
                           250, y - 500,
                           arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(450, 200, 60, arcade.color.BLACK, num_segments=8, tilt_angle=5)
arcade.draw_triangle_filled(750, y + -40,
                           -40, y - 800,
                          5000, y - 6000,
                           arcade.color.LIGHT_GRAY)
arcade.draw_triangle_filled(750, y + 70,
                           -40, y - 800,
                          9000, y - 6000,
                           arcade.color.DARK_GRAY)
arcade.draw_triangle_filled(750, y + -40,
                           -40, y - 800,
                          5000, y - 6000,
                           arcade.color.LIGHT_GRAY)



arcade.draw_rectangle_filled(640, SCREEN_HEIGHT / 1.3, 60, 40, arcade.csscolor.SANDY_BROWN)

arcade.draw_text("the mountain", 100, SCREEN_HEIGHT - 50, arcade.color.RED_DEVIL)
arcade.draw_text("my house", 600, SCREEN_HEIGHT - 115, arcade.color.RED_DEVIL)

arcade.finish_render()

arcade.run()
