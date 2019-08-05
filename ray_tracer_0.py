from vec3 import Vec3, unit_vector
from ray import Ray


def hit_sphere(center: Vec3, radius: float, ray: Ray):

    oc = ray.origin - center

    a = ray.direction.dot(ray.direction)
    b = 2.0*oc.dot(ray.direction)
    c = oc.dot(oc) - radius**2.0
    discriminant = b*b - 4*a*c

    if discriminant < 0:
        return -1.0
    else:
        return (-b - discriminant**0.5)/(2*a)


def color(ray):

    t = hit_sphere(Vec3(0.0,0.0,-1.0),0.5,ray)
    if t > 0:
        N = unit_vector(ray.point_at_parameter(t) - Vec3(0.0,0.0,-1.0))
        return Vec3(N.x+1.0,N.y+1.0,N.z+1.0)*0.5

    unit_direction = unit_vector(ray.direction)
    t = 0.5*(unit_direction.y+1.0)

    return (1-t)*Vec3(1.0,1.0,1.0) + t*Vec3(0.5,0.7,1.0)


def main():

    nx = 200
    ny = 100

    f = open("generated_images/first_sphere.ppm","w")
    f.write("P3\n%d %d\n255\n"%(nx,ny))

    lower_left_corner = Vec3(-2.0,-1.0,-1.0)
    horizontal = Vec3(4.0,0.0,0.0)
    vertical = Vec3(0.0,2.0,0.0)
    origin = Vec3(0.0,0.0,0.0)

    for y in reversed(range(0,ny)):
        for x in range(0,nx):
            u = float(x)/float(nx)
            v = float(y)/float(ny)
            r = Ray(origin, lower_left_corner + horizontal*u + vertical*v)
            col = color(r)

            f.write(col.color_string(scale=255.99))

    f.close()


if __name__ == '__main__':
    main()
