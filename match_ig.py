import cat
with open("data.seq", mode="r") as f:
    for i in f:
        start = [j for j in range(len(i)) if i[j] =="@"]
        # print(len(start))
start.insert(0,0)
output = open("data.in", "w") # "w" means we will write to outputfilename
gi_match = dict()
for i in range(15):
    output.write(cat.headers[i][1] + ": " + str(start[i]) + '\n')
    gi_match[cat.headers[i][1]] = str(start[i])
