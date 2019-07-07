from PIL import Image, ImageDraw, ImageFont
import random
import filehandling


def grab_word():
    word_list = filehandling.readFromFile("nounlist.txt")
    word = random.choice(word_list)
    print(word)
    return word

def text_wrap(text, font, max_width):

    lines = []
   
    if font.getsize(text)[0] <= max_width:
        lines.append(text) 
    else:
        words = text.split(' ')  
        i = 0
        while i < len(words):
            line = ''         
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
 
            lines.append(line)    
    return lines


def create_image(fonts,location,text):
    im = Image.open("bobpaint.jpg")
    im_size = im.size
    font = ImageFont.truetype("C:\\Windows\Fonts\\impact.ttf", 50)
    lines = text_wrap("Happy little " + grab_word(), font, 365-90)
    line_height = font.getsize('hg')[1]
    draw = ImageDraw.Draw(im)
    x = 90
    y = 70
    for line in lines:
        draw.text((x,y), line, fill=(0,0,0,0),font = font)
        y = y + line_height
    im.save("bob_paint.jpg")
