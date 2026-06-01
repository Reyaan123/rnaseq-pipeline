import sys
filename = sys.argv[1]
with open(filename, "r") as f:
 
    i=0
    sequences=[]

    for line in f:
        i=i+1
        if i%4==2:
            sequences.append(line.strip())

    print(f"Total Lines: {i} \nTotal reads: {i//4} ")
    print("Sequences:")
    for seq in sequences:
         print(seq)