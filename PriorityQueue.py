"""
Simulating A Priority Queue
Written by: Elifnaz Gulsen
"""

"""
This function reads in the file provided, and divides into a list of
lists to use later on as calls
input: none
output: returns list of list of calls
"""
def readFile():
    file = open("emergencies.txt",'r')
    lisCommands = []
    for line in file:
        lisCommands.append(line.split())
    file.close()
    return lisCommands

"""
This function adds a job into the queue based on the priority ordering,
1-30 (1 being lowest, and 30 being highest priority)
input: Linked List(queue), item(job) to insert into linked list.
output: sorted linked list with highest priority as first node
"""
def addToQueue(item):
    global jobs
    currentJob = {}
    currentJob['data'] = item
    #if priority of item we are adding is greater than(or equal to)the one after it
    #add the item to the beginning of the list (or if queue empty currently)
    if jobs == None or (int(item[2]) >= int(jobs['data'][2])):
        currentJob['next'] = jobs
        jobs = currentJob
        return jobs
    
    #if our node > node we are comparing then we break out of the while loop
    #our previous node points to the node we want to add, and we point our
    #node's next to the after
    previous = jobs
    afterNode = previous['next']
    while afterNode != None and int(item[2]) < int(afterNode['data'][2]):
        previous = afterNode
        afterNode = afterNode['next']

    previous['next'] = currentJob
    currentJob['next'] = afterNode
    
    return jobs

"""
This function modifies a given call's priority accordingly
Then it deletes the old node and adds it again as if it were a new node
For these purposes, we call the remove() and addToQueue() functions for help
input: call we want to change the priority of
output: returned list, call with modified priority
"""
def modifyPriority(item):
    pointer = jobs
    while pointer != None:
        if int(item[1]) == int(pointer['data'][1]):
            pointer['data'][2] = item[2]
            delItem = remove(pointer['data'])
            addNew = addToQueue(pointer['data'])
        pointer = pointer['next']

    return jobs
    
    
"""
This function returns the number of calls associated with each call type
input: none
output: number of medical, traffic and crime calls
"""
def showStatistics():
    numMedical = 0
    numTraffic = 0
    numCrime = 0
    pointer = jobs
    while pointer != None:
        if pointer['data'][3] == 'traffic':
            numTraffic += 1
            pointer = pointer['next']
        elif pointer['data'][3] == 'medical':
            numMedical += 1
            pointer = pointer['next']
        else: 
            numCrime += 1
            pointer = pointer['next']
            
    return "medical calls:", numMedical,"traffic calls:",numTraffic,"crime calls:",numCrime


"""
This function removes a job that has been responded to, 
removes the node from the head of the linked list
input: Linked list
output: Our linked list, minus the job we have just removed
"""
def removeFromFront():
    global jobs
    if jobs == None:
        return "No current emergencies - Time for a coffee break!"
        
    print("Responding to Call:",int(jobs['data'][1]))
    print("")
    jobs = jobs['next']
    return jobs


"""
This function removes a job from any node location  in the linked list
input: none
output: linked list, minus the job we have removed
"""
def remove(item):
    global jobs
    pointer = jobs
    #if it's the first item, just return jobs = jobs['next']
    if int(pointer['data'][1]) == int(item[1]):
        jobs = jobs['next']
        return jobs
    
    #after node is the node after our pointer
    #when we reach the item we would like to remove, pointer settles on that
    #node, then our previous will be pointing at our afterNode,
    #deleting the node that the item we wish to delete is in.
    afterNode = pointer['next']
    while pointer!= None and int(pointer['data'][1]) != int(item[1]):
        previous = pointer
        afterNode = afterNode['next']
        pointer = pointer['next']
        
    previous['next'] = afterNode
    return jobs
    
    
    

"""
This function returns the details of a call
input: None
output: call details
"""
def callDetails(item):
    pointer = jobs
    details = ""
    #go through the linked list until we reach the ID number we want to find
    while pointer != None:
        if int(pointer['data'][1]) == int(item[1]):
               details = details + str(pointer['data'])
        pointer = pointer['next']
        
    return details

"""
This function returns the average priority of the calls in the linked list
input : None
output: integer showing the average priority of the calls in the linked list
"""
def averagePriority():
    pointer = jobs
    add = 0
    num = 0    
    while pointer != None:
        add = add + int(pointer['data'][2])
        pointer = pointer['next']
        num = num + 1 
    avg = (add)/(num)
    return avg
                               

"""
This function prints the data values in the queue
input: None
output: jobs shown line by line 
"""
def printQueue():
    pointer = jobs
    contents = ""
    while pointer != None:
        contents = contents + "\n" + str(pointer['data'])
        pointer = pointer['next']
    return contents
    
"""
main function starts program execution
input : none
"""
def main():
    list_commands = readFile()
    global jobs
    #we start with an empty queue to add calls to
    jobs = None
    
    for i in list_commands:
        if i[0] == "received":
            add = addToQueue(i)
            print("Adding Call",i[1],"to the queue.")
            print(int(i[2]),"is the priority of the call")
            print("Call",int(i[1]),"is of type:",i[3])
            print("")

        elif i[0] == "modify":
            print("Modifying Priority of Call:",i[1])
            print("")
            modify = modifyPriority(i)
        
        elif i[0] == "statistics":
            showStats = showStatistics()
            print("Current Statistics:")
            print(showStats)
            print("")
            
        elif i[0] == "details":
            showDetails = callDetails(i)
            print(" - - - - - - - - - - - - - - - - - - -")
            print("Details of Call",i[1],":")
            print(showDetails)
            print(" - - - - - - - - - - - - - - - - - - -")
            print("")

        elif i[0] == "respond":
            respond = removeFromFront()

        elif i[0] == "remove":
            print("Removing Call:",i[1])
            print("")
            removeItem = remove(i)
            
        else: # show the queue and average priority
            currentQueue = printQueue()
            findAvg = averagePriority()
            print("___________________________________________________")
            print("C U R R E N T    Q U E U E: ")
            print(currentQueue)
            print("\nAverage Priority of Calls: %.2f \n" % findAvg)
            print("___________________________________________________")
            print("")

main()
