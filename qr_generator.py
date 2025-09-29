import qrcode

url = "https://www.linkedin.com/in/pwtandev/"

img = qrcode.make(url)

img.save("qr_generator.png")

img.show()