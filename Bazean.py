

def main():

	#open the file for reading
	myfile =open('Charles_Wang_EagleFord_Well_meta.txt','r') 
	next(myfile)

	#initialize my variables
	Operator_List = [] #full list of operators
	master_operator_dict = {} # dictionary for unique operators
	Total_Oil = 0 
	Prev_Oil_Prod = 0
	Prev_Prod_Month = 0
	Best_Operator = ['temp',0,13,0,0]
	Best_Productivity = 0
	#Iterate through the file
	for i in myfile:

		flag = True #Flag to account for null data
		new_well = [] #initialize each well
		x = i.split('\t') #split it by tabs

		Oil_Prod = x[17] 
		Operator_Name = x[53]
		Prod_Month = x[60]
		Well_Name = x[70]

		#if data is null or identical to the previous line, don't append into dictionary or list
		if Oil_Prod == 0 or Operator_Name == '' or Prod_Month==0:
			flag = False
		if Prev_Oil_Prod == Oil_Prod and Prev_Prod_Month == Prod_Month:
			flag = False

		Prev_Prod_Month = Prod_Month
		Prev_Oil_Prod = Oil_Prod



		#append all the data into a list
		while flag == True: 
			flag = False
			new_well.append(Operator_Name)
			new_well.append(Well_Name)
			new_well.append(Oil_Prod)
			new_well.append(Prod_Month)
			#each unique list of each well should look like [Operator,Well,Oil Production, Production months]
			#master_operator_dict has all the data in a 2D list with the keys being the operator and a 2 D list of [Operator name, Well name, Oil Production, Production Months] being the value
 
			if Operator_Name not in master_operator_dict:
					master_operator_dict[Operator_Name] = [new_well]

			else:
				master_operator_dict[Operator_Name].append(new_well)



#Get the values from the dictionary to look at each operator
	for keys in master_operator_dict:
		Total_Oil =0 
		Total_Prod_Months = 0
		Well_Counter = 0
		Temp_List = []
		Productivity = 0	

		for values in master_operator_dict.get(keys):
			#Look at each well list [Operator, Well, Oil Production, Production months]


			Total_Prod_Months = Total_Prod_Months + int(values[3])
			Total_Oil = Total_Oil + int(values[2])
			Well_Counter = Well_Counter + 1 
		
		Average_Oil = Total_Oil/Well_Counter
		Total_Prod_Months = Total_Prod_Months//Well_Counter #approximate the months by dividing by # of wells. 




		#add it into a temporary list
		Temp_List.append(keys)
		Temp_List.append(Total_Oil)
		Temp_List.append(Total_Prod_Months)
		Temp_List.append(Well_Counter)
		Temp_List.append(Average_Oil)

		#Keep track of best performing operator
		#greater than 12 to so that wells have been producing for atleast two years and have more than 3 wells as an operator
		if int(Best_Operator[2]) > 12 and Total_Prod_Months/Well_Counter>24 and Well_Counter>3: 
			Productivity= Average_Oil/Total_Prod_Months
			Best_Productivity = Best_Operator[4]/Best_Operator[2]
			if Productivity>Best_Productivity:
				Best_Operator=Temp_List


		#add the list [Operator,Total Oil, Total Months, # of Wells, Average Oil per well]
		Operator_List.append(Temp_List)



	#iterate thru the list of unique operators
	for i in Operator_List:
		print("Company:",i[0])
		print('Produced:',i[1],'barrels of oil.')
		print("Number of Months:",i[2],'months.')
		if i[3]==1:
			print ('Number of Wells:',i[3],'well.')
		else:	
			print ('Number of Wells:',i[3],'wells.')
		print('Average Oil Production Per Well:',i[4],'barrels of oil per well.')
		print('')

	print('')	
	print ("The best operator going forward is",Best_Operator[0])
	print('Produced:',Best_Operator[1],'barrels of oil.')
	print("Number of Months:",Best_Operator[2],'months.')
	print ('Number of Wells:',Best_Operator[3],'wells.')
	print('Average Oil Production Per Well:',Best_Operator[4],'barrels of oil per well.')
	print('')
		










main()