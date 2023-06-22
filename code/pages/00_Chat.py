import streamlit as st
from streamlit_chat import message
from utilities.helper import LLMHelper

def clear_text_input():
    st.session_state['question'] = st.session_state['input']
    st.session_state['input'] = ""

def clear_chat_data():
    st.session_state['input'] = ""
    st.session_state['question'] = None
    st.session_state['write_report'] = None
    st.session_state['chat_history'] = []
    st.session_state['source_documents'] = []

def execute_write_report():
    clear_chat_data()
    st.session_state['write_report'] = "Write credit risk report for: " + st.session_state['select_write_report']

# Initialize chat history
if 'question' not in st.session_state:
    st.session_state['question'] = None
if 'write_report' not in st.session_state:
    st.session_state['write_report'] = None
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'source_documents' not in st.session_state:
    st.session_state['source_documents'] = []

llm_helper = LLMHelper()

# Chat 
st.text_input("You: ", placeholder="type your question", key="input", on_change=clear_text_input)
clear_chat = st.button("Clear chat", key="clear_chat", on_click=clear_chat_data)

write_report = st.selectbox("Write credit risk report for:", options=['None', 'Castleton', 'Enovos', 'ESB'], index=0, key="select_write_report", on_change=None)
write_report_button = st.button("Generate Report", key="generate_report", on_click=execute_write_report)

if st.session_state['write_report']:
    question, result, _, sources = llm_helper.get_semantic_answer_lang_chain(st.session_state['write_report'], st.session_state['chat_history'])
    st.session_state['chat_history'].append((question, result))
    st.session_state['source_documents'].append(sources)

if st.session_state['question']:
    question, result, _, sources = llm_helper.get_semantic_answer_lang_chain(st.session_state['question'], st.session_state['chat_history'])
    st.session_state['chat_history'].append((question, result))
    st.session_state['source_documents'].append(sources)

if st.session_state['chat_history']:
    for i in range(len(st.session_state['chat_history'])-1, -1, -1):
        message(st.session_state['chat_history'][i][1], key=str(i))
        st.markdown(f'\n\nSources: {st.session_state["source_documents"][i]}')
        message(st.session_state['chat_history'][i][0], is_user=True, key=str(i) + '_user')
