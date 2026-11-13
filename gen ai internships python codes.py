for i in range(11):
    print("7 *", i, "=", 7*i)

i = 0

while(i != 11): # it has to end somewhere
  print(i)
  i = i+1
import array as arr
a = arr.array('i',[1,2,3,4])
for i in range(0,4):
  print(a[i], end="\t") 


#set
s = set()

s.add(1)
s.add(2)
print(s)


set1 = set([4, 5, (6, 7)])
set1.update([10, 11])
print(set1)

set1.update([1,2,3,1,2,3,4,5])

