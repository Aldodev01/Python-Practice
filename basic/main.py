
#! Segitiga
for i in range(9):
    for j in range(i + 1):
      print(j + 1, "x", j + 1, "=", end=" " + str((j + 1) * (j + 1)) + ", ")
    print("\n");