import numpy as np


print("Hello, Please follow the instructions to calculate AHP for your criteria and alternatives :- \n")

####### CRITERIA INPUTS
number_of_criteria = int(input("Enter the number of criteria :- "))

criteria_names = []

for i in range(number_of_criteria):
    criteria_names.append(input(f"Enter your {i+1} criteria :- "))

print('\n')

#################################### CRITERIA CALCULATION #########################################################


criteria_inputs = int(number_of_criteria*(number_of_criteria-1)/2)


def calculate_criteria(preferences):
    list_sum=[]
    average_list=[]


    matrix = np.ones(number_of_criteria**2)
    k=0
    matrix.shape = (number_of_criteria,number_of_criteria)
    for i in range(number_of_criteria):
        for j in range(number_of_criteria):
            if(j>i):
                matrix[i][j]=preferences[k]
                k=k+1
            elif i>j:
                matrix[i][j]=1/matrix[j][i]
            else:
                pass
                
    for j in range(number_of_criteria):
        sum1=0
        for i in range(number_of_criteria):
            sum1=sum1+matrix[i][j]
        list_sum.append(sum1)

    weighted_matrix=np.zeros(shape=(number_of_criteria,number_of_criteria))
    for j in range(number_of_criteria):
        for i in range(number_of_criteria):
            weighted_matrix[i][j]=float(matrix[i][j]/list_sum[j])
    average_list.append(np.mean(weighted_matrix,axis=1))
    average_list = np.array(average_list)
    average_list.shape = (number_of_criteria,)
    #print("average list -->     ",average_list)
    return average_list 

criteria_preferences = []


t=0
z=1
for i in range(criteria_inputs):
    if(z==number_of_criteria):
        t=t+1
        z=t+1
    criteria_preferences.append(int(input(f'Enter your preference for {criteria_names[t]} over {criteria_names[z]} :- ')))
    z=z+1    
weights = calculate_criteria(criteria_preferences).reshape(number_of_criteria,1)

###############################################################################################################


###### ALTERNATIVES INPUT
print('\n')
number_of_alternatives = int(input("Enter the number of alternatives :- "))

alternatives_names = []

for i in range(number_of_alternatives):
    alternatives_names.append(input(f"Enter your {i+1} alternatives :- "))



#################################ALTERNATIVES CALCULATION######################################################





''' alternatives_inputs = int(number_of_alternatives*(number_of_alternatives-1)/2)


def calculate_alternatives(preferences):
    list_sum=[]
    average_list=[]


    matrix = np.ones(number_of_alternatives**2)
    k=0
    matrix.shape = (number_of_alternatives,number_of_alternatives)
    for i in range(number_of_alternatives):
        for j in range(number_of_alternatives):
            if(j>i):
                matrix[i][j]=preferences[k]
                k=k+1
            elif i>j:
                matrix[i][j]=1/matrix[j][i]
            else:
                pass
                
    for j in range(number_of_alternatives):
        sum1=0
        for i in range(number_of_alternatives):
            sum1=sum1+matrix[i][j]
        list_sum.append(sum1)

    weighted_matrix=np.zeros(shape=(number_of_alternatives,number_of_alternatives))
    for j in range(number_of_alternatives):
        for i in range(number_of_alternatives):
            weighted_matrix[i][j]=float(matrix[i][j]/list_sum[j])
    average_list.append(np.mean(weighted_matrix,axis=1))
    average_list = np.array(average_list)
    average_list.shape = (number_of_alternatives,)
    #print("average list -->     ",average_list)
    return average_list 




for j in range(number_of_criteria):
    t=0
    z=1
    alternatives_preferences = []
    for i in range(alternatives_inputs):
        if(z==number_of_alternatives):
            t=t+1
            z=t+1
        alternatives_preferences.append(int(input(f'Enter your preference for {alternatives_names[t]} over {alternatives_names[z]} :- ')))
        z=z+1 
 '''



alternatives_inputs = int(number_of_alternatives*(number_of_alternatives-1)/2)

def calculate_alternatives(preferences):
    list_sum=[]
    average_list=[]

    matrix = np.ones(number_of_alternatives**2)
    k=0
    matrix.shape = (number_of_alternatives,number_of_alternatives)
    for i in range(number_of_alternatives):
        for j in range(number_of_alternatives):
            if(j>i):
                matrix[i][j]=preferences[k]
                k=k+1
            elif i>j:
                matrix[i][j]=1/matrix[j][i]
            else:
                pass
                
    for j in range(number_of_alternatives):
        sum1=0
        for i in range(number_of_alternatives):
            sum1=sum1+matrix[i][j]
        list_sum.append(sum1)

    weighted_matrix=np.zeros(shape=(number_of_alternatives,number_of_alternatives))
    for j in range(number_of_alternatives):
        for i in range(number_of_alternatives):
            weighted_matrix[i][j]=float(matrix[i][j]/list_sum[j])
    average_list.append(np.mean(weighted_matrix,axis=1))
    average_list = np.array(average_list)
    average_list.shape = (number_of_alternatives,)
    #print("average list -->     ",average_list)
    return average_list 


final=[]
for j in range(number_of_criteria): 
    t=0
    z=1
    alternatives_preferences=[]
    print('\n')
    print(f"FOR CRITERIA {criteria_names[j]} \n")
    for i in range(alternatives_inputs):
        if(z==number_of_alternatives):
            t=t+1
            z=t+1
        alternatives_preferences.append(int(input(f'Enter your preference for {alternatives_names[t]} over {alternatives_names[z]} :- ')))
        z=z+1 
    
    final.append(calculate_alternatives(alternatives_preferences))

final=np.array(final)

results = np.sum(weights*final,axis=0)

print('\n')

for i in range(number_of_alternatives):
    print(f"You can choose {alternatives_names[i]} with a probability of {round(results[i]*100,3)} % \n")



