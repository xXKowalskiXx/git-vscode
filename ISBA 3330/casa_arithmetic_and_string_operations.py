
# -------------------------------------------------------
#                         6.1
# Chapter 6.1 "A string is a sequence" code
# -------------------------------------------------------

# Do not forget to change values for the variables fruit and s
# -----------------------------------------
name= 'Jonathan'
letter = name[1]
print(letter) 
# Prints: o

letter = name[0]
print(letter)
# Prints: J
# -----------------------------------------
# letter = name[1.5]

# TypeError: string indices must be integers

# -------------------------------------------------------
#                         6.2
# Chapter 6.2 "Getting the length of a string using len" code
# -------------------------------------------------------
# -----------------------------------------

name = 'Jonathan'
len(name)
print(len(name)) #returns 8


# length = len(name)
# last = name[length]
# IndexError: string index out of range

length = len(name)

last_letter = name[length-1]
print(last_letter)

last_letter= name[length-2]
print(last_letter)

# -----------------------------------------

# -------------------------------------------------------
#                         6.3
# Chapter 6.3 "Traverse through a string with a loop" code
# -------------------------------------------------------
name= 'Jonathan'

index = 0                 # the beginning of the index 
while index < len(name):  # 0 < 8:
    letter = name[index]  # pulling letter out of index
    print(letter)         # printing that letter
    index = index + 1     # pointing to the next index to the right


index = len(name) -1      # length of the string = 8 , -1 to get the Index position.
while index >= 0:         # while len(name)-1 = 7 >= 0:
    letter = name[index]  # pull letter out of index
    print(letter)         # print letter
    index = index - 1     # point to the next index to your left

for char in name:
    print(char)

for char in reversed(name): #reverse() works too
    print(char)


# -------------------------------------------------------
#                         6.4
# Chapter 6.4 "String Slices" code
# -------------------------------------------------------

name = 'Jonathan Juarez'

print(name[0:8])
# Prints: Jonathan
print(name[9:15])
# Prints: Juarez

name = 'Jonathan'
name[:3]
print(name[:3])
# Prints: Jon
print(name[3:])
# Prints: athan

print(name[:]) #[Start,Stop], Start at the beginnning and go all the way to the end
# Pirnts: Jonathan Juarez

# Do not forget to comment out the lines of code that will trigger Type and Index errors.




