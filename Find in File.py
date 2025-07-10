# mbox-short.txt 
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        line1 = line.rstrip().split(":")[1]
        value = float(line1)
        total = total + value
        count = count + 1
avg = total / count
print("Average spam confidence:", avg)