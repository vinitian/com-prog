# Q5: Messy Travel Records

def create_record():
    
    records = []
    x = input()
    while x != 'q':
        a, b, c = x.split()
        records.append([a,b,c])
        x = input()
        

    return records


def sort_list(records):
    r = []
    
    for i in range(len(records)):
        d = [int(e) for e in records[i][1].split('/')]
        date = [d[2], d[1], d[0]]
        r.append([records[i][0], date, records[i][2]])
        #print(date)
    #print(r)
    #print('-'*20)
    x = sorted(r)

    sorted_records = []
    for i in range(len(x)):
        s = str(x[i][1][2]) + '/' + str(x[i][1][1]) + '/' + str(x[i][1][0])
        sorted_records.append([x[i][0], s, x[i][2]])
        
    return sorted_records


def create_output(sorted_records):
    name = []
    trip = []
    
    for i in sorted_records:
        if i[0] not in name:
            name.append(i[0])
            trip.append([i[1]+':'+i[2]])
        else:
            trip[name.index(i[0])].append(i[1]+':'+i[2])
    
    return name, trip
    

def main():
    records = create_record()
    
    if records == []:
        print('No records!')
    else:
        #print(records)
        #print('-'*20)
        r = sort_list(records)
        #print(r)
        #print('-'*20)
        name, trip = create_output(r)
        for i in range(len(name)):
            print(name[i], end= ' ')
            print(trip[i])

exec(input())
