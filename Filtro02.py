from PIL import Image, ImageFilter
import sys

if __name__ == "__main__":
  print(f'Argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    print(f"argumentos:{i}: {arg}")

img = Image.open(sys.argv[1])

kernel = ImageFilter.Kernel((3,3), (0,1,0,1,-4,1,0,1,0), 1, 0)

img1 = img.filter(kernel)

img1.save(sys.argv[2])