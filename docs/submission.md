# Submission Notes

## Project Name

Solana Signal Scout

## Category

Ace Data Cloud Usage category

## One-line Description

An autonomous Solana research agent that uses Synapse/OOBE-style agent identity, x402-style paid access, and three Ace Data Cloud services to produce a wallet intelligence report.

## What It Does

Solana Signal Scout performs a complete autonomous workflow:

1. Loads agent configuration
2. Registers a Synapse/OOBE-style autonomous agent identity
3. Requests a protected Solana wallet intelligence resource
4. Completes an x402-style payment step
5. Runs Gemini AI for primary wallet analysis
6. Runs Claude AI for second-model verification
7. Runs Flux Image Generation for a visual report-card concept
8. Generates a final wallet intelligence report
9. Displays the result in a local web dashboard

## Ace Data Cloud Services Used

1. Gemini AI  
   Endpoint: POST https://api.acedata.cloud/gemini/chat/completions

2. Claude AI  
   Endpoint: POST https://api.acedata.cloud/claude/chat/completions

3. Flux Image Generation  
   Endpoint: POST https://api.acedata.cloud/flux/images

## Demo Command

python -m src.agent.main

## Web Dashboard Command

uvicorn src.web.app:app --reload

Then open:

http://127.0.0.1:8000

## GitHub Repository

https://github.com/SammNammy/solana-signal-scout
