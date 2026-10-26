import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 Enterprise Knowledge Assistant")
st.caption("AI-powered knowledge assistant for enterprise documents")

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/ask"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question about your organization's documents..."):

    # Display user question
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    try:
        # Send question to FastAPI
        response = requests.post(
            API_URL,
            json={"question": prompt},
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        answer = data.get(
            "answer",
            "No answer was returned."
        )

        sources = data.get("sources", [])

        # Display assistant answer
        with st.chat_message("assistant"):
            st.markdown(answer)

            if sources:
                st.markdown("**Sources:**")

                unique_sources = set()

                for source in sources:
                    source_name = source.get("source", "Unknown")
                    page = source.get("page", "Unknown")

                    source_key = (source_name, page)

                    if source_key not in unique_sources:
                        unique_sources.add(source_key)

                        st.caption(
                            f"📄 {source_name} — Page {page}"
                        )

        # Save assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except requests.exceptions.ConnectionError:
        with st.chat_message("assistant"):
            st.error(
                "Unable to connect to the FastAPI backend. "
                "Please make sure the backend server is running."
            )

    except requests.exceptions.RequestException as error:
        with st.chat_message("assistant"):
            st.error(
                f"An error occurred while contacting the backend: {error}"
            )