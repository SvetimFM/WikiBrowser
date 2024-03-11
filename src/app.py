import streamlit as st
import time

from app_logic.wiki_browser import convert_select_llm, agent_execute


def user_form():
    st.title("Chat with Wikipedia")
    st.subheader("This app allows you to chat with Wikipedia.")
    st.sidebar.subheader("Please select a model and enter a question.")

    llm = st.sidebar.radio('Select LLM:',['OpenAI GPT3','Anthropic Opus'])
    llm = convert_select_llm(llm)

    topic = st.sidebar.text_area('Enter a question or a topic you wish to learn about:')
    button = st.sidebar.button('Submit')

    if button or topic:
        start_time = time.time()
        try:
            model_output = agent_execute(llm=llm, user_input=topic)
            st.write(model_output)

            end_time = time.time()
            elapsed_time = end_time - start_time

            st.write(f"Request took: {elapsed_time:.2f} seconds")

        except Exception as e:
            st.error(f"Error: {e}")


def main():
    user_form()


if __name__ == '__main__':
    main()
