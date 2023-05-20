import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../data/processed/frame_380.jpg')
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.waitforbuttonpress()
plt.close('all')
