import streamlit as st
import pandas as pd

def main():
	"""BATALHA DE DADOS"""

	st.title("BATALHA DE DADOS")

	menu = ["Home","Estudante","Professor(a)"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")

	elif choice == "Estudante":
		st.subheader("Seção do Estudante")
		
		if st.sidebar.checkbox("Estudante"):
			st.subheader("Desafio do Estudante")			

	elif choice == "Professor(a)":
		st.subheader("Seção do(a) Professor(a)")

		if st.sidebar.checkbox("Professor(a)"):
			st.subheader("Diário de Classe")			


if __name__ == '__main__':
	main()
