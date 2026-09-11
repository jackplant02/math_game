# Math Quiz

A terminal-based math game challenge with 8 questions, increasing in difficulty from basic arithmetic to multivariable calculus and differential equations. 

Math problems are randomly generated. 

## Math Topics (The Questions)
1. **Arithmetic:** Addition and subtraction
2. **Multiplication:** Basic integer multiplication
3. **Algebra:** Finding roots of quadratic equations
4. **Calculus I:** Evaluating first derivatives of polynomials
5. **Linear Algebra:** Computing vector dot products
6. **Calculus II:** Finding the enclosing area between two curves (integration)
7. **Multivariable Calculus:** Computing directional derivatives of $f(x,y)$
8. **Differential Equations:** Solving systems of linear homogeneous differential equations (Initial Value Problems)

The game also tracks your score out of 8, and prevents you from re-answering already correctly answered questions. 

## Installation and Running

### Option 1: Standalone Executable 
Pre-compiled executables are available for Windows, macOS, and Linux.

1. Navigate to the [Releases](https://github.com/jackplant02/math_game/releases) tab.
2. Download the `.zip` or `.tar.gz` file that matches your operating system and processor architecture.
3. Extract the downloaded file.
4. **On Windows:** Double-click the extracted executable to play.
5. **On Linux:** Open your terminal, navigate to the folder, and run the file.

**Note for macOS Users (Gatekeeper Bypass):**
Because this app is an open-source project, macOS will flag it as unidentified/unverifiable.
* Double-click the extracted executable. A pop-up will appear stating that the app could not be opened.
* Open **Privacy & Security** in your macOS Settings.
* Scroll down to the bottom of the page, and you will see a notification that says '"mathquiz" was blocked to protect your Mac.'
* Click 'Open Anyway' next to this message.
* In the pop-up that appears, click 'Open Anyway', and authenticate.
* You only need to do this the first time you run the app.

### Option 2: Install via Python
Ensure you have Python 3 installed on your system.

1. Clone this repository:
```bash
git clone https://github.com/jackplant02/math_game.git
cd math_game
```

2. Create and activate a virtual environment
```bash
# On macOS and Linux:
python3 -m venv venv
source venv/bin/activate

# On Windows (Command Prompt):
python -m venv venv
venv\Scripts\activate
```

3. Install the game locally:
```bash
pip install -e .
```

3. Run the game:
```bash
mathquiz
``` 
