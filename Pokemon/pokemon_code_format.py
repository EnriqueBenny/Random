def main():
    otpt = read()
    print(otpt)
    #writer(otpt)

def read():
    otpt = ''
    lst = []
    with open('/Users/erikuben/Documents/Programming/GitHub/Random/Pokemon/cheat_code_input.txt', 'r') as reader:
        for line in reader:
            nl = line.split(' ')
            fi = nl[0]
            si = nl[1]
            lst.append(fi)
            lst.append('+')
            lst.append(si)
            lst.append('+')
            
    for item in lst:
        otpt += item
    return otpt

def writer(otpt):
    with open ('cheat_code_output.txt', 'a') as appender:
        appender.write(otpt)


if __name__ == '__main__':
    main()