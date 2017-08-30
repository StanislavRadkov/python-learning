n = int(input())
l = input().split(' ')

if(all(int(i) > 0 for i in l) and any(i == i[::-1] for i in l)):
    print('True')
else:
    print('False')
