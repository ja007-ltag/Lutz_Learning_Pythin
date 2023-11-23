import mymod

if __name__ == '__main__':
    test_list = [
        "test2.txt",
        "test_file.txt",
        "scenario_0055_0001_0001_0001.log",
        "mymod.py",
    ]

    for name in test_list:
        mymod.test(name)
