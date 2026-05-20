# Solana Signal Scout

Solana Signal Scout is an autonomous Solana research agent demo built for the OOBE / Ace Data Cloud autonomous agent bounty.

The agent performs a full autonomous workflow:

1. Loads agent configuration
2. Registers a Synapse/OOBE-style agent identity
3. Requests a protected Solana wallet intelligence resource
4. Completes an x402-style payment step
5. Runs Ace Data Cloud-style analysis
6. Generates a wallet intelligence report
7. Serves the result in a local web dashboard

## Why This Project Exists

Most crypto research tools require a human to manually gather wallet data, pay for premium APIs, interpret signals, and write a report.

Solana Signal Scout turns that into a small autonomous workflow. The agent acts on its own, moves through a paid data access flow, analyzes the result, and produces a decision-ready report.

## Demo Commands

Install dependencies:

python -m pip install -r requirements.txt

Run the autonomous agent:

python -m src.agent.main

Or on Windows PowerShell:

.\scripts\run_agent.ps1

Start the web dashboard:

uvicorn src.web.app:app --reload

Then open:

http://127.0.0.1:8000

## What the Agent Produces

The report includes:

- Target Solana wallet
- Agent identity
- Payment status
- Paid resource name
- Risk score
- Opportunity score
- Signals
- Final recommendation
- Autonomous steps completed

Reports are saved to:

reports/latest_report.json
reports/latest_report.md

## Project Structure

src/
  agent/
    main.py
  services/
    ace_client.py
    synapse_client.py
    x402_client.py
  web/
    app.py

docs/
  demo_script.md
  submission.md

scripts/
  run_agent.ps1

## Notes

This demo is intentionally deterministic so judges can run it locally without private keys.

The service adapters are separated cleanly so live Ace Data Cloud, Synapse, and x402 integrations can be added without rewriting the agent loop.
