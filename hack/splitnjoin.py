

def split_and_join(line):
    # write your code here
    no_of_Words=line.split()
    result="-".join(no_of_Words);
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)