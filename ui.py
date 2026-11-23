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
    st.sidebar.title("Update Flags")
    Property = st.sidebar.selectbox("What flag would you like to change?", ["InGame", "Lucky", "Hundo", "3Star", "Shiny", "XXS", "XXL", "Shadow", "Purified"])
    
    PokemonDexNumber = st.sidebar.text_input("Please provide the Pokémon Dex number(s) (e.g., 1 or 1-100):")
    
    if "-" in PokemonDexNumber:
        numbers = list(map(int, PokemonDexNumber.split('-')))
        isValidNumber = pdk.ValidateDexNumber(Pokedex, numbers[0], numbers[1])
    else:
        isValidNumber = pdk.ValidateDexNumber(Pokedex, int(PokemonDexNumber), 1)
    
    if isValidNumber and st.sidebar.button("Update"):
        if "-" in PokemonDexNumber:
            for num in range(numbers[0], numbers[1] + 1):
                Pokedex[str(num)][Property] = True
        else:
            Pokedex[PokemonDexNumber][Property] = True
        
        pdk.WritePokedexIntoMemory(Pokedex)
        st.sidebar.success("Changes have been saved.")
    elif not isValidNumber and st.sidebar.button("Update"):
        st.sidebar.error("Invalid number provided.")

def list_pokemon(Pokedex):
    st.sidebar.title("List Pokemon")
    Property = st.sidebar.selectbox("Which list would you like to see?", ["Lucky", "Hundo", "3Star", "Shiny", "XXS", "XXL", "Shadow", "Purified"])
    
    display_by = st.sidebar.radio("Display by:", ("Name", "Dex Number"))
    
    if display_by == "Name":
        for pokemon_dex, properties in Pokedex.items():
            if not properties[Property] and properties['InGame']:
                st.write(properties['Name'])
    else:
        for pokemon_dex, properties in Pokedex.items():
            if not properties[Property] and properties['InGame']:
                st.write(pokemon_dex)

def math_question(Pokedex):
    st.sidebar.title("Math/Percentage Breakdown")
    Property = st.sidebar.selectbox("Which percentage would you like to see?", ["Lucky", "Hundo", "3Star", "Shiny"])
    
    NumPokemonAvail = 0
    NumOfPokemon = 0
    
    for pokemon_dex, properties in Pokedex.items():
        if properties["InGame"]:
            NumPokemonAvail += 1
        if properties[Property]:
            NumOfPokemon += 1
    
    percentage = (NumOfPokemon / NumPokemonAvail) * 100 if NumPokemonAvail > 0 else 0
    st.sidebar.write(f"Number of {Property} Pokemon: {NumOfPokemon}/{NumPokemonAvail} ({percentage:.2f}%)")

if __name__ == "__main__":
    main()
