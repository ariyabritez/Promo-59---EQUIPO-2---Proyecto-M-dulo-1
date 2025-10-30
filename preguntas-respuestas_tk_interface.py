import tkinter as tk
import random

class JuegoGeografia:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Geografía")
        
        titulo = tk.Label(root, text="🌍 EL GRAN JUEGO DE PREGUNTAS Y RESPUESTAS DE GEOGRAFÍA:🌍", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)

        self.preguntas = {
            "¿Qué río pasa por Budapest?": "Danubio",
            "¿Cuántas comunidades autónomas tiene España?": "17",
            "¿Cuál es la ciudad más poblada del mundo?": "Tokio",
            "¿Cuál es el río más largo de España?": "Tajo",
            "¿Dónde está el Taj Mahal?": "India",
            "¿Cuántas lenguas co-oficiales hay en España?": "4",
            "¿En qué continente está el monte Everest?": "Asia"
        }
        self.reset_game()
        
        self.label_estado = tk.Label(root, text="Aciertos: 0  Fallos: 0", font=("Arial", 13))
        self.label_estado.pack(pady=4)
        
        self.label_pregunta = tk.Label(root, text="", font=("Arial",14))
        self.label_pregunta.pack(pady=8)
        
        self.entry_respuesta = tk.Entry(root, font=("Arial", 13))
        self.entry_respuesta.pack(pady=4)
        
        self.btn_enviar = tk.Button(root, text="Responder", font=("Arial", 12), command=self.comprobar_respuesta)
        self.btn_enviar.pack(pady=2)

        self.label_resultado = tk.Label(root, text="", font=("Arial",12))
        self.label_resultado.pack(pady=8)

        self.btn_nueva_partida = tk.Button(root, text="Nueva partida", font=("Arial", 12), command=self.nueva_partida)
        # NO pack aquí

        self.nueva_pregunta()

    def reset_game(self):
        self.preguntas_partida = self.preguntas.copy()
        self.aciertos = 0
        self.fallos = 0

    def nueva_partida(self):
        # FUERZA que se oculte el botón
        self.btn_nueva_partida.pack_forget()
        self.reset_game()
        self.label_resultado.config(text="")
        self.label_estado.config(text=f"Aciertos: {self.aciertos}  Fallos: {self.fallos}")
        self.btn_enviar.config(state="normal")
        self.entry_respuesta.config(state="normal")
        self.nueva_pregunta()

    def nueva_pregunta(self):
        if not self.preguntas_partida:
            self.finalizar_juego()
            return
        self.pregunta, self.respuesta = random.choice(list(self.preguntas_partida.items()))
        self.label_pregunta.config(text=self.pregunta)
        self.entry_respuesta.config(state="normal")
        self.entry_respuesta.delete(0, tk.END)
        self.btn_enviar.config(state="normal")

    def comprobar_respuesta(self):
        respuesta_jugadora = self.entry_respuesta.get().strip().lower()
        correcta = self.respuesta.strip().lower()
        if respuesta_jugadora == correcta:
            self.aciertos += 1
            self.label_resultado.config(text="¡¡👌Correcto!!")
        else:
            self.fallos += 1
            self.label_resultado.config(text=f"¡¡🙈Has fallado!! La respuesta correcta era: {self.respuesta}")

        self.label_estado.config(text=f"Aciertos: {self.aciertos}  Fallos: {self.fallos}")
        self.preguntas_partida.pop(self.pregunta)

        if self.aciertos == 5 or self.fallos == 3:
            self.finalizar_juego()
        else:
            self.nueva_pregunta()

    def finalizar_juego(self):
        self.label_pregunta.config(text="")
        self.entry_respuesta.delete(0, tk.END)
        self.entry_respuesta.config(state="disabled")
        self.btn_enviar.config(state="disabled")
        if self.aciertos == 5:
            self.label_resultado.config(text="¡🥳🎉Has ganado! Eres muy buena en geografía.")
        else:
            self.label_resultado.config(text="¡¡😩👎Eliminada!! Otra vez será...🤷‍♀️")
        print("DEBUG: Mostrando botón 'Nueva partida'")  # Línea para ver salida en consola
        self.btn_nueva_partida.pack(pady=10)
        self.root.update_idletasks()  # Fuerza update visual

# Ejecutar interfaz
if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoGeografia(root)
    root.mainloop()
