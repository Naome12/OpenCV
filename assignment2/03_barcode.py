import cv2
from pyzbar.pyzbar import decode

# Load the image
image_path = "barcode.png"
image = cv2.imread(image_path)

# Decode the barcode
barcodes = decode(image)

# Extract and print the barcode data
for barcode in barcodes:
    barcode_data = barcode.data.decode("utf-8")
    barcode_type = barcode.type
    print(f"Decoded Barcode: {barcode_data}, Type: {barcode_type}")
