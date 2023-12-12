import networkx as nx
import random as rn
from datetime import datetime

def gen_graph_file(n,prob,num):
    #initializing
    n=n
    prob=prob
    graph_num=num
    G=[]
    adj=[]
    file_name=str(n)+"_"+str(prob)[2]+".text"
    file1=open("./instance_graph/"+file_name,"w")

    #set the seed 
    rn_seed=datetime.now().timestamp()
    rn.seed(rn_seed)


    # G.append(nx.gnp_random_graph(n,prob,seed=seed,directed=False))

    #generating
    for i in range(graph_num):
        seed=rn.randrange(0,100000000)
        g=nx.gnp_random_graph(n,prob,seed=seed,directed=False)
        while not nx.is_connected(g):
            seed+=1
            g=nx.gnp_random_graph(n,prob,seed=seed,directed=False)
        G.append(g)
        adj.append(G[i].edges())
    
    #modify isomorphic
    for i in range(graph_num-1):
        for j in range(i+1,graph_num):
            while nx.is_isomorphic(G[i],G[j]):
                seed=rn.randrange(0,100000000)
                G[j]=nx.gnp_random_graph(n,prob,seed=seed,directed=False)
            

    #check isomorphic
    for i in range(graph_num):
        for j in range(graph_num):
            if nx.is_isomorphic(G[i],G[j]) and i!=j:
                print("isomorphic : ",i,j)    

    #writing into the file
    for L in adj:
        file1.write(str(L)+"\n")


    file1.close()
   
 