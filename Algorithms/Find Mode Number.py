def findMode(ls):
    newLs = set(ls)
    dic={}
    for i in newLs:
        dic[i]=ls.count(i)
    return [k for k, v in dic.items() if v == max(list(dic.values()))]