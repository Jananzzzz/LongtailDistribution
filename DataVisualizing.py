import csv

import matplotlib.pyplot as plt

x0 = 0
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
with open("C:/Users/16591/Desktop/MachineLearningLab/Challenge2_LongtailedDistributionEmotionRecognition/code/dataset/fer2013B.csv", 'r') as f:
    reader = csv.reader(f)
    list_csv = list(reader)
    for line in list_csv:
     if line[-1] == 'Training':
          if line[0] == 'emotion':
               {}
          elif line[0] == '0':
               x0 = x0 + 1
          elif line[0] == '1':
               x1 = x1 + 1
          elif line[0] == '2':
               x2 = x2 + 1
          elif line[0] == '3':
               x3 = x3 + 1
          elif line[0] == '4':
               x4 = x4 + 1
          elif line[0] == '5':
               x5 = x5 + 1
          elif line[0] == '6':
               x6 = x6 + 1

y = [x0, x1, x2, x3, x4, x5, x6]
Y = sorted(y)
#print(y)
#print(Y)
X = [0, 1, 2, 3, 4, 5, 6]

for i in range(7):
     for j in range(7):
          if Y[i] == y[j]:
               X[i] = j



plt.rcParams["figure.figsize"] = [15.00, 5.00]

default_x_ticks = range(len(X))
plt.xticks(default_x_ticks, X)
plt.plot(default_x_ticks, Y)
#plt.show()


#plt.hist(Y)
plt.savefig("B_training.png")
