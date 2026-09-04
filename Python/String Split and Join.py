def split_and_join(line):
    # write your code here
    list1 = line.split(" ")
    line_join = "-".join(list1)
    return line_join

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
