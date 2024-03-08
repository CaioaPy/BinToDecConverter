num_dec = input("Insert the decimal number you wish to convert to binary: \n")

num_bin = []
num_dec = int(num_dec)

for n in reversed(range(0, 8)):
    n = 2**n
    if num_dec>=n:
        num_dec = num_dec - n
        num_bin.append("1")
    elif num_dec < n:
        num_bin.append("0")
print("Number in binary: ")
print("".join(num_bin))