# Working through Ray Tracing in a Weekend

class Vec3(object):

    def __init__(self, e0: float, e1: float, e2: float):

        self.__e = [e0, e1, e2]

    @property
    def x(self):
        return self.__e[0]

    @property
    def y(self):
        return self.__e[1]

    @property
    def z(self):
        return self.__e[2]

    @property
    def r(self):
        return self.__e[0]

    @property
    def g(self):
        return self.__e[1]

    @property
    def b(self):
        return self.__e[2]

    def __pos__(self):
        return self

    def __neg__(self):
        return Vec3(-self.__e[0], -self.__e[1], -self.__e[2])

    def __getitem__(self, item: int):
        if item < 0 or item > 2:
            print("Vec3 index out of bounds: %d" % item)
            return self.__e[0]
        else:
            return self.__e[item]

    def __add__(self, other):

        return Vec3(self.__e[0] + other.__e[0],
                    self.__e[1] + other.__e[1],
                    self.__e[2] + other.__e[2])

    def __sub__(self, other):

        return Vec3(self.__e[0] - other.__e[0],
                    self.__e[1] - other.__e[1],
                    self.__e[2] - other.__e[2])

    def __mul__(self, other):
        if type(other)==Vec3:
            return Vec3(self.__e[0]*other.__e[0],
                        self.__e[1]*other.__e[1],
                        self.__e[2]*other.__e[2])
        else:
            return Vec3(self.__e[0]*other,
                        self.__e[1]*other,
                        self.__e[2]*other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other)==Vec3:
            return Vec3(self.__e[0]/other.__e[0],
                        self.__e[1]/other.__e[1],
                        self.__e[2]/other.__e[2])
        else:
            return Vec3(self.__e[0]/other,
                        self.__e[1]/other,
                        self.__e[2]/other)

    def __iadd__(self, other):
        self.__e[0] += other.__e[0]
        self.__e[1] += other.__e[1]
        self.__e[2] += other.__e[2]
        return self

    def __isub__(self, other):
        self.__e[0] -= other.__e[0]
        self.__e[1] -= other.__e[1]
        self.__e[2] -= other.__e[2]
        return self

    def __imul__(self, other):
        if type(other)==Vec3:
            self.__e[0] *= other.__e[0]
            self.__e[1] *= other.__e[1]
            self.__e[2] *= other.__e[2]
        else:
            self.__e[0] *= other
            self.__e[1] *= other
            self.__e[2] *= other
        return self

    def __itruediv__(self, other):
        if type(other)==Vec3:
            self.__e[0] /= other.__e[0]
            self.__e[1] /= other.__e[1]
            self.__e[2] /= other.__e[2]
        else:
            self.__e[0] /= other
            self.__e[1] /= other
            self.__e[2] /= other
        return self

    def __pow__(self, power):

        return Vec3(self.__e[0]**power,
                    self.__e[1]**power,
                    self.__e[2]**power)

    def dot(self, other):
        return self.__e[0]*other.__e[0] + \
               self.__e[1]*other.__e[1] + \
               self.__e[2]*other.__e[2]

    def cross(self, other):
        return Vec3(self.__e[1]*other.__e[2] - self.__e[2]*other.__e[1],
                    self.__e[2]*other.__e[0] - self.__e[0]*other.__e[2],
                    self.__e[0]*other.__e[1] - self.__e[1]*other.__e[0])

    def norm(self):

        return (self.dot(self))**0.5

    def squared_length(self):

        return self.dot(self)

    def __str__(self):

        return "%f %f %f"%(self.__e[0],self.__e[1],self.__e[2])

    def color_string(self, scale=255.99):

        return "%d %d %d\n"%(int(self.r*scale),
                             int(self.g*scale),
                             int(self.b*scale))


def unit_vector(vector: Vec3):

    return vector/vector.norm()


def test_vec3():

    v1 = Vec3(0.0,1.0,3.0)
    v2 = Vec3(2.0,5.0,4.0)

    print("v1 is %s"%v1)
    print("v2 is %s"%v2)
    print("v1+v2 is %s"%(v1+v2))
    print("v1*v2 is %s"%(v1*v2))
    print("v1/v2 is %s"%(v1/v2))
    print("v1dotv2 is %s"%(v1.dot(v2)))
    print("v2dotv1 is %s"%(v2.dot(v1)))
    print("v1xv2 is %s"%(v1.cross(v2)))
    print("v2xv1 is %s"%(v2.cross(v1)))
    print("|v1| is %s"%v1.norm())
    print("|v2| is %s"%v2.norm())


def generate_hello_world_image():

    nx = 200
    ny = 100

    f = open("test_image_vec3.ppm","w")
    f.write("P3\n%d %d\n255\n"%(nx,ny))
    for y in reversed(range(0,ny)):
        for x in range(0,nx):
            vec = Vec3(float(x)/float(nx), float(y)/float(ny), 0.2)

            vec*=255.99

            ir = int(vec.r)
            ig = int(vec.g)
            ib = int(vec.b)

            f.write("%d %d %d\n"%(ir, ig, ib))

    f.close()


def main():
    test_vec3()
    generate_hello_world_image()


if __name__ == '__main__':
    main()
