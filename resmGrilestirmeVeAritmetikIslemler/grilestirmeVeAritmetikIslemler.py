import cv2
import numpy as np

resim=cv2.imread("natsugray.png")
cv2.imshow("Natsu ve Gray",resim)


resimGri=cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grileşmiş Resim",resimGri)


yukseklik,genislik,kanalSayisi=resim.shape#bgr olarak 3 kanal var. [x y 3]
print("Orijinal boyutlar: ", yukseklik,genislik,kanalSayisi)

yukseklik2,genislik2=resimGri.shape         #resmi grileştirdikten sonra kanal sayısı 1  düşer ve yazılmaz.Bu nedenle sadece 2 değişken oluşturabiliriz. 
print("Oynanmış boyutlar: ", yukseklik2,genislik2)



cv2.waitKey(0)
cv2.destroyAllWindows()