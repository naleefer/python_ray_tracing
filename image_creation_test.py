def main():
    nx = 200
    ny = 100

    f = open("test_image.ppm","w")
    f.write("P3\n%d %d\n255\n"%(nx,ny))
    for y in reversed(range(0,ny)):
        for x in range(0,nx):
            r = float(x)/float(nx)
            g = float(y)/float(ny)
            b = 0.2
            ir = int(255.99*r)
            ig = int(255.99*g)
            ib = int(255.99*b)
            f.write("%d %d %d\n"%(ir, ig, ib))

    f.close()


if __name__ == '__main__':
    main()
