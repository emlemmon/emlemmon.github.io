file_name = input("Enter file: ")
a_file = open(file_name, "r")

def checkBalance(file):
    opening = ["[", "{", "("]
    closing = ["]", "}", ")"]
    newStack = []

    for line in file:
        for x in line:
            if x in opening:
                newStack.append(x)
            elif x in closing:
                if len(newStack) == 0:
                    return "unbalanced"
                else:
                    start = newStack.pop()
                    if start == "[" and x != "]":
                        return "unbalanced"
                    elif start == "{" and x != "}":
                        return "unbalanced"
                    elif start == "(" and x != ")":
                        return "unbalanced"
    if len(newStack) == 0:
        return "balanced"
    else:
        return "unbalanced"

print(checkBalance(a_file))