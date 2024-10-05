bir = 1

while bir <= 10:
    print("")
    print("basamak :", bir)

    for i in range(1,11):
        msj = "{} x {} = {}".format(i,bir,(i*bir))
        print(msj)
    bir += 1