from PIL import Image, ImageDraw

new_image = Image.new("RGB", (400, 400), (0, 0, 0))

draw = ImageDraw.Draw(new_image)

draw.line((0, 0, 100, 200), fill=(255, 0, 0), width=1)
draw.ellipse((90, 190, 120, 220), 'yellow')
draw.line((120, 20, 120, 250), 'white', 1)
draw.rectangle((300, 300, 350, 350), 'blue', 'green', 1)
draw.arc((50, 90, 350, 390), 50, 360, 'red')
new_image.save('img.png', "PNG")
