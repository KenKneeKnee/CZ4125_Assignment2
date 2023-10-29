import pandas as pd
import ast
import networkx as nx
from pyvis.network import Network

df = pd.read_csv("Processed_4.csv")

# get total number of publications in SCSE
def get_total_publi_df(df):
    # Create a total publication dictionary
    total_publi = {}
    for e in df['Publication Counts'].values:
        e = ast.literal_eval(e)
        for k,v in e.items():
            if k in total_publi:
                total_publi[k] += v
            else:
                total_publi[k] = v

    # Create and return a sorted dataframe
    years = []
    counts = []
    for k,v in total_publi.items():
        years.append(k)
        counts.append(v)
    rdf = pd.DataFrame(list(zip(years, counts)),columns =['Year', 'Count'])
    
    return rdf.sort_values(by = "Year", ascending = True)

# Get a publication dictionary with year as key 
# and values as sorted publication count by faculty
def get_sorted_publi_dict(df):
    names = df['Full Name'].values
    publications = df['Publication Counts'].values
    publi_by_prof = {}
    for i in range(len(df)):
        name = names[i]
        publi = ast.literal_eval(publications[i])
        for k,v in publi.items():
            if k not in publi_by_prof:
                publi_by_prof[k] = [(v,name)]
            else:
                publi_by_prof[k].append((v,name))

    for k in publi_by_prof:
        publi_by_prof[k].sort(reverse = True)

    return publi_by_prof

# Returns graph by field
def field_graph(df,w):
    net = Network()
    net.repulsion()
    n = len(df)

    names = df['Full Name'].values
    fields = df['Fields'].values

    # Add nodes
    for i in range(n):
        net.add_node(names[i], label = names[i])

    pairs = []
    for i in range(n-1):
        for j in range(i+1,n):
            weight = len(set(ast.literal_eval(fields[i])) & set(ast.literal_eval(fields[j])))
            if weight >=w:
                pairs.append((names[i],names[j]))
    for pair in pairs:
        net.add_edge(pair[0], pair[1])

    return net

def co_author_graph(df,p):
    net = Network()
    net.repulsion()
    n = len(df)
    
    names = df['DBLP Name'].values
    coa = df['Co-Authorship'].values

    # Add nodes
    for i in range(n):
        net.add_node(names[i], label = names[i])
    
    pairs = []
    for i in range(n):
        temp = ast.literal_eval(coa[i])
        for ca in temp:
            if temp[ca] >= p:
                pairs.append([names[i],ca])

    for pair in pairs:
        net.add_edge(pair[0], pair[1])

    return net




