from ezgraphics import GraphicsImage

origin = GraphicsImage("download.png")
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

