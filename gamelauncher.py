import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import json

class GameLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Launcher")
        self.root.geometry("400x300")

        # Lista di giochi e file di salvataggio
        self.games_file = "games.json"
        self.games = []

        # Area di input per il percorso del gioco
        self.game_path_var = tk.StringVar()
        tk.Entry(root, textvariable=self.game_path_var, width=40).pack(pady=10)

        # Bottone per aggiungere gioco
        tk.Button(root, text="Aggiungi Gioco", command=self.add_game).pack(pady=5)

        # Lista di bottoni per i giochi
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)

        # Carica i giochi salvati
        self.load_games()

    def add_game(self):
        game_path = self.game_path_var.get()
        if game_path and os.path.exists(game_path):
            self.games.append(game_path)
            self.create_game_button(game_path)
            self.save_games()
            self.game_path_var.set("")
        else:
            messagebox.showerror("Errore", "Percorso del gioco non valido!")

    def create_game_button(self, game_path):
        game_name = os.path.basename(game_path)
        button = tk.Button(self.buttons_frame, text=game_name, command=lambda: self.launch_game(game_path))
        button.pack(fill="x", pady=2)

    def launch_game(self, game_path):
        try:
            subprocess.Popen([game_path])
        except Exception as e:
            messagebox.showerror("Errore", f"Impossibile aprire il gioco:\n{e}")

    def save_games(self):
        # Salva i giochi in un file JSON
        with open(self.games_file, 'w') as file:
            json.dump(self.games, file)

    def load_games(self):
        # Carica i giochi dal file JSON
        if os.path.exists(self.games_file):
            with open(self.games_file, 'r') as file:
                self.games = json.load(file)
                for game_path in self.games:
                    self.create_game_button(game_path)

# Esegui l'applicazione
root = tk.Tk()
app = GameLauncher(root)
root.mainloop()
