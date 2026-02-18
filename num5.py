def favourite_fruit(fruits, user_choice):
    if user_choice in fruits:
        return fruits.index(user_choice)
    else:
        return "სიაში არ არის"


fruit_list = ['apple', 'banana', 'orange', 'grapes']
user_input = input("რომელია თქვენი საყვარელი ხილი? ")

print(favourite_fruit(fruit_list, user_input))

