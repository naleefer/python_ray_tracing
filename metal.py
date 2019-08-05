from vec3 import Vec3, unit_vector
from ray import Ray
from material import Material
from lambertian import random_in_unit_sphere


def reflect(v_in: Vec3, normal: Vec3):

    return v_in - 2*v_in.dot(normal)*normal


class Metal(Material):

    def __init__(self, albedo: Vec3, fuzz: float=0.0):

        self.albedo = albedo
        if fuzz > 1.0:
            self.fuzz = 1.0
        elif fuzz < 0.0:
            self.fuzz = 0.0
        else:
            self.fuzz = fuzz

    def scatter(self, r_in: Ray,
                hit_rec):

        reflected = reflect( unit_vector(r_in.direction), hit_rec.normal)
        scattered_ray = Ray(hit_rec.p, reflected + self.fuzz*random_in_unit_sphere())
        attenuation = self.albedo
        return (scattered_ray.direction.dot(hit_rec.normal) > 0), \
                scattered_ray, \
                attenuation
