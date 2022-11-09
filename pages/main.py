import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import plost

st.set_page_config(page_title="MSMT", page_icon=":bar_chart:", layout="wide")

@st.cache
def get_data_from_excel():
    df = pd.read_csv('data.csv')
    return df
def get_data_from_excel2():
    df2 = pd.read_csv('dataset.csv')
    return df2

df = get_data_from_excel()

# ---- SIDEBAR ----
region = st.sidebar.selectbox(
    'Select a Region',
    options=df["Region"].unique()
)
st.sidebar.write('You selected:', region)

# ------END SIDEBAR --------
df_selection = df.query(
    "Region == @region"
)

# ---- MAINPAGE ----
st.title(":bar_chart: MSMT")
st.markdown("##")

prevalence = (df_selection["Prevalence"].sum())
analyzed = int(df_selection["samples analyzed"].sum())
positives = int(df_selection["number of positives"].sum())

left_column, middle_column, right_column = st.columns(3)

percentage = 100
with left_column:
    st.subheader(" # of Positives:")
    st.subheader(positives)
with middle_column:
    st.subheader("Samples Analyzed:")
    st.subheader(analyzed)
with right_column:
    st.subheader("Prevalence:")
    st.subheader(prevalence)

st.markdown("""---""")

# SALES BY PRODUCT LINE [BAR CHART]
   