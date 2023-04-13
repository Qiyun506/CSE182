with open("datafile.txt", mode="r") as f:
    data = []
    datadict = dict()
    for line in f:
        data.append(line)
    currKey = "1"
    for i in data:
        if i[0] == ">":
            currKey = i
            datadict[currKey] = list()
        else:
            datadict[currKey].append(i)
#sequence headers:
seqLength = dict()
for i in datadict:
    l = ""
    for j in datadict[i]:
        for k in j:
            if(k != "\n"): l = l + k
    seqLength[i] = l
    
# print result:
headers = []
for i in seqLength:
    print("header: " + i + "\n"+ "Seq Length: " + str(len(seqLength[i])) + "\n")
    arr = i.split('|')
    headers.append(arr)

# print(headers)

        

