from ezgraphics import GraphicsImage


def BlackAndWhite(file):
    origin = GraphicsImage(file)
    width = origin.width
    height = origin.height
    print(height, width)

    image_bw = GraphicsImage(width, height)
    for row in range(height):
        for col in range(width):
            pixel = origin.getPixel(row, col)
            media = (pixel[0] + pixel[1] + pixel[2]) // 3
            pixel_bw = (media, media, media)
            image_bw.setPixel(row, col, pixel_bw)
    image_bw.save("risultato.gif")

def Blur(file, k = 5):
    origin = GraphicsImage(file)
    width = origin.width
    height = origin.height
    print(height, width)
    image_blur = GraphicsImage(width, height)
    for row_base in range(height // k):
        for col_base in range(width// k):
            red, green, blue = 0, 0, 0
            for r in range(k):
                for c in range (k):
                    red += origin.getRed(k*row_base+r, k*col_base+c)
                    green += origin.getGreen(k*row_base+r, k*col_base+c)
                    blue += origin.getBlue(k*row_base+r, k*col_base+c)
            red //= k*k, 
            green //= k*k
            blue //= k*k
            for r in range(k):
                for c in range (k):
                    image_blur.setPixel(row_base+r, col_base + c, (red,green,blue))
    image_blur.save("risultato.gif")


Blur("download.png")