ch = open("characters.csv","r")
new_ch = open("new_characters.csv","w")

for line in ch:
    new_ch.write(line.split(",")[0] + "\n")
