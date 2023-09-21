import modul_1 
print(modul_1.max1(5,9))

import modul_1 as m1  #dlya sokrasheniya

print(m1.max1(5,9))
#vtoroy sposob

from modul_1 import max1

print(max1(5,9))

from modul_1 import *  # import vseh functiy