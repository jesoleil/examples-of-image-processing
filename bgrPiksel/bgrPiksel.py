import cv2
import numpy as np

gojo=cv2.imread("gojo3.png")

#gojo[50,30]=[255,255,255] #50 piksel aşağı in 30 piksel sağa kay ve o pikselin rengini beyaz yap demektir.

'''for i in range(100):
    gojo[50,i]=[255,255,255]'''
    
#gojo[:,:,0]=255 #3. parametre olan bgr parametresindeki blue değerine ulaşıp değerini 255 yapıyoruz.
#Burada 3. parametre 0 olursa maviefekt, 1 olursa yeşil, 2 olursa ise kırmızı efekt vermiş oluruz.
#Özetle 0--> blue 1-->green 2-->red i temsil eder.

'''gojo[:,:,2]=255
gojo[:,:,1]=255 '''  # sarı efekt oluşturdu

#♦gojo[300:600,600:800,0]=255 #Belli bir alana efekt uygulama

'''gojo[100:250,400:550,1]=200
gojo[100:250,400:550,0]=100'''


cv2.imshow("Gojo Satoru",gojo)

#print(gojo[(230,80)])  #bgr değeri bulma --> 230 piksel aşağı in, 80 piksel sağa kay ve bulduğun pikselin renk değerlerini yaz.
#print("Resmin Boyutu  :" + str(gojo.size))
#print("Resmin Özellikleri :" + str(gojo.shape))
#print("Resmin Veri Tipi  :" + str(gojo.dtype))






cv2.waitKey(0)
cv2.destroyAllWindows()