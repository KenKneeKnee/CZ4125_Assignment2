import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import networkx as nx
from pyvis.network import Network

import scse

st.title("SCSE Profile")
st.write(f'Total number of faculty members: **{len(scse.df)}**')

st.header("Intraschool Field Network")
field_container = st.container()
with field_container:
    min_weight = st.slider("Select minimum shared fields:",1,5)
    generate = st.button("Generate graph")
    if generate:
        fg = scse.field_graph(scse.df,min_weight)
        fg.save_graph('graphs/field_graph.html')
        HtmlFile = open('graphs/field_graph.html', 'r', encoding='utf-8')
        components.html(HtmlFile.read(), height=400)

st.header("Publications")
publi_container = st.container()
with publi_container:
    st.subheader("Total publication schoolwide")
    total_publi_df = scse.get_total_publi_df(scse.df)
    st.bar_chart(data=total_publi_df, x='Year', y='Count')

    st.subheader("Publication count by faculty")
    publi_dict = scse.get_sorted_publi_dict(scse.df)
    year = st.slider("Select publication year:", min(publi_dict),max(publi_dict), value = 2000)
    temp_df = pd.DataFrame(publi_dict[year], columns=['Count','Faculty'])
    temp_df = temp_df.truncate(after = 19)
    st.write(
        alt.Chart(temp_df).mark_bar().encode(x=alt.X('Faculty', sort=None),y='Count')
        )
    
st.header("Intraschool Co-Authorship Network")
ca_container = st.container()
with ca_container:
    min_publications = st.slider("Select minimum number of joint publications:",1,100)
    ca = scse.co_author_graph(scse.df,min_publications)
    ca.save_graph('graphs/ca_graph.html')
    HtmlFile = open('graphs/ca_graph.html', 'r', encoding='utf-8')
    components.html(HtmlFile.read(), height=400)


        


