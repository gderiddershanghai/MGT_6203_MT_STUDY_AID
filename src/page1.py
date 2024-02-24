# import streamlit as st


# # Define a list of dictionaries, each representing a question and its details
# questions = [
#     {'question': "What's my name?", 'options_list': ['Frank', 'Mike', 'Apple_pie', 'Correcto'], 'correct_answer': 'Correcto'},
#     {'question': "What's the capital of France?", 'options_list': ['Paris', 'Berlin', 'Madrid', 'Lisbon'], 'correct_answer': 'Paris'},
#     {'question': "2 + 2?", 'options_list': ['3', '4', '5', '6'], 'correct_answer': '4'},
#     {'question': "What's the color of the sky?", 'options_list': ['Blue', 'Green', 'Red', 'Yellow'], 'correct_answer': 'Blue'}
# ]

# def question_generator(label, options, question_key):
#     # Display the question and return the user's selection
#     question = st.radio(label=label, options=options, key=question_key)
#     return question

# def main():
#     # Iterate over each question in the list
#     for i, q in enumerate(questions, start=1):
#         label = q['question']
#         options = q['options_list']
#         correct_answer = q['correct_answer']
#         question_key = f"question_{i}"  # Unique key for each question

#         question = question_generator(label, options, question_key)

#         # Use a unique key for each submit button to handle them individually
#         if st.button('Submit', key=f"submit_{i}"):
#             if question == correct_answer:
#                 st.success('Great work!')
#             else:
#                 st.error(f"Ai, the correct answer was {correct_answer}")

#             # Optionally, provide a way to review material related to the question
#             if 'slides' in q:
#                 st.write(f"You can review {q['slides']}")

# if __name__ == "__main__":
#     main()

import streamlit as st

questions = [
    {'question': "What's my name?", 'options_list': ['Frank', 'Mike', 'Apple_pie', 'Correcto'], 'correct_answer': 'Correcto'},
    {'question': "What's the capital of France?", 'options_list': ['Paris', 'Berlin', 'Madrid', 'Lisbon'], 'correct_answer': 'Paris'},
    {'question': "2 + 2?", 'options_list': ['3', '4', '5', '6'], 'correct_answer': '4'},
    {'question': "What's the color of the sky?", 'options_list': ['Blue', 'Green', 'Red', 'Yellow'], 'correct_answer': 'Blue'}
]

def apply_custom_css():
    custom_css = """
    <style>
        .question-style {
            font-size: 20px; /* Customize the font size as needed */
            font-weight: bold; /* Optional: Make the question bold */
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def question_generator(label, options, question_key):
    # Display the question as a radio button
    question = st.radio(label='please select the coorect answer', options=options, key=question_key)  # Note: label is handled separately with markdown
    return question

def main():
    # Apply the custom CSS for styling
    apply_custom_css()

    # Iterate over each question in the list
    for i, q in enumerate(questions, start=1):
        label = q['question']
        options = q['options_list']
        correct_answer = q['correct_answer']
        question_key = f"question_{i}"  # Unique key for each question

        # Display the question with custom styling
        st.markdown('-------------------------------')

        st.markdown(f'<div class="question-style">{label}</div>', unsafe_allow_html=True)

        question = question_generator(label, options, question_key)

        # Use a unique key for each submit button to handle them individually
        if st.button('Submit', key=f"submit_{i}"):
            if question == correct_answer:
                st.success('Great work!')
            else:
                st.error(f"Ai, the correct answer was {correct_answer}")

            # Optionally, provide a way to review material related to the question
            if 'slides' in q:
                st.write(f"You can review {q['slides']}")

if __name__ == "__main__":
    main()
