biography = {
 "name": "Lars",
 "hometown": "Dubai" , 
 "age": "18",
}
#Declare variables inside a dictionary 

print(*biography.values(), sep='\n')
#print dictionary variables in separate lines 

print('\n')

print(biography["name"]+"\n")
print(biography["hometown"]+"\n")
print(biography["age"]+"\n")
#print variables in a dictionary using specific values 

print('\n' + "Additional Exercise")

name1 = input('Enter name: ')
hometown1 = input('Enter hometown: ')
age1 = input('Enter age: ')
#declare variables using user input

biography2 = {
 "name": name1,
 "hometown": hometown1 , 
 "age": age1,
}
#declare values in variable inside a dictionary using user input

print (biography2)

