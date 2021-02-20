from PIL import ImageGrab

resx = 32
resy = 18

while True:
    samples = []
    px = ImageGrab.grab().resize((resx, resy)).load()

    for y in range(resy -1, 0, -1):
        samples.append(px[0,y])

    for x in range(0, resx):
        samples.append(px[x,0])

    for y in range(1, resy):
        samples.append(px[resx-1, y])

    print(samples)
