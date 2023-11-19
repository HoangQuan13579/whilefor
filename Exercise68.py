count=0
while (True):
     data=input("Enter 8 bits of data:")
     if data == " ": break 
     elif len(data)==8:
        for i in data:
            if i!= "1" and i!= "0":
                 print("Invalid! Please re-enter!")
                 continue
        else:
            for i in data:
                if i=="1":
                    count += 1
            if count % 2 == 0:
                print("parity_bit = 0")
            else: 
                print("parity_bit = 1")
     elif len(data)!=8:
         print("Invalid data length.")