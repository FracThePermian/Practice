import numpy as np
import scipy
import matplotlib.pyplot as plt


living_area = np.array([2104, 1600, 2400, 1416, 3000]) #(sqrt ft)**2
bedrooms = np.array([3, 3, 3, 2, 4])
y = np.array([400, 330, 369, 232, 540]) #in $1000s of dollars
hold = np.array([1]*5)
alpha = 0.5 #learning rate
print(living_area, '\n', bedrooms, '\n', y, '\n', hold, type(hold))
x = np.concatenate((hold, living_area, bedrooms)).reshape(3, 5)
# training_set[[0,1]] = training_set[[1,0]]
# training_set = training_set.T
# training_set[0,2] = training_set[2,0]
x = x.T
print(x, '\n\n')
print(x[0][:])

weight = np.array([0]*3)

weight = weight + alpha * (y[0] - (weight @ x[0][:])) * x[0][:]
print(weight)

for j in range(len(y)):
    weight = weight + alpha * (y[j]) - (weight @ x[j][:]) * x[j][:]
    print(weight)



# weight = weight + alpha * 1
# weight[0] = weight[0] + alpha * (price[0] - (weight @ training_set[0][:]) * training_set[0][0])
# print(weight)




#
# weight = [0]*3
#
#
# weight[0] = weight[0] + alpha*(price[0]-(weight[0]+weight[1]*living_area[0]+weight[2]*bedrooms[0]))*1
# weight[1] = weight[1] + alpha*(price[0]-(weight[0]+weight[1]*living_area[0]+weight[2]*bedrooms[0]))*living_area[0]
# weight[2] = weight[2] + alpha*(price[0]-(weight[0]+weight[1]*living_area[0]+weight[2]*bedrooms[0]))*bedrooms[0]
#
# weight = 1
#
#
# print(weight)




# plt.scatter(living_area, bedrooms)
# plt.show()































