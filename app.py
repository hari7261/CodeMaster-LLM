import streamlit as st
import ollama
import subprocess
from code_editor import code_editor

# Initialize
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar controls
with st.sidebar:
    st.header("Settings")
    language = st.selectbox(
        "Programming Language",
        ["Python", "JavaScript", "Java", "C++", "Go"],
        index=0
    )
    explain_mode = st.toggle("Explain Code", True)
    
    # Clear chat history button
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
# Main interface
col1, col2 = st.columns([0.7, 0.3])

with col1:  # Code editor
    response_dict = code_editor(
        code="# Enter your code here",
        lang=language.lower(),
        height=300,
        key="code_editor"
    )
    # Handle different response formats from code_editor
    user_code = ""
    if response_dict:
        if isinstance(response_dict, dict):
            user_code = response_dict.get('text', '') or response_dict.get('code', '')
        elif isinstance(response_dict, str):
            user_code = response_dict
    
    # Debug: Show what code is detected
    if user_code and user_code.strip() != "# Enter your code here":
        st.caption(f"Code detected: {len(user_code)} characters")

with col2:  # Terminal emulator
    st.header("Terminal")
    terminal_output = st.empty()
    if st.button("Run Code"):
        if user_code and user_code.strip() and user_code.strip() != "# Enter your code here":
            with st.spinner("Executing..."):
                try:
                    # Use the correct Python executable path
                    python_exe = r"C:\Users\Hariom kumar\AppData\Local\Programs\Python\Python312\python.exe"
                    
                    if language.lower() == "python":
                        result = subprocess.run(
                            [python_exe, "-c", user_code],
                            capture_output=True,
                            text=True,
                            timeout=10
                        )
                        output = result.stdout if result.stdout else result.stderr
                        if output:
                            terminal_output.code(output)
                        else:
                            terminal_output.success("Code executed successfully (no output)")
                    else:
                        terminal_output.warning(f"Code execution only supported for Python. Selected: {language}")
                except subprocess.TimeoutExpired:
                    terminal_output.error("Code execution timed out (10 seconds)")
                except Exception as e:
                    terminal_output.error(f"Error executing code: {str(e)}")
        else:
            terminal_output.warning("Please enter some code to execute.")

# Chat interaction
st.header("💬 Chat Assistant")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input(f"Ask {language} question..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Build conversation context
        conversation_context = ""
        for msg in st.session_state.messages[-5:]:  # Last 5 messages for context
            role = "Human" if msg["role"] == "user" else "Assistant"
            conversation_context += f"{role}: {msg['content']}\n\n"
        
        # Custom prompt based on mode
        if explain_mode:
            custom_prompt = f"""Analyze and fix this: {prompt}

RESPONSE STRUCTURE:
1. **Analysis**: Brief problem identification
2. **Explanation**: What's wrong and why
3. **Code**: Working solution with 2-3 word comments only
4. **Implementation**: How the fix works
5. **Summary**: Key points in 2-3 sentences

Keep each section concise and focused."""
        else:
            custom_prompt = f"""Fix this: {prompt}

RESPONSE STRUCTURE:
1. **Problem**: What's wrong (1 sentence)
2. **Code**: Clean solution with minimal comments
3. **Summary**: Brief explanation (1 sentence)

Be direct and concise."""
        
        # Stream response from DeepSeek-Coder
        full_response = ""
        try:
            response = ollama.generate(
                model="gemma3",
                prompt=custom_prompt,
                stream=True
            )
            
            for chunk in response:
                full_response += chunk["response"]
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            message_placeholder.error(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})