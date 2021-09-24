from PIL import Image, ImageFilter
import sys

if __name__ == "__main__":
  print(f'Argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    print(f"argumentos:{i}: {arg}")

img = Image.open(sys.argv[1])

matriz = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = matriz[i,j][0]
        pixel = int((r )/3)
        matriz[i,j] = (pixel)

img.save(sys.argv[2])