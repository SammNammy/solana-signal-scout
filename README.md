# Solana Signal Scout

Solana Signal Scout is an autonomous Solana research agent demo built for the OOBE / Ace Data Cloud autonomous agent bounty.

This project targets the Ace Data Cloud Usage category.

The bounty asks agents in this category to use x402 with Ace Data Cloud's payment facilitator and use at least 3 distinct Ace Data Cloud services. This repo currently documents and models the 3-service workflow with Gemini AI, Claude AI, and Flux Image Generation.

## Autonomous Workflow

The agent performs this flow:

1. Loads agent configuration
2. Registers a Synapse/OOBE-style agent identity
3. Requests a protected Solana wallet intelligence resource
4. Completes an x402-style payment step
5. Runs Gemini AI for primary wallet analysis
6. Runs Claude AI for second-model verification
7. Runs Flux Image Generation for a visual report-card concept
8. Generates a final wallet intelligence report
9. Serves the result in a local web dashboard

## Ace Data Cloud Services

### 1. Gemini AI

Endpoint:

POST https://api.acedata.cloud/gemini/chat/completions

Purpose:

Primary Solana wallet intelligence analysis.

### 2. Claude AI

Endpoint:

POST https://api.acedata.cloud/claude/chat/completions

Purpose:

Second-model verification and risk review.

### 3. Flux Image Generation

Endpoint:

POST https://api.acedata.cloud/flux/images

Purpose:

Visual report-card generation for demo and social sharing.

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
- Ace services used
- Risk score
- Opportunity score
- Signals
- Final recommendation
- Autonomous steps completed

Reports are generated locally at:

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
  ace_services.md
  demo_script.md
  submission.md

scripts/
  run_agent.ps1

## Notes

This demo is intentionally deterministic so judges can run it locally without private keys.

The service adapters are separated cleanly so live Ace Data Cloud, Synapse, and x402 integrations can be added without rewriting the agent loop.
