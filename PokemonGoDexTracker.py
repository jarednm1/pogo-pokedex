import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
import json
import re

FilePath = "PokedexFull.json"

# Original Functions
def ReadPokedexIntoMemory():
    with open(FilePath) as file:
        return json.load(file)

def WritePokedexIntoMemory(Pokedex):
    with open(FilePath, 'w') as file:
        json.dump(Pokedex, file, indent=4)

def ValidateDexNumber(Pokedex, num1, num2):
    keys = Pokedex.keys()
    lastEntry = int(max(Pokedex.keys(), key=int))
    return 0 < int(num1) <= lastEntry and 0 < int(num2) <= lastEntry

def ChangeDesiredFlag(Pokedex, Property):
    dex_input = simpledialog.askstring("Input", f"Enter Dex Number(s) for {Property} (e.g., 1 or 1-10):")
    if not dex_input:
        return

    if "-" in dex_input:
        try:
            numbers = re.findall(r'\d+', dex_input)
            start, end = int(numbers[0]), int(numbers[1])
            if not ValidateDexNumber(Pokedex, start, end):
                raise ValueError
            for num in range(start, end + 1):
                Pokedex[str(num)][Property] = True
        except:
            messagebox.showerror("Error", "Invalid range.")
            return
    else:
        if not ValidateDexNumber(Pokedex, dex_input, 1):
            messagebox.showerror("Error", "Invalid Dex number.")
            return
        Pokedex[dex_input][Property] = True

    WritePokedexIntoMemory(Pokedex)
    messagebox.showinfo("Success", f"{Property} updated successfully.")

def HowWouldYouLikeItListed(Pokedex, Property):
    choice = messagebox.askquestion("List by", "List by Name? (No = Dex Number)")
    by_name = (choice == 'yes')

    listed = []
    for dex, props in Pokedex.items():
        if not props[Property] and props["InGame"]:
            listed.append(props["Name"] if by_name else dex)

    show_scrollable_list(f"{Property} Remaining", listed)

def ListPokemonChoice(Pokedex):
    def pick(prop):
        HowWouldYouLikeItListed(Pokedex, prop)
    options = [
        ("Remaining Luckies", "Lucky"),
        ("Remaining Hundos", "Hundo"),
        ("Remaining 3Stars", "3Star"),
        ("Remaining Shinies", "Shiny"),
        ("Remaining XXS", "XXS"),
        ("Remaining XXL", "XXL"),
        ("Remaining Shadow", "Shadow"),
        ("Remaining Purified", "Purified"),
    ]
    window = tk.Toplevel()
    window.title("Remaining Lists")
    for label, prop in options:
        tk.Button(window, text=label, width=30, command=lambda p=prop: pick(p)).pack(pady=2)

def MathQuestionAnswer(Pokedex, Property):
    total, obtained = 0, 0
    for props in Pokedex.values():
        if props["InGame"]:
            total += 1
        if props[Property]:
            obtained += 1
    messagebox.showinfo("Percentage", f"{Property} Pokémon: {obtained}/{total} ({obtained/total:.2%})")

def MathQuestionChoice(Pokedex):
    options = [
        ("Luckies", "Lucky"),
        ("Hundos", "Hundo"),
        ("3Stars", "3Star"),
        ("Shinies", "Shiny")
    ]
    window = tk.Toplevel()
    window.title("Math Breakdown")
    for label, prop in options:
        tk.Button(window, text=label, width=30, command=lambda p=prop: MathQuestionAnswer(Pokedex, p)).pack(pady=2)

def show_scrollable_list(title, items):
    window = tk.Toplevel()
    window.title(title)
    text_area = scrolledtext.ScrolledText(window, width=50, height=20)
    text_area.pack()
    text_area.insert(tk.END, ", ".join(items))

# Main GUI
def main_gui():
    root = tk.Tk()
    root.title("Pokémon Go Dex Tracker")

    def wrapped_change(prop):
        Pokedex = ReadPokedexIntoMemory()
        ChangeDesiredFlag(Pokedex, prop)

    def wrapped_list():
        Pokedex = ReadPokedexIntoMemory()
        ListPokemonChoice(Pokedex)

    def wrapped_math():
        Pokedex = ReadPokedexIntoMemory()
        MathQuestionChoice(Pokedex)

    menu = [
        ("Mark Pokémon as In Game", lambda: wrapped_change("InGame")),
        ("Update Lucky List", lambda: wrapped_change("Lucky")),
        ("Update Hundo List", lambda: wrapped_change("Hundo")),
        ("Update 3 Star List", lambda: wrapped_change("3Star")),
        ("Update Shiny List", lambda: wrapped_change("Shiny")),
        ("Update XXS List", lambda: wrapped_change("XXS")),
        ("Update XXL List", lambda: wrapped_change("XXL")),
        ("Update Shadow List", lambda: wrapped_change("Shadow")),
        ("Update Purified List", lambda: wrapped_change("Purified")),
        ("List Pokémon", wrapped_list),
        ("Math/Percentage Breakdown", wrapped_math),
        ("Exit", root.quit),
    ]

    for label, cmd in menu:
        tk.Button(root, text=label, width=40, command=cmd).pack(pady=4)

    root.mainloop()

if __name__ == "__main__":
    main_gui()