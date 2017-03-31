import glob
import sys, qrcode

arquivos = glob.glob('list/*.png')
dc = qrcode.Decoder()
txt = open("decode.txt", "a")
for arquivo in arquivos:
	dc.decode(arquivo)
	txt.write(dc.result() + "\n")

close(txt)
