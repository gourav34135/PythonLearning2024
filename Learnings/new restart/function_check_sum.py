# program to check weather the combination of two numbers has a sum of 10 from given list

def check_sum(l,s):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==s:
                return True
    return False
print(check_sum([2,5,6,4,7,3,8,9,1],10))
    
