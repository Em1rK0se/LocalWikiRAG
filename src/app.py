import streamlit as st
import time
from rag_engine import RAGEngine

# Initialize the RAG logic
if 'engine' not in st.session_state:
    st.session_state.engine = RAGEngine()

# Page configuration
st.set_page_config(page_title="Local Wikipedia Assistant", page_icon="🤖")
st.title("Local Wikipedia RAG Assistant")

# Sidebar for Reset and Context Visibility
with st.sidebar:
    st.header("Settings")
    show_context = st.checkbox("Show source chunks", value=False)
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask about a person or place..."):
    # Add user message to state and display
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response with Latency Measurement
    with st.chat_message("assistant"):
        start_time = time.time() # Start timer for latency measurement
        
        # 1. Retrieve context chunks
        context = st.session_state.engine.retrieve_context(prompt)
        
        # 2. Generate answer
        full_answer = st.session_state.engine.generate_answer(prompt, context)
        
        end_time = time.time() # End timer
        latency = end_time - start_time
        
        # 3. Streaming effect for better UI/UX
        placeholder = st.empty()
        current_text = ""
        for word in full_answer.split():
            current_text += word + " "
            placeholder.markdown(current_text + "▌")
            time.sleep(0.05) # Small delay to simulate streaming
        
        placeholder.markdown(current_text)
        
        # Display latency and source information
        st.caption(f"Response time: {latency:.2f} seconds")
        
        if show_context and context:
            with st.expander("Source Chunks"):
                for i, chunk in enumerate(context):
                    st.write(f"**Chunk {i+1}:** {chunk}")

    # Save to session state
    st.session_state.messages.append({"role": "assistant", "content": full_answer})

    # source venv/bin/activate
    # streamlit run src/app.py