from PIL import Image,ImageFont,ImageDraw
import os

def watermark ():
    # pictures = [
    #     # Image.open("orig.webp"),
    #     # Image.open("qwer.png"),
    #     # Image.open("flow.png")
    # ]
    pictures = os.listdir("images")
    pictures = [Image.open(f"images/{name}") for name in pictures]
    for index,picture in enumerate(pictures):
        izobr = picture.resize(size = (400,300))
        draw = ImageDraw.Draw(izobr)
        font = ImageFont.truetype("arial.ttf",size = 20)
        draw.text((100,150),text = "expensive",fill = "grey",font = font)
        izobr.save(f"{index}.png")
watermark()