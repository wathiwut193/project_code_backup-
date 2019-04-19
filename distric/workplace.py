with open('distric.txt','r',encoding='utf-8') as file:
    distric = file.readlines()
    work = []
    for add in distric:
        add = add.strip()
        work.append(add)
    work.sort()
    work.sort(key=len,reverse=True)
    print(work)
#print(distric)
#print(len(distric))

with open('distric_sort_long_to_short.txt','w+',encoding='utf-8') as writefile:

    writefile.readlines()
    writefile.write('|'.join(work))

    file.close()
    writefile.close()
