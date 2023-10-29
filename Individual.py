import streamlit as st
import pandas as pd
import faculty
 
st.header("Faculty Profile")
faculty_name = st.selectbox("Choose a faculty member:",faculty.faculty_names)

######################## Main Section ########################
st.write(f'DR-NTU link: {faculty.get_drntu(faculty_name,faculty.df)}')
st.write(f'DBLP link: {faculty.get_dblp(faculty_name,faculty.df)}')

#st.divider()
st.subheader(f'About Prof {faculty_name}')
st.write(faculty.get_bio(faculty_name,faculty.df))
st.divider()

######################## Extras Section ########################
field_col, aff_col = st.columns(2)
field = faculty.get_field(faculty_name,faculty.df)
if field:
    with field_col:
        st.subheader("Fields")
        for f in field: st.write(f)

research_interest = faculty.get_research_interest(faculty_name,faculty.df)
if research_interest:
    interest_col = st.expander("Reaserch Interests")
    with interest_col:
        for i in research_interest: st.write(i)

aff = faculty.get_affiliation(faculty_name,faculty.df)
if aff:
    with aff_col:
        st.subheader("Affiliated Instituitions")
        for a in aff: st.write(a)
st.divider()

######################## Publications Section ########################
st.subheader("Publications")
publication_df = faculty.get_publication_df(faculty_name,faculty.df)
st.write(f"Total number of publications: **{sum(publication_df['Count'].values)}** ")
st.bar_chart(data=publication_df, x='Year', y='Count')
st.divider()

######################## Co-authors Section ########################
st.subheader("Co-Authors within SCSE")
ca_dict = faculty.get_coauthor(faculty_name,faculty.df)
st.write(f'Total number of Co-Authors: **{len(ca_dict)}**')
ca_col = st.expander("List of Co-Authors and publication counts")
with ca_col:
    for k,v in ca_dict.items(): st.write(f'{k}: **{v}**')







