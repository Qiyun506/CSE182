import cat

output = open("data.seq", "w") # "w" means we will write to outputfilename
counter = 1
for i in cat.seqLength:
    output.write(cat.seqLength[i])
    if counter < len(cat.seqLength):
        output.write("@")
        counter+=1
