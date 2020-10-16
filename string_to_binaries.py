st = "This is a string"
# The bytearray() Function returns a bytearray object,
# which is a mutable sequence of integers in the range 0 <=x < 256.
# If you want immutable sequence of integers, use bytes() function.
arr = bytearray(st, "utf8")
print(list(arr))

# bin() function converts an integer number to a binary string prefixed with 0b.
print(f"Primer byte: {arr[0]}\nel equivalente en binario: {bin(arr[0])}\n")

# map() is a built-in function that allows you to process and transform all the items in an iterable
# without using an expglicit for loop,
binarios = map(bin, bytearray(st, "utf8"))
print("Conversión del bytearray a lista de binarios")
print(list(binarios))
