import numpy as np
import streamlit as st
from PIL import Image
st.title("Atv 4: RGB")

# 1 Leitura da foto
st.header("1. Leitura da foto")
col1, col2 = st.columns(2)

foto = Image.open("imagens/foto.png").convert("RGB")
img = np.array(foto)
col1.image(img)
col2.text(img.shape)
col2.text(img[100, 100])

# 2 Canais
st.header("2. Canais")
col1, col2 = st.columns(2)
col1.image(img[:, :, 0], caption="R")
col1.image(img[:, :, 1], caption="G")
col1.image(img[:, :, 2], caption="B")
so_r = img.copy()
so_r[:, :, 1] = 0
so_r[:, :, 2] = 0
col2.image(so_r, caption="só R")
so_g = img.copy()
so_g[:, :, 0] = 0
so_g[:, :, 2] = 0
col2.image(so_g, caption="só G")
so_b = img.copy()
so_b[:, :, 0] = 0
so_b[:, :, 1] = 0
col2.image(so_b, caption="só B")

# 3 Cubo e BGR
st.header("3. Cubo e BGR")
col1, col2 = st.columns(2)
vertices = {
    "preto (0, 0, 0)": (0, 0, 0),
    "branco (255, 255, 255)": (255, 255, 255),
    "amarelo (255, 255, 0)": (255, 255, 0),
    "ciano (0, 255, 255)": (0, 255, 255),
}
for nome, cor in vertices.items():
    col1.image(np.full((60, 60, 3), cor, dtype=np.uint8), caption=nome)
bgr = img[:, :, ::-1]
col2.image(bgr, caption="BGR")

# 4 Tons de cinza
st.header("4. Tons de cinza")
col1, col2 = st.columns(2)
media = img.mean(axis=2).astype(np.uint8)
col1.image(media, caption="média")
ponderada = (0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]).astype(np.uint8)
col2.image(ponderada, caption="média ponderada")
