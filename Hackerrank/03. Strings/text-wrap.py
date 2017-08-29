if __name__ == '__main__':
    def wrap(string, max_width):
        return textwrap.fill(string, max_width)

    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)