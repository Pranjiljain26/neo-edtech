import streamlit as st


# Page functions
def home_page():
    st.write("Welcome to the Home Page!")

    # Add Connect Wallet button
    if st.button("Connect Wallet"):
        # Redirect to the NEO website when button is clicked
        st.markdown(
            '<meta http-equiv="refresh" content="0;url=https://neo.org/" />',
            unsafe_allow_html=True,
        )

    st.write("## NEON3 for Beginners")
    st.video("https://www.youtube.com/watch?v=I_vCOzEbSMI")

    # Center-align the button
    st.markdown(
        '<div style="text-align: center;">'
        + '<button style="width: 150px;">Enroll Now @99</button>'
        + "</div>",
        unsafe_allow_html=True,
    )


def courses_page():
    st.write("Welcome to the Courses Page!")

    # Link-button to watch Course 1 video
    st.markdown(
        '<div style="text-align: center;">'
        + '<a href="https://www.youtube.com/watch?v=KPHKgvOknNo&list=PLsyeobzWxl7q3X-LBEm0xP1cHUeNhbk16&index=1&pp=iAQB" target="_blank">'
        + '<button style="width: 150px;">Watch Video 1</button>'
        + "</a>"
        + "</div>",
        unsafe_allow_html=True,
    )

    # Add some space
    st.write("\n")

    # Link-button to watch Course 2 video
    st.markdown(
        '<div style="text-align: center;">'
        + '<a href="https://www.youtube.com/watch?v=nBXpx-wuYL0&list=PLsyeobzWxl7q3X-LBEm0xP1cHUeNhbk16&index=2&pp=iAQB" target="_blank">'
        + '<button style="width: 150px;">Watch Video 2</button>'
        + "</a>"
        + "</div>",
        unsafe_allow_html=True,
    )

    st.write("\n")

    # Link-button to assessment page
    # Assessment button
    if st.button("Assessment"):
        assessment_page()

    st.write("\n")

    # Increase the size of the button and center-align
    st.markdown(
        '<div style="text-align: center;">'
        + '<button style="width: 200px; height: 60px; font-size: 18px;">Get Bounty</button>'
        + "</div>",
        unsafe_allow_html=True,
    )


# ... (Other functions and imports)


def assessment_page():
    st.write("Welcome to the Assessment Page!")
    st.write("## Take the assessment here...")
    st.write("Welcome to the assessment! Please answer the questions below.")

    correct_answers = {
        "Question 1": "A programming language",
        "Question 2": "A secondary cryptocurrency",
        "Question 3": "Delegated Byzantine Fault Tolerance (dBFT)",
        "Question 4": "100 million NEO",
    }

    # Question 1
    st.write("Question 1: What is Neo in the context of blockchain technology?")
    options1 = [
        "A programming language",
        "A cryptocurrency",
        "A consensus algorithm",
        "None of the above",
    ]
    selected_option1 = st.radio("Select your answer:", options1)

    # Question 2
    st.write("Question 2: What does GAS represent in the Neo blockchain?")
    options2 = [
        "Global Asset System",
        "Gasoline for running smart contracts",
        "A secondary cryptocurrency",
        "Gaming and Applications System",
    ]
    selected_option2 = st.radio("Select your answer:", options2)

    # Question 3
    st.write("Question 3: Which consensus algorithm does Neo use?")
    options3 = [
        "Proof of Work (PoW)",
        "Proof of Stake (PoS)",
        "Delegated Proof of Stake (DPoS)",
        "Delegated Byzantine Fault Tolerance (dBFT)",
    ]
    selected_option3 = st.radio("Select your answer:", options3)

    # Question 4
    st.write("Question 4: What is the maximum total supply of NEO tokens?")
    options4 = ["100 million NEO", "21 million NEO", "1 billion NEO", "1 trillion NEO"]
    selected_option4 = st.radio("Select your answer:", options4)

    # Calculate total score
    score = 0
    if selected_option1 == correct_answers["Question 1"]:
        score += 1
    if selected_option2 == correct_answers["Question 2"]:
        score += 1
    if selected_option3 == correct_answers["Question 3"]:
        score += 1
    if selected_option4 == correct_answers["Question 4"]:
        score += 1

    # Display results after submitting
    if st.button("Submit"):
        st.write("Results:")

        st.write(f"Total Score: {score}")

        if score >= 3:
            st.write("Pass! Congratulations!")
        else:
            st.write("Failed. Please try again.")


# ... (Other functions and main app logic)


def certification_page():
    st.write("Welcome to the Certification Page!")
    st.write("## Claim your certification")

    # Center-align the button
    st.markdown(
        '<div style="text-align: center;">'
        + '<button style="width: 200px; height: 60px; font-size: 18px;">Claim your certificate</button>'
        + "</div>",
        unsafe_allow_html=True,
    )


# Main app
def main():
    st.title("Navigation App")

    menu = [
        "Home",
        "Courses",
        "Certification",
    ]
    choice = st.sidebar.selectbox("Select a page", menu)

    if choice == "Home":
        home_page()
    elif choice == "Courses":
        courses_page()
    elif choice == "Certification":
        certification_page()
    elif choice == "Assessment":
        assessment_page()


if __name__ == "__main__":
    main()
