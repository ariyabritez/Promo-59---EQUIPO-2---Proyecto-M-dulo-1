import tkinter as tk
import random

# Preguntas y respuestas
preguntas = {
    "¿Qué río pasa por Budapest?": "Danubio",
    "¿Cuántas comunidades autónomas tiene España?": "17",
    "¿Cuál es la ciudad más poblada del mundo?": "Tokio",
    "¿Cuál es el río más largo de España?": "Tajo",
    "¿Dónde está el Taj Mahal?": "India",
    "¿Cuántas lenguas co-oficiales hay en España?": "4",
    "¿En qué continente está el monte Everest?": "Asia"
}

# Convertir a lista
preguntas_restantes = list(preguntas.items())

# Variables de juego
aciertos = 0
fallos = 0

# Lógica principal
def siguiente_pregunta():
    global pregunta_actual, respuesta_correcta
    if aciertos < 5 and fallos < 3 and preguntas_restantes:
        pregunta_actual, respuesta_correcta = random.choice(preguntas_restantes)
        preguntas_restantes.remove((pregunta_actual, respuesta_correcta))
        lbl_pregunta.config(text=pregunta_actual)
        entry_respuesta.delete(0, tk.END)
        lbl_resultado.config(text="")
        lbl_estado.config(text=f"Aciertos: {aciertos}  Fallos: {fallos}")
    else:
        finalizar_juego()

def comprobar_respuesta():
    global aciertos, fallos
    respuesta_jugadora = entry_respuesta.get().strip().lower()
    if respuesta_jugadora == respuesta_correcta.strip().lower():
        aciertos += 1
        lbl_resultado.config(text="¡¡👌Correcto!!")
    else:
        fallos += 1
        lbl_resultado.config(text=f"¡¡🙈Has fallado!! La respuesta correcta era: {respuesta_correcta}")
    lbl_estado.config(text=f"Aciertos: {aciertos}  Fallos: {fallos}")
    root.after(1200, siguiente_pregunta)  # Espera 1.2 seg, luego sigue

def finalizar_juego():
    lbl_pregunta.config(text="")
    entry_respuesta.config(state='disabled')
    btn_responder.config(state='disabled')
    if aciertos == 5:
        lbl_resultado.config(text="¡🥳🎉Has ganado! Eres muy buena en geografía.")
    else:
        lbl_resultado.config(text="¡¡😩👎Eliminada!! Inténtalo de nuevo.")

# Interfaz principal
root = tk.Tk()
root.title("Juego de Geografía")

lbl_titulo = tk.Label(root, text="🌍EL GRAN JUEGO DE PREGUNTAS Y RESPUESTAS DE GEOGRAFÍA:🌍", font=("Arial", 14))
lbl_titulo.pack(pady=10)

lbl_estado = tk.Label(root, text=f"Aciertos: {aciertos}  Fallos: {fallos}", font=("Arial", 12))
lbl_estado.pack()

lbl_pregunta = tk.Label(root, text="", font=("Arial", 12), wraplength=400)
lbl_pregunta.pack(pady=10)

entry_respuesta = tk.Entry(root, font=("Arial", 12))
entry_respuesta.pack(pady=5)

btn_responder = tk.Button(root, text="Responder", font=("Arial", 12), command=comprobar_respuesta)
btn_responder.pack(pady=5)

lbl_resultado = tk.Label(root, text="", font=("Arial", 12))
lbl_resultado.pack(pady=10)

siguiente_pregunta()

root.mainloop()