from vec3 import Vec3
from ray import Ray

class Material(object):

    def scatter(self, r_in: Ray,
                hit_rec)->[bool, Vec3, Vec3]:
        raise NotImplementedError
