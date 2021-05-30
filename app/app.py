import streamlit as st
import pandas as pd


def main():
    """BATALHA DE DADOS"""

    st.title("BATALHA DE DADOS")

    menu = ["Home", "Professor(a)"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Professor(a)":
        st.subheader("Seção do(a) Professor(a)")

        if st.sidebar.checkbox("Professor(a)"):
            st.subheader("Diário de Classe")


if __name__ == '__main__':
    main()
