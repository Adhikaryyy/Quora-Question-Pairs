import streamlit as st
import pickle
import helper



model=pickle.load(open('duplicate_q_pairs_model.pkl','rb'))


st.header('Quora Duplicate Question Pairs')
q1=st.text_input('Enter question 1')
q2=st.text_input('Enter question 2')

if st.button('click me'):
    query=helper.query_point_creator(q1,q2)
    result=model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')


