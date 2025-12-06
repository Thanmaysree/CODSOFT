
import customtkinter as ctk
import random
import time
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Rock Paper Scissors – Modern Edition")
app.geometry("700x600")

# ------------------------------
# Game Variables
# ------------------------------
user_score = 0
comp_score = 0
choices = ["Rock", "Paper", "Scissors"]
emojis = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

# ------------------------------
# GUI Elements
# ------------------------------
title_label = ctk.CTkLabel(app, text="Rock • Paper • Scissors", font=("Arial", 28, "bold"))
title_label.pack(pady=20)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 24))
result_label.pack(pady=10)

choice_frame = ctk.CTkFrame(app)
choice_frame.pack(pady=20)

user_choice_label = ctk.CTkLabel(choice_frame, text="You: ?", font=("Arial", 35))
user_choice_label.grid(row=0, column=0, padx=20)

comp_choice_label = ctk.CTkLabel(choice_frame, text="Computer: ?", font=("Arial", 35))
comp_choice_label.grid(row=0, column=1, padx=20)

score_label = ctk.CTkLabel(app, text="Score → You: 0 | Computer: 0", font=("Arial", 20))
score_label.pack(pady=15)

status_label = ctk.CTkLabel(app, text="", font=("Arial", 20))
status_label.pack(pady=10)

# ------------------------------
# Game Logic
# ------------------------------
def determine_winner(user, comp):
    if user == comp:
        return "It's a Tie!"
    if (user == "Rock" and comp == "Scissors") or \
       (user == "Scissors" and comp == "Paper") or \
       (user == "Paper" and comp == "Rock"):
        return "You Win!"
    return "You Lose!"


# ------------------------------
# Animation Thread (Computer Shuffle)
# ------------------------------
def animate_computer_choice(final_choice):
    for _ in range(10):  
        comp_choice_label.configure(text="Computer: " + random.choice(list(emojis.values())))
        time.sleep(0.1)
    comp_choice_label.configure(text=f"Computer: {emojis[final_choice]}")


# ------------------------------
# User Selection
# ------------------------------
def play_round(user_choice):
    global user_score, comp_score

    # Show user selection
    user_choice_label.configure(text=f"You: {emojis[user_choice]}")

    # Random computer choice + animation
    comp_choice = random.choice(choices)
    threading.Thread(target=animate_computer_choice, args=(comp_choice,), daemon=True).start()

    # Determine winner
    result = determine_winner(user_choice, comp_choice)

    # Update scores
    if result == "You Win!":
        user_score += 1
    elif result == "You Lose!":
        comp_score += 1

    score_label.configure(text=f"Score → You!!: {user_score} | Computer: {comp_score}")
    result_label.configure(text=result, text_color="cyan")

    # Status update
    status_label.configure(text=f"You chose {user_choice} • Computer chose {comp_choice}")


# ------------------------------
# Buttons
# ------------------------------
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20)

for txt in choices:
    ctk.CTkButton(
        button_frame,
        text=f"{txt} {emojis[txt]}",
        width=120,
        height=50,
        corner_radius=20,
        font=("Arial", 18),
        command=lambda c=txt: play_round(c)
    ).pack(side="left", padx=10)

# ------------------------------
# Reset Button
# ------------------------------
def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    score_label.configure(text="Score → You!!: 0 | Computer: 0")
    result_label.configure(text="")
    status_label.configure(text="")
    user_choice_label.configure(text="You: ?")
    comp_choice_label.configure(text="Computer: ?")

reset_btn = ctk.CTkButton(app, text="Reset Game", fg_color="red", hover_color="#cc0000", command=reset_game)
reset_btn.pack(pady=15)

# ------------------------------
app.mainloop()


