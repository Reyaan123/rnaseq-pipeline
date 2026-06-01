import sys
if len(sys.argv) < 2:
    print("Usage: python fastq_parser.py <filename>")
    sys.exit(1)
filename = sys.argv[1]

i=0
sequences=[]
with open(filename, "r") as f:
 
   
    for line in f:
        i+=1
        if i%4==2:
            sequences.append(line.strip())
print(f"Total Lines: {i} \nTotal reads: {i//4} ")
print("Sequences:")
for seq in sequences:
     print(seq , len(seq) ,"bp")
    