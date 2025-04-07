first, second, value = 0, 0, ""

for first in range(2, 10) :
    value = value + (" #%2d단 #" % (first))
print(value)

for first in range(1, 10):
    value = ""
    for second in range(2, 10):
        value = value + str("%2dX%2d=%2d" % (second, first, second*first))
    print(value) 
    