
#immutable objects are fundamentally expensive to “change”, because doing so involves creating a copy. Changing mutable objects is cheap.

#Immutable are quicker to access than mutable objects.

#Mutable objects are great to use when you need to change the size of the object, example list, dict etc.. Immutables are used when you need to ensure that the object you made will always stay the same.



import datetime

import time



print(datetime.date.fromtimestamp(time.time()))




















