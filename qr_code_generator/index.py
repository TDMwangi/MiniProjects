import pyqrcode

msg = input("Type your secret message: ")

code = pyqrcode.create(msg)

code.png("QRCODE.png", scale=5)

print("QR Code generated successfully!")
