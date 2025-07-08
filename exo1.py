import main

def higher_value(num1, num2):
   higher = max(num1, num2)
   print(f"La valeur la plus haute est {higher}")
   return higher

def compare(num1, num2):
    if((num1 > num2)):
        print(1)
        return 1
    elif((num1 < num2)):
        print(-1)
        return -1
    else:
        print(0)
        return 0


def user_play(user_input1, user_input2):
    higher_value(user_input1, user_input2)
    compare(user_input1, user_input2)

user_input1 = int(input("Entre une premier nombre: "))
user_input2 = int(input("Entre un second nombre: "))
user_play(user_input1, user_input2)