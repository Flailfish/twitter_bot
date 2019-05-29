from PIL import Image, ImageDraw, ImageFont
import random
import filehandling


def grab_word():
    word_list = filehandling.readFromFile("nounlist.txt")
    word = random.choice(word_list)
    print(word)
    return word

def create_image(fonts,location,text):
    im = Image.open("C:\\Users\\Derek\\Pictures\\bobbob.jpg")
    font = ImageFont.truetype("C:\\Windows\Fonts\\impact.ttf", 75)
    draw = ImageDraw.Draw(im)
    draw.text((60, 50), "Happy little " + grab_word(), font=font)
    draw = ImageDraw.Draw(im)
    
    im.save("bob.png")
