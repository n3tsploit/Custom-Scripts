with open("words.text", "r") as r:
    lines = r.readlines()
    for line in lines:
        result = bin(int(line))[2:]
        length = len(result)
        if length != 29 :
            padding = (29-length) * "0"
            result = padding + str(result)
        print(f"{result}")