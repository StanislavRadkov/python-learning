if __name__ == '__main__':
    def count_substring(string, sub_string):
        count = 0
        i = 0
        for i in range(len(string)):
            if string[i:i + len(sub_string)] == sub_string:
                count += 1

        return count

    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)