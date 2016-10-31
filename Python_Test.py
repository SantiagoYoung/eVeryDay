

def tester(start, label):
    def nested():
        print label, start
    return nested











if __name__ == '__main__':
    print tester(100, 99)()
    print tester