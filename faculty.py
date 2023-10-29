# Backend file for Individual Page
import pandas as pd
import ast

df = pd.read_csv("Processed_4.csv")
faculty_names = df["Full Name"].values

# Get Functions
def get_email(name,df):
    row = df.loc[df['Full Name'] == name]
    return row['Email'].values[0]

def get_drntu(name,df):
    row = df.loc[df['Full Name'] == name]
    return row['DR-NTU URL'].values[0]

def get_dblp(name,df):
    row = df.loc[df['Full Name'] == name]
    return row['DBLP URL'].values[0]

def get_bio(name,df):
    row = df.loc[df['Full Name'] == name]
    return row['Biography'].values[0]

def get_field(name,df):
    row = df.loc[df['Full Name'] == name]
    string = row['Fields'].values[0]
    return ast.literal_eval(string)

def get_research_interest(name,df):
    row = df.loc[df['Full Name'] == name]
    string = row['Research Interest'].values[0]
    return ast.literal_eval(string)

def get_affiliation(name,df):
    row = df.loc[df['Full Name'] == name]
    string = row['Affiliations'].values[0]
    return ast.literal_eval(string)

def get_coauthor(name,df):
    row = df.loc[df['Full Name'] == name]
    string = row['Co-Authorship'].values[0]
    ca = ast.literal_eval(string)
    return dict(sorted(ca.items(), key=lambda x: -x[1]))



# Return a Pandas Dataframe so that Streamlit can plot
def get_publication_df(name,df):
    row = df.loc[df['Full Name'] == name]
    publi = ast.literal_eval(row['Publication Counts'].values[0])
    years = []
    counts = []
    for k,v in publi.items():
        years.append(k)
        counts.append(v)
    years.reverse()
    counts.reverse()
    rdf = pd.DataFrame(list(zip(years, counts)),
               columns =['Year', 'Count'])
    return rdf

    




