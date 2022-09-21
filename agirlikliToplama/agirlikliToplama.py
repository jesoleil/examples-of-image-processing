import cv2
import numpy as np
resim1=cv2.imread("prometyum.jpg")
resim2=cv2.imread("rutenyum.jpg")


'''print(resim1[100,200])  #y,x koordinatındaki nokta(piksel)nın bgr değerini verir.
print(resim2[150,200])
print(resim1[100,200]+resim2[150,200]) #iki noktanın bgr değerleri toplamını verir.'''


cv2.imshow("Prometyum",resim1)
cv2.imshow("Rutenyum",resim2)


toplam=cv2.add(resim1,resim2)
cv2.imshow("Toplanmis Resim",toplam)

agirliktiToplam=cv2.addWeighted(resim1, 0.7, resim2, 0.3, 0)  #gama değeri her zaman 0 
cv2.imshow("Agirlikli Toplanmis Resim", agirliktiToplam)

cv2.waitKey(0)
cv2.destroyAllWindows()