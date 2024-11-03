import streamlit as st
import random

# Part 1: Portfolio
def portfolio():
    st.title("My Portfolio")
    st.write("Welcome to my portfolio! Here you'll find information about my projects, skills, and interests.")
    
    st.header("About Me")
    st.write("Hi! I'm [Your Name], a [Your Role] with a passion for [Your Interests].")
    
    st.header("Projects")
    st.write("- **Project 1**: Description of your first project.")
    st.write("- **Project 2**: Description of your second project.")
    
    st.header("Skills")
    st.write("Here are some of my skills:")
    st.write("- Skill 1")
    st.write("- Skill 2")
    st.write("- Skill 3")
    
    st.header("Contact")
    st.write("Feel free to reach out to me at [Your Email].")

# Part 2: Guessing Game
def guessing_game():
    st.title("Guessing Game")

    # Select Mode
    mode = st.selectbox("Choose Game Mode", ["User Guessing", "Machine Guessing"])

    if mode == "User Guessing":
        user_guessing_game()
    else:
        machine_guessing_game()

def user_guessing_game():
    st.header("User Guessing Game")
    st.write("Try to guess the number I'm thinking of between 1 and 100!")
    number = random.randint(1, 100)
    
    if "user_guess" not in st.session_state:
        st.session_state.user_guess = None
    
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0

    guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)
    
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess == number:
            st.success(f"Congratulations! You've guessed the number in {st.session_state.attempts} attempts.")
        elif guess < number:
            st.warning("Try a higher number.")
        else:
            st.warning("Try a lower number.")
    
    if st.button("Play Again"):
        st.session_state.user_guess = None
        st.session_state.attempts = 0
        st.experimental_rerun()

def machine_guessing_game():
    st.header("Machine Guessing Game")
    st.write("Think of a number between 1 and 100 and the machine will try to guess it!")
    
    if "lower_bound" not in st.session_state:
        st.session_state.lower_bound = 1
    if "upper_bound" not in st.session_state:
        st.session_state.upper_bound = 100
    if "machine_guess" not in st.session_state:
        st.session_state.machine_guess = None
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0
    
    if st.button("Make a Guess"):
        st.session_state.attempts += 1
        mid = (st.session_state.lower_bound + st.session_state.upper_bound) // 2
        st.session_state.machine_guess = mid
        st.write(f"Is your number {mid}?")
        
        feedback = st.radio("Select Feedback", ["Correct", "Higher", "Lower"])
        
        if feedback == "Correct":
            st.success(f"The machine guessed your number in {st.session_state.attempts} attempts!")
        elif feedback == "Higher":
            st.session_state.lower_bound = mid + 1
        else:
            st.session_state.upper_bound = mid - 1
    
    if st.button("Play Again"):
        st.session_state.lower_bound = 1
        st.session_state.upper_bound = 100
        st.session_state.machine_guess = None
        st.session_state.attempts = 0
        st.experimental_rerun()

# Main Application
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Portfolio", "Guessing Game"])
    
    if selection == "Portfolio":
        portfolio()
    else:
        guessing_game()

if __name__ == "__main__":
    main()
