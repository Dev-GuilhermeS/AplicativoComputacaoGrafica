from PIL import Image
import sys

if __name__ == "__main__":
  print(f'Argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    print(f"argumentos:{i}: {arg}")

img= Image.open(sys.argv[1])

rotaciona = img.transpose(Image.ROTATE_90)

rotaciona.save(sys.argv[2])