score = input("Enter Score: ")
fsc = float(score)

if 0.0 <= fsc <= 1.0:
    if fsc >= 0.9 :
        print("A")
    elif fsc >= 0.8 :
        print("B")
    elif fsc >= 0.7 :
        print("C")
    elif fsc >= 0.6 :
        print("D")
    elif fsc < 0.6 :
        print("F")

else :
    print("Error")