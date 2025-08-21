import pyray as rl

class Game:
    def __init__(self, camera):
        self.camera = camera
        self.delta = 0.2

    def update(self):
        if rl.is_key_down(rl.KEY_RIGHT):
            self.camera.move(self.delta, 0)
        if rl.is_key_down(rl.KEY_LEFT):
            self.camera.move(-self.delta, 0)
        if rl.is_key_down(rl.KEY_UP):
            self.camera.move(0, -self.delta)
        if rl.is_key_down(rl.KEY_DOWN):
            self.camera.move(0, self.delta)

    def draw(self):
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)

        rl.begin_mode_3d(self.camera.get_camera())

        rl.draw_grid(20, 1.0)
        rl.draw_cube((0, 0.5, 0), 1, 1, 1, rl.BLUE)
        rl.draw_cube_wires((0, 0.5, 0), 1, 1, 1, rl.BLACK)

        rl.end_mode_3d()

        rl.draw_text("Vue de Haut - Camera 3D", 10, 10, 20, rl.DARKGRAY)

        rl.end_drawing()
