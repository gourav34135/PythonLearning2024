# python function program to get the square of all the elements of a dictionary

def square(dic):
    fall={}
    for key,value in dic.items():
        fall[key]=value**2
    return fall

sample_dict={"gourav":45,"samay":12,"siddhartha":10,"pablo_escobar":55}

print(square(sample_dict))
