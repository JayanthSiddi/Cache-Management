#Cache Management First in First Out (FIFO), Least Frequently Used (LFU)

cache=[]
request=[]
def myfunc():
    while True:
     x = int(input("Enter a number "))
     request.append(x)
     if x == 0:
        break
    del request[-1]
    print("Type 1 for first in first out (fifo)")
    print("Type 2 for least frequently used (lfu)")
    print("Type Q to terminate the program")
    proginput = input()
    if proginput == '1':
        fifo(request)
    elif proginput == '2':
        lfu(request)
    else:
        print("Your program is terminated")
def fifo(request):
   for i in request:
    if i in cache:
        print("Hit")
    else:
        print("Miss")
        cache.append(i)
        if len(cache) > 8:
           del cache[0] 
   print(cache,'cache')
   cache.clear()
   request.clear()
   myfunc()
def lfu(request):
   lst=[]
   dic={}
   lst1=[]
   dic1={}
   for i in request:
     lst1.append(i)

     if i in list(dic.keys()):
       print('Hit')
     else:
       print('Miss')

     dic[i]=lst1.count(i)
     if len(dic.keys())>8:
       dic1=dic.copy()
       dic1.popitem()

       for (i,j) in dic1.items():

        if j==min(dic1.values()):
          lst.append(i)
       dic.pop(min(lst))
       lst.clear()
   cache=list(dic.keys())
   print(cache)
   request.clear()
   cache.clear()
   myfunc()
myfunc()