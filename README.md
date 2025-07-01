# ShellGPT

> Translate natural language into safe, executable Linux shell commands using AI.

**ShellGPT** is a command-line utility that converts human language (like _"find all large PDF files"_) into valid Linux shell commands, powered by the Cohere Command R+ language model. It also includes a built-in safety checker to prevent harmful or destructive commands from being run.

---

## Features

- Converts natural language tasks into Linux shell commands using AI
- Confirms before running any command
- Built-in safety checks to block dangerous commands (`rm -rf`, `dd`, fork bombs, etc.)
- Simple CLI interface
- Local `.env` support for secure API key management

---

## Demo

```
$ python shellgpt.py
Enter task (e.g., 'find all jpgs'): find all pdf files modified in last 2 days

[>] Suggested command:
find . -iname "*.pdf" -mtime -2

Run this command? (y/n): y

[i] Running command...

./report_2024.pdf
./slides/day2_notes.pdf
```

---

## Tech Stack

- Python 3.8+
- [Cohere Command R+](https://cohere.com/) (LLM)

---

## Safety First

ShellGPT uses a custom `safe_executor.py` module to block risky commands:

```python
DANGEROUS_KEYWORDS = ["rm", "shutdown", "reboot", ":(){", "dd", "mkfs", "wget", "curl"]
```

You can extend or customize this list in `safe_executor.py`.

---

## How to Use

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/shellgpt.git
cd shellgpt
```

### 2. Set up virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add your `.env` file
Create a file named `.env`:
```
COHERE_API_KEY=your_api_key_here
```

Get a free API key from [cohere.com](https://dashboard.cohere.com/api-keys).

### 4. Run the CLI tool
```bash
python shellgpt.py
```

## Sample Prompts

| Natural Language                             | Shell Command                                      |
|---------------------------------------------|----------------------------------------------------|
| Find all JPG images in Downloads            | find ~/Downloads -iname "*.jpg"                   |
| Show current memory usage                   | free -h                                            |
| List files over 100MB in /tmp               | find /tmp -type f -size +100M                      |
| Kill all Chrome processes                   | pkill chrome                                       |
| Search for "error" in log files             | grep -i "error" *.log                              |

---
