n = 5
for num in range(n,0,-1):
    output = ""
    seq = num
    while seq > 0:
        output = output + str(seq)
        seq = seq-1
    print(output)