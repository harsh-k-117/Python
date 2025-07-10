def computepay(h, r):
    if h <= 40:
        p = h * r
        return p

    elif h > 40 :
        extra_rate = r * 1.5
        extra_hrs = h - 40
        p = (40 * r) + (extra_hrs * extra_rate)
        return p

hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter the rate per hour: ")
r = float(rate)
pay = computepay(h, r)
print("Pay", pay)
