#!/usr/bin/env python
# coding: utf-8

# In[48]:


# finding the sodium wave length
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


# In[49]:


measurements=[4.9924,4.9954,4.9983,5.0013,5.0048,5.0077,5.0108,5.0137,5.0166,5.0195,5.0226,5.0255,5.0284,5.0318]
measurements_array = np.array(measurements)
x=[0, 10, 20, 30, 41, 51, 61, 71, 81, 91, 101, 111, 121, 132]
x=np.array(x)
y_err = 0.5*10**-4


# In[12]:





# In[16]:


coefficients = np.polyfit(x,measurements_array , 1)
m, c = coefficients

line = np.poly1d(coefficients)
x_line = np.linspace(min(x), max(x), 14)
y_line = line(x_line)
sig_y=sum((measurements_array-y_line)**2)/12
delta=14*(sum(x**2))-(sum(x))**2
error=np.sqrt(((sig_y*14)/delta))
print(error)
r2 = r2_score(measurements_array, y_line)
print("R2 value: " ,r2)
#y_err=[15*10**-4,0.5*10**-4,0.5*10**-4,0.5*10**-4,0.5*10**-4,0.5*10**-4,0.5*10**-4,0.5*10**-4,0.5*10**-4,0.5*10**-4,0.5*10**-4,0.5*10**-4,0.5*10**-4,0.5*10**-4]


# In[5]:


plt.scatter(x,measurements,s=20,label='Data')
#plt.errorbar(x, y, yerr=y_err, fmt='o', capsize=5, label='Data')
plt.plot(x_line, y_line, color='red', label='Fitted line')
plt.title("Distance Moved By The Movable Mirror vs Number Of Fringes Passed The Reference Point")
plt.xlabel('Numbe Of Finges Passed Through The Referenece Point')
plt.ylabel('Distance Travell By Movable Mirror (mm)')
plt.legend()
plt.show()
plt.savefig("wavelength.png")


# In[18]:


wavelength=2*m*10**6
print(wavelength) 
print("calculated value of sodium wavelength: 596.2 +/- 2.5 nm")

print("orginal value is: 589.3 nm" )


# In[97]:


# finding the sodium doublet length


# In[47]:


measurements2=[5.1637,5.4257,5.7344,6.0324,6.3220,6.5951,6.9058,7.2160,7.4909,7.7890,8.0666,8.3892,8.6305]
measurements2_array=np.array(measurements2)
x1=[0,1,2,3,4,5,6,7,8,9,10,11,12]
x1=np.array(x1)
coefficients1 = np.polyfit(x1,measurements2_array , 1)
m1, c1 = coefficients1
print(m1)
line = np.poly1d(coefficients1)
x_line1 = np.linspace(min(x1), max(x1), 13)
y_line1 = line(x_line1)
sig_y1=sum((measurements2-y_line1)**2)/11
delta1=13*(sum(x1**2))-(sum(x1))**2
error1=np.sqrt(((sig_y1*13)/delta1))
print(error1)
plt.scatter(x1,measurements2_array,s=20,label="Data")
plt.plot(x_line1, y_line1, color='red', label='Fitted line')
plt.title("Distance Moved By The Movable Mirror vs Number Of Number Of Times Fringes Disappear")
plt.xlabel('Numbe Of Times Fringers Disappear')
plt.ylabel('Distance Travell By Movable Mirror (mm)')
plt.legend()
plt.show()
plt.savefig("sodium doublet")


# In[43]:


doublet_wavelength=589.592-588.995
#print(doublet_wavelength)
print("orginal value is:0.597 nm" )
doublet=(589.294**2)/(2*m1*10**6)
error5=(doublet/m1)*error1
print(error5)
#print(doublet)
print("calculated value of doublet: 0.594 +/- 0.003 nm")
r2_1 = r2_score(measurements2, y_line1)
print("R2 value: " ,r2_1)


# In[45]:


# laser wavelength
x2 = [0,10, 20, 30, 40, 50,60,70,80,90,100]
y = [7.6342, 7.6370, 7.6400, 7.6428, 7.6455, 7.6482, 7.6511,7.6539, 7.6567,7.6593,7.6620]
#y_err = [0.5, 0.2, 0.8, 0.3, 0.6]  # Error values for each data point

# Plotting with error bars
#plt.errorbar(x, y, yerr=y_err, fmt='o', capsize=5)


# Optional: Customize the plot
plt.scatter(x2,y,s=20,label="data")
coefficients2 = np.polyfit(x2,y , 1)
m2, c2 = coefficients2
print(m2)
line = np.poly1d(coefficients2)
x_line2 = np.linspace(min(x2), max(x2), 11)
y_line2 = line(x_line2)
plt.plot(x_line2, y_line2, color='red', label='Fitted line')
plt.title("Distance Moved By The Movable Mirror vs Number Of Fringes Passed The Reference Point")
plt.xlabel('Numbe Of Finges Passed Through The Referenece Point')
plt.ylabel('Distance Travell By Movable Mirror (mm)')
plt.legend()
# Display the plot
plt.show()
plt.savefig("laser light wavelength")


# In[46]:


x2=np.array(x2)
sig_y2=sum((y-y_line2)**2)/9
delta2=14*(sum(x2*x2))-(sum(x2))**2
error2=np.sqrt(((sig_y*11)/delta2))
print(error2)
print("calculated value of sodium wavelength: 556.2 +/- 2.7 nm")
print("green laser wavelength value is: 532 nm" )
r2_1 = r2_score(y, y_line2)
print("R2 value: " ,r2_1)      


# In[ ]:





# In[ ]:




