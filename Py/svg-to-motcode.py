string_buff = ""

with open('out.svg', encoding="utf-8") as f:
    read_data = f.read()
    read_data = read_data.split("<polyline points=")
    for el in read_data:
        if el[0]!="\"":
            continue
        ell = el.split(" stroke")[0]
        ell = ell.strip("\"")

        # print(ell)

        # string_buff += ell.replace(","," ")    
        arr = ell.split(",")
        arr = [str(int(float(a))) for a in arr]    

        arr.insert(0, 'U')
        arr.insert(3, 'D')
        q = (" ").join(arr)
        string_buff+= (q+" ")

print(string_buff)


