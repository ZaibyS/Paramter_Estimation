import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from random import randint as rand


def Ret_Func(DOL,a,b):
	return a*np.power(DOL,b)  #Formula to calculate to the retention

	
Cohort1 = pd.read_csv("Retention_2.csv" , header = None)
Cohort1.set_index(0,inplace = True)
Ret_list_1 = []

#First part, calculating the retention of each DOL
for col in Cohort1.columns:
	Ret_list_1.append( ( sum(Cohort1[col])) / len(Cohort1) ) 
	
	
DOL_1 = [ 1 , 2 , 4 , 8 , 25 ]
plt.plot(DOL_1,Ret_list_1 , 'b-' , label = 'empirical retention')		#plotting the graph for retention of DOL
plt.xlabel('Day of life(DOL)')
plt.ylabel('Retention')
plt.title('Relationship between DOL and retention')		


#Second Part, estimating the parameters of the functions that are a and b
popt, pcov = curve_fit(Ret_Func, DOL_1, Ret_list_1)		
plt.plot(DOL_1, Ret_Func(DOL_1, *popt), 'r-' ,label='approximated retention')  #plotting the graph based on the estimated parameter


#Third part
#creating a list of DOL for future prediction
DOL_2= list(range(1,31))   
Ret_list_2 =  np.around(Ret_Func(DOL_2, *popt)*1000)  
plt.plot(DOL_2, Ret_list_2/1000, 'g-' ,label='simulated retention')	#plotting the graph of new cohort
plt.legend(loc='upper right')
player = list(range(1001,2001))		#creating a list of players


Cohort2 = pd.DataFrame()	#created an empty dataframe
Cohort2['Player number'] = player	
Cohort2.set_index('Player number' , inplace = True)		#resetting the dataframe index


#prediciting the value of each DOL based on estimated paramters.
for i in range(len(DOL_2)): 
	j = Ret_list_2[i]	
	dummylist = [0]*1000	
	while(j >= 1):	
		dummyval = rand(0 , 999)	
		if(dummylist[dummyval] == 0):	
			dummylist[dummyval] = 1
			j-=1
	Cohort2 [i] = dummylist		#creating a new column for each day with the values
	
	
Cohort2.to_csv("Retention.csv")	 #storing the dataframe is csv file
plt.show()	

