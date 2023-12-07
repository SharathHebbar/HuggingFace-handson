import os
import streamlit as st
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class UserInterface():

    def __init__(self, ):
        st.warning("Warning: Some models may not work and some models may require GPU to run")
        st.text("An Open Source Chat Application")
        st.header("Open LLMs")

        self.API_KEY = st.sidebar.text_input(
            'API Key',
            type='password',
            help="Type in your HuggingFace API key to use this app"
        )

        models_name = (
            "HuggingFaceH4/zephyr-7b-beta",
            "Open-Orca/Mistral-7B-OpenOrca",
        )
        self.models = st.sidebar.selectbox(
            label="Choose your models",
            options=models_name,
            help="Choose your model",
        )

        self.temperature = st.sidebar.slider(
            label='Temperature',
            min_value=0.1,
            max_value=1.0,
            step=0.1,
            value=0.5,
            help="Set the temperature to get accurate or random result"
        )

        self.max_token_length = st.sidebar.slider(
            label="Token Length",
            min_value=32,
            max_value=2048,
            step=16,
            value=64,
            help="Set max tokens to generate maximum amount of text output"
        )


        self.model_kwargs = {
            "temperature": self.temperature,
            "max_length": self.max_token_length
        }

        os.environ['HUGGINGFACEHUB_API_TOKEN'] = self.API_KEY

    
    def form_data(self):

        try:
            if not self.API_KEY.startswith('hf_'):
                st.warning('Please enter your API key!', icon='⚠')
                text_input_visibility = True
            else:
                text_input_visibility = False
            

            if "messages" not in st.session_state:
                    st.session_state.messages = []

            st.write(f"You are using {self.models} model")

            for message in st.session_state.messages:
                with st.chat_message(message.get('role')):
                    st.write(message.get("content"))
            
            context = st.sidebar.text_input(
                 label="Context",
                 help="Context lets you know on what the answer should be generated"
                 )

        
            question = st.chat_input(
                 key="question",
                 disabled=text_input_visibility
            )


            template = """
            Answer the question based on the context, if you don't know then output "Out of Context"
            Context: {context}
            Question: {question}

            Answer: 
            """
            prompt = PromptTemplate(
                template=template,
                input_variables=[
                    'question',
                    'context'
                ]
            )
            llm = HuggingFaceHub(
                repo_id = self.models,
                model_kwargs = self.model_kwargs
            )

            if question:
                llm_chain = LLMChain(
                    prompt=prompt,
                    llm=llm,
                )

                result = llm_chain.run({
                    "question": question,
                    "context": context
                })

                if "Out of Context" in result:
                    result = "Out of Context"
                st.session_state.messages.append(
                    {
                        "role":"user",
                        "content": f"Context: {context}\n\nQuestion: {question}"
                    }
                )
                with st.chat_message("user"):
                    st.write(f"Context: {context}\n\nQuestion: {question}")
                
                if question.lower() == "clear":
                    del st.session_state.messages
                    return
                
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": result
                    }
                )
                with st.chat_message('assistant'):
                    st.markdown(result)

        except Exception as e:
            st.error(e, icon="🚨")

model = UserInterface()
model.form_data()