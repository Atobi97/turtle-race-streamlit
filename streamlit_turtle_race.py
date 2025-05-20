import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Setup
st.set_page_config(page_title="Turtle Race", layout="centered")
st.title("🐢 Turtle Race with Visualization")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = {color: 0 for color in colors}
finish_line = 100
y_positions = np.arange(len(colors))

# Inputs
user_bet = st.selectbox("Which turtle will win the race?", colors)
bet_amount = st.number_input("Bet an amount ($)", min_value=1, step=1)
start_race = st.button("Start Race")

def plot_race(positions):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlim(0, finish_line + 10)
    ax.set_ylim(-1, len(colors))
    ax.set_yticks(y_positions)
    ax.set_yticklabels([color.capitalize() for color in colors])
    ax.set_xlabel("Race Track")
    ax.grid(True, axis='x', linestyle='--', alpha=0.5)

    for i, color in enumerate(colors):
        ax.scatter(positions[color], y_positions[i], color=color, s=300, edgecolors='black', marker='>')
    return fig

# Run the race
if start_race:
    st.write("🏁 The race has started!")
    winner = None
    chart_area = st.empty()

    while not winner:
        for color in colors:
            positions[color] += random.randint(1, 10)
            if positions[color] >= finish_line:
                winner = color
                break

        fig = plot_race(positions)
        chart_area.pyplot(fig)
        time.sleep(0.3)

    st.success(f"The {winner} turtle won the race! 🏆")

    if winner == user_bet:
        winnings = bet_amount * 6
        st.balloons()
        st.success(f"You won ${winnings}!")
    else:
        st.error(f"You lost your bet. The {winner} turtle won.")

