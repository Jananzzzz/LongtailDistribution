# this is a file for test some little code

'''
import csv
import numpy as np
'''
# import torch
# import torch.nn
# from inspect import getsource
# 
# input = torch.randn(3, 7, dtype = torch.float32)
# train = torch.randn(3)


# create an iterator, then use next() to iterate it:

list = [1,2,34,4,5,5]
print(max(list))

'''

list = [1, 2, 3, 4]
myIteratableList = iter(list)
for i in range(len(list)):
    x = next(myIteratableList)
    print(x)
'''
'''
with open("C:/Users/16591/Desktop/MachineLearningLab/Challenge2_LongtailedDistributionEmotionRecognition/code/dataset/fer2013A.csv", 'r') as csvin: 
            data = csv.reader(csvin)
            next(data)
            for row in data:
                face = [int(pixel) for pixel in row[1].split()]
                face = np.asarray(face).reshape(48, 48)
                face = face.astype('uint8')              # unsigned integer 0-255
                print(face)
'''

'''

'''