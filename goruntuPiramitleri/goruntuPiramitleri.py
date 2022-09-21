import cv2
import numpy as np
'''resim=cv2.imread("radyo_aktif_madde.jpg")

cv2.imshow("Radyoaktif Madde",resim)

ikiKatBuyuk=cv2.pyrUp(resim)
cv2.imshow("Radyoaktif Madde - İki Kati Buyuk ",ikiKatBuyuk)

ikiKatKucuk=cv2.pyrDown(resim)
cv2.imshow("Radyoaktif Madde - İki Kati Kucuk ",ikiKatKucuk)

print("Orijinal : ",resim.shape)
print("Büyültülmüş : ",ikiKatBuyuk.shape)
print("Büyültülmüş : ",ikiKatKucuk.shape)'''

resim=np.zeros((300,300,3),dtype="uint8") #zeros fonksiyonu tüm elemanları 0 olan bir matris dizisi oluşturur.
print(resim)

cv2.waitKey(0)
cv2.destroyAllWindows()