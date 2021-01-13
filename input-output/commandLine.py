from sys import argv

print('The number of cmd line args', len(argv))
print('The line of cmd line args', argv)
print('Print all them')
argv.remove(argv[0]) # it removes first index value

[print(i) for i in argv]

# program to print sum of given numbers provided as cmd line args
argv.remove(argv[0])
if argv == []:
    print('The sum is', 0)
else:
    print('The sum is', sum((int(i) for i in argv)))

# space is the separator between command line args. All args are str by default
# long space separator string should be enclosed by "" [python file.py "file x.txt"] otherwise it will consider each as different string
# if we put '', it will return only 'file [python file.py 'file x.txt']

