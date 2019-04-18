def find_longest(s):
    longest = 1  # 0 最短为1
    length = 1
    for i, char in enumerate(s):
        if i == 0:
            continue

        if s[i] == s[i - 1]:
            longest = length if length > longest else longest
            length = 1  # 0  出现变化重置为1
        else:
            length += 1

    return longest


if __name__ == '__main__':
    s = input()
    print(find_longest(s))
