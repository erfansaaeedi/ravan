import streamlit as st
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (ChatPromptTemplate, HumanMessagePromptTemplate,
                               MessagesPlaceholder,
                               SystemMessagePromptTemplate)


def generate_response(input, template,key):
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo-16k",
        openai_api_key=key,
    )

    system_msg_template = SystemMessagePromptTemplate.from_template(template=template)

    human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")

    prompt_template = ChatPromptTemplate.from_messages(
        [
            system_msg_template,
            MessagesPlaceholder(variable_name="history"),
            human_msg_template,
        ]
    )

    conversation = ConversationChain(
        memory=st.session_state.buffer_memory,
        prompt=prompt_template,
        llm=llm,
        verbose=True,
    )

    return conversation({"input": input})["response"]
