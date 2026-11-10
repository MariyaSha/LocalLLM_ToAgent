# Turn Local LLM into AI Agent with Python

Build a semi-autonomous AI agent using Python and free, locally running AI models!

This project demonstrates how to combine **🐍 Python Logic**, **🧠 AI Decisions**, and **✨ AI Generation** to automate repetitive workflows without paid AI APIs.

## 🎥 Video Tutorial

This repository contains the source code and project files from my Python Simplified video tutorial. I walk you through this repo step by step, building the Quickstart code together:

<a href="https://youtu.be/rYElE9GZudA" target="_blank"><img width="600" alt="Turn Local LLM into AI Agent with Python" src="https://github.com/user-attachments/assets/e46db13c-f850-45e4-a662-f0f477fdfebc"/></a>

## ⚙️ Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/MariyaSha/LocalLLM_ToAgent.git
cd LocalLLM_ToAgent

conda create -n local_agent python=3.12
conda activate local_agent

pip install -r requirements.txt
```

Make sure you have enough storage space for the models.

## 🐈 Project 1: QuickStart — Qwen + Flux

**Folder:** `quickstart/`

A beginner-friendly Jupyter notebook that demonstrates a simple AI agent loop.

- **Qwen** generates image descriptions and evaluates images.
- **Flux** generates images based on Qwen's descriptions.
- **Python** controls the loop until Qwen approves an image.

Open `quickstart/Quickstart.ipynb` in Jupyter or VS Code and follow the cells step by step. Such that:

To launch JupyterLab from the correct directory:

```bash
cd quickstart
jupyter lab
```

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

### Example Output

Here's an example of the agent running on an **NVIDIA RTX 5090 (32 GB VRAM)**. This is the exact output I received:

```text
🐍 Loading NVIDIA Nemotron...
You are using version 3 of 'kernels-community/liger-kernels', but version 4 is available.
WARNING:kernels._versions:You are using version 3 of 'kernels-community/mamba-ssm', but version 4 is available.
WARNING:kernels._versions:You are using version 3 of 'kernels-community/mamba-ssm', but version 4 is available.
WARNING:kernels._versions:You are using version 3 of 'kernels-community/mamba-ssm', but version 4 is available.
WARNING:kernels._versions:You are using version 3 of 'kernels-community/mamba-ssm', but version 4 is available.
WARNING:kernels._versions:You are using version 3 of 'kernels-community/mamba-ssm', but version 4 is available.
🐍 Nemotron loaded!

🐍 Searching businesses...
🧠 Choosing competitors...
   ✓ B.C HVAC
   ✓ Sundawn Integrated Services
⏱ Competitors selected (2.6s)

🐍 Exploring B.C HVAC...
🧠 Choosing pages...
   ✓ 8 pages selected (3.1s)
✨ Researching pages...
   ✓ https://bchvacservices.ca (15.2s)
   ✓ https://bchvacservices.ca/about (11.8s)
   ✓ https://bchvacservices.ca/priority-one (12.9s)
   ✓ https://bchvacservices.ca/priority-one-app (8.5s)
   ✓ https://bchvacservices.ca/services (15.0s)
   ✓ https://bchvacservices.ca/rebates (16.5s)
   ✓ https://bchvacservices.ca/service-areas (9.1s)
   ✓ https://bchvacservices.ca/contact (12.2s)
✨ Creating competitor overview...
🐍 Saved competitor_1.md (31.1s)

🐍 Exploring Sundawn Integrated Services...
🧠 Choosing pages...
   ✓ 8 pages selected (3.0s)
✨ Researching pages...
   ✓ https://sundawn.com (12.0s)
   ✓ https://sundawn.com/about/ (16.4s)
   ✓ https://sundawn.com/nationwide-hvac-services/ (16.5s)
   ✓ https://sundawn.com/hvac-services/ (7.5s)
   ✓ https://sundawn.com/boiler-service/ (14.2s)
   ✓ https://sundawn.com/refrigeration/ (13.1s)
   ✓ https://sundawn.com/cooling-towers/ (13.0s)
   ✓ https://sundawn.com/contact-us/ (9.2s)
✨ Creating competitor overview...
🐍 Saved competitor_2.md (23.4s)

✨ Creating final market research report...
🐍 Saved market_research.md (41.7s)

✓ Research complete!
⏱ Total execution time: 319.8s
```

**Total execution time: ~5.5 minutes**, excluding model initialization. Results and execution times will vary depending on your hardware and the websites being researched.