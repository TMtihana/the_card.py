print("Hello, let's create a birthday card")
name = str(input("Please enter your friend's name "))
birth_year = int(input("Please enter your friends year of birth "))
age1 = str(int(2023) - birth_year)
print("Now you can enter your personal message for your friend ")
personalized_message = str(input("Please enter your personalized message "))
signature = str(input("Please now enter your own name to sign your card! "))
print(name + ", let's celebrate your " + age1 +" years of awesomeness! Wishing you a day filled with joy and laughter as you turn " + age1)
print(personalized_message)
print("With love and best wishes,")
print(signature)