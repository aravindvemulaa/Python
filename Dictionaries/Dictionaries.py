#dictionaries

#dictionary is collection of  key:value pairs. 
#dictionary is orderd, mutable and have keys:value pairs
#keys are unique but values can be duplicate

thisdict ={
    "name":"John",
    "age ":30,
    "city":"Newyork"
}
print(type(thisdict))
print(thisdict)

thisdict['state']='Texas'
print(thisdict)

thisdict.update(city= 'Los Angeles')
print(thisdict)

#removing items from dictionary

students= {
    "name":"ravi",
    "class" :10,
    "rollno":25,
    "fname":"remo"
}

students.pop("name")      #it will remove the value of the key specified
print(students)
del students["fname"]      # using del keyword to remove item by its key name
print(students)         
students.popitem()         #it removes last item from the dictionary
print(students)
students.clear()
print(students)            #it will clear all the elements in the dictionary

# nested dictionary
Avengers={
    "team1":{
        "captain": "steve Rogers",
        "iron_man": "tony_stark"
    },
    "team2":{
        "black_widow": "Natasha Romanoff",
        "wanda": "Wanda Maximoff"
    }
}
print(Avengers)
print(Avengers["team1"])
print(Avengers["team2"])
print(Avengers['team1']['captain'])

for key in Avengers["team2"]:
    print(Avengers["team2"][key])

for x in Avengers:
    print(x)


for x in Avengers:
    print(Avengers[x])
    print(Avengers[x])


for x in Avengers:
    print(x,Avengers[x])    
