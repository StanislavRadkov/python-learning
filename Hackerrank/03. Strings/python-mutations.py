if __name__ == '__main__':
    def mutate_string(string, position, character):
        return string[:position] + character + string[position + 1:]

    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)