# Python Training Project

A clean and reproducible Python development environment setup.

## Project Structure
```text
python-training/
│
├── env/               # Python Virtual Environment (Not tracked by Git)
├── src/               # Application source code
├── tests/             # Unit tests folder
├── docs/              # Project documentation
├── logs/              # System/application logs
├── .gitignore         # Files to ignore in Git
├── README.md          # Project documentation and setup guide
└── requirements.txt   # Third-party project dependencies
```

## Environment Requirements
- **Python Version:** 3.12.10

## Setup Instructions

Follow these step-by-step instructions to recreate and run the development environment on your local machine.

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd python-training
```

### 2. Create the Virtual Environment
Create an isolated virtual environment inside the project directory:
```bash
py -3.12 -m venv env
```

### 3. Activate the Virtual Environment
Activate the environment based on your Operating System:
- **Windows (Command Prompt):**
  ```cmd
  env\Scripts\activate
  ```
- **Windows (PowerShell):**
  ```powershell
  .\env\Scripts\Activate.ps1
  ```
- **macOS / Linux:**
  ```bash
  source env/bin/activate
  ```

Once activated, your terminal prompt will show `(env)`.

### 4. Install Dependencies
Install all required third-party libraries using pip:
```bash
pip install -r requirements.txt
```

### 5. Running the Project
To run the main application from the source directory:
```bash
python src/main.py
```

### 6. Running Tests
To execute unit tests using pytest, run:
```bash
pytest
```
 
