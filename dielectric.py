import random

from vec3 import Vec3, unit_vector
from ray import Ray
from material import Material
from metal import reflect


def refract(v_in: Vec3, normal: Vec3, n1_n2: float)->[bool, Vec3]:

    uv_in = unit_vector(v_in)
    dt = uv_in.dot(normal)
    discriminant = 1.0 - n1_n2*n1_n2*(1-dt*dt)

    if discriminant > 0:
        refracted = n1_n2*(uv_in - normal*dt)-normal*(discriminant**0.5)
        return True, refracted
    else:
        return False, None


def schlick(cosine: float, ref_idx: float):

    r0 = (1-ref_idx) / (1+ref_idx)
    r0 = r0*r0

    return r0 + (1-r0)*pow(1-cosine, 5)


class Dielectric(Material):

    def __init__(self, ref_idx: float):

        self.ref_idx = ref_idx
        self.inv_ref_idx = 1.0/ref_idx
        self.attenuation = Vec3(1.0,1.0,1.0)

    def scatter(self, r_in: Ray,
                hit_rec):

        if r_in.direction.dot(hit_rec.normal) > 0:
            outward_normal = -hit_rec.normal
            n1_n2 = self.ref_idx
            cosine = self.ref_idx * r_in.direction.dot(hit_rec.normal) / r_in.direction.norm()
        else:
            outward_normal = hit_rec.normal
            n1_n2 = self.inv_ref_idx
            cosine = -r_in.direction.dot(hit_rec.normal) / r_in.direction.norm()

        ret_val, refracted = refract(r_in.direction, outward_normal, n1_n2)
        if ret_val:
            reflect_prob = schlick(cosine, self.ref_idx)
        else:
            reflect_prob = 1.0

        if random.random() < reflect_prob:
            reflected = reflect(unit_vector(r_in.direction), hit_rec.normal)
            scattered_ray = Ray(hit_rec.p, reflected)
        else:
            scattered_ray = Ray(hit_rec.p, refracted)

        return True, scattered_ray, self.attenuation
