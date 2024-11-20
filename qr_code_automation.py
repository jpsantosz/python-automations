import qrcode as qr

qr_code = qr.QRCode(version=1,
                    error_correction=qr.constants.ERROR_CORRECT_L,
                    box_size=50,
                    border=1)

qr_code.add_data("https://pt.wikipedia.org/wiki/Club_de_Regatas_Vasco_da_Gama")
qr_code.make(fit=True)

img = qr_code.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")