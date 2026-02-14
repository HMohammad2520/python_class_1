import classes

import classes.java_learning
import classes.python_learning

from classes.java_learning import students as java_students
from classes.python_learning import students as python_student


from datetime import datetime


temp = open('last_run.txt', 'a').close()
file = open('last_run.txt', 'r+')
now = datetime.now()

data = file.read()

if data == '':
    print('Writing to file')
    file.write(str(datetime.now().strftime('%d/%m/%Y, %H:%M:%S')))
    file.close()

elif datetime.strptime(data, '%d/%m/%Y, %H:%M:%S') < now:
        import sys
        print('Exiting Program')
        sys.exit(0)


print('This is first time app is running')
