dog={"name":"sheru","color":"white","breed":"kutta","legs":"4","age":"3"}
student={"first_name":"Prashanth","last_name":"A","gender":"Male","age":"22","marital_status":"NA","skills":["PYTHON","c++","AI engineer","Databases"],"country":"India","city":"Bengaluru","address":"Doddabettahlli"}

print(len(student))
print(student["skills"],student["country"],student["city"],student["address"])

print(type(student))

print(type(student["skills"]))

student["skills"].append("Machine_learning")
print(student["skills"])


tuple(student.items())

print(type(student))

del dog

