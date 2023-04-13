import match_ig
SeqLength = match_ig.cat.seqLength
input = "MHIQITDFGTAKVLSPDS"
idx = []
count = 0
for i in SeqLength:
    if SeqLength[i].find(input) != -1:
        idx.append(count)
    count +=1
gis = []
for i in match_ig.gi_match:
    gis.append(i)

for i in idx:
    print(gis[i])