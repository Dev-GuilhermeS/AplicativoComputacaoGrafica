from PIL import Image
import sys

if __name__ == "__main__":
  print(f'Argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    print(f"argumentos:{i}: {arg}")

img = Image.open(sys.argv[1])

matriz = img.load()

gamma = 0.3

for y in range (img.size[0]):
    for x in range (img.size[1]):

        r = int((matriz[y, x][0]/255) ** gamma * 255)
        g = int((matriz[y, x][1]/255) ** gamma * 255)
        b = int((matriz[y, x][2]/255) ** gamma * 255)
        matriz[y, x] = (r, g, b)

img.save(sys.argv[2])