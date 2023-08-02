from PIL import Image, ImageFilter

im = Image.open('saritocat.PNG')
w,h = im.size
print('Original image size: %sx%s' % (w,h))

im.thumbnail((w//2, h//2))
print("Resize image to %sx%s" % (w//2,h//2))
im.save('thumbnail.PNG','PNG')

im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.png','png')