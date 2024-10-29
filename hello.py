import streamlit as st
st.write('Hello world')
st.write('Hello space!')
st.slider()

df_reshaped = pd.read_csv('data/us-population-2010-2019-reshaped.csv')

with st.sidebar:
    st.title('🏂 US energy usage Dashboard title')
    
    criteria_list = list(df_reshaped.criteria.unique())[::-1]
    
    selected_criteria = st.selectbox('Select criteria to filter', criteria_list, index=len(criteria_list)-1)
    criteria = df_reshaped[df_reshaped.criteria]
    criteria_sorted = criteria.sort_values(by="population", ascending=False)

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
