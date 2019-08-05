import random

from vec3 import Vec3, unit_vector
from ray import Ray
from camera import Camera
from lambertian import Lambertian
from metal import Metal
from object3d import Object3DList
from hit_record import HitRecord
from sphere import Sphere


def color(ray: Ray, world: Object3DList, depth: int):
    h_rec = HitRecord()

    if world.hit(ray, 0.001, float("inf"), h_rec):
        retval, s_ray, attenuation = h_rec.material.scatter(ray, h_rec)
        if depth < 50 and retval:
            return attenuation * color(s_ray, world, depth + 1)
        else:
            return Vec3(0.0, 0.0, 0.0)
    else:

        unit_direction = unit_vector(ray.direction)
        t = 0.5 * (unit_direction.y + 1.0)
        return (1 - t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0)


def main():
    # nx = 1000
    # ny = 500
    # ns = 30
    nx = 200
    ny = 100
    ns = 10

    f = open("generated_images/balls_world_fuzz.ppm", "w")
    f.write("P3\n%d %d\n255\n" % (nx, ny))

    cam = Camera(upper_left_corner=Vec3(-2.0,1.5,-1.0),
                 horizontal=Vec3(4.0,0.0,0.0),
                 vertical=Vec3(0.0,-2.0,0.0),
                 origin=Vec3(0.0,0.5,0.0))

    world = Object3DList(
        [Sphere(Vec3(0.0, -1000.0, -1.0),
                1000.0,
                Lambertian(albedo=Vec3(0.8, 0.8, 0.8))),
         Sphere(Vec3(0.0, 0.5, -1.0),
                0.5,
                Lambertian(albedo=Vec3(0.8, 0.3, 0.3))),
         Sphere(Vec3(0.0, 0.1, -0.5),
                0.1,
                Lambertian(albedo=Vec3(0.5, 0.2, 0.5))),
         Sphere(Vec3(0.75, 0.25, -0.5),
                0.25,
                Metal(albedo=Vec3(0.6, 0.8, 0.8), fuzz=0.5)),
         Sphere(Vec3(-0.75, 0.25, -0.75),
                0.25,
                Metal(albedo=Vec3(0.8, 0.6, 0.2), fuzz=0.0))
         ])

    # Note break with guide convention, vertical pixels start with index 0 at top
    for y in range(0, ny):
        for x in range(0, nx):
            col = Vec3(0.0, 0.0, 0.0)
            for _ in range(0, ns):
                u = (float(x) + random.random()) / float(nx)
                v = (float(y) + random.random()) / float(ny)
                r = cam.get_ray(u, v)
                col += color(r, world, 0)

            col /= ns

            col = col ** 0.5

            f.write(col.color_string(scale=255.99))

    f.close()


if __name__ == '__main__':
    main()
