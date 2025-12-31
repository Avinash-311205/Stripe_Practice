def calculatepenalty(log: str, closing_time: int):
    n = len(log)
    penalty = 0
    
    for i in range(n):
        if i < closing_time:
            if log[i] == "N":
                penalty += 1
        
        else:
            if log[i] == "Y":
                penalty += 1
    return penalty
    
def getminimaltime(log: str):
    n = len(log)
    
    penalty = log.count("Y")
    
    min_penalty = penalty
    best_closing_time = 0
    
    for t in range(n):
        if log[t] == "Y":
            penalty -= 1 
        else:
            penalty += 1
            
        if penalty < min_penalty:
            min_penalty = penalty
            best_closing_time = t + 1 
            
    return best_closing_time

def getallclosing(log: str):
    tokens = log.split()
    stack = []
    result = []

    for token in tokens:
        if token == "BEGIN":
            stack.append([])

        elif token == "END":
            store_log = ''.join(stack.pop())
            result.append(getminimaltime(store_log))

        else:
            stack[-1].append(token)
    return result


