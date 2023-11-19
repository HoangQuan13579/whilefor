daycu=input("Nhap day can ma hoa: ")
shift=int(input("So nac ma hoa: "))
daymoi=""
dayalphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range (0,len(daycu)):
    for j in range (0,len(dayalphabet)):
        if daycu[i]==dayalphabet[j]:
              kytumoi=dayalphabet[(j+shift)%26]
              daymoi=daymoi+kytumoi
print(daymoi)