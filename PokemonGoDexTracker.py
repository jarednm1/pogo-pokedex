import re
import ast
import json
import time

# Globals
FilePath = "PokedexFull.json"

# Data Storage
def ReadPokedexIntoMemory():
    with open(FilePath) as file:
        Pokedex = json.load(file)
    return Pokedex

def WritePokedexIntoMemory(Pokedex):
    with open(FilePath, 'w') as file:
        # Indent maintains readability
        json.dump(Pokedex, file, indent=4)
    print("Changes have been saved")
    print("=========================================================")
    print(" ")

# General Manipulation Function
def ChangeDesiredFlag(Pokedex, Property):

    print(f"You are changing {Property}")
    print("What Pokemon Has Been Updated?")
    # Note: this is a string
    print("Ranges Accepted In The Following Format: 1-100")
    PokemonDexNumber = input("Please Provide The Pokemon Dex Number(s):")

    keys = Pokedex.keys()
    lastEntry = max(Pokedex.keys(), key=int)

    if(PokemonDexNumber > lastEntry or PokemonDexNumber <= "0"):
        print("Number Provided Does Not Exist")
    else:
        if ("-" in PokemonDexNumber):
            numbers = re.findall(r'\d+', PokemonDexNumber)
            beginingDexNumber = int(numbers[0])
            endDexNumber = int(numbers[1])

            if(beginingDexNumber > lastEntry or beginingDexNumber < "0" or endDexNumber > lastEntry or endDexNumber < "0"):
                print("Number(s) Provided Does Not Exist")
            else:            
                for num in range(beginingDexNumber, endDexNumber + 1):
                    Pokedex[str(num)][Property] = True
        else:
            Pokedex[PokemonDexNumber][Property] = True

        WritePokedexIntoMemory(Pokedex)

def ListPokemonChoice(Pokedex):
    print("What Remaining List Would You Like?")
    print("1. Remaining Luckies")
    print("2. Remaining Hundos")
    print("3. Remaining 3Stars")
    print("4. Remaining Shinies")
    print(" ")
    print("Provide The Number Associated With Your Choice")

    PromptChoice = input("Choice: ")

    if(PromptChoice == "1"):
        ListRemainingPokemon(Pokedex, "Lucky")
    elif(PromptChoice == "2"):
        ListRemainingPokemon(Pokedex, "Hundo")
    elif(PromptChoice == "3"):
        ListRemainingPokemon(Pokedex, "3Star")
    elif(PromptChoice == "4"):
        ListRemainingPokemon(Pokedex, "Shiny")
    else:
        print("Farewell")

def ListRemainingPokemon(Pokedex, Property):
    ListOfPokemon = ""
    for PokemonDexNumber, PokedexProperties in Pokedex.items():
        if(PokedexProperties[Property] == False and PokedexProperties['InGame'] == True):
            ListOfPokemon = ListOfPokemon + PokedexProperties['Name'] +", "
            #Another Option..
            #print(f"{PokedexProperties['Name']}, ")
    
    print(ListOfPokemon)
    print("=========================================================")
    print(" ")
    
def MathQuestionChoice(Pokedex):
    print("What Percentage Would you like to see")
    print("1. Luckies Obtained")
    print("2. Hundos Obtained")
    print("3. 3Stars Obtained")
    print("4. Shinies Obtained")
    print(" ")
    print("Provide The Number Associated With Your Choice")

    PromptChoice = input("Choice: ")

    if(PromptChoice == "1"):
        MathQuestionAnswer(Pokedex, "Lucky")
    elif(PromptChoice == "2"):
        MathQuestionAnswer(Pokedex, "Hundo")
    elif(PromptChoice == "3"):
        MathQuestionAnswer(Pokedex, "3Star")
    elif(PromptChoice == "4"):
        MathQuestionAnswer(Pokedex, "Shiny")
    else:
        print("Farewell")

def MathQuestionAnswer(Pokedex, Property):
    NumPokemonAvail = 0
    NumOfPokemon = 0
    for PokemonDexNumber, PokedexProperties in Pokedex.items():
        if(PokedexProperties["InGame"] == True):
            #ListOfPokemon = ListOfPokemon + PokedexProperties['Name'] +", "
            #Another Option..
            #print(f"{PokedexProperties['Name']}, ")
            NumPokemonAvail = NumPokemonAvail + 1

        if(PokedexProperties[Property] == True):
            #ListOfPokemon = ListOfPokemon + PokedexProperties['Name'] +", "
            #Another Option..
            #print(f"{PokedexProperties['Name']}, ")
            NumOfPokemon = NumOfPokemon + 1
    
    print(f"Number of {Property} Pokemon {NumOfPokemon}/{NumPokemonAvail}")
    print("=========================================================")
    print(" ")
    return

# Main 
try:
    while(True):
        # Load Data
        Pokedex = ReadPokedexIntoMemory()

        print(" ")
        print("What Would You Like To Do?")
        print("1. Pokemon Added To Game")
        print("2. Update Lucky List")
        print("3. Update Hundo List")
        print("4. Update 3 Star List")
        print("5. Update Shiny List")
        print("6. List Pokemon")
        print("7. Math/Precentage Breakdown")
        print("8. End Program")
        print(" ")
        print("Provide The Number Associated With Your Choice")
        PromptChoice = input("Choice: ")

        if(PromptChoice == "1"):
            ChangeDesiredFlag(Pokedex, "InGame")
        elif(PromptChoice == "2"):
            ChangeDesiredFlag(Pokedex, "Lucky")
        elif(PromptChoice == "3"):
            ChangeDesiredFlag(Pokedex, "Hundo")
        elif(PromptChoice == "4"):
            ChangeDesiredFlag(Pokedex, "3Star")
        elif(PromptChoice == "5"):
            ChangeDesiredFlag(Pokedex, "Lucky")
        elif(PromptChoice == "6"):
            ListPokemonChoice(Pokedex)
        elif(PromptChoice == "7"):
            MathQuestionChoice(Pokedex)
        else:
            print("Farewell")
            break

except:
    #print("BLEW UP LOL")
    throw