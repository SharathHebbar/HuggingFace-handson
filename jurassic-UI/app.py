import streamlit as st
from source_code import text_completion, chat, GEC, paraphrase, contextual_answer, summarize, improvements
st.title("AI21 Studio Jurassic")

st.image(
    image="assets\jurassic.jpg",
    caption="Jurassic",
)

st.sidebar.title("Select your preferred tasks")

jurassic_models = [
    "j2-light",
    "j2-ultra",
    "j2-mid",
]
tasks = [
    "Generic",
    "Specific"
]

# task = st.sidebar.selectbox(
#     label="Select your Model",
#     options = tasks
# )

disabled = False
# if task == "Generic":
#     disabled = False

# task_disable = False
# if task == "Specific":
#     task_disable = True


# generic_tasks = [
#     "Text Completion",
#     # "Chat"
# ]

specific_tasks = [
    # "Contextual Answers",
    "Paraphrase",
    "Summarize",
    "Grammetical Error Corrections",
    "Text Improvements"
]

# choose_task = generic_tasks
# if task == "Specific":
#     choose_task = specific_tasks  

choose_task = specific_tasks  

choose = st.sidebar.selectbox(
    label="Select your tasks",
    options = choose_task,

)

# model = st.sidebar.selectbox(
#     label="Select your Model",
#     options = jurassic_models,
#     disabled=disabled
# )


# numResults = st.sidebar.number_input(
#     label="Select Number of results",
#     min_value=1,
#     max_value=5,
#     value=1,
#     disabled=disabled
# )

# maxTokens = st.sidebar.number_input(
#     label="Max Number of Tokens to generate",
#     min_value=32,
#     max_value=2048,
#     value=200,
#     step=2,
#     disabled=disabled
# )

# temperature = st.sidebar.slider(
#     label="Temperature",
#     min_value=0.1,
#     max_value=1.0,
#     value=0.5,
#     step=0.1,
#     disabled=disabled
# )

# topP = st.sidebar.slider(
#     label="Top P",
#     min_value=0.1,
#     max_value=1.0,
#     value=0.6,
#     step=0.1,
#     disabled=disabled
# )

# topKReturn = st.sidebar.slider(
#     label="Top K",
#     min_value=1,
#     max_value=10,
#     value=5,
#     step=1,
#     disabled=disabled
# )

# context = st.sidebar.text_input(
#     label="Context",
# )

# if choose == "Chat":
#     question = st.chat_input(key="Question")
#     if context is None:
#         context = "Everything"
#     # template = f"<|system|>\nYou are a intelligent chatbot and expertise in {context}.</s>\n<|user|>\n{question}.\n<|assistant|>"
#     template = f"{context}\n{question}"
#     if "messages" not in st.session_state:
#         st.session_state.messages = []
#     for message in st.session_state.messages:
#         with st.chat_message(message.get('role')):
#             st.write(message.get("content"))
#     st.session_state.messages.append(
#         {
#             "role":"user",
#             "content": f"Question: {question}"
#         }
#     )
#     if question:
#         result = chat(model, template, numResults, maxTokens, temperature, topKReturn, topP)
#         with st.chat_message("user"):
#             st.write(f"Context: {context}\n\nQuestion: {question}")

#         if question.lower() == "clear":
#             del st.session_state.messages

#         st.session_state.messages.append(
#             {
#                 "role": "assistant",
#                 "content": result
#             }
#         )
#         with st.chat_message('User'):
#             st.write(f"Context: {context}\n\nQuestion: {question}")
#         with st.chat_message('assistant'):
#             st.markdown(result)
if 0 > 1:
    pass
else:
    question = st.text_area(label="Question")
    # if context is None:
    #     context = "Everything"
    # template = f"<|system|>\nYou are a intelligent chatbot and expertise in {context}.</s>\n<|user|>\n{question}.\n<|assistant|>"
    
    # if choose == "Text Completion":
    #     if question:
    #         result = text_completion(model, template, numResults, maxTokens, temperature, topKReturn, topP)
    #         st.markdown(result)
    # if choose == "Contextual Answers":
    #     if question:
    #         result = contextual_answer(context, question)
    #         st.markdown(result)
    if choose == "Paraphrase":
        if question:
            result = paraphrase(question)
            st.markdown(result)
    elif choose == "Summarize":
        if question:
            result = summarize(question)
            st.markdown(result)
    elif choose == "Grammetical Error Corrections":
        if question:
            result = GEC(question)
            st.markdown(result)
    elif choose == "Text Improvements":
        if question:
            result = improvements(question)
            st.markdown(result)
    