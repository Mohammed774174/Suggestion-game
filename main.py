import random 
number=random.randint(1,10)
print("Enter a number between 1 and 10")

count_error = 3
success_count = 0

while count_error > 0:
    try:
        x = int(input())
        if 1 <= x <= 10:
            success_count += 1
            print("The number is between 1 and 10")
            if success_count == 3:
                print("Success! You entered a valid number three times.")
                break
        else:
            print("The number is not between 1 and 10")
            count_error -= 1
            if count_error > 0:
                print(f"Try again. You have {count_error} attempts left.")
            else:
                print("No attempts left.")
    except ValueError:
        count_error -= 1
        if count_error > 0:
            print(f"Invalid input. Please enter an integer. You have {count_error} attempts left.")
        else:
            print("Invalid input. No attempts left.")