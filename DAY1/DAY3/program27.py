import sys
l = [10, 20, 30]
print("List:", l)
print("\nUsing _sizeof():", l.sizeof_())
print("Using sys.getsizeof():", sys.getsizeof(l))
print("\nMemory after adding elements:")
for i in range(2):
    l.append(i)
    print("List:", l)
    print("_sizeof:", l.sizeof_())
    print("getsizeof:", sys.getsizeof(l))