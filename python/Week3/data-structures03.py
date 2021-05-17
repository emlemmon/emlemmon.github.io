oddNum = []
evenNum = []
prompt = int(input("Enter a number (0 to quit): "))
while prompt != 0:
    if(int(prompt) % 2 != 0):
        oddNum.append(prompt)
    else:
        evenNum.append(prompt)
    prompt = int(input("Enter a number (0 to quit): "))
print()
print("Even numbers: ")
for num in evenNum:
    print(num)

print()
print("Odd numbers: ")
for num in oddNum:
    print(num)
    