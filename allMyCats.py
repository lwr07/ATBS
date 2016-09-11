catNames = []
while True:
    print('Enter the name of cat {0} (or enter nothing to stop.):'.format(str(len(catNames) + 1)))
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)
    # This a github test comment
    # This is a second github test
