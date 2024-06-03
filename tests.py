1. def jojo(a,b,c):
    print([a,b,c])

jojo('hi','world','hello')

2. class Cls1(list):
    def __sub__(self, other):
        for i in other:
            if i in self:
                self.remove(i)
        return self
list1 = Cls1(['a','v','c'])
list2 = Cls1(['v'])
list3 = list1 - list2
print(list3)
3. import asyncio
import os

file = open('txt','w')
file.write('hi')
file.close()
a = input('Введите название папки: ')
os.mkdir(a)
os.rename('txt', f'{a}/xtx')

async def sleep():
  await asyncio.sleep(10)
  os.remove(f'{a}/xtx')
  os.rmdir(f'{a}')

asyncio.run(sleep())

