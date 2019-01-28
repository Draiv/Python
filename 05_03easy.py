# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
import sys

b = sys.argv[0]
copy = ('copy_' + str(b))
a = open(b, 'r', encoding = 'UTF-8')
c = open(copy, 'w', encoding = 'UTF-8')
c.write(a.read())
c.close()
print(' Копия готова под именем - ', copy)


# shutil.copy(b, copy) #Ну вы поняли) но это не по программе, пока мучался вспоминая, нашел