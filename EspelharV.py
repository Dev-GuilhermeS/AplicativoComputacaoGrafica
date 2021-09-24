from PIL import Image
import sys

if __name__ == "__main__":
  print(f'Argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    print(f"argumentos:{i}: {arg}")

img= Image.open(sys.argv[1])

espelhadaV = img.transpose(Image.FLIP_TOP_BOTTOM)


espelhadaV.save(sys.argv[2])