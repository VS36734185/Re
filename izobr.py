from PIL import Image,ImageFilter,ImageEnhance
picture = Image.open("orig.webp")
#picture.show()
print("size",picture.size)
print("format",picture.format)
print("colourmode",picture.mode)

width,height = picture.size
picsmall = picture.resize((width//2,height//2))
#picsmall.show()

obrez = picture.crop(box = (100,100,width-100,height-100))
#obrez.show()

blure = picture.filter(ImageFilter.BLUR)
#blure.show()
gaus = picture.filter(ImageFilter.GaussianBlur(radius=50))
#gaus.show()

enh = ImageEnhance.Brightness(picture)
yar = enh.enhance(2.5)
black = enh.enhance(0.5)
#yar.show()
#black.show()


enh = ImageEnhance.Contrast(picture)
yar = enh.enhance(2.5)
black = enh.enhance(-1)
#yar.show()
#black.show()

black.save("izobr.png")

pc = Image.open("flow.png")
wdth, hght = pc.size
new_width = 500
scale = new_width / wdth
new_height = int(hght * scale)

pc_resized = pc.resize((new_width, new_height))

enh = ImageEnhance.Contrast(pc_resized)
pc_enhanced = enh.enhance(2.5)
pc_enhanced.show()
pc_enhanced.save("flow.png")

