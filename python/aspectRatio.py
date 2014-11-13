def ratio(a,b):
    #generate a wide aspect ratio
    if a < b:
        c = b
        b = a
        a = c
    # not always a float value, cast before division
    return float(a)/float(b)



if __name__ == '__main__':
    x = ratio( 640, 1136)
    y = ratio( 1920, 1080)
    z = ratio( 1334, 750)
    print x,y,z
