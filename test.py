class Test:

    def __init__(self):
        pass


if __name__ == '__main__':
    s = ['1', '2', '3', '4']

    test = ''
    for i in s:
        test += '{} '.format(i)

    print(test)
