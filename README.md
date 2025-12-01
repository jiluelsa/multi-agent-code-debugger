⚡ Multi-Agent Code Debugger  
_A Lightweight Autonomous Bug-Fixing System Using Multi-Agent Architecture_

---

📌 Overview

Multi-Agent Code Debugger is a fully functional, multi-agent Python application that analyzes code, detects bugs, refactors issues, and runs automated tests — all through a clean web UI.

Built as a part of google's AI intensive course, it demonstrates:

- Multi-Agent system design  
- LLM-powered agent reasoning  
- Tool execution (pytest + filesystem access)  
- Flask-based UI  
- Memory logging & pipeline orchestration  

---

🧠 Problem Statement

Debugging software manually is slow and error-prone. Developers often struggle with:

- Detecting hidden bugs  
- Refactoring code cleanly  
- Repeatedly running tests  
- Understanding code behavior  

There is a need for an autonomous debugging assistant that can analyze, fix, and validate code end-to-end.

---

🚀 Solution Summary

This project uses four cooperating agents, each performing a specialized part of debugging:

🔹 1. Code Analyzer Agent  
Summarizes the structure, complexity, and potential issues in the input code.

🔹 2. Bug Finder Agent  
Identifies likely bugs using rule-based logic & LLM classification.

🔹 3. Refactor Agent (LLM-powered + rule-based)  
Fixes the detected bugs and generates cleaner code.

🔹 4. Test Runner Agent  
Runs tests using `pytest` and reports pass/fail results.

🔸 Bonus: Orchestrator  
A higher-level agent that coordinates multiple rounds of improvement until code becomes stable.

---

🏗️ Architecture Diagram

                              ┌───────────────────────┐
                    │      User / UI        │
                    │  (Flask Web Frontend) │
                    └─────────┬─────────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │  run_pipeline   │
                     │  Orchestrator   │
                     └─────────┬───────┘
                               │
         ┌─────────────────────┴─────────────────────┐
         │                                             │
         ▼                                             ▼
┌─────────────────┐                          ┌─────────────────┐
│ Code Analyzer   │                          │  Bug Finder     │
│ - Summarizes    │                          │ - Detects       │
│   structure     │                          │   bugs          │
│ - Finds issues  │                          │ - Debug prints  │
└─────────┬───────┘                          └─────────┬───────┘
          │                                              │
          └───────────────┐      ┌──────────────────────┘
                          ▼      ▼
                     ┌─────────────────┐
                     │ Refactor Agent  │
                     │ - Removes debug │
                     │   prints        │
                     │ - Fixes bugs    │
                     │ - Cleans code   │
                     └─────────┬───────┘
                               │
                               ▼
                     ┌─────────────────┐
                     │ Test Runner     │
                     │ - Runs pytest   │
                     │ - Reports pass/ │
                     │   fail results │
                     └─────────┬───────┘
                               │
                               ▼
                    ┌───────────────────────┐
                    │ Results Sent to UI     │
                    │ - Analysis            │
                    │ - Bugs Found          │
                    │ - Refactored Code     │
                    │ - Test Results        │
                    └───────────────────────┘


🧩 Features Implemented for the AI Agents Capstone

 ✔ Multi-Agent System  
- Analyzer agent  
- Bug finder agent  
- Refactor agent  
- Test runner agent  
- Orchestrator agent (optional loop execution)

 ✔ Tools  
- Uses filesystem tools (read/write, save refactored code)  
- Runs pytest as a testing tool  
- LLM API calls using Google Gemini  
- Multi-step pipeline combines 4 agents sequentially  

 ✔ Memory + State  
- Logger for agent actions  
- Orchestrator stores last run in memory  

 ✔ Context Engineering  
- Code summarized before LLM calls  
- Issues extracted to reduce LLM token load  

 ✔ Bonus Eligible  
- LLM use ✔  
- Deployable agent runtime via Flask ✔  
- Can be deployed on Cloud Run ✔  
- Video demo compatible ✔  

---

🌐 Web UI (Flask)

User can:

- Upload or paste Python code  
- Run debugging pipeline  
- View results in beautiful formatted cards  
- See analysis, detected bugs, refactored code, and test output  
- Includes animations & modern gradient design  

---

📁 Project Structure

multi-agent-code-debugger/
│
├── app.py # Flask web server
├── run_pipeline.py # Agent orchestration for UI
│
├── agents/
│ ├── code_analyzer.py
│ ├── bug_finder.py
│ ├── refactor_agent.py
│ ├── test_runner.py
│ ├── orchestrator.py
│
├── utils/
│ ├── file_manager.py
│ ├── logger.py
│
├── templates/
│ └── index.html # Web UI
│
├── static/
│ └── styles.css # Styling and animations
│
└── README.md


---

🛠️ Installation

```bash
git clone https://github.com/jiluelsa/multi-agent-code-debugger.git
cd multi-agent-code-debugger
pip install -r requirements.txt

Set your environment variable:
GOOGLE_API_KEY="your key here"

Run the app:
python app.py

Running Tests

Tests automatically run inside the TestRunner agent:
pytest -q

Example Input
def add(a, b):
    print("debugging...")  # remove this
    return a == b          # wrong logic


Output:

Debug print detected
Comparison misuse detected
Refactored code returned
Test results displayed

🎥 Screenshots:
# UI — Home Page
(screenshots/ui1.png)

# Multi-Agent Flow
(screenshots/ui2.png)
(screenshots/ui2.png)




👤 Team Members

Jilu Elsa Jacob

G Yadulal Bhaskar

Akhil P Shaji


