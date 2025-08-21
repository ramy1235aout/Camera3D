import pyray as rl

class Camera3D:
    def __init__(self):
        self.camera = rl.Camera3D()
        self.camera.position = rl.Vector3(0.0, 20.0, 10.0)  
        self.camera.target = rl.Vector3(0.0, 0.0, 0.0)      
        self.camera.up = rl.Vector3(0.0, 1.0, 0.0)         
        self.camera.fovy = 45.0                  
        self.camera.projection = rl.CAMERA_PERSPECTIVE

    def get_camera(self):
        return self.camera

    def move(self, delta_x, delta_z):
        self.camera.position.x += delta_x
        self.camera.target.x += delta_x
        self.camera.position.z += delta_z
        self.camera.target.z += delta_z
