import random

from vec3 import Vec3, unit_vector
from ray import Ray
from camera import Camera
from object3d import Object3DList
from hit_record import HitRecord
from sphere import Sphere

from lambertian import Lambertian
from metal import Metal
from dielectric import Dielectric


def populate_world() -> Object3DList:
    obj_list = [Sphere(Vec3(0.0, -1000.0, -0.0),
                       1000.0,
                       Lambertian(albedo=Vec3(0.8, 0.8, 0.8)))
                ]

    sphere_radius = 0.5

    for idx in range(0, 3):
        for idz in range(0, 3):
            for idy in range(0, 3):
                pos = Vec3(
                    (idx - 1) * 4 * sphere_radius,
                    (2 * idy + 1) * sphere_radius,
                    (idz - 1) * 4 * sphere_radius)
                n = random.random()
                if n < 0.33:
                    alb = 0.8 * Vec3(random.random(),
                                     random.random(),
                                     random.random())
                    obj_list.append(
                        Sphere(pos, sphere_radius,
                               Lambertian(albedo=alb)))
                elif n >= 0.33 and n < 0.66:
                    alb = 0.8 * Vec3(random.random(),
                                     random.random(),
                                     random.random())
                    fuzz = 0.2 * random.random()
                    obj_list.append(
                        Sphere(pos, sphere_radius,
                               Metal(albedo=alb, fuzz=fuzz)))
                else:
                    ref_idx = random.random() * 0.5 + 1
                    obj_list.append(
                        Sphere(pos, sphere_radius,
                               Dielectric(ref_idx=ref_idx)))

    return Object3DList(obj_list)


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
    random.seed(65)

    nx = 1500
    ny = 1000
    ns = 50

    f = open("generated_images/balls_world_fuzz_glass_big.ppm", "w")
    f.write("P3\n%d %d\n255\n" % (nx, ny))

    look_f = Vec3(-3.0, 3.5, 5.0)
    look_a = Vec3(0.0, 0.5, 0.0)

    cam = Camera(look_from=look_f,
                 look_at=look_a,
                 vec_up=Vec3(0.0, 1.0, 0.0),
                 v_fov=60.0,
                 aspect=nx / ny,
                 aperture=0.02,
                 focus_dist=(look_f - look_a).norm())

    world = populate_world()

    # Note break with guide convention, vertical pixels start with index 0 at top
    stride = nx * ns
    for y in range(0, ny):
        print("Calculating row: %d/%d"%(y,ny))
        for x in range(0, nx):
            col = Vec3(0.0, 0.0, 0.0)
            for _ in range(0, ns):
                u = (float(x) + random.random()) / float(nx)
                v = (float(y) + random.random()) / float(ny)
                r = cam.get_ray(u, v)
                col += color(r, world, 0)

                # print(y * stride + x * ns + _)

            col /= ns

            col = col ** 0.5

            f.write(col.color_string(scale=255.99))



    f.close()


if __name__ == '__main__':
    main()
