num_dec = input("Insert the decimal number you wish to convert to binary: \n")

# list that gonna show the binary number at the end of the code
num_bin = []
# number reciver
num_dec = int(num_dec)

for n in reversed(range(0, 12)):
    n = 2**n
    if num_dec>=n:
        num_dec = num_dec - n
        num_bin.append("1")
    elif num_dec < n:
        num_bin.append("0")
print("Number in binary: ")
print("".join(num_bin))
