A = 9987

B = str(A)
C = len(B)
if C == 1:
    print(A)
elif C == 2:
    D = int(B[0])
    E = int(B[1])
    print(D+E)
elif C == 3:
    D = int(B[0])
    E = int(B[1])
    F = int(B[2])
    print(D+E+F)
elif C == 4:
    D = int(B[0])
    E = int(B[1])
    F = int(B[2])
    G = int(B[3])
    print(D+E+G+F)