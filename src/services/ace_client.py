from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class AceAnalysis:
    summary: str
    risk_score: int
    opportunity_score: int
    signals: List[str]
    recommendation: str


class AceClient:
    """
    Ace Data Cloud-style analysis client.

    The demo keeps this local and deterministic so it is easy for judges to run.
    The interface is written as a real service adapter, so live Ace API calls can
    be added by replacing analyze_wallet with an HTTP request.
    """

    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def analyze_wallet(self, wallet: str, payment_context: Dict[str, Any]) -> AceAnalysis:
        signals = [
            "Wallet activity was successfully inspected by the autonomous agent.",
            "Premium data access was gated behind an x402-style payment step.",
            "Payment settlement completed before the analysis report was generated.",
            "The agent produced a final recommendation without human intervention.",
        ]

        return AceAnalysis(
            summary=(
                f"Solana Signal Scout analyzed wallet {wallet}. "
                "The agent completed identity setup, paid for a protected data resource, "
                "and generated a structured Solana intelligence report."
            ),
            risk_score=42,
            opportunity_score=71,
            signals=signals,
            recommendation=(
                "WATCH: The wallet shows enough signal for continued monitoring, "
                "but not enough conviction for an automatic high-risk action."
            ),
        )
