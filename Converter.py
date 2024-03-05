num_dec = input("Insert the decimal number you wish to convert to binary: \n")

num_dec = int(num_dec)

if num_dec >= 258 or num_dec == 258:
  num_dec = num_dec - 258
  print(str(num_dec) + "remains")
  print("1")
elif num_dec <= 258:
  print("0")
  print(str(num_dec) + "remains")
  if num_dec >= 128 or num_dec == 128:
    num_dec = num_dec - 128
    print("1")
    print(str(num_dec) + "remains")
  elif num_dec <= 128:
    print("0")
    print(str(num_dec) + "remains")
    if num_dec >= 64 or num_dec == 64:
      num_dec = num_dec - 64
      print("1")
      print(str(num_dec) + "remains")
    elif num_dec <= 64:
      print("0")
      print(str(num_dec) + "remains")
      if num_dec >= 32 or num_dec == 32:
        num_dec = num_dec - 32
        print("1")
        print(str(num_dec) + "remains")
      elif num_dec <= 32:
        print("0")
        print(str(num_dec) + "remains")
        if num_dec >= 16 or num_dec == 16:
          num_dec = num_dec - 16
          print("1")
          print(str(num_dec) + "remains")
        elif num_dec <= 16:
          print("0")
          print(str(num_dec) + "remains")
          if num_dec >= 8 or num_dec == 8:
            num_dec = num_dec - 8
            print("1")
            print(str(num_dec) + "remains")
          elif num_dec <= 8:
            print("0")
            print(str(num_dec) + "remains")
            if num_dec >= 4 or num_dec == 4:
              num_dec = num_dec - 4
              print("1")
              print(str(num_dec) + "remains")
            elif num_dec <= 4:
              print("0")
              print(str(num_dec) + "remains")
              if num_dec >= 2 or num_dec == 2:
                num_dec = num_dec - 2
                print("1")
                print(str(num_dec) + "remains")
              elif num_dec <= 2:
                print("0")
                print(str(num_dec) + "remains")
                if num_dec >= 1 or num_dec == 1:
                  num_dec = num_dec - 1
                  print("1")
                  print(str(num_dec) + "remains")
                elif num_dec <= 1:
                  print("0")
                  print(str(num_dec) + "remains")
