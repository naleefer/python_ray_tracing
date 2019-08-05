import random

from vec3 import Vec3, unit_vector
from ray import Ray
from camera import Camera
from object3d import Object3DList, HitRecord
from sphere import Sphere


def color(ray: Ray, world: Object3DList):

    h_rec = HitRecord()

    if world.hit(ray, 0.0, float("inf"), h_rec):
        return Vec3(h_rec.normal.x+1.0,
                    h_rec.normal.y+1.0,
                    h_rec.normal.z+1.0)*0.5

    unit_direction = unit_vector(ray.direction)
    t = 0.5*(unit_direction.y+1.0)

    return (1-t)*Vec3(1.0,1.0,1.0) + t*Vec3(0.5,0.7,1.0)


def main():

    nx = 200
    ny = 100
    ns = 30

    f = open("generated_images/first_world.ppm","w")
    f.write("P3\n%d %d\n255\n"%(nx,ny))

    cam = Camera()

    world = Object3DList(
            [Sphere(Vec3(0.0,0.0,-1.0), 0.5),
             Sphere(Vec3(0.0,-100.5,-1.0),100)])

    # Note break with guide convention, vertical pixels start with index 0 at top
    for y in range(0,ny):
        for x in range(0,nx):
            col = Vec3(0.0,0.0,0.0)
            for _ in range(0, ns):
                u = (float(x)+random.random())/float(nx)
                v = (float(y)+random.random())/float(ny)
                r = cam.get_ray(u, v)
                col += color(r, world)

            col /= ns

            f.write(col.color_string(scale=255.99))

    f.close()


if __name__ == '__main__':
    main()
