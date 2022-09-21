import cv2
import numpy as np

resim=cv2.imread("sukuna.png")

kesit=resim[200:500,600:1000] #sırasıyla y ve x koordinatı
cv2.imshow("Kesit Alani",kesit)


resim[0:300,0:400]=kesit      #alınan kesitiresme yapıştırma
resim[500:600,150:200]=(0,150,255) #belli bir alana efekt uygulama (0,150,255) değerleri sırasıyla blue green red değerleridir.
cv2.imshow("Sukuna",resim)


#resim[100,150] demek resimde 100 piksel aşağı, 150 piksel sağa git ve bulduğun pikseli (nokta) işaretle demektir.

#Resimde belli bir bölgeyi dikdörtgen içine almak için önce sol alt kçşenin x,y koordinatlarını 
#sonra da sağ üst köşenin x,y koordinatlarını yazarız ardından bgr değerini belirtiriz ve en sonda thickness yani çerçevenin kalınlığı.
cv2.rectangle(resim, (100,150), (200,300),[0,0,255],3)
cv2.imshow("Sukuna", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()