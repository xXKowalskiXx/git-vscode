# Jonathan Juarez
# CIS 3330
# CODE 1 - Weather Assistant
# Conversion formula: (Temperature in °F - 32) * .5556
# Note that the message to user should be the following
# "What is the temperature outside: "
# ---------------------------------------------------------------
def main():

     user_temp = input("What is the temperature outside: ")
     temp = float(user_temp)
     celsius = (temp - 32) * .5556

<<<<<<< HEAD
     if celsius > 20:
          print("\nWear a hat")
     elif 10 <= celsius <= 20:
          print("\nWear a light jacket")
     else:
          print("\nWear a heavy jacket")
if __name__ == "__main__":
    main()
=======
    if answer.lower() == "quit":
         break
    
    unit =(input("Is that in F or C? "))
    temp = int(answer)

    if unit.upper() == "F":
         celsius = (temp- 32) * .5556
    else: 
        celsius = temp
    if celsius > 20:
         print( "\nWear a hat")
    elif 10 <= celsius <= 20:
         print("\nWear a light jacket")
    elif celsius < 10:
         print("\nWear a heavy jacket")
    else:
         print("Not a Valid Answer, Please try again. ")


    # if 90 <= temp <= 100:
    #     print("wear a hat")
    # elif 75 <= temp <=89:
    #     print("wear a light shirt")
    # elif 65 <= temp <= 74:
    #     print("wear a coat")
    # elif temp < 64:
    #     print("cover up well")
    # else:
    #     print("Not a valid answer, Please try again")



# def main():
#     pass  # replace this line with your code


# if __name__ == "__main__":
#     main()


# Conversion formula: (Temperature in °F - 32) * .5556
>>>>>>> f25c77807a79bfaea5f23ab958f49b393d2e043b
