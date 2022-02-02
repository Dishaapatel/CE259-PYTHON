#Import collection.
import collections;

#Insert number of inputs.
N = int(input())
dic = collections.OrderedDict()

for i in range(N):
    word = input()
    if word in dic:
        dic[word] +=1
    else:
        dic[word] = 1

print(len(dic));

for k,v in dic.items():
    print(v,end = " ");
