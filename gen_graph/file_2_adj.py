import networkx as nx

def get_adj_from_files(file_name):

    #initializing
  
    file1=open(file_name,"r")
    graph_str=[]
    graph=[]
    graph_num=0

    #set the adj matrices
    matrices=file1.read().split("\n")
    del matrices[-1]
    #conver str to graph matrix
    for i in matrices:
        graph_str.append(i.split("), "))
    for l in graph_str:
        # print(l)
        graph.append([])
        for obj in l:
            indx=obj.find('(')
            graph[graph_num].append([int(obj[indx+1]),int(obj[indx+4])])
        graph_num+=1
    # get the graph matrix
    # for item in graph:
    #     print(item)
    #draw by graph matrix
    # G=nx.Graph()
    #G.add_edges_from(graph[3])
    # nx.draw_networkx(G,with_labels=True)
    
    return graph