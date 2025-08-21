import pyray as rl
from Camera2D import Camera3D
from game import Game


rl.init_window(800, 600, "Vue de Haut - Camera 3D")
rl.set_target_fps(60)


camera = Camera3D()

game = Game(camera)


while not rl.window_should_close():
    game.update()
    game.draw()


rl.close_window()
