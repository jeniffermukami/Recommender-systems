"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import streamlit.components.v1 as components


# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
links = pd.read_csv('movies_link.csv')


# App declaration
def main():
    st.sidebar.image("resources/imgs/tryy.gif")


    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview","EDA","Creator"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Have you ever imagined how Amazon Prime, Netflix, and Google predict your taste in movies so easily? It is no rocket science, that after completing one movie/series you loved, and rated it on these platforms, a few more adds up to the suggested or ‘You May Like this ‘ section in seconds! It is Machine Learning. A recommendation system predicts and filters user preferences after learning about the user’s past choices. As simple as that!")


        st.markdown("<h2 style='text-align: center; color: white;'>Content Based Filtering</h2>", unsafe_allow_html=True)
        st.write("")
        col1, col2 = st.columns(2)
        with col1:
            st.image('resources/imgs/content based filtering.png',use_column_width=True)
        with col2:
            st.write('')
            st.markdown("<p style='text-align: center; color: white;'>Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback.:</p>", unsafe_allow_html=True)
        
        st.markdown("<h2 style='text-align: center; color: white;'>Collaborative Filtering</h2>", unsafe_allow_html=True)
        st.write("")
        col1, col2 = st.columns(2)
        with col1:
            st.image('resources/imgs/collaborative filtering 2.png')
        with col2:
            st.markdown("<p style='text-align: center; color: white;'>Collaborative filtering uses algorithms to filter data from user reviews to make personalized recommendations for users with similar preferences. This is the hallmark for Recommender Systems, Giving greater insights into what users/customers are interested</p>", unsafe_allow_html=True)
    
    if page_selection == "Creator":
        st.markdown("<h1 style='text-align: center; color: white;'>Creator</h1>", unsafe_allow_html=True)
        st.image('resources/imgs/jenny2.jpeg',use_column_width=True)
        st.markdown("<h2 style='text-align: center; color: white;'>Contact Info</h2>", unsafe_allow_html=True)
        col = st.columns(1)
    
        st.markdown("<p style='text-align: center; color: white;'>Jeniffer Mariga</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: white;'>mukamijeniffer6@gmail.com</p>", unsafe_allow_html=True)

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
