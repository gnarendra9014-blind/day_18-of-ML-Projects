# 🖋️ Day 18: Whiteboard to Code Converter

Part of the **25 Days of ML Projects** series. This AI-powered tool converts hand-drawn diagrams, whiteboards, or flowcharts into clean, production-ready code (Python or JavaScript) using Groq's latest Large Language Models.

---

## 🚀 Overview
Ever sketched a flowchart on a whiteboard and wished it could instantly become code? This project makes that possible. It uses:
1.  **Llama 4 Scout (Vision)**: To analyze the visual structure, shapes, and text of your diagram.
2.  **Llama 3.3 (Reasoner)**: To translate the visual description into structured, logical programming code.

## ✨ Features
- **Multimodal AI**: High-fidelity image analysis using native vision models.
- **Duo-Language Support**: Generate code in **Python** or **JavaScript**.
- **Instant Output**: Saves generated code directly to your local workspace.
- **Clean Structure**: Modular design for vision processing and code generation.

## 🛠️ Tech Stack
- **AI Platform**: [GroqCloud](https://console.groq.com/)
- **Vision Model**: `meta-llama/llama-4-scout-17b-16e-instruct`
- **Gen Model**: `llama-3.3-70b-versatile`
- **Language**: Python 3.x
- **Configuration**: `python-dotenv` for secure environment management.

---

## ⚙️ Setup & Installation

### 1. Prerequisites
- Python 3.8+
- A [Groq API Key](https://console.groq.com/keys)

### 2. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/gnarendra9014-blind/day_18-of-ML-Projects.git
cd day18-whiteboard-to-code
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory and add your API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🖥️ Usage
1.  **Prepare your image**: Save your whiteboard sketch or diagram as a `.jpg` or `.png`.
2.  **Run the app**:
    ```bash
    python app.py
    ```
3.  **Provide inputs**:
    - Enter the full path to your image.
    - Choose your preferred language (`python` or `js`).
4.  **Check Output**: The tool will print a description of your diagram, the generated code, and save a new file (e.g., `my_diagram_generated.py`) in your folder.

---

## 📁 Project Structure
```text
day18-whiteboard-to-code/
├── app.py             # Main entry point & CLI
├── vision.py          # Vision AI (Image description)
├── generator.py       # Code Synthesis (Text to Code)
├── requirements.txt   # Project dependencies
└── .env               # Environment secrets (Ignore in Git!)
```

## 📜 License
This project is part of the 25 Days of ML challenge and is open for educational use. 🚀
