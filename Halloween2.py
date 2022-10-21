import random
 

class House():

    def __init__(self):
       
        random_rating = random.random()*10
        self.rating = round(random_rating,3)

    def return_rating(self):
       
        return self.rating
   
   
def highest(x, y, matrix, prevloc):

    up, down, left, right = 0.0, 0.0, 0.0, 0.0

    # if neighbor value exists and
    # if neighbor is not one of the previous neighbors

    if 0<= y+1 <= 4 and [x,y+1] not in prevloc:
        up = matrix[x][y+1]

    if 0<= y-1 <= 4 and [x,y-1] not in prevloc:
        down = matrix[x][y-1]
       
    if 0<= x-1 <= 4 and [x-1,y] not in prevloc:
        left = matrix[x-1][y]
       
    if 0<= x+1 <= 4 and [x+1,y] not in prevloc:
        right = matrix[x+1][y]

    neighbor = [up, down, left, right]
   
   
    #return position value of maximum neighbor
   
    if max(neighbor) == neighbor[0]:
        return [x,y+1]
   
    elif max(neighbor) == neighbor[1]:
        return [x,y-1]
   
    elif max(neighbor) == neighbor[2]:
        return [x-1,y]
   
    elif max(neighbor) == neighbor[3]:
        return [x+1,y]


def main():

    visit = int(input("number of visits? "))

    matrix = []

    #create House instances in 5*5 matrix
    for i in range(5):
        matrix.append(list())
        for j in range(5):
            matrix[i].append(House().return_rating())
           
    print("\nrating of each neighborhood: ")        
    print(matrix)


    #finding maximum starting point and storing position of x and position of y
    max_startp = []
    max_rate = 0.0

    for i in range(5):
        for j in range(5):
            if matrix[i][j] > max_rate:
                max_rate = matrix[i][j]
                max_startp.append([i,j])


    posx = max_startp[-1][0]
    posy = max_startp[-1][1]

    trapcount = 0
    #path shows the rating of the house that corresponds to each 'path_loc'
    #path_loc shows the final path
    path = []
    path.append(matrix[posx][posy])
    path_loc = [[posx, posy]]

    #repeat n times (visit-1 since first value found)
    #find h (returns next movement position)
    #append path h
   
    for i in range(visit-1):
       
        h = highest(posx,posy,matrix,path_loc)
       
        if h[0]>=5 or h[1]>=5:
            trapcount = True
            path.clear()
            path_loc.clear()
            print("\nalternative solution generating...------------------------------")
            break
       
        path.append(matrix[h[0]][h[1]])
        path_loc.append(h)
       
        posx = h[0]
        posy = h[1]
       
    #when trapped, starting value is random position,
    #but find the greatest neighbor and so on
    #repeat in while loop until trapped path does not occur
    while trapcount == True:

        posx2 = random.randint(1,4)
        posy2 = random.randint(1,4)

        path.append(matrix[posx2][posy2])
        path_loc.append([posx2,posy2])

       
        for i in range(visit-1):
           
            h2 = highest(posx2,posy2,matrix,path_loc)
           
           
            if h2[0]>=5 or h2[1]>=5:
                path.clear()
                path_loc.clear()
                trapcount = 1
                break
           
           
            path.append(matrix[h2[0]][h2[1]])
            path_loc.append(h2)
           

            posx2 = h2[0]
            posy2 = h2[1]
       
        if len(path_loc) == visit:
            trapcount = False
        else:
            continue
           
       

    #find and print average rating of neighborhood
    total1 = 0
    for i in range(5):
        for j in range(5):
            total1 += matrix[i][j]
    average1 = round(total1/25,4)
    print("\naverage rating of neighborhood: " + str(average1))
           
    #print final path
    print("\nfinal path for %d visits: " %visit, end="")
    print(path_loc)

    #print rating for each "path" that was generated
    print("\nrating for each path: ", end="")
    print(path)
   
    #find and print average rating for each path
    total2 = 0
    for i in path:
        total2 += i
    average2 = round(total2/visit,4)
    print("average rating for final path: " + str(average2))
   


       

if __name__ == "__main__":

    main()
