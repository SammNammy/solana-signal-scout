import json
import os
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from src.services.ace_client import AceClient
from src.services.synapse_client import SynapseClient
from src.services.x402_client import X402Client


console = Console()


def build_report(agent_profile, wallet, payment_context, analysis):
    return {
        "project": "Solana Signal Scout",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "target_wallet": wallet,
        "agent": {
            "id": agent_profile.agent_id,
            "name": agent_profile.name,
            "purpose": agent_profile.purpose,
            "created_at": agent_profile.created_at,
        },
        "payment_context": payment_context,
        "ace_analysis": {
            "summary": analysis.summary,
            "risk_score": analysis.risk_score,
            "opportunity_score": analysis.opportunity_score,
            "signals": analysis.signals,
            "recommendation": analysis.recommendation,
            "services_used": [
                {
                    "service_name": service.service_name,
                    "endpoint": service.endpoint,
                    "purpose": service.purpose,
                    "output": service.output,
                }
                for service in analysis.services_used
            ],
        },
        "autonomy_steps": [
            "Loaded agent configuration",
            "Registered autonomous agent identity",
            "Requested protected Solana intelligence resource",
            "Completed x402-style payment settlement",
            "Ran Gemini AI wallet analysis",
            "Ran Claude AI verification",
            "Generated Flux visual report concept",
            "Generated final decision report",
        ],
    }


def save_report(report):
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    json_path = reports_dir / "latest_report.json"
    md_path = reports_dir / "latest_report.md"

    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    services_text = "\n".join(
        f"- **{service['service_name']}**: `{service['endpoint']}` - {service['purpose']}"
        for service in report["ace_analysis"]["services_used"]
    )

    signals_text = "\n".join(
        f"- {signal}" for signal in report["ace_analysis"]["signals"]
    )

    steps_text = "\n".join(
        f"- {step}" for step in report["autonomy_steps"]
    )

    markdown = f"""# Solana Signal Scout Report

Generated at: {report["generated_at"]}

## Target Wallet

`{report["target_wallet"]}`

## Agent

- ID: `{report["agent"]["id"]}`
- Name: {report["agent"]["name"]}
- Purpose: {report["agent"]["purpose"]}

## Payment Context

- Resource: `{report["payment_context"]["resource"]}`
- Amount: {report["payment_context"]["amount_usdc"]} USDC
- Network: {report["payment_context"]["network"]}
- Status: {report["payment_context"]["payment_status"]}
- Facilitator: {report["payment_context"]["facilitator"]}

## Ace Data Cloud Services Used

{services_text}

## Ace Analysis

{report["ace_analysis"]["summary"]}

Risk score: **{report["ace_analysis"]["risk_score"]}/100**

Opportunity score: **{report["ace_analysis"]["opportunity_score"]}/100**

## Signals

{signals_text}

## Recommendation

**{report["ace_analysis"]["recommendation"]}**

## Autonomous Steps

{steps_text}
"""

    md_path.write_text(markdown, encoding="utf-8")

    return json_path, md_path


def render_console_report(report):
    console.print(Panel.fit("Solana Signal Scout completed an autonomous research run", title="Agent Run"))

    table = Table(title="Decision Report")
    table.add_column("Field")
    table.add_column("Value")

    table.add_row("Target Wallet", report["target_wallet"])
    table.add_row("Payment Status", report["payment_context"]["payment_status"])
    table.add_row("Ace Services", "Gemini AI, Claude AI, Flux Image Generation")
    table.add_row("Risk Score", str(report["ace_analysis"]["risk_score"]))
    table.add_row("Opportunity Score", str(report["ace_analysis"]["opportunity_score"]))
    table.add_row("Recommendation", report["ace_analysis"]["recommendation"])

    console.print(table)


def main():
    load_dotenv()

    agent_name = os.getenv("AGENT_NAME", "Solana Signal Scout")
    wallet = os.getenv("TARGET_WALLET", "DemoWallet111111111111111111111111111111111")
    ace_api_key = os.getenv("ACE_API_KEY", "demo-key")
    ace_base_url = os.getenv("ACE_API_BASE_URL", "https://api.acedata.cloud")
    synapse_agent_id = os.getenv("SYNAPSE_AGENT_ID", "demo-agent")
    payment_private_key = os.getenv("PAYMENT_PRIVATE_KEY", "demo-private-key")

    synapse = SynapseClient(agent_id=synapse_agent_id, agent_name=agent_name)
    x402 = X402Client(private_key=payment_private_key)
    ace = AceClient(api_key=ace_api_key, base_url=ace_base_url)

    agent_profile = synapse.register_agent()
    payment_context = x402.get_payment_context(resource=f"solana-wallet-intel:{wallet}")
    analysis = ace.analyze_wallet(wallet=wallet, payment_context=payment_context)

    report = build_report(
        agent_profile=agent_profile,
        wallet=wallet,
        payment_context=payment_context,
        analysis=analysis,
    )

    json_path, md_path = save_report(report)
    render_console_report(report)

    console.print(f"\nSaved JSON report: {json_path}")
    console.print(f"Saved Markdown report: {md_path}")


if __name__ == "__main__":
    main()
