marks = {
       "Harry" : 100,
       "Sonu" : 50,
       "Ram" : 43
} 

#print(marks, type(marks))
#print(marks["Harry"]) #print error

#print(marks.items())
print(marks.keys())
#print(marks.values())
#marks.update({"Harry" : 98 ,"priya" : 58})
#print(marks)
#print(marks.get("Harry")) #print None
print(marks.pop("Harry","sham"))
