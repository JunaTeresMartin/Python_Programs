#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

def letterCombinations( digits):
    dic={'2':['a','b','c'],'3':['d','e','f']}
    new=[]
    empty=[]
    for d in digits:
        if d in dic: 
            for v in dic[d]:
                new.append(d+v)
        else:
            return empty
    return new
            
n=letterCombinations('')
print(n)