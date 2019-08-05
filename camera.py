import math
import random

from vec3 import Vec3, unit_vector
from ray import Ray


def random_in_unit_disk():

    while True:

        p = 2.0*Vec3(random.random(), random.random(), 0.0) - Vec3(1.0,1.0,0.0)
        if p.squared_length() < 1.0:
            break

    return p


class Camera(object):

    def __init__(self,
                 look_from: Vec3=Vec3(3.0,3.0,2.0),
                 look_at: Vec3=Vec3(0.0,0.0,-1.0),
                 vec_up: Vec3=Vec3(0.0, 1.0, 0.0),
                 v_fov: float=90.0,
                 aspect: float=1.0,
                 aperture: float=0.0,
                 focus_dist: float=1.0):

        self.lens_radius = aperture/2.0

        theta = v_fov*3.14159/180.0
        half_height = math.tan(theta/2.0)
        half_width = aspect*half_height

        w = unit_vector(look_from-look_at)
        self.u = unit_vector(vec_up.cross(w))
        self.v = w.cross(self.u)

        self.origin = look_from
        self.upper_left_corner = look_from - \
                                 half_width*self.u*focus_dist + \
                                 half_height*self.v*focus_dist - w*focus_dist
        self.horizontal = 2*half_width*self.u*focus_dist
        self.vertical = -2*half_height*self.v*focus_dist

    def get_ray(self, s: float, t: float):

        rd = self.lens_radius*random_in_unit_disk()
        offset = self.u*rd.x + self.v*rd.y

        return Ray(self.origin+offset,
                   self.upper_left_corner +
                   s*self.horizontal +
                   t*self.vertical - self.origin - offset)
