from collections import deque
def preprocessing(s: str)->list[list[str]]:
    s.strip()
    l=[]
    n=len(s)
    i=0
    while i<n:
        if s[i]=='{':
            i+=1
            p=""
            while s[i]!="}":
                p+=s[i]
                i+=1
            i+=1
            c=p.split(',')
            l.append(c)
        else:
            l.append(s[i])
            i+=1
    return l

def getcombinations(s:str):
    li=preprocessing(s)
    d=deque()
    d.add(li[0].split())