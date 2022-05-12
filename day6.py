"""
numpy, matplotlib, pandas
heatmap(folium)
"""

"""
install numpy --> pip3 install numpy
"""

#import numpy as np

# a=np.array([1,2,3,4])

#print(a)  -->[1 2 3 4] rank 1 array

#print(type(a)) ---> <class 'numpy.ndarray'>

#print(a.shape) -->(4,)

#print(a[0],a[1],a[2]) --> 1 2 3

# b=np.array([[1,2,3],[4,5,6]])

# print(b)     [[1 2 3]
#            [4 5 6]]

# print(b.shape)  --> (2,3)

# print(b[0][1]) --->2
# print(b[0,1])  -->2

# a=np.zeros([4,4])

# print(a)  -->[[0. 0. 0. 0.]
#                [0. 0. 0. 0.]
#                [0. 0. 0. 0.]
#                [0. 0. 0. 0.]]

# a=np.ones([4,2])

# print(a)  -->[[1. 1.]
#               [1. 1.]
#               [1. 1.]
#               [1. 1.]]

# a=np.full([4,5],1999)

# print(a) -->[[1999 1999 1999 1999 1999]
#              [1999 1999 1999 1999 1999]
#              [1999 1999 1999 1999 1999]
#              [1999 1999 1999 1999 1999]]

# a=np.eye(3)

# print(a) -->[[1. 0. 0.]
#              [0. 1. 0.]
#              [0. 0. 1.]]

# a=np.random.randint(2,100,(2,2))

# print(a)  -->[[71 79]
#               [61 41]]   some 2x2 array with random integers ranging 2-100

# x=np.array([[1,2],[3,4]])
# y=np.array([[5,6],[7,8]])

# print(np.add(x,y))  -->[[ 6  8]
#                         [10 12]]

# print(np.subtract(x,y)) -->[[-4 -4]
#                             [-4 -4]]

# print(np.multiply(x,y))  --> [[ 5 12]
#                               [21 32]]

# print(np.divide(y,x)) -->[[5.         3.        ]
#                           [2.33333333 2.        ]]

# print(np.sqrt(x)) -->[[1.         1.41421356]
#                      [1.73205081 2.        ]]

# print(np.dot(x,y)) -->[[19 22]
#                        [43 50]]

"""
pip3 install matplotib

"""
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,3*np.pi,0.1)
# y=np.sin(x)
# plt.plot(x,y)
# plt.show()
""" ploting 2 lines in a single graph"""
# y_s=np.sin(x)
# y_c=np.cos(x)
# plt.plot(x,y_s)
# plt.plot(x,y_c)
# plt.show()

""" adding labels and title and legend"""
# y_s=np.sin(x)
# y_c=np.cos(x)
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.plot(x,y_s)
# plt.plot(x,y_c)
# plt.title("Sine & Cosine Graph")
# plt.legend(['Sin','Cos'])
# plt.show()

""" Pandas 
pip3 install pandas
# """
# import pandas as pd
# df=pd.read_csv('train.csv')
# print(df)
# print(df.head())

""" Folium """

# import folium
# import numpy as np
# import pandas as pd

# df=pd.read_csv('train.csv')
# from folium import plugins
# StationArr=df[['Y',"X"]].values
# m=folium.Map(location=[StationArr[0][0],StationArr[0][1]],zoom_start=15)
# m.add_child(plugins.HeatMap(StationArr[:50000],radius=15))
# m.save('abc.html')

