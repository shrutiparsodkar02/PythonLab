def count(s1, sub, flag):
    length = len(s1)
    if sub in s1:
        if s1 == "" and sub == "":
            return 1
        elif sub == "":
            return length + 1
        elif flag == False:  # Non-overlapping
            count = 0
            start = 0
            while True:
                start = s1.find(sub, start)
                if start == -1:
                    break
                count += 1
                start += len(sub) #here we will move after substring is found ones
            return count
        elif flag == True:  # Overlapping
            count = 0
            start = 0
            while True:
                start = s1.find(sub, start)
                if start == -1:
                    break
                count += 1
                start += 1  # Move one character ahead to check for overlapping
            return count
    else:
        return 0


res1 = count("sgggs", "",False)
print("nonoverlaping--->",res1) 
res2=count("","",True)
print("overlaping--->",res2) 
