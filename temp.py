girilen_saniye=int(input("Saniye Gir:"))

saniye= girilen_saniye % 60
dakika= (girilen_saniye//60)%60
saat= ((girilen_saniye//60)//60)//60
print(saat,dakika,saniye, sep=":")
print(str(saat)+":"+str(dakika)+":"+str(saniye))
" Saat dakika saniye programı"


