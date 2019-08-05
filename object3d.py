from ray import Ray
from hit_record import HitRecord


class Object3D(object):

    def hit(self, r: Ray,
                  t_min: float,
                  t_max: float,
                  rec: HitRecord)->bool:
        raise NotImplementedError


class Object3DList(Object3D):

    def __init__(self, object_list):
        self.object_list = object_list

    def hit(self, r: Ray,
                  t_min: float,
                  t_max: float,
                  rec: HitRecord)->bool:

        temp_rec = HitRecord()
        hit_anything = False
        closest_hit = t_max

        for object_3d in self.object_list:
            if object_3d.hit(r, t_min, closest_hit, temp_rec):
                hit_anything = True
                closest_hit = temp_rec.t
                rec.t = temp_rec.t
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal
                rec.material = temp_rec.material

        return hit_anything
