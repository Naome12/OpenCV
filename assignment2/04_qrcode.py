import cv2
from pyzbar.pyzbar import decode

# Load the QR code image
image_path = "qrcode.png"
image = cv2.imread(image_path)

# Decode the QR code
qr_codes = decode(image)

# Extract and print QR code data
for qr in qr_codes:
    qr_data = qr.data.decode("utf-8")
    qr_type = qr.type
    print(f"Decoded QR Code: {qr_data}, Type: {qr_type}")
