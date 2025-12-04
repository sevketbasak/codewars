def maskify(cc):
    result = ""
    for i in range (0, len(cc)):
        result += "#" if i <= len(cc) - 5 and len(cc) > 4 else cc[i]
    return(result)

maskify("SF$SDfgsd2eA")