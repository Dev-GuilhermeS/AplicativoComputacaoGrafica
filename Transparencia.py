from PIL import Image
import sys

if __name__ == "__main__":
  print(f'Argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    print(f"argumentos:{i}: {arg}")

img= Image.open(sys.argv[1])

imgpng = img.convert('RGBA')

print(img.getbands())
print(imgpng.getbands())

pixels = list(imgpng.getdata())

for i, p in enumerate(pixels) :
    pixels[i] = (p[0], p[1], p[2], 128)

outputImg = Image.new('RGBA', img.size)
outputImg.putdata(pixels)
outputImg.save(sys.argv[2])