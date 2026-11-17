from PIL import Image,ImageDraw,ImageFont

collage = Image.new("RGB",(800,600),"Green")
picture = Image.open("flow.png").resize((400,300))
collage.paste(picture,(0,0))
picturetw = Image.open("izobr.png").resize((400,300))
collage.paste(picturetw,(400,0))

prin = ImageDraw.Draw(collage)
font = ImageFont.load_default()
#font = ImageFont.truetype("consolas.ttf",size = 20)
prin.text((400,300),text = "Print",fill = "Yellow",font = font)

background = Image.new("RGB", (800,600), "LightBlue")
draw = ImageDraw.Draw(background)
try: 
   
     title_font = ImageFont.truetype("arial.ttf", size=60)
     text_font = ImageFont.truetype("arial.ttf", size=30)
except IOError:
    title_font = ImageFont.load_default()
    text_font = ImageFont.load_default()


title = "Good Luck!"
 
draw.text((300,200), title, font=title_font, fill="white")


motiv_text = "Let's GO"
  
draw.text((400,500), motiv_text, font=text_font, fill="yellow")


background.save("motivational_poster.png")  


























collage.show()