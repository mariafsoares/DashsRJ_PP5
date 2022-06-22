import streamlit as st
import pandas as pd
from PIL import Image

DATA_URL = ("./PP5_streamlit_data.xlsx")

st.set_page_config(page_title="VOAs PP5",
                   layout="centered",
                   initial_sidebar_state="auto")

# External CSS
main_external_css = """
        <style>
            .sidebar.sidebar-content{
            background-image: linear-gradient(#0E1117,#0E1117);
            color: #0E1117}
        </style>"""
st.markdown(main_external_css, unsafe_allow_html=True)

icon = Image.open("./Imagem2.png") #braskem_logo
st.sidebar.image(icon, use_column_width=True,) #caption="VOAs Entregues"

st.title("ANALISADORES VIRTUAIS PP5 📈")
st.sidebar.title("PRODUTOS APTOS PARA UTILIZAÇÃO")

values = {'IF EXT': ['X','X','X','X','X','-','-','-','-'],
          'IF RCT': ['-','-','-','X','-','X','X','-','-'],
              'XO': ['-','X','X','X','-','X','-','X','X']}

df_aux = pd.DataFrame(data=values)
df_aux.index = ['H 125','H 201','HP 550R','PD943XP','RP 340R','PH 0952','RP 225M','H 301','H 503']
st.table(df_aux)

@st.cache(persist=True)
def load_data():
    data = pd.read_excel(DATA_URL)
    return data

data = load_data()

#st.dataframe(data)

select = st.sidebar.selectbox('LINHA DE PRODUÇÃO', ['PP5'], key='1')
st.markdown("#### Dashboard de Acompanhamento dos Modelos entregues por Produto")

if select == 'PP5':    
    st.write("## PP5")
    df = data.loc[data['LINHA']=='PP5']

    select_pr = st.sidebar.selectbox('PROCESSO', ['REAÇÃO','EXTRUSÃO'], key='1')

    if select_pr == 'REAÇÃO':
        df = df.loc[df['PROCESSO']=='REAÇÃO']
        select_ana = st.sidebar.selectbox('ANÁLISE', ['ÍNDICE DE FLUIDEZ','SOLÚVEIS EM XILENO'], key='1')

        if select_ana == 'SOLÚVEIS EM XILENO':
            df = df.loc[df['ANÁLISE']=='SOLÚVEIS EM XILENO', 'PRODUTO'].reset_index().drop(columns=['index'])
            st.subheader("PRODUTOS ENTREGUES PARA SOLÚVEIS EM XILENO REAÇÃO 👇 ")
            st.table(df)

        else:
            df = df.loc[df['ANÁLISE']=='ÍNDICE DE FLUIDEZ', 'PRODUTO'].reset_index().drop(columns=['index'])    
            st.subheader("PRODUTOS ENTREGUES PARA IF REAÇÃO 👇 ")
            st.table(df)
    else:
        df = df.loc[df['PROCESSO']=='EXTRUSÃO']
        select_ana = st.sidebar.selectbox('ANÁLISE', ['ÍNDICE DE FLUIDEZ','SOLÚVEIS EM XILENO'], key='1')

        #if select_ana == 'DENSIDADE':
        #    df = df.loc[df['ANÁLISE']=='DENSIDADE', 'PRODUTO'].reset_index().drop(columns=['index'])
        #    st.subheader("PRODUTOS ENTREGUES PARA DENSIDADE EXTRUSÃO 👇 ")
        #    st.table(df)

        if select_ana == 'ÍNDICE DE FLUIDEZ':
            df = df.loc[df['ANÁLISE']=='ÍNDICE DE FLUIDEZ', 'PRODUTO'].reset_index().drop(columns=['index'])    
            st.subheader("PRODUTOS ENTREGUES PARA IF EXTRUSÃO 👇 ")
            st.table(df)

        else:
            st.write('Não há analisadores para Solúveis em Xileno Extrusão.')                
