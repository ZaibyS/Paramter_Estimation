# Paramter_Estimation

The file Retention.csv contains retention data of a cohort of 1000 players. For all
players S1 to S1000, the retention data is given for the five days dol = 1, dol = 2, dol = 4,
dol = 8, and dol = 25. Each line begins with a player’s number and then contains the
player’s retention values separated by commas. 

1) First I calculated the average retention for each day(1,2,4,8,25).
2) Estimated the parameters based on a formula (a*np.power(DOL,b)).
3) Predicted the values of the future retention days from (1,2....,30). The output is stored in a CSV file.
4) PLotted the graph of above mention points.
