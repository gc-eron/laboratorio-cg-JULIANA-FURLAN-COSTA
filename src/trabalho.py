import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

foto = Image.open("imagens/foto.png").convert("RGB")
img = np.array(foto)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
altura, largura = img.shape[0], img.shape[1]


# 3. Matiz girada
st.header("3. Matiz girada")
col1, col2 = st.columns(2, vertical_alignment="bottom")

giro = col1.slider("Giro (graus)", 0, 360, 120)
h = hsv[:, :, 0].astype(int)
h = (h + giro // 2) % 180
hsv_h = hsv.copy()
hsv_h[:, :, 0] = h
col1.image(img, caption="Original")
col2.image(cv2.cvtColor(hsv_h, cv2.COLOR_HSV2RGB), caption="Matiz")


# 8. Negativo
st.header("8. Negativo")
col1, col2 = st.columns(2)

negativo = 255 - img
col1.image(img, caption="Original")
col2.image(negativo, caption="Negativo")


# 10. Negativo numa região
st.header("10. Negativo numa região")
col1, col2 = st.columns(2, vertical_alignment="bottom")

y = col1.slider("y", 0, altura - 1, altura // 4)
x = col1.slider("x", 0, largura - 1, largura // 4)
t = col1.slider("tamanho", 10, largura, largura // 3)
neg_regiao = img.copy()
neg_regiao[y:y + t, x:x + t] = 255 - neg_regiao[y:y + t, x:x + t]
col2.image(neg_regiao, caption="Negativo na região")


# 11. Espelhamento
st.header("11. Espelhamento")
col1, col2 = st.columns(2)

col1.image(img[:, ::-1], caption="Horizontal")
col2.image(img[::-1, :], caption="Vertical")


# 12. Simetria
st.header("12. Simetria")
col1, col2 = st.columns(2)

meio = largura // 2
simetria = img.copy()
esquerda = img[:, :meio]
simetria[:, largura - meio:] = esquerda[:, ::-1]
col1.image(img, caption="Original")
col2.image(simetria, caption="Simetria")


# 16. Granulado
st.header("16. Granulado")
col1, col2 = st.columns(2, vertical_alignment="bottom")

intensidade = col1.slider("Intensidade", 0, 150, 50)
ruido = np.random.randint(-intensidade, intensidade + 1, img.shape)
granulado = img.astype(int) + ruido
granulado = np.clip(granulado, 0, 255).astype(np.uint8)
col1.image(img, caption="Original")
col2.image(granulado, caption="Granulado")
