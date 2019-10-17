def merge_the_tools(string, k):
    substrings = (string[i:i + k] for i in range(0, len(string), k))
    for i in substrings:
        new_string = ''
        for f in i:
            if f not in new_string:
                new_string = ''.join([new_string, f])

        print(new_string)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
