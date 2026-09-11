# Math Quiz

A terminal-based math game challenge with 8 questions, increasing in difficulty from basic arithmetic to multivariable calculus and differential equations. 

Math problems are randomly generated, meaning that you will almost never see the exact same problem twice. 

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

### Option 1: macOS Standalone (Apple Silicon Only)
If you are on an M-Series Mac, you can run the game without installing Python.

1. Download the latest macOS `.zip` release from the [Releases](https://github.com/jackplant02/math_game/releases) tab.
2. Unzip the file to extract the `mathquiz` executable
3. Bypass macOS Security (Gatekeeper). Because this app is an open-source project, macOS will flag it as unidentified/unverifiable.
   * Double click the `mathquiz` executable. A pop-up will appear stating that the app could not be opened.
   * Open **Privacy & Security** in your macOS Settings.
   * Scroll down to the bottom of the page, and you will see a notification that says '"mathquiz" was blocked to protect your Mac.'
   * Click 'Open Anyway' next to this message.
   * In the pop-up that appears, click "Open Anyway", and authenticate.
   * You only need to do this the first time you run the app.

### Option 2: Run via Python (Windows, Linux, and Intel Macs)
Ensure you have Python 3 installed on your system.

1. Clone this repository:
```bash
git clone https://github.com/jackplant02/math_game.git
cd math_game
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
# On macOS and Linux
python3 math_game.py

# On Windows:
python math_game.py
```
