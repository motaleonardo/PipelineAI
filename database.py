import psycopg2
from psycopg2 import sql
from dataContract import Vendas
import streamlit as st
from dotenv import load_dotenv
import os

#Carregar Variaveis do Arquivo .env
load_dotenv()

#Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

#Função para salvar os dados validados no PostgreSQL


