print('GO')

def testArguments(*args):
    print(args)

def testArgumentsAsDict(**kwargs):
    print(kwargs)

testArguments(1, 3, 3)
testArgumentsAsDict(name='test', value='test')
