# Create an empty list with the name 'a', print the value of a and type(a).
# a=["Rishi", "Rahul", "Priya"]
# print(a)
# print(type(a))

# Create a list , languages = ['R','Python', 'SAS', 'Scala', 42],
languages = ['R','Python', 'SAS', 'Scala', 42]
print(len(languages))

for x in languages: #Using for loop iterate and print all the elements in the list
    print(x)

for x in languages: #Select the second item, 'Python' and store it in a new variable named 'temp'
    if x == "Python":
        temp = x
        print(temp) #Print the value of temp and type(temp)
        print(type(temp)) 
        break

#Append the element 'Java' in the list
languages.append("Java")