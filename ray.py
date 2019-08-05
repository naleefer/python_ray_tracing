from vec3 import Vec3, unit_vector


class Ray(object):

    def __init__(self, origin: Vec3, direction: Vec3):

        self.__origin = origin
        self.__direction = direction

    @property
    def origin(self):
        return self.__origin

    @property
    def direction(self):
        return self.__direction

    def point_at_parameter(self, distance):

        return self.__origin + self.__direction*distance


def test_ray():

    ray = Ray(Vec3(0.0,0.0,0.0), Vec3(1.0,1.0,1.0))

    print("Origin at %s"%ray.origin)
    print("Direction is %s"%ray.direction)
    print("Unit vector direciton is %s"%unit_vector(ray.direction))

    distance = -5.0
    print("%f meters gives point %s"%(distance,
                                      ray.point_at_parameter(distance)))


def main():
    test_ray()


if __name__ == '__main__':
    main()
