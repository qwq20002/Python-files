def read(data):
    file=open(data).readlines()
    basicInfo={}
    #去掉换行符
    for i in range(len(file)):
        file[i]=file[i].replace("\n",'')
    for i in file[0:5]:
        basicInfo[i.split(":")[0]]=i.split(":")[1]
    title=basicInfo.get("TITLE")
    bpm=int(basicInfo.get("BPM"))
    offset=float(basicInfo.get("OFFSET"))
    start=0
    Pad=file[5]
    return basicInfo,Pad
