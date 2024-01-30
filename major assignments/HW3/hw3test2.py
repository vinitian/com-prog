movies = {
 '573a139cf29313caabcf6fb1': {
    'title': 'Pèl Adrienn',
    'year': 2010,
    'genres': ['Drama'],
    'rating': 67
    },
 '573a13aaf29313caabd21654': {
     'title': 'In My Sleep',
     'year': 2010,
     'genres': ['Drama', 'Mystery', 'Thriller'],
     'rating': 33
     },
 '573a13acf29313caabd29366': {
     'title': 'The Secret Life of Walter Mitty',
     'year': 2013,'genres': ['Adventure', 'Comedy', 'Drama'],
     'rating': 70
     },
 '573a13aef29313caabd2c99e': {
    'title': 'The Pacific',
    'year': 2010, 
    'genres': ['Action', 'Adventure', 'Drama']
    }, 
 '573a13aef29313caabd2d001': {
    'title': 'The Rum Diary',
    'year': 2011, 
    'genres': ['Comedy', 'Drama']
    }, 
 '573a13aef29313caabd2d6e9': {
    'title': 'Gnomeo & Juliet', 
    'year': 2011, 
    'genres': ['Animation', 'Comedy', 'Family']
    }, 
 '573a13aef29313caabd2e9e5': {
    'title': 'The Three Stooges', 
    'year': 2012, 
    'genres': ['Comedy']
    }, 
 '573a13aef29313caabd2edcd': {
    'title': 'The Crimson Petal and the White',
    'year': 2011,
    'genres': ['Drama', 'Romance']
    }
 }

query = {'year':2016, 'genres':'drama'}

search = []
for ID in movies:
    print(movies[ID])
    count = 0
    for q in query:              
        if q in movies[ID]:
            if q == 'genres':
                query[q] = query[q].lower()
                print(query[q])
                print(movies[ID][q])
                if query[q] in (x.lower() for x in movies[ID][q]):
                    count += 1
            elif movies[ID][q] == query[q]:
                count += 1
            else:
                break 
        else:
            break
        print('---> ' + q)
    if count == len(query):
        search.append(ID)
        
print('-'*50)
print('search: ', end='')
print(search)

for ID in search:
    pass
        