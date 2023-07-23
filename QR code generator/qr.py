import qrcode
from PIL import Image

# Data to be encoded
data ="https://www.google.com/"

qr=qrcode.QRCode(version=1,box_size=10,border=3)
qr.add_data(data)
qr.make(fit=True)

# Encoding data using make() function
image=qr.make_image(fill="block",back_color="white")

# Saving as an image file
image.save("qr_code.png")
Image.open("qr_code.png")
