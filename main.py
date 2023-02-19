# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            # Process closing bracket
            if not opening_brackets_stack:
                # Case when a closing bracket has no matching opening bracket
                return i + 1
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                # Case when a closing bracket matches the wrong opening bracket
                return i + 1

    if opening_brackets_stack:
        # Case when there are unmatched opening brackets
        return opening_brackets_stack[0].position

    # Case when all brackets are matched
    return "Success"

def main():
        do=input("F or I")
        if "F" in do:
            name = input("Enter file name: ")
            with open(name, "r", encoding="latinl") as file:
                text=file.read()
            mismatch = find_mismatch(text)
            if mismatch == "Success":
                print("Success")
            else:
                print(mismatch)
        elif "I" in do:
            text = input()
            mismatch = find_mismatch(text)
            if mismatch == "Sucess":
                print("Success")
            else:
                print(mismatch)

if __name__ == "__main__":
    main()
