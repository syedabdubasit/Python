#append: List.append
list=[5,6,7,8]
list.append(5)
print("Append",list)

#Slicing
#var_name=[starting_index:Ending_index
num=[1,3,5,7,9]
number=num[2:4]
print("Slicing",number)


#sort=Ascending order/Descending order
list=[2,4,6,8,10]
list.sort()
print("Ascending order:",list)
list.sort(reverse=True)
print("Descending order:",list)


#sorting method on string
list2=['Apple','Banana','kivi','Mango','Blueberry']
list2.sort()
print("Fruits in Ascending order:",list2)
list2.sort(reverse=True)
print("Fruits in descending order:",list2)





#creating a list
list1=[]
print(len(list1))
list3=[3,4,7,8,6]
print("The length of a list:",len(list3))



#Reverse
list4=[2,6,4,8,7]
list4.reverse()
print("The Reverse of a list:",list4)




#Negative indexing
print("The last element is:",list4[-1])


#Insert: First we wiil add index number and the element which you want to add
list5=['Basit','Sayyam',34,8.9]
list5.insert(2,'Sara')
print("Insert",list5)

#Remove
list5=['Basit','Sayyam',34,8.9]
list5.remove('Sayyam')
print("Remove Method:",list5)



#Pop:
list5=['Basit','Sayyam',34,8.9]
list5.pop(2)
print("Pop Method:",list5)
