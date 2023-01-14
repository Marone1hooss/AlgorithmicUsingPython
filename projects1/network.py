#importing all the needed libraries
import sys
import heapq
#Reading the file and converting his elements into a list of integers
data =[]
with open(sys.argv[1]) as file:
    x=file.readline().rstrip().split()  #reading the first line
    for line in file:  #reading the rest of the file 
        start,end,cost=line.rstrip().split()
        
        
        data.append([int(cost),int(start),int(end)])

nnodes=x[0]
nedges=x[1]
#adj is a dictionary that contains every element of the graph with all his possible connections
adj={i:[] for i in range(1,int(nnodes)+1)}

for i in data:
    dis=i[0]
    n1=i[1]
    n2=i[2]
    adj[n1].append([dis,n1,n2])
    adj[n2].append([dis,n2,n1])
 


#prim is a function that uses prims algorithm to solve spanning tree problem
def prims(adj,nnodes):
    #A boolean dictionary that contains even the nood is visited or not 
    visitedb={i:False for i in range(1,int(nnodes)+1)}
    #The total cost of the tree
    cost=0  
    #The visited elements of the tree
    visited=set() 
    #the connections of the tree
    connections={i:[] for i in range(1,int(nnodes)+1)} 
     #all the possible connections to the tree
    pc=[[0,1,1]] 
   
    heapq.heapify(pc)
   
    while len(visited)<nnodes and len(pc)!=0:
#The closest element to the tree  
        dic,start,end=heapq.heappop(pc)

        if visitedb[end]:
            continue

        cost+=dic
        visited.add(end)
        visitedb[end]=True
        connections[start].append(end)
#Adding all the connections of the element to the pc if they are not already there
        for i in adj[end]:   
            if not visitedb[i[2]]:

                heapq.heappush(pc,i) 


    remove=connections[1].pop(0)

    #displaying the resulte
    print("---------------------------------------------------------------------------------------------------")
    print("")
    print("Prims algorithm:")
    print("")
    print("the cost is :",cost)


    for i in connections:

        if connections[i]!=[]:
            print(i,end=" ")

            for j in connections[i]:
                print(j,end=" ")

            print('')

#kruskal's algorithm

def kruskals(data,nnodes):

    cost=0
    visitedb={i:False for i in range(1,int(nnodes)+1)}
    visited=set()
    connections={i:[] for i in range(1,int(nnodes)+1)}

    group={i:int for i in range(1,int(nnodes)+1)}
    a=1
    heapq.heapify(data)


    while len(visited)<nnodes:#while we didn't visite all the elements

        min=heapq.heappop(data)#the edge with the minimum distance
        dic=min[0]
        n1=min[1]
        n2=min[2]

        #if the two limits of the edge are visited 
        if visitedb[n1] and visitedb[n2]:
            #checking if they are in the same group
            if group[n1]==group[n2]:
                continue
            x=group[n1]
            y=group[n2]
            cost+=dic
            connections[n1].append(n2)
            #connecting the two groups
            for i in group:
                if group[i]==y:
                    group[i]=x

        #if one of theme is already visited
        elif visitedb[n1]:
            cost+=dic
            visited.add(n2)
            visitedb[n2]=True
            connections[n1].append(n2)
            group[n2]=group[n1]
        elif visitedb[n2]:
            cost+=dic
            visited.add(n1)
            visitedb[n1]=True
            connections[n2].append(n1)
            group[n1]=group[n2]


        #if no one of theme is connected 
        else:
            cost+=dic
            visited.add(n1)
            visited.add(n2)
            visitedb[n1]=True
            visitedb[n2]=True
            group[n1]=a
            group[n2]=a
            a+=1

            if n1<n2:
                connections[n1].append(n2)
            else:
                connections[n2].append(n1)
           
    
    print("-------------------------------------------------------------------------------------------------------------")
    print("")
    print("Kruskal's algorithm: ")
    print("")
    print("the cost is :",cost)
    print("")


    for i in connections:

        if connections[i]!=[]:
            print(i,end=" ")

            for j in connections[i]:
                print(j,end=" ")

            print('')





#calling the functions
prims(adj,int(nnodes))
kruskals(data,int(nnodes))
