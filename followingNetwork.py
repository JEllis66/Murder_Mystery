import random

# list length (x) must be at least follow this equation to have sufficient number of followers (y = maxFollowing, z = maxFollowers): 
# x = (y+z+1)
lst = ["a","b","c","d","e","f","g","h","i","j","k","l","m"] #pull in from database
following = {}
followers = {}
possibleToFollow = []
maxFollowers = 4
maxFollowing = 4
numRunsToSuccess = 1
runApp = "re-roll"

def initialize(input):

    global following
    global followers

    for ind in input:
        following[ind] = []
        followers[ind] = 0
        
    addFollowing()

def addFollowing():
    
    global following
    global followers
    global maxFollowers
    global maxFollowing
    global runApp
    global numRunsToSuccess
    totCount = len(lst)
    
    if(totCount <= maxFollowing+1):
        
        for ind in lst:
            
            tmp = lst.index(str(ind))
            
            result = lst[:tmp] + lst[tmp+1:]
            following[str(ind)] = result
            followers[str(ind)] = len(following[str(ind)])
            
    elif(totCount > maxFollowing+1 ):

        if ( (len(lst)) < (maxFollowers + maxFollowing + 1) ):
            maxFollowers = int( (len(lst)-1)/2 )
            maxFollowing = maxFollowers
        
        if ( (len(lst)) > (maxFollowers*maxFollowers) ):
            maxFollowers += 1
            maxFollowing += 1
            
        
        for ind in lst:
            currentIndexNum = lst.index(str(ind))
            charValue = str(ind)

            possibleToFollow = lst[:currentIndexNum] + lst[currentIndexNum+1:]
            chooseFollower(possibleToFollow,charValue)

        for ind in lst:
            if(str(ind) == str(lst[len(lst)-1]) and int(followers[str(ind)]) >= (maxFollowers-1) ):
                break
            elif( int(followers[str(ind)]) < (maxFollowers-1) or len(following[ind]) < (maxFollowing-1)):
                print("Index containing character", ind, "had", int(followers[str(ind)]), "followers")
                following = {}
                followers = {}
                numRunsToSuccess+=1
                runApp = "re-roll" 
                return

        runApp = "done"
        print("Total runs = ", numRunsToSuccess)
        print("Max Following: ",maxFollowing)
        print("Max Followers: ", maxFollowers)
        print("Following: ", following)
        print("Followers: ", followers)

        return               

def chooseFollower(inputLst, inputChar):

    global following
    global followers
    
    if(len(inputLst) < 1 or len(following[inputChar]) >= maxFollowing):
        return
    
    randomIndex = random.randrange(len(inputLst))
    toFollow = str(inputLst[randomIndex])
    
    if(followers[toFollow] == maxFollowers):
        
        chooseFollower(removeIndex(inputLst, toFollow),inputChar)
    
    elif(followers[toFollow] < maxFollowers):
        
        followers[toFollow] = followers[toFollow] + 1
        following[inputChar].append(toFollow)
        chooseFollower(removeIndex(inputLst, toFollow),inputChar)

def removeIndex(inputLst, toFollow):

    removeIndx = inputLst.index(toFollow)
    newList = inputLst[:removeIndx] + inputLst[removeIndx+1:]
    return newList

def runApplication():
    while(runApp == "re-roll"):

        initialize(lst)


runApplication()


