doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
for i in doc_list:
    j=i
    res=j.strip('.').split(' ')
    print(res)
    if 'Casino' in res:
        print(doc_list.index(i))
        break
    