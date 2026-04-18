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

[LPI Sandbox] Server started — 7 read-only tools available
### Determine Which SMILE Phase the User is Currently in

The user's project of a digital twin concept of a hospital room in Unity shows alignment with several aspects of the SMILE methodology. Specifically, it is aligned with **Phase 1: Reality Emulation**.

### Explain Why Using Specific Definitions from the Sources

The project revolves around creating a shared reality canvas for understanding and visualizing a hospital room environment. This aligns with defining the "where, when, and who" of the sociotechnological ecosystem in Phase 1 of SMILE.

- **Source 2**: The user is clearly working on establishing a shared reality canvas in **Phase 1**.
  
### Identify Technical Steps Needed to Reach the Next Phase

To progress from **Phase 1: Reality Emulation** to **Phase 2: Concurrent Engineering**, the user will need to:

1. **Define Scope (As-is to To-be)**:
   - Define the current and future state of the hospital room as a digital twin concept.
   
2. **Invite Stakeholders to Innovate Together**:
   - Involve stakeholders in the process of innovation and conceptualizing the new hospital room.

3. **Validate Hypotheses Virtually Before Committing Resources**:
   - Use virtual simulations to validate ideas before committing resources for physical implementation.

4. **Establish Collective Truth**:
   - Connect with stakeholders through a shared reality canvas, establishing what everyone can agree on as truth.

5. **Define the Minimal Viable Twin (MVT)** and Feedback Loops:
   - Define an MVP for the hospital room concept.
   - Establish feedback loops to ensure that the digital twin accurately reflects the physical environment.

### CITATIONS

- **Source 2**: "In order to think outside the box, one has to define the box first. What is the starting point and boundary of your sociotechnological ecosystem?"
  - The user is defining boundaries and scope for their project.
  
- **Source 3**: "What does the Minimal Viable Twin look like, and how do we validate it virtually before investing in physical implementation?"
  - This aligns with validating hypotheses through virtual simulations before committing resources.

By following these steps, the user can progress from Phase 1 to Phase 2 of SMILE's methodology.

```


