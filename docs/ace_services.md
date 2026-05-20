# Ace Data Cloud Services Used

For the Ace Data Cloud Usage category, Solana Signal Scout is designed around three distinct Ace Data Cloud services.

## Service 1: Gemini AI

Endpoint:

POST https://api.acedata.cloud/gemini/chat/completions

Purpose:

Gemini AI reviews the target Solana wallet activity and creates the first wallet intelligence summary.

## Service 2: Claude AI

Endpoints shown in Ace Data Cloud:

POST https://api.acedata.cloud/v1/chat/completions
POST https://api.acedata.cloud/claude/chat/completions

Purpose:

Claude AI performs a second-model verification pass. It checks whether the Gemini analysis is reasonable and flags risk or uncertainty.

## Service 3: Flux Image Generation

Endpoint:

POST https://api.acedata.cloud/flux/images

Purpose:

Flux generates a visual summary card for the agent report, useful for demos and X posts.

## Bounty Category

This project targets:

Ace Data Cloud Usage category

The intended workflow is:

Trigger -> SAP/OOBE-style agent identity -> x402 payment step -> Gemini analysis -> Claude verification -> Flux visual report -> final autonomous output.
