# Section 7: Explore GitHub Copilot Chat

## Guide: Using GitHub Copilot Chat in Visual Studio Code

GitHub Copilot Chat is a powerful feature that lets you interact with AI directly in your editor, ask questions, get code suggestions, and automate tasks. Here’s a practical guide to making the most of Copilot Chat:

### 1. Setting Up

- **Install the Python Extension:**
  - Open the Extensions panel in VS Code.
  - Search for "Python" (by Microsoft) and click Install.
- **Open Relevant Files:**
  - Use the Explorer panel to open the files you want to work with (e.g., `addition.py`, `subtraction.py`).

### 2. Opening Copilot Chat

- Click the chat icon on the left sidebar to open the Copilot Chat window.

### 3. Using Agents

- **Workspace Agent:**
  - Type `@workspace` to interact with your project’s structure and files.
  - Example: `@workspace what's my current folder structure?`
- **VS Code Agent:**
  - Type `@vscode` to get help from VS Code documentation.
  - Example: `@vscode what's the shortcut to open a file?`
- **Terminal Agent:**
  - Type `@terminal` for terminal-related questions.
  - Example: `@terminal how do I run a Python file?`

### 4. Providing Context

- Use hash commands to give Copilot context:
  - `#editor` — Uses the active file’s content.
  - `#file` — Lets you select a file from your project.
  - `#selection` — Uses the currently selected text in the editor.
  - `#terminalLastCommand` — Uses your last terminal command.
  - `#terminalSelection` — Uses selected text in the terminal.

### 5. Using Slash Commands

- **/explain** — Explains selected code or the active file.
- **/fix** — Finds and fixes issues in the active file.
- **/new** — Creates a new workspace or project based on your input.
- **/test** — Generates test cases for selected code or the active file.
- **/clear** — Clears the chat window.
- **/notebook** — Creates a new Jupyter notebook based on your input.

### 6. Example Workflows

- **Generate a Microservice:**
  - `/new a Python microservice for the addition and subtraction files in Lesson 1, video 3.`
  - Copilot will generate a new folder structure, files, and a README.
- **Create Unit Tests:**
  - Select code or a file, then type `/test` to generate unit tests quickly.
- **Explain or Fix Code:**
  - Use `/explain` or `/fix` for instant help with understanding or correcting code.

### 7. Tips

- You can preview generated files before creating a new workspace.
- Use the chat window to automate repetitive tasks and get instant documentation or code help.
- Clear the chat window with `/clear` to keep things organized.

---

By following these steps, you can leverage GitHub Copilot Chat to streamline your development workflow, automate tasks, and get real-time coding assistance—all within Visual Studio Code.