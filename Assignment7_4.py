total_number = []
sum = 0
count = 0
print("Enter 'done' to end the process or enter integer.")
while True:
    num = input("Please enter an interger: ")
    if num.lower() == "done":
        print("Bye!!!")
        break

    try:
        number = int(num)
        total_number.append(number)
        sum = sum + number
        count += 1
        avg = sum / count
        print(f"{total_number}, Average = {avg:.2f}")
        
    except:
        print("Enter 'done' to end the process or enter integer.")