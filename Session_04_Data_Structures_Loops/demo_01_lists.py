# declare a list


my_list = ['a','b','c','d','e']

# both lines belowe create empty list
your_list = list()
our_list = []

#print list

print(my_list)
print(your_list)
print(our_list)

# access list elements

print(my_list[0])
# print(my_list[5]) # error becasue larger than list
print(my_list[-2]) # goes backwards
print(my_list[-5])

# Changing list elements

my_list[3] = "banana"
print(my_list)

# my_list[5] = "apple" # index error for using index 5

# add elements to list (append())

your_list.append("Dune")
your_list.append("Mike")
your_list.append("Sally")

print(your_list)

# len()
print(len(your_list))
# print(your_list[len(your_list)]) # Error

# this gets the last element of the list
print(your_list[len(your_list)-1]) # Error



# list.count()



# removing from a list (del)

del(my_list[1])
print(my_list)

# list.remove()
my_list.remove("banana")
print(my_list)

# Deep vs shallow copies (with list.copy())

my_list_1 = my_list
# help(my_list.copy)
my_list_2 = my_list.copy


print(my_list)
print(my_list_1)
print(my_list_2)
my_list.append("Pride and Predjudice")

print(my_list)
print(my_list_1)
print(my_list_2)



# Iterating over a list

for string in my_list:
    print(string)

for banana in my_list:
    print(banana)

for my_var in my_list:
    print(my_var)



a = [1,2,3,4]

for letter in a:
    print(letter + 5)