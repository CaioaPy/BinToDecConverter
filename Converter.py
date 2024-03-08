num_dec = input("Insert the decimal number you wish to convert to binary: \n")

num_bin = []
num_dec = int(num_dec)

if num_dec >= 258 or num_dec == 258:
  num_dec = num_dec - 258
  print(str(num_dec) + "remains")
  num_bin.append("1")
elif num_dec <= 258:
  num_bin.append("0")
  print(str(num_dec) + "remains")
  if num_dec >= 128 or num_dec == 128:
    num_dec = num_dec - 128
    num_bin.append("1")
    print(str(num_dec) + "remains")
  elif num_dec <= 128:
    num_bin.append("0")
    print(str(num_dec) + "remains")
    if num_dec >= 64 or num_dec == 64:
      num_dec = num_dec - 64
      num_bin.append("1")
      print(str(num_dec) + "remains")
    elif num_dec <= 64:
      num_bin.append("0")
      print(str(num_dec) + "remains")
      if num_dec >= 32 or num_dec == 32:
        num_dec = num_dec - 32
        num_bin.append("1")
        print(str(num_dec) + "remains")
      elif num_dec <= 32:
        num_bin.append("0")
        print(str(num_dec) + "remains")
        if num_dec >= 16 or num_dec == 16:
          num_dec = num_dec - 16
          num_bin.append("1")
          print(str(num_dec) + "remains")
        elif num_dec <= 16:
          num_bin.append("0")
          print(str(num_dec) + "remains")
          if num_dec >= 8 or num_dec == 8:
            num_dec = num_dec - 8
            num_bin.append("1")
            print(str(num_dec) + "remains")
          elif num_dec <= 8:
            num_bin.append("0")
            print(str(num_dec) + "remains")
            if num_dec >= 4 or num_dec == 4:
              num_dec = num_dec - 4
              num_bin.append("1")
              print(str(num_dec) + "remains")
            elif num_dec <= 4:
              num_bin.append("0")
              print(str(num_dec) + "remains")
              if num_dec >= 2 or num_dec == 2:
                num_dec = num_dec - 2
                num_bin.append("1")
                print(str(num_dec) + "remains")
              elif num_dec <= 2:
                num_bin.append("0")
                print(str(num_dec) + "remains")
                if num_dec >= 1 or num_dec == 1:
                  num_dec = num_dec - 1
                  num_bin.append("1")
                  print(str(num_dec) + "remains")
                elif num_dec <= 1:
                  num_bin.append("0")
                  print(str(num_dec) + "remains")
print(num_bin)