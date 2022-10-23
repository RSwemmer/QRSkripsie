import qrcode
img = qrcode.make('www.escapefromtarkov.com')
type(img)  # qrcode.image.pil.PilImage
img.save("QRcodes/test.png")