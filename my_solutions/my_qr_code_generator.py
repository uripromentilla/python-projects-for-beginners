# Generate QR Code from URL

import qrcode

# Input text or URL
url = input("Enter the text or URL: ").strip()

# Input filename
filename = input("Enter the filename: ").strip()

# Generate QR Code as filename
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(url)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)

print(f"QR code saved as {filename}")
