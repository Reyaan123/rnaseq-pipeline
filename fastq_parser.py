with open("sample.fastq", "r") as f:
 
    i=0
    for line in f:
        i=i+1

    print(f"Total Lines: {i} \nTotal reads: {i//4} ")