def countWord(file,word):
    ans=[]
    with open(file,"r") as f:
        for i in f.readlines():
            ans.extend(i.split())
    count=0
    for i in range(len(ans)):
        if(ans[i]==word):
            count+=1
    return count
