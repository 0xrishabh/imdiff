import cv2
import numpy as np

class imdiff():
	def __init__(self,image1,image2, dvalue=70):
		self.image1 = cv2.imread(image1)
		self.image2 = cv2.imread(image2)
		self.dvalue = dvalue
		self.row = self.image1.shape[0]
		self.col = self.image1.shape[1]		

	def diff(self,image1,image2):
		total = 0
		for i in range(len(image1)):
			total += abs(int(image1[i])-int(image2[i]))

		if total>self.dvalue:
			return True
		return False

	def run(self):
		for x in range(self.row):
			for y in range(self.col):
				if self.diff(list(self.image1[x,y]),list(self.image2[x,y])):
					self.image2[x,y] = [0,0,0]
		return np.array(self.image2)





## Uncomment to see results

'''
diff = imdiff("test/image1.jpg","test/image2.jpg",70).run()
print(diff)
cv2.imshow("Diff Image", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''