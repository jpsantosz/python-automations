# Importando a biblioteca qrcode para geração de QRcode (A biblioteca Pillow é necessária para que o módulo qrcode funcione corretamente ao gerar imagens.)
import qrcode as qr

# Definindo as especificações do QRcode a ser gerado
qr_code = qr.QRCode(version=1,
                    error_correction=qr.constants.ERROR_CORRECT_L,
                    box_size=50,
                    border=1)

# Incluindo o conteúdo do QRcode
qr_code.add_data("https://pt.wikipedia.org/wiki/Club_de_Regatas_Vasco_da_Gama")
qr_code.make(fit=True)

# Gerando e salvando a imagem do QRcode
img = qr_code.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")