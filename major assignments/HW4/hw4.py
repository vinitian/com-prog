import numpy as np

# Function 1
def generate_followed_by_dict(infile):
    followed_by = {}
    f = open(infile, "r")
    s = f.readlines()
    for i in range(len(s)):
        s[i] = s[i].strip('\n').split(',')
        followed_by[s[i][0]] = s[i][1:]
    
    return followed_by


# Function 2
def generate_followed_by_matrix(followed_by_dict):
    
    person_names = list(followed_by_dict.keys())
    for i in followed_by_dict:
        for j in followed_by_dict[i]:
            if j not in person_names:
                # print(j)
                person_names.append(j)
    person_names = sorted(person_names)
    
    for name in person_names:
        if name not in followed_by_dict:
            followed_by_dict[name] = []

    followed_by_dict2 = {}
    for k, v in sorted(followed_by_dict.items()):
        followed_by_dict2[k] = v
    
    n = len(person_names)
    
    matrix = np.zeros((n, n), dtype = int)
    for k, v in followed_by_dict.items():
        for i in v:
            matrix[person_names.index(k)][person_names.index(i)] = 1
            #print(str(k),end='')
            #print(person_names.index(i))
    
    return matrix, person_names


# Function 3
def generate_degree_matrix(A):
    total = np.sum(A, axis=1)
    #print(total)
    degree_matrix = np.zeros_like(A)
    for i in range(A.shape[0]):
        degree_matrix[i][i] = total[i]
        
    return degree_matrix


# Function 4
def get_top_influencer(M, person_names):
    degree_matrix = generate_degree_matrix(M)
    top = np.max(degree_matrix)
    #print(top)
    top_list = []
    for i in range(degree_matrix.shape[0]):
        if degree_matrix[i][i] == top:
            top_list.append(person_names[i])
            
    return top_list
    

# Function 5
def generate_similarity_matrix_among_influencers(M, person_names):
    n = M.shape[0]
    #print(n)
    for i in reversed(range(n)):
        isZero = M[i]==0
        if all([x for x in isZero == True]):
            M = np.delete(M, (i), axis=0)
            person_names.pop(i)
    #print('-----------')
    #print(person_names)
    #print(M)
    #print('-----------')
    N = np.zeros_like(M, float)
 
    n = M.shape[0]        
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            #print(person_names[i], person_names[j])
            a = np.sum(M[i])
            b = np.sum(M[j])
            #print(a, b)
            C = (M[i] + M[j])
            C = C[C == 2]
            c = len(C)
            #print(c)
            N[i][j] = round(c/(a+b-c), 2)
            #print(M[i][j])
            #print('----')
            
    N = N[:, :N.shape[0]]   
    return N, person_names

    
            
# Function 6
def get_all_pairs_of_most_similar_influencers(S, only_influencers):
    
    n = S.shape[0]
    max = np.max(S)
    pairs = []
    count = 0
    
    if max == 0 :
        return []
    
    for i in range(n):
        for j in range(i+1, n):
            if S[i, j] == max:
                pairs.append((only_influencers[i], only_influencers[j]))
                
    return pairs
            



# -----------------------------
'''
# print(generate_followed_by_dict('infile_1.txt'))
d = generate_followed_by_dict('infile_1.txt')
print(d)

m, p = generate_followed_by_matrix(d)
print(m)
print(p)

#dgr = generate_degree_matrix(m)
#print(dgr)

#top = get_top_influencer(m, p)
#print(top)

sm, p2 = generate_similarity_matrix_among_influencers(m, p)
print(sm)
print(p2)

pairs = get_all_pairs_of_most_similar_influencers(sm, p2)
print(pairs)
'''

# Testcase 2
followed_by_dict = generate_followed_by_dict("infile_5.txt")
print(followed_by_dict)
M, person_names = generate_followed_by_matrix(followed_by_dict)
print("M = ", M)
print("person_names", person_names)
D = generate_degree_matrix(M)
print("D = ", D)
print("top influencers = ", get_top_influencer(M, person_names))
SM, all_influencers = generate_similarity_matrix_among_influencers(M, person_names)
print("similarity_matrix = ", SM)
print(all_influencers)

pairs = get_all_pairs_of_most_similar_influencers(SM, all_influencers)
print(pairs)


