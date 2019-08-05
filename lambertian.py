import random

from vec3 import Vec3
from ray import Ray
from material import Material


def random_in_unit_sphere():
    while True:
        p = 2.0 * Vec3(random.random(),
                       random.random(),
                       random.random()) - Vec3(1.0, 1.0, 1.0)

        if p.squared_length() < 1.0:
            break

    return p


class Lambertian(Material):

    def __init__(self, albedo: Vec3 = Vec3(0.5, 0.5, 0.5)):
        self.albedo = albedo

    def scatter(self, r_in: Ray,
                hit_rec):
        target = hit_rec.p + hit_rec.normal + random_in_unit_sphere()
        scattered_ray = Ray(hit_rec.p, target - hit_rec.p)
        attenuation = self.albedo

        return True, scattered_ray, attenuation
