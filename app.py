import streamlit as st
#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("relatorio-sisref-sad - relatorio-sisref-sad.csv")

st.title("Visualização de dados do relatorio so SISREF", anchor=False)
st.write("Tabela", df)

