# Turn Local LLM into AI Agent with Python

Build a semi-autonomous AI agent using Python and free, locally running AI models!

This project demonstrates how to combine **🐍 Python Logic**, **🧠 AI Decisions**, and **✨ AI Generation** to automate repetitive workflows without paid AI APIs.

## ⚙️ Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/MariyaSha/LocalLLM_ToAgent.git
cd LocalLLM_ToAgent
pip install -r requirements.txt
```

Make sure you have enough storage space for the models.

## 🐈 Project 1: QuickStart — Qwen + Flux

**Folder:** `quickstart/`

A beginner-friendly Jupyter notebook that demonstrates a simple AI agent loop.

- **Qwen** generates image descriptions and evaluates images.
- **Flux** generates images based on Qwen's descriptions.
- **Python** controls the loop until Qwen approves an image.

Open `quickstart/Quickstart.ipynb` in Jupyter or VS Code and follow the cells step by step.

🤖 **Models:** Qwen3-VL-8B-Instruct + FLUX.1-schnell  
💾 **Storage:** ~50 GB combined

## 🚀 Project 2: Market Research Agent — NVIDIA Nemotron

**Files:** `app.py`, `tools.py`, `prompts/`

A real-world AI agent that searches for local businesses, selects competitors, researches their websites, and generates detailed market research reports.

The workflow uses five reusable Markdown prompts and Python to control when Nemotron makes decisions or generates content.

**Run from the repository root:**

```bash
python app.py
```

To customize your research, edit `CITY` and `TRADE` at the top of `app.py`.

🤖 **Model:** NVIDIA Nemotron Nano 9B v2  
💾 **Storage:** ~18 GB

The agent generates `competitor_1.md`, `competitor_2.md`, and `market_research.md`.
