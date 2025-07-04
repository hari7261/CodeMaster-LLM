# 🚀 CodeMaster-LLM

An intelligent code helper application built with Streamlit that combines a live code editor, terminal execution, and AI-powered assistance for multiple programming languages.

## ✨ Features

- **📝 Interactive Code Editor** - Syntax highlighting for Python, JavaScript, Java, C++, and Go
- **⚡ Live Code Execution** - Run Python code instantly with real-time output
- **🤖 AI Assistant** - Get intelligent help with coding questions and debugging
- **💬 Chat Interface** - Persistent conversation history with context awareness
- **🔧 Terminal Integration** - Execute code with proper error handling and timeout protection
- **🎛️ Customizable Settings** - Toggle between explanation modes and clear chat history

## 🖼️ Screenshots

### Main Interface
![CodeMaster-LLM Interface](/Screenshot%202025-07-04%20152428.png)
*Clean and intuitive interface with code editor, terminal, and chat*

### AI Assistant in Action
![AI Assistant](/Screenshot%202025-07-04%20152453.png)
*Structured responses with analysis, code fixes, and explanations*

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/hari7261/CodeMaster-LLM.git
cd CodeMaster-LLM
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Install Ollama** (for AI functionality)
   - Download from [ollama.ai](https://ollama.ai)
   - Install the required model:
```bash
ollama pull gemma3
```

4. **Run the application**
```bash
streamlit run app.py
```

## 📋 Requirements

Create a `requirements.txt` file with:
```
streamlit>=1.46.0
ollama>=0.5.0
streamlit-code-editor>=0.1.22
```

## 🚀 Usage

1. **Code Editor**: Write your code in the left panel with syntax highlighting
2. **Run Code**: Click "Run Code" to execute Python scripts in the terminal
3. **AI Chat**: Ask questions about programming, get code fixes, and explanations
4. **Settings**: Toggle explanation modes and manage chat history

## 🎯 AI Response Structure

The AI provides structured responses:

### Explain Mode ON:
- **Analysis**: Problem identification
- **Explanation**: What's wrong and why
- **Code**: Clean solution with minimal comments
- **Implementation**: How the fix works
- **Summary**: Key takeaways

### Explain Mode OFF:
- **Problem**: Quick issue identification
- **Code**: Direct solution
- **Summary**: Brief explanation

## 🔧 Configuration

- **Python Path**: Automatically detects your Python installation
- **Timeout**: 10-second execution limit for safety
- **Languages**: Support for Python execution (others for syntax highlighting)
- **AI Model**: Uses Gemma3 via Ollama

## 📂 Project Structure

```
CodeMaster-LLM/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── screenshot1.png    # Interface screenshot
└── screenshot2.png    # AI assistant screenshot
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit** - For the amazing web framework
- **Ollama** - For local AI model execution
- **streamlit-code-editor** - For the code editor component

## 📧 Contact

**Hariom Kumar** - [@hari7261](https://github.com/hari7261)

Project Link: [https://github.com/hari7261/CodeMaster-LLM](https://github.com/hari7261/CodeMaster-LLM)

---

⭐ If you found this project helpful, please give it a star!
