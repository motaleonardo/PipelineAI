import streamlit as st
from datetime import datetime, time
from dataContract import Vendas
from pydantic import ValidationError


def main ():
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
    email = st.text_input("Campo de texto para inserção do e-mail do vendedor")
    data = st.date_input("Campo para selecionar a data em que a venda foi realizada",format="DD/MM/YYYY")
    hora = st.time_input("Campo para selecionar a hora em que a venda foi realizada", value=time(9, 0))
    valor = st.number_input("Campo numérico para inserir o valor monetário da venda realizada", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Campo numérico para inserir a quantidade de produtos vendidos", min_value=1, step=1)
    produto = st.selectbox("Campo de seleção para escolher o produto vendido",options=["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama 3.0"])

    if st.button("Enviar"):

        try:
            data_hora = datetime.combine(data, hora)
            venda = Vendas(
                email = email, 
                data = data_hora, 
                valor = valor, 
                quantidade = quantidade,
                produto = produto
            )
            st.write(venda)
        except ValidationError as e:
            st.error(f"Deu erro {e}")



if __name__=="__main__":
    main()