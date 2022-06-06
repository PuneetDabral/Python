# # for n in range(5):
# # for n in range(3,5):
# for n in range(2,10,4):
#     # do somthing
#     print(n)


array = ['a','b','c','d']

# for n in range(len(array)):
#     print(n,array[n])
# first to len ,kha tk chala ne h ,or kha sai shuru krni h 
for n in range(len(array)-1,-1,-1):
    print(n,array[n])