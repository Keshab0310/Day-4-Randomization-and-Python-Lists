fruits = ["apple", "banana"  , "cherry"] #This is the list of different fruits.
states_of_canada =  ["Alberta","British Columbia","New Brunswick","Newfoundland and Labrador","Nova Scotia",
"Northwest Territories","Nunavut","Ontario","Prince Edward Island","Qubec","Saskatchewan","Yukon"] #These are all the states of canada
print(states_of_canada[1])# This will print British Columbia, which is in the second position of the list of state of canada.
#To get the item of  a specific index, you can use square brackets []. As above example.
#we can get the items from last  to first by using negative sign (-) in front, Below is the example
print(fruits[-1])   # This will print 'cherry' as it is the last item in the list.
fruits.append("grape")    #Adding an item at the end of the list.
fruits.extend(["kiwi","orange"])     # Adding multiple items at once.
fruits.remove( "banana" )      # Removing an item based on its value.
#These are the basic  operations for adding/removing items from lists.

