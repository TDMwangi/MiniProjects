from pyzbar.pyzbar import decode
from PIL import Image

print("Welcome to QR Code Reader")

img = Image.open("QRCODE.png")

d = decode(img)

print(d[0].data.decode())
