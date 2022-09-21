import cv2
import numpy as np

resim=cv2.imread("mystogan.jpg")
cv2.imshow("Mystogan",resim)

aynalananResim=cv2.copyMakeBorder(resim, 400, 400, 250, 250, cv2.BORDER_REFLECT)
cv2.imshow("Aynalanan Mystogan",aynalananResim)

uzatılanResim=cv2.copyMakeBorder(resim, 400, 400, 250, 250, cv2.BORDER_REPLICATE)
cv2.imshow("Uzatılan Mystogan",uzatılanResim)

tekrarlananResim=cv2.copyMakeBorder(resim, 400, 400, 250, 250, cv2.BORDER_WRAP)
cv2.imshow("Tekrarlanan Mystogan",tekrarlananResim)

cerceveliResim=cv2.copyMakeBorder(resim, 400, 400, 400, 400, cv2.BORDER_CONSTANT,value=(75,150,255)) #constatnt default değeri siyah renktir
cv2.imshow("Çerçceveli Mystogan",cerceveliResim)


cv2.waitKey(0)
cv2.destroyAllWindows()