# Setup & Installation

### Prerequisites
- Python 3.10+
- Node.js & npm 
- Ollama (With qwen2.5:1.5b pulled)

### Installation
Clone the Repo:
- git clone https://github.com/Life-Atlas/lpi-agent.git
- cd lpi-agent

### Environment Setup:

- python -m venv venv
- venv\Scripts\activate  # Windows
- pip install -r requirements.txt

### LPI Server Build:
Ensure your lpi-developer-kit is built (npm run build). Update the path in agent.py to point to your local kit.

### Usage Example
Run the agent from the terminal to get an audit of your project:

Sample Input:  python agent.py "I have made a digital twin concept of a hospital room in Unity which shows patient changing colours based on its vitals. How does this align with SMILE?"

Sample Output :

```

PS C:\Users\G15\Documents\GitHub\lpi-agent> python agent.py "I have made a digital twin concept of a hospital room in Unity which shows patient changing colours based on its vitals. How does this align with SMILE?"
[LPI Sandbox] Server started — 7 read-only tools available
[*] Accessing LPI Methodology...
[DEBUG] Tool Call Evidence (Overview): # S.M.I.L.E. â€” Sustainable Methodology for Impact Lifecycl...
[DEBUG] Tool Call Evidence (Phase Detail): # Phase 1: Reality Emulation

## Duration
Days to Weeks

## ...

--- AUDIT ANALYSIS START ---

### Step 1: Determine Which SMILE Phase the User is Currently in

Based on the provided context, the user has created a digital twin concept of a hospital room in Unity which shows patient changing colors based on its vitals.

This indicates that the user is currently **Phase 1: Reality Emulation**. The reasoning is:
- **Reality Canvas**: The user has established a shared reality canvas for their project.
- **Duration and Description**: This phase describes creating a shared reality canvas with an emphasis on spatial-temporal understanding.
- **Key Activities and Deliverables**: These activities align well with the "Create a shared reality canvas" described in Source 1.

### Step 2: Explain Why, Using Specific Definitions from the Sources

The user has created a digital twin concept for a hospital room using Unity. This project is aligned closely with the first phase of SMILE methodology because it involves creating a shared reality canvas to establish where, when, and who on the planet.

Here’s how this aligns:

- **Source 1 Context**: "Create a shared reality canvas â€” establishing where, when, and who." The user has done just that by using Unity to visualize their concept in a shared environment.
- **Source 2 Context**: "Define the scope (as-is to to-be), invite stakeholders to innovate together, validate hypotheses virtually before committing resources." This phase is similar as it involves defining scope, inviting innovation, and validating ideas before physical implementation.

### Step 3: Identify What Technical Steps Are Needed to Reach the Next Phase

To progress from **Phase 1: Reality Emulation** to **Phase 2: Concurrent Engineering**, several technical steps are needed:

1. **Define the Scope (As-is to To-be)**:
   - Establish the current state of the hospital room and define its future improvements or changes.
   
2. **Inviting Stakeholders to Innovate Together and Validate Hypotheses Virtually**:
   - Collaborate with stakeholders through virtual user interaction, scenario planning, and validation exercises.
   
3. **Define a Minimal Viable Twin (MVT) for Validation**:
   - Develop a digital twin model that closely mirrors the hospital room concept to validate hypotheses before physical implementation.

4. **Emulate Virtual Scenarios**:
   - Create and simulate different scenarios using the MVT to test out ideas without physically modifying anything.
   
5. **Create an As-Is/To-BE Scope Document and Validation Hints**:
   - Document the current state of the room and prepare for future changes, ensuring validation is performed before physical implementation.

### Step 4: Mandatory Citations

This should be done at the end of each sentence to adhere to the audit requirement. The user can now reference specific parts from their project and its context with these citations:

- Reality Emulation (Source 1): Establish shared reality canvas
- Concurrent Engineering (Source 2): Define scope, invite innovation, validate hypotheses virtually

The final summary for clarity:
- "In order to think outside the box, one has to define the box first. What is the starting point and boundary of your sociotechnological ecosystem?" [Source 1]
- "What does the Minimal Viable Twin look like, and how do we validate it virtually before investing in physical implementation?" [Source 2]

============================================================
PROVENANCE: Data grounded via LPI MCP Server toolsets.
============================================================

```


