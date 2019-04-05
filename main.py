from myboxclass import MyBox
b = MyBox()
b.add(2)
b.add('second')
b.add(5.7)
b.add('Student')
b.add(8)
b.add('Teacher')
b.remove('second')
if ('first' in b) and (len(b) > 0):
    b.remove('first')
for i in b:
    print(i)
