import tkinter as tk
from tkinter import ttk
import pygame
import math

QUESTIONS = [
    "1.    What technology is used to record cryptocurrency transactions?",
    "2.    What tool would you use to reduce the digital image size?",
    "3.    Which computer language is most widely used?",
    "4.    Who was the first emperor of Rome?",
    "5.    Which year was the Declaration of Independence signed?",
    "6.    The United States bought Alaska from which country?",
    "7.    Who was the first woman to make a million dollars in the United States?",
    "8.    What old disease was also known as the ‘Black Death’?",
    "9.    Which 2 languages were featured on the Rosetta Stone?",
    "10.   What is the capital of Australia?",
    "11.   What city is the Oriental Peral Tower located in?",
    "12.   What is the capital of Zimbabwe?",
    "13.   What is the tallest mountain in the world counting underwater?",
    "14.   How many countries have a capital name that is the same as their country?",
    "15.   Which country holds Mount Everest?",
    "16.   Which of the following is directly produced during photosynthesis in plants?",
    "17.   What is the element name for Uranium?",
    "18.   How many types of black holes have we discovered?",
    "19.   What's at the bottom of the ocean?",
    "20.   When is the next time we think the planets will align?",
    "21.   What is the rarest blood type?",
    "22.   Who won the Fifa World Cup in 2018?",
    "23.   Which tennis players won Roland Garros in Paris for the 2024 men and women?",
    "24.   How many holes do you play in the average round of golf?",
    "25.   Which team has won the most Premier League titles?",
    "26.   What shape is a modern-day soccer ball?",
    "27.   What is the only team that has gone undefeated in Premier League?",
    "28.   Who is the character used by Nintendo as a mascot?",
    "29.   How old was Harry Potter when he entered Hogwarts?",
    "30.   What alter ego is Bruce Wayne best known for?",
    "31.   How many lines do you have to make in the Tetris game to do Tetris?",
    "32.   What is Ash's pokemon that has never entered a pokeball?",
    "33.   Which of these titles does not correspond to an Adele album title?"
]
OPTIONS = [
    ["Digital wallet", "Mining", "Blockchain"],
    ["Filter", "Crop", "Rotate"],
    ["C//", "Python", "Javascript"],
    ["Augustus", "Julius Ceaser", "Caligula"],
    ["1783", "1744", "1776"],
    ["Russia", "Canada", "Mexico"],
    ["Neerja Sethi", "Madam C.J. Walker", "Alice Walton"],
    ["Tuberculosis", "Bubonic Plague", "Yellow Fever"],
    ["Arabic, Egyptian", "English, Egyptian", "Greek, Egyptian"],
    ["Sydney", "Melbourne", "Canberra"],
    ["Paris", "Shanghai", "Tokyo"],
    ["Harare", "Preoria", "Rabat"],
    ["Mount Everest", "K2", "Mauna Kea"],
    ["11", "6", "15"],
    ["Bhutan, India", "Himalaya, Bangladesh", "Nepal, China"],
    ["Glucose and Oxygen", "Carbon Dioxide and Water", "ATP and Lactic Acid"],
    ["Un", "U", "Um"],
    ["4", "5", "8"],
    ["Crustaceans", "Sand", "Sharks"],
    ["2034", "2028", "2041"],
    ["AB+", "O-", "AB-"],
    ["Argentina", "France", "United Kingdom"],
    ["Alcaraz and Swiatek", "Sabalenka and Sinner", "Paolini and Djokovic"],
    ["9", "29", "18"],
    ["Arsenal", "Manchester United", "Liverpool"],
    ["Sphere", "Truncated Icosahedron", "Prolate Spheroid"],
    ["Liverpool", "Manchester United", "Arsenal"],
    ["Mario", "Sonic", "Zelda"],
    ["10", "11", "13"],
    ["Batman", "Superman", "Dwayne Johnson"],
    ["4", "9", "17"],
    ["Pikachu", "Greninja", "Noctowl"],
    ["21", "23", "25"]
]
ANSWERS = [
    3, 2, 3, 1, 3, 1, 2, 2, 3, 3, 2, 1, 3, 1, 3,
    1, 2, 1, 1, 2, 3, 2, 1, 3, 2, 2, 3, 1, 2, 1,
    1, 1, 2
]

TOTAL_QS = len(QUESTIONS)
XP_PER_CORRECT = 10

pygame.mixer.init()
pygame.mixer.music.load("chess.mp3")
pygame.mixer.music.play()

root = tk.Tk()
root.title("Trivia Time with EXP")
root.configure(bg="Aquamarine")
root.geometry("800x500")              

welcome = tk.Label(
    root, text="Welcome to Trivia Time!", bg="snow2",
    font=("Times New Roman", 36), justify="center"
)
welcome.pack(fill="x", pady=10)

exp_label = ttk.Label(root, text="Experience Points", font=("Arial", 12))
exp_label.pack()
exp_bar = ttk.Progressbar(
    root, orient="horizontal", length=500, mode="determinate",
    maximum=TOTAL_QS * XP_PER_CORRECT, value=0
)
exp_bar.pack(pady=(0, 15))


def open_quiz():
    quiz_win = tk.Toplevel(root)
    quiz_win.title("Trivia Time Quiz")
    quiz_win.geometry("800x600")
    quiz_win.configure(bg="aquamarine")

    header = tk.Frame(quiz_win, bg="aquamarine")
    header.pack(fill="x", padx=10, pady=(10, 0))
    elapsed = 0
    timer_lbl = tk.Label(header, text="00:00", font=("Arial", 14), bg="aquamarine")
    timer_lbl.pack(side="right")

    def update_timer():
        nonlocal elapsed
        elapsed += 1
        m, s = divmod(elapsed, 60)
        timer_lbl.config(text=f"{m:02d}:{s:02d}")
        if quiz_win.winfo_exists():
            timer_lbl.after(1000, update_timer)
    update_timer()

    frame = tk.Frame(quiz_win, bg="aquamarine")
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    score = 0
    q_index = 0

    question_lbl = tk.Label(
        frame, text=QUESTIONS[q_index], font=("Arial", 16),
        bg="snow2", wraplength=760, justify="left"
    )
    question_lbl.pack(pady=(0, 15))

    answer_var = tk.IntVar(value=0)
    rbuttons = []
    for i in range(3):
        rb = ttk.Radiobutton(
            frame, text=OPTIONS[q_index][i],
            variable=answer_var, value=i+1
        )
        rb.pack(anchor="w", pady=2)
        rbuttons.append(rb)

    def next_question():
        nonlocal score, q_index
        if answer_var.get() == ANSWERS[q_index]:
            score += 1
            new_xp = min(exp_bar["value"] + XP_PER_CORRECT, exp_bar["maximum"])
            exp_bar["value"] = new_xp

        q_index += 1
        if q_index >= TOTAL_QS:
            for w in frame.winfo_children():
                w.destroy()
            final_text = (
                f"Quiz Complete!\n"
                f"Score: {score} / {TOTAL_QS}\n"
                f"EXP Earned: {int(exp_bar['value'])}\n"
                f"Time: {timer_lbl.cget('text')}"
            )
            final_lbl = tk.Label(
                frame, text=final_text, font=("Arial", 18),
                bg="snow2", wraplength=760, justify="center"
            )
            final_lbl.pack(pady=100)
            return

        question_lbl.config(text=QUESTIONS[q_index])
        answer_var.set(0)
        for idx, rb in enumerate(rbuttons):
            rb.config(text=OPTIONS[q_index][idx])

    next_btn = ttk.Button(frame, text="Next", command=next_question)
    next_btn.pack(pady=20)

start_btn = ttk.Button(root, text="Click for Trivia Time Quiz!", command=open_quiz)
start_btn.pack(pady=10)


root.mainloop()
