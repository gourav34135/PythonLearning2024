def solve(s):
    #solve_name=s.title()
    word_list= s.split(" ")
    print(word_list)
    name_list = []
    solve_name =''
    for word in word_list:
        if word== '':
            solve_name = solve_name + " "
        elif len(word) == 1:
            solve_name=  solve_name + word.upper() + " "
        else:
            solve_name = solve_name + word[0].upper() + word[1:] + " "
    return solve_name.strip()
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
