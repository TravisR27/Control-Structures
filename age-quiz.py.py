# This task will explain how the use of how control structures work, i.e else,if and elif statements

# List of the different symbols you will use and meanings
# == This means Equal to
# >= This means Greater than/equal to >/>=
# <= This means Less than/equal to </<=
# != This means Not equal to

# Here asks user to enter Age
age = int(input("Please enter your Age: ")) 

# If age is 100 or over
if age >= 100:
    print("Sorry You're Dead.")

# Elif a person is 65 or older
elif age >= 65 and age <=99:
    print("Enjoy your retirement.")

# Elif person is 40 and older
elif age >= 40 and age < 65:
    print("You're over the hill.")

# Elif a person is any other ages within the ranges
elif age >= 22 and age <=39:
    print("Age is but a number.")

# Elif person is 21 exactly
elif age == 21:
    print("Congrats on your 21st.")
    
# If a person is 13 or younger
elif age < 13: 
    print("You qualify for the kiddie discount.")
# Else for any other Age Ranges
else:
    print("Age is but a Number.")
