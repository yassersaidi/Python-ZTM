from PIL import Image,ImageFilter


img = Image.open(r"images\pikachu.jpg")

blur_filter = img.filter(ImageFilter.BoxBlur(5.0))
gray_filter = img.convert('L')#L --> Gray
rotate_image = img.rotate(180)
resize_image = img.resize((300,300))
crop_box = (100,100,400,400)
crop_image = img.crop(crop_box)


gray_filter.save("./export/grday.png","png")
blur_filter.save("./export/blur.png","png")
rotate_image.save("./export/45deg.png","png")
resize_image.save("./export/resized.png","png")
crop_image.save("./export/crop_image.png","png")
crop_image.show()

