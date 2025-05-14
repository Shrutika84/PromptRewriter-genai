import streamlit as st
from prompts import rewrite_prompts
from llm_utils import run_ollama_model

st.title("🔁 Prompt Rewriter with GenAI")

# Step 1: Model selector dropdown
model_choice = st.selectbox(
    "Choose a model to generate rewritten prompts",
    options=["mistral", "llama2", "codellama"],
    index=0
)

# Step 2: Prompt input
user_input = st.text_area("Enter your prompt here")

if st.button("Rewrite Prompt"):
    with st.spinner(f"Generating with {model_choice}..."):
        for style, template in rewrite_prompts.items():
            full_prompt = template.format(user_input=user_input)
            output = run_ollama_model(full_prompt, model=model_choice)
            st.markdown(f"### ✨ {style} Style")
            st.write(output)
