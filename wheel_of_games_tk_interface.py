import tkinter as tk
import random

JUEGOS = [
    ("Piedra, papel o tijera🪨🗞️✂️", "Tami"),
    ("Ahorcado☠️", "Fabi y Julia"),
    ("Preguntas y respuestas❓💡", "Ruth")
]
BONUS = ("Tic tac toe❌⭕", "Galia")

class RuletaJuegos:
    def __init__(self, root):
        self.root = root
        self.root.title("Ruleta DEMO - Proyecto Juegos")
        self.usados = []

        self.titulo = tk.Label(root, text="¡RULETA DEMO! ¿Qué juego vamos a presentar?", font=("Arial", 16, "bold"))
        self.titulo.pack(pady=20)

        self.lbl_resultado = tk.Label(root, text="", font=("Arial", 14))
        self.lbl_resultado.pack(pady=20)

        self.btn_girar = tk.Button(root, text="Tirar Ruleta", font=("Arial", 14), command=self.girar_ruleta)
        self.btn_girar.pack(pady=10)

        self.lbl_bonus = tk.Label(root, text="", font=("Arial", 14, "bold"))
        self.lbl_bonus.pack(pady=20)

    def girar_ruleta(self):
        restantes = [j for j in JUEGOS if j not in self.usados]
        if restantes:
            elegido = random.choice(restantes)
            self.usados.append(elegido)
            self.lbl_resultado.config(
                text=f"► Os presentamos nuestra versión del juego\n\n{elegido[0]} presentado por {elegido[1]}"
            )
            self.lbl_bonus.config(text="")
            if len(self.usados) == len(JUEGOS):
                self.btn_girar.config(text="Descubre el BONUS 🎁")
        else:
            self.lbl_resultado.config(text="")
            self.lbl_bonus.config(
                text=f"🟣 BONUS: ¡Y de regalo...🎁!\n{BONUS[0]} presentado por {BONUS[1]}"
            )
            self.btn_girar.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = RuletaJuegos(root)
    root.mainloop()