import sys
if len(sys.argv) < 2:
    print("Usage: python fastq_parser.py <filename>")
    sys.exit(1)
filename = sys.argv[1]

i=0
sequences=[]
quality=[]
with open(filename, "r") as f:
 
   
    for line in f:
        i+=1
        if i%4==2:
            sequences.append(line.strip())
        if i%4==0:
            quality.append(line.strip())
print(f"Total Lines: {i} \nTotal reads: {i//4} ")
print("Sequences:")
for seq, qual in zip(sequences, quality):
     print(seq , len(seq) ,"bp")
     print(f"Quality: {qual}")
     scores = [ord(char) - 33 for char in qual]
     avgscore = sum(scores)/len(scores)
     print (f"Average Quality: {round(avgscore,2)}")
     if avgscore == 40:
        print ("Perfect Score - PASS")
     elif avgscore > 30:
         print("Good Quality - PASS")
     elif avgscore > 20:
         print("Mediocre - FAIL")
     else:
         print ("Poor Quality - FAIL")
         