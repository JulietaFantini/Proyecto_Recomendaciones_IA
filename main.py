
import streamlit as st
from pantallas.pantalla_1 import pantalla_1
from pantallas.pantalla_2 import pantalla_2
from pantallas.pantalla_3 import pantalla_3

def main():
    if "pantalla_actual" not in st.session_state:
        st.session_state["pantalla_actual"] = "pantalla_1"

    def cambiar_pantalla(nueva_pantalla):
        st.session_state["pantalla_actual"] = nueva_pantalla

    pantalla_actual = st.session_state["pantalla_actual"]

    if pantalla_actual == "pantalla_1":
        pantalla_1(cambiar_pantalla)
    elif pantalla_actual == "pantalla_2":
        pantalla_2(cambiar_pantalla)
    elif pantalla_actual == "pantalla_3":
        pantalla_3(cambiar_pantalla)

if __name__ == "__main__":
    main()
