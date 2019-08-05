from vec3 import Vec3
from ray import Ray
from object3d import Object3D
from hit_record import HitRecord
from material import Material


class Sphere(Object3D):

    def __init__(self, center: Vec3, radius: float, material: Material):

        self.cen = center
        self.r = radius
        self.rsquared = radius*radius
        self.material = material

    def hit(self, ray: Ray,
                  t_min: float,
                  t_max: float,
                  rec: HitRecord)->bool:

        oc = ray.origin - self.cen

        a = ray.direction.dot(ray.direction)
        b = oc.dot(ray.direction)
        c = oc.dot(oc) - self.rsquared
        discriminant = b * b - a * c

        if discriminant > 0:
            d_sqrt = discriminant**0.5
            temp = (-b - d_sqrt)/(a)
            if temp < t_max and temp > t_min:
                rec.t = temp
                rec.p = ray.point_at_parameter(temp)
                rec.normal = (rec.p - self.cen)/self.r
                rec.material = self.material
                return True

            temp = (-b + d_sqrt)/(a)
            if temp < t_max and temp > t_min:
                rec.t = temp
                rec.p = ray.point_at_parameter(temp)
                rec.normal = (rec.p - self.cen)/self.r
                rec.material = self.material
                return True

        return False


def main():

    from lambertian import Lambertian

    sphere = Sphere(Vec3(0.0,0.0,2.0), 0.5, Lambertian())

    r1 = Ray(Vec3(0.0,0.0,0.0), Vec3(0.0,0.0,1.0))
    r2 = Ray(Vec3(0.0,0.0,0.0), Vec3(0.1,0.0,1.0))

    t_min = 0.0
    t_max = 100.0

    hit_record = HitRecord()

    if sphere.hit(r1, t_min, t_max, hit_record):
        print(hit_record)

    if sphere.hit(r2, t_min, t_max, hit_record):
        print(hit_record)


if __name__ == '__main__':
    main()
