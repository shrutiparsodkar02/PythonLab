def DFA_end_with_b(text):
    # Define final states and alphabet
    final_state = ["q1"]
    alpha = ["a", "b"]
    
    def q0(text):
        if text == "":
            return "q0"
        elif text[0] in alpha:
            if text[0] == "a":
                return q0(text[1:])
            else:  # text[0] == "b"
                return q1(text[1:])
        else:
            return "Rejected"
    
    def q1(text):
        if text == "":
            return "q1"
        elif text[0] in alpha:
            if text[0] == "b":
                return q1(text[1:])
            else:  # text[0] == "a"
                return q0(text[1:])
        else:
            return "Rejected"
    
    def DFA(text):
        last_state = q0(text)
        print(last_state)
        if last_state in final_state:
            return "Accepted"
        else:
            return "Rejected"
    
    return DFA(text)

# Test the function
res = DFA_end_with_b("abba")
print(res)

