import os
def get_CWD():
    cd=os.getcwd()
    return cd
if __name__=='__main__':
    cd=get_CWD()
    print("Current Working Directory is :",cd)
