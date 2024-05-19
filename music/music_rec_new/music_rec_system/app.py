import streamlit as st
import pickle
import pandas as pd
import requests
import PIL.Image as Image

def fetch_poster(music_title):
    url = "https://saavn.dev/api/search/songs"

    querystring = {"query":music_title}

    response = requests.get(url, params=querystring)

    data=response.json()
    return data



def recommend(musics):
    music_index = music[music['title'] == musics].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_music = []
    recommended_music_poster = []
    for i in music_list:
        music_title = music.iloc[i[0]].title
        recommended_music.append(music.iloc[i[0]].title)
        recommended_music_poster.append(fetch_poster(music_title))
    return recommended_music, recommended_music_poster


music_dict = pickle.load(open(r'D:\music-\music\music_rec_new\musicrec.pkl', 'rb'))
music = pd.DataFrame(music_dict)

similarity = pickle.load(open(r'D:\music-\music\music_rec_new\similarities.pkl', 'rb'))
st.title('Music Recommendation System')

selected_music_name = st.selectbox('Select a music you like', music['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_music_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        img1=Image.open("D:\\music-\\music\\static\\bg1.jpg")
        st.image(img1)
        
    with col2:
        st.text(names[1])
        img2=Image.open("D:\\music-\\music\\static\\bg2.jpg")
        st.image(img2)        
    with col3:
        
        st.text(names[2])
        img3=Image.open("D:\\music-\\music\\static\\bg3.jpg")
        st.image(img3)         
    with col4:
        
        st.text(names[3])
        img4=Image.open("D:\\music-\\music\static\\bg4.jpg")
        st.image(img4)         
    with col5:
        
        st.text(names[4])
        img5=Image.open("D:\\music-\\music\\static\\OIP.jpeg")
        st.image(img5)        
