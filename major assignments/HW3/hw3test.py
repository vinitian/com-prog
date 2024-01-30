

# Function 1
def load_data_to_movie_dict(file_name):
    import json
    # use json.loads to turn string into dictionary
    # return the movies info in dictionary form
    file = open(file_name, 'r')
    movie_dict = {}
    
    for i in file:
        
        each_dict = json.loads(i)
        
        id = str(each_dict['_id']['$oid'])
        title = str(each_dict['title'])
        year = int(each_dict['year']['$numberInt'])
        
        if 'genres' in each_dict:
            genres = list(each_dict['genres'])
        else:
            genres = None
            
        rating = None
        
        if 'tomatoes' in each_dict and ('viewer' in each_dict['tomatoes']) and ('meter' in each_dict['tomatoes']['viewer']):
            rating = int(each_dict['tomatoes']['viewer']['meter']['$numberInt'])
        
    
        if genres == None:
            if rating == None:
                movie_dict[id] = {"title": title, "year": year}
            else:
                movie_dict[id] = {"title": title, "year": year, "rating": rating}
        else:
            if rating == None:
                movie_dict[id] = {"title": title, "year": year, "genres": genres}
            else:
                movie_dict[id] = {"title": title, "year": year, "genres": genres, "rating": rating}

    return movie_dict


# Function 2
def yearly_summary_by_genre(year, movies):
    # return the dictionary of genre as the key and summary of length and min max rating as the value

      
    # 'Genre':[sum, num, min, max]
    all_genre = {'Action': 0, 'Adventure': 0, 'Animation': 0, 'Biography': 0, 'Comedy': 0, 'Crime': 0, 'Documentary': 0, 'Drama': 0, 'Family': 0, 'Fantasy': 0, 'History': 0, 'Horror': 0, 'Music': 0, 'Musical': 0, 'Mystery': 0, 'News': 0, 'Romance': 0, 'Sci-Fi': 0, 'Short': 0, 'Sport': 0, 'Thriller': 0, 'War': 0, 'Western': 0}
    all_ratings = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
   
    for ID in movies:
        if movies[ID]['year'] == year:
            if 'genres' in movies[ID]:
            
                if 'rating' in movies[ID]:
                    for i in movies[ID]['genres']:
                        #add ratings to the list
                        all_ratings[list(all_genre).index(i)].append(movies[ID]['rating'])
                        
                        #num
                        all_genre[i] += 1
                        
                else:
                    for i in movies[ID]['genres']:
                        #num
                        all_genre[i] += 1
                    
            
            else:
                continue
        else:
            continue
        
    summary = {}
    for i in all_genre:
        summary[i] = {
            'num':all_genre[i],
            'rating': {           
                'avg':round(sum(all_ratings[list(all_genre).index(i)])/all_genre[i]),
                'min':min(all_ratings[list(all_genre).index(i)]),
                'max':max(all_ratings[list(all_genre).index(i)])
                }
            }

  
    return summary


# Function 3
def search_movie_keys(query, movies):
  # return a list of ids
  
  # create array search
    search = []
    for_sort = []
    for ID in movies:
        # print(movies[ID])
        count = 0
        for q in query:              
            if q in movies[ID]:
                if q == 'genres':
                    query[q] = query[q].lower()
                    #print(query[q])
                    #print(movies[ID][q])
                    if query[q] in (x.lower() for x in movies[ID][q]):
                        count += 1
                elif movies[ID][q] == query[q]:
                    count += 1
                else:
                    break 
            else:
                break
            #print('---> ' + q)
        if count == len(query):
            search.append(ID)
            for_sort.append([movies[ID]['title'], movies[ID]['year']])
    
    # sort search
#     for_sort checker
#     print(for_sort)
#     print('-'*50)
    for_sort = sorted(for_sort)
#     print(for_sort)
#     print('-'*50)
    
    search_final = []
    for i in for_sort:
        for j in search:
            if (movies[j]['title'] == i[0]) and (j not in search_final):
                search_final.append(j)

    return search_final



# Function 4
def search_movie_title(query_title, movies):
    # return a list of ids
  
    #keyword
    query_title = query_title.lower()
    
    kw = query_title
  
    result = []
    ID_list = []
    
    query_list = query_title.split()
    l = len(query_list)
    for n in reversed(range(1,l+1)):
        #print('n = ' + str(n))
        kw_list = []
        for i in range(l):

            if i+n <= l:
                #print(str(i)+':'+str(i+n) + ' is ', end='')
                kw = ' '.join(query_list[i:i+n])
                # print(kw)
                kw_list.append(kw)
                
        kw_list = list(set(kw_list))
        print(kw_list)
        for kw in kw_list:
            for ID in movies:
                if (kw + ' ' in movies[ID]['title'].lower() + ' '):
                    
                    
                    
                    if ID not in ID_list:
                        result.append([-1, len(movies[ID]['title'].split()), movies[ID]['title'], movies[ID]['year'], ID])
                        ID_list.append(ID)
                        
                    else:
                        result[ID_list.index(ID)][0] -= 1
              
        if result != []:
            break
        
    #print(result)
    
    # sort
    result = sorted(result)
    #print('sorted' + '-'*50)
    #print(result)
    
    all_ID = []
    for i in result:
        all_ID.append(i[-1])

    return all_ID

# --------------------------------------------------

movies = load_data_to_movie_dict('movies_2010_2013.json')
#print(movies)
#print('-'*50)
#print(yearly_summary_by_genre(2010, movies))
#print('-'*50)
# query = {'title':'My Way'}
# search = search_movie_keys(query, movies)
# print(search)

# search sort checker
# print('-'*50)
# i = 1
# for ID in search:
#     print(str(i) + ' : ', end='')
#     print(movies[ID])
#     i += 1

# print('-'*50)
# result = search_movie_title('italy china italy', movies)
# print(result)
# 
# print('result' + '-'*50)
# i = 1
# for ID in result:
#     print(str(i) + ' : ', end='')
#     print(movies[ID])
#     i += 1

x = yearly_summary_by_genre(2013,movies)['Adventure']
print(x)
# exec(input().split())