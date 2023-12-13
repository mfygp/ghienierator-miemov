from PIL import Image, ImageDraw, ImageFont

print("генератор мемов запущен")
type=input("введите 1 если нужен только нижний текст и 2 если нижний и верхний")
top_text=""
bottom_text=""
if type=="1":
  bottom_text=input("Введите нижний текст:")
elif type=="2": 
  top_text=input("Введите верхний текст: ")
  bottom_text=input("Введите нижний текст:")
else:
  print("Ошибка, я не смог вас понять.")
  quit()
print(top_text, bottom_text)
memes=["banda.jpg","egoist.jpg","cat.png"]
print("выбери картинку мема")
for i in range(len(memes)):
  print(i,memes[i])
a=int(input("введите номер картинки"))

image=Image.open(memes[a])
w,h=image.size
print(w,h)
draw=ImageDraw.Draw(image)
font=ImageFont.truetype("Arial.ttf",size=70)
text=draw.textbbox((0,0),top_text,font)
print(text)
draw.text(((w-text[2])/2,10),top_text,font=font,fill='black')

text=draw.textbbox((0,0),bottom_text,font)
draw.text(((w-text[2])/2,h-100),bottom_text,font=font,fill='purple')

image.save("newpicture.png")