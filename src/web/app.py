from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
import json


app = FastAPI(title="Solana Signal Scout")


@app.get("/", response_class=HTMLResponse)
def home():
    report_path = Path("reports/latest_report.json")

    if report_path.exists():
        report = json.loads(report_path.read_text(encoding="utf-8"))
    else:
        report = {
            "project": "Solana Signal Scout",
            "target_wallet": "Run the agent first with: python -m src.agent.main",
            "payment_context": {
                "payment_status": "not generated yet",
                "amount_usdc": "n/a",
                "network": "n/a",
            },
            "ace_analysis": {
                "summary": "No report has been generated yet.",
                "risk_score": "n/a",
                "opportunity_score": "n/a",
                "recommendation": "Run the agent to create a report.",
                "signals": [],
                "services_used": [],
            },
            "autonomy_steps": [],
        }

    services = "".join(
        f"""
        <li>
          <strong>{service["service_name"]}</strong><br />
          <code>{service["endpoint"]}</code><br />
          <span>{service["purpose"]}</span>
        </li>
        """
        for service in report["ace_analysis"].get("services_used", [])
    )

    signals = "".join(f"<li>{signal}</li>" for signal in report["ace_analysis"]["signals"])
    steps = "".join(f"<li>{step}</li>" for step in report["autonomy_steps"])

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Solana Signal Scout</title>
        <style>
          body {{
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            margin: 0;
            padding: 40px;
          }}
          .card {{
            max-width: 980px;
            margin: 0 auto;
            background: #111827;
            border: 1px solid #334155;
            border-radius: 20px;
            padding: 28px;
            box-shadow: 0 20px 80px rgba(0,0,0,0.35);
          }}
          h1 {{ color: #93c5fd; }}
          h2 {{ color: #bfdbfe; margin-top: 28px; }}
          code {{
            background: #1e293b;
            padding: 3px 6px;
            border-radius: 6px;
            word-break: break-word;
          }}
          .metrics {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            margin-top: 20px;
          }}
          .metric {{
            background: #1e293b;
            padding: 16px;
            border-radius: 14px;
          }}
          .label {{ color: #94a3b8; font-size: 13px; }}
          .value {{ font-size: 24px; font-weight: bold; margin-top: 6px; }}
          li {{ margin-bottom: 12px; }}
        </style>
      </head>
      <body>
        <main class="card">
          <h1>Solana Signal Scout</h1>
          <p>Autonomous Solana wallet research agent using Synapse/OOBE-style identity, x402-style payments, and three Ace Data Cloud services.</p>

          <h2>Target Wallet</h2>
          <code>{report["target_wallet"]}</code>

          <div class="metrics">
            <div class="metric">
              <div class="label">Payment Status</div>
              <div class="value">{report["payment_context"]["payment_status"]}</div>
            </div>
            <div class="metric">
              <div class="label">Risk Score</div>
              <div class="value">{report["ace_analysis"]["risk_score"]}</div>
            </div>
            <div class="metric">
              <div class="label">Opportunity Score</div>
              <div class="value">{report["ace_analysis"]["opportunity_score"]}</div>
            </div>
          </div>

          <h2>Ace Data Cloud Services Used</h2>
          <ul>{services}</ul>

          <h2>Analysis</h2>
          <p>{report["ace_analysis"]["summary"]}</p>

          <h2>Recommendation</h2>
          <p><strong>{report["ace_analysis"]["recommendation"]}</strong></p>

          <h2>Signals</h2>
          <ul>{signals}</ul>

          <h2>Autonomous Steps</h2>
          <ul>{steps}</ul>
        </main>
      </body>
    </html>
    """
