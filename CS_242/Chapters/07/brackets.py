from linked_stack import LinkedStack


def bracketsBalance(exp):
    # create new stack
    stk = LinkedStack()
    # scan across the expression
    for ch in exp:
        if ch in ['[', '(']:
            # push opening bracket
            stk.push(ch)
        elif ch in [']', ')']:
            # process closing bracket
            # if stack is empty or, we are at the end of stack, that means this is a floating closing bracket
            if stk.isEmpty():
                return False
            # pop character from top of stack and inspect
            chFromStack = stk.pop()
            # brackets must be of same type and match up
            if ch == ']' and chFromStack != '[' or ch == ')' and chFromStack != '(':
                return False
    return stk.isEmpty()


def main():
    exp = input("Enter a bracketed expression: ")
    if bracketsBalance(exp):
        print("OK")
    else:
        print("NOT OK")


if __name__ == "__main__":
    main()
