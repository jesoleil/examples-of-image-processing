import cv2
import numpy as np
resim=cv2.imread("gojo.png")
#resim=cv2.imread("gojo.png",0) resmi siyah beyaza çevirir
cv2.imshow("Gojo",resim)
#print(resim) matris renk değerleri
#print(resim.size) resmin boyutu (genişlik*yükseklik*kanal sayısı)(shape fonksiyonundan gelen değerlerin çarpımı ile bulunur)
#Eğer resim siyah beyaz olsaydı kanal sayısı 1 olurdu ve shape fonksiyonunda yazmazdı
#print(resim.dtype)resmin tipi --- her bir piksel 8 bit
#print(resim.shape) resmin 3 kanalı var çünkü renkli(rgb)
#cv2.imwrite("Gojo_SB.png",resim) siyah beyaz resmi kaydetme işlemi
cv2.waitKey(0)
cv2.destroyAllWindows()