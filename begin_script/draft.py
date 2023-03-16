import os

# os.system('systeminfo')

# print(os.popen('systeminfo').read())

for i, line in enumerate(os.popen('systeminfo')):
    # if i == 4: break
    print('%05d) %s' % (i, line.strip().encode('utf-8')))
