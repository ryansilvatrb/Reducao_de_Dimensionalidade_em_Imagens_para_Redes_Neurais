# Redução de Dimensionalidade em Imagens para Redes Neurais

Este projeto foi desenvolvido como parte de um desafio da **DIO (Digital Innovation One)**.  
O objetivo é realizar um pré-processamento de imagens utilizando **bibliotecas do Python**, transformando uma imagem colorida em escala de cinza e depois em binária (preto e branco).  

## 🚀 Tecnologias utilizadas
- [Python 3.13+](https://www.python.org/)
- [OpenCV](https://opencv.org/) (`pip install opencv-python`)
- [Matplotlib](https://matplotlib.org/) (`pip install matplotlib`)

## 📌 Funcionalidades
- Carrega uma imagem colorida (`.png`, `.jpg`, etc.).
- Converte a imagem para **RGB** (correta exibição no Matplotlib).
- Converte para **tons de cinza** (0 a 255).
- Converte para **imagem binária** (preto e branco) usando **threshold**.
- Exibe os três resultados lado a lado:
  1. Imagem original
  2. Imagem em cinza
  3. Imagem binária

## 📷 Exemplo de uso
```bash
python lenas.py
