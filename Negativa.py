from PIL import Image
import sys

if __name__ == "__main__":
  print(f'Argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    print(f"argumentos:{i}: {arg}")

img = Image.open(sys.argv[1])
print(img.size)

matriz = img.load()

for y in range (img.size[0]):
    for x in range (img.size[1]):

        r = 255 - matriz[y, x][0]
        g = 255 - matriz[y, x][1]
        b = 255 - matriz[y, x][2]
        matriz[y, x] = (r, g, b)

img.save(sys.argv[2])