# Private Human Gate

        **Repo:** `Synthesis-SelfProtocol`  
        **Primary track:** SelfProtocol  
        **Submission hold:** wait for human approval before registration or live submission.

        A privacy-preserving human verification layer that must approve high-impact agent actions before any treasury or exchange workflow is planned.

        ## Selected concept

        This repo places privacy-preserving human verification in front of high-impact agent actions. A guard contract records proof attestations and policy windows, while Python middleware ensures no treasury or exchange action is planned without a valid identity check.

        ## Idea set

        1. ZK Human Check for Treasury Actions
2. Privacy-Preserving Operator Approval
3. Consent-Bound Agent Identity

        ## Prize overlap targets

        - Venice Private Agents
- MetaMask Delegations
- ENS
- Lido stETH Treasury
- Uniswap Agentic Finance
- Status L2

        ## Architecture

        ```mermaid
        flowchart TD
    Signals[SelfProtocol signals] --> Discover[Discover]
    Discover --> Plan[Plan bounded action]
    Plan --> DryRun[Dry run + policy check]
    DryRun --> Guard[SelfGateRegistry]
    Guard --> Execute[Execute when live mode is enabled]
    Execute --> Verify[Verify proofs + receipts]
    Verify --> Persist[Write agent_log.json + submission snippet]
    Persist --> Storage[Store proof plan for Filecoin / receipts]
        ```

        ## Repo structure

        ```text
        Synthesis-SelfProtocol/
├── README.md
├── LICENSE
├── .env.example
├── .gitignore
├── agent.json
├── agent_log.json
├── pyproject.toml
├── Makefile
├── docs/
│   ├── architecture.mmd
│   ├── demo_video_script.md
│   └── security.md
├── src/
│   └── SelfGateRegistry.sol
├── script/
│   └── Deploy.s.sol
├── agents/
│   ├── __init__.py
│   └── self_gate.py
├── scripts/
│   ├── run_agent.py
│   └── plan_live_demo.py
├── submissions/
│   └── synthesis.md
└── tests/
    └── test_project_context.py
        ```

        ## Tech stack

        Solidity 0.8.24 skeleton, Python 3.13 standard library, JSON manifests, Foundry-style layout, MIT license

        ## Security guardrails

        - principal and spend policies are separated by design
        - whitelist, cap, and cooldown checks gate every action
        - dry-run hashes are recorded before any live execution path
        - compute budgets are explicit and live mode is opt-in
        - secrets are loaded from environment variables only
        - structured logs are appended for every discover-plan-execute-verify step

        ## Autonomy loop

        1. Discover candidate signals and external state.
2. Plan an action bundle with explicit budget, target, and purpose.
3. Run a dry-run check and policy validation before any execution path.
4. Execute only when live mode, wallets, and credentials are supplied.
5. Verify receipts, proofs, and notes, then append structured logs.

        ## Local MVP status

        - [x] README, manifests, and security notes created
        - [x] contract and agent-loop skeletons created
        - [x] local git repository initialized with an initial commit
        - [ ] operator wallet addresses attached
        - [ ] real API keys added through `.env`
        - [ ] live TxIDs recorded
        - [ ] registration and submission executed

        ## Live demo and TxID plan

        1. load real credentials into `.env`
        2. run `python3 scripts/plan_live_demo.py` to print the checklist
        3. replace placeholder wallet fields in `agent.json`
        4. enable `LIVE_MODE=true` for controlled execution
        5. record resulting TxIDs and paste them into `submissions/synthesis.md`

        ## Why this ranks first

        This concept ranks highest because it overlaps Venice Private Agents, MetaMask Delegations, ENS while keeping the
        execution envelope explicit, dry-run-first, and honest about what still needs
        real credentials before anything touches a chain.
