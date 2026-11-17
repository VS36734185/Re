from PIL import Image, ImageDraw, ImageFont

def create_invitations():
    friends = ['Слава']
    background_path = 'photo.png'
    font_path = 'arial.ttf'

    try:
        title_font = ImageFont.truetype(font_path, size=60)
        text_font = ImageFont.truetype(font_path, size=30)
    except IOError:
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()

    for friend in friends:
        img = Image.open(background_path).convert('RGBA')
        draw = ImageDraw.Draw(img)
        text = f"Дорогой {friend}, приглашаю тебя на праздник!"
        draw.text((300,200), "invite",font=title_font, fill="white")
        draw.text((50, 400), text, font=text_font, fill='white')

        img.save(f'invite_{friend}.png')

create_invitations()




    
