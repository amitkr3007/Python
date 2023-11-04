states_of_India =["BIHAR","UP","Maharashtra","Gujarat"]

print(states_of_India[0])
print(states_of_India[-2])

states_of_India[1]="MP"
print(states_of_India[1])

states_of_India.extend(["Rajasthan","Punjab"])
print(states_of_India[-2])
states_of_India.insert(2,"AP")

print(states_of_India)


state_Capital =["Patna","Bhopal","Hyderabad","Mumbai","Gandhi Nagar","Jaipur","Chandigarh"]

state =[states_of_India,state_Capital]

print(state)