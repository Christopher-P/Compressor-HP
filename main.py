d = {}
last = 'start'
try:
    with open("small-data") as infile:
        for line in infile:
            for i in line:
                if i in d.keys():
                    #print(i, 'is in')
                    #d[i] = []
                    print(last, i)
                    if last in d[i].keys():
                        d[i][last] = d[i][last] + 1
                    else:
                        d[i][last] = {i:1}
                else:
                    d[last] = {i:1}
                    
                print(d)

                last = i   
except Exception as e:
    print(e)
    print(d)
    print(len(d))


'''
        print(line)
        words = line.split()
        for i in words:
            n = ''.join(x for x in i if x.isalpha())
            if n in d.keys():
                d[n] += 1
            else:
                d[n] = 0   
                      
                
print(d)
print(d['the'])
print(d['from'])

count = 0
for i in d:
    if d[i] > 4:
        count += 1

print(count)

print(len(d))
'''
