import streamlit as st
import PokemonGoDexTracker as pdk

def main():
    # Load data once and pass it around instead of loading every time a function is called
    Pokedex = pdk.ReadPokedexIntoMemory()
    
    st.title('Pokemon Go Dex Tracker')
    choice = st.sidebar.selectbox("Select an option", ["Update Flags", "List Pokemon", "Math/Percentage Breakdown"])

    if choice == "Update Flags":
        update_flags(Pokedex)
    elif choice == "List Pokemon":
        list_pokemon(Pokedex)
    elif choice == "Math/Percentage Breakdown":
        math_question(Pokedex)

def update_flags(Pokedex):
    # Implement the updating logic here using Streamlit components like sliders, text inputs etc.
    pass

def list_pokemon(Pokedex):
    # Implement listing functionality with Streamlit UI elements
    pass

def math_question(Pokedex):
    # Implement Math/Percentage calculation with Streamlit UI components
    pass

if __name__ == "__main__":
    main()
