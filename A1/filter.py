import cat
import textwrap
seq = cat.seqLength
rats = ["RAT", "Mus"]
for i in seq:
    print("\n")
    if any([x in i for x in rats]):
        print(i)
        string = ""
    # print("-------------")
    # print(seq[i])

        for j in seq[i]:
            string = string + j
            # print(len(string))
            if(len(string) == 60):
                print(string)
                string = ""
