# Cohere's imports
import cohere as co
from cohere.classify import Example
from conversant.prompt_chatbot import PromptChatbot
from conversant.utils import demo_utils

# Sreamlit
import streamlit as st
from streamlit_chat import message
import streamlit.components.v1 as components

# general imports
import ast
import copy
import os
import sys
import emoji
from typing import Literal, Optional, Union

os.environ["COHERE_API"] = "mhsnOPXxi1m91vlrQJ6VsKFoDVhiqlKPeYHtEsZV"

COHERE_API = os.environ["COHERE_API"]

co = co.Client(COHERE_API)

#------------------------------------------------------------
COMPONENT_NAME = "streamlit_chat"

root_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(root_dir, "frontend/build")

_streamlit_chat = components.declare_component(
    COMPONENT_NAME,
    path = build_dir)

USER_AVATAR_SHORTCODE = ":bust_in_silhouette:"

# data type for avatar style
AvatarStyle = Literal[ 
    "adventurer", 
    "adventurer-neutral", 
    "avataaars",
    "big-ears",
    "big-ears-neutral",
    "big-smile",
    "bottts", 
    "croodles",
    "croodles-neutral",
    "female",
    "gridy",
    "human",
    "identicon",
    "initials",
    "jdenticon",
    "male",
    "micah",
    "miniavs",
    "pixel-art",
    "pixel-art-neutral",
    "personas",
]

def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text 

def chat_message(message: str,
                 is_user: bool = False,
                 avatar_style: Optional[AvatarStyle] = None,
                 seed: Optional[Union[int, str]] = 42,
                 key: Optional[str] = None):
    
    if not avatar_style:
        avatar_style = "pixel-art-neutral" if is_user else "bottts"

    _streamlit_chat(message=message, seed=seed, isUser=is_user, avatarStyle=avatar_style, key=key)
#---------------------------------------------------------------

st.title("Health-E: AI healthcare assistant")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []



health_e = PromptChatbot.from_persona("health-e", client=co)
chat_message("Hi! How may I help you today?", key="1") 

first_message = st.text_input("talk to me", key="input_prompt")
chat_message(first_message, is_user=True, key="2")

chat_message(health_e.reply(first_message), key="3")

second_message = st.text_input("anything else", key="second_prompt")
chat_message(second_message, is_user=True, key="4")

chat_message(health_e.reply(second_message), key="5")










































# # Cohere's imports
# import cohere as co
# from cohere.classify import Example
# from conversant import PromptChatbot
# from conversant.prompts import ChatPrompt

# # Sreamlit
# import streamlit as st

# # General imports
# import pandas as pd
# import textwrap
# import numpy as np
# import json

# import os

# os.environ["COHERE_API"] = "mhsnOPXxi1m91vlrQJ6VsKFoDVhiqlKPeYHtEsZV"

# COHERE_API = os.environ["COHERE_API"]

# co = co.Client(COHERE_API)

# # Let's let the user pick from the default persona

# st.title("Health-E AI bot")