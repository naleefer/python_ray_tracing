from vec3 import Vec3
from material import Material
from lambertian import Lambertian


class HitRecord(object):

    def __init__(self, t:float=0.0,
                 p:Vec3=Vec3(0.0,0.0,0.0),
                 normal:Vec3=Vec3(0.0,0.0,0.0),
                 material:Material=Lambertian()):

        self.t = t
        self.p= p
        self.normal=normal
        self.material=material

    def __str__(self):

        return "Hit at %f m at point %s with normal vector %s"%(self.t,
                                                                self.p,
                                                                self.normal)


def main():

    hr = HitRecord()

    print(hr)


if __name__ == '__main__':
    main()
