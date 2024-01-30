
def distance1(x1, y1, x2, y2):
    # returns the distance between points (x1, yl) and (x2, y2)
    # Usage example: dl = distancel (0.0, 0, 3, 4) > dl = 5.0
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return d

def distance2(p1, p2):
    #p1 and p2 are lists.
    #each list is a point, which has 2 indices, storing x and y
    # returns the distance between p1 and p2
    #Usage example: d2 = distance2 ([0.0, 0], [3, 4]) -> d2 = 5.0
    d = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
    return d

def distance3(c1, c2):
    # cl and c2 are lists that represent circles
    # each list has 3 indices, storing center x and y, and radius
    # returns the distance between the center of cl and c2, as well
    # as display if the circle cl and c2 are overlapping or not
    # Usage example: d3, overlap = distance3([0.0, 0, 1], [5, 0, 2]) # > d3 = 5.0, overlap = False
    
    d = ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)**0.5
    # from https://math.stackexchange.com/questions/275514/two-circles-overlap
    return d, round((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2, 10) <= round((c1[2]+c2[2])**2, 10)

def perimeter(points):
    # points is a list of points
    # each point is a list with 2 indices (storing x and y) these points are the corners of the polygon (for k-gon, there are k points total, k>=3)
    # returns the perimeter of the polygon that is defined by the input points
    p = 0
    for i in range(-1,len(points)-1):
        p += distance1(points[i][0],points[i][1],points[i+1][0],points[i+1][1])
    return p

exec(input().strip()) # must have this line when submitting to grader