import random
L=[]
for i in range(random.randint(1,100)):
   temp=[]

   for j in range(random.randint(1,30)):
      temp.append('{:.3f}'.format(random.random()*1000))

   L.append(','.join(temp))


with open('input_data.csv', 'wb') as fout:
    fout.write('\n'.join(L))

