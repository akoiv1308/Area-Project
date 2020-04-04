#AREA OF A TRIANGLE#
'''
coordinate = []

y = 0
while y < 10:
    x = 0
    while x < 10:
        coordinate.append((x,y))
        x += 1
    coordinate.append((x,y))
    y += 1
print(coordinate)
'''
pip install matplotlib

# importing the required module 
import matplotlib.pyplot as plt 
  
# x axis values 
x = [1,2,3] 
# corresponding y axis values 
y = [2,4,1] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show() 