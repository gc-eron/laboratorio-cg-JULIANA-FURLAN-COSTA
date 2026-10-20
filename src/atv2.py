import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)


bandeira = np.zeros((12, 18, 3), dtype=np.uint8)
bandeira[1:4, :18] = (0, 0, 0) 
bandeira[4:8, :18] = (255, 0, 0) 
bandeira[8:12, :18] = (250, 200, 0)
st.image(ampliar(bandeira))