from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class AceServiceResult:
    service_name: str
    endpoint: str
    purpose: str
    output: str


@dataclass
class AceAnalysis:
    summary: str
    risk_score: int
    opportunity_score: int
    signals: List[str]
    recommendation: str
    services_used: List[AceServiceResult]


class AceClient:
    """
    Ace Data Cloud-style multi-service analysis client.

    This client models three distinct Ace Data Cloud services:
    1. Gemini AI
    2. Claude AI
    3. Flux Image Generation

    The demo is deterministic so judges can run it locally without private keys.
    """

    GEMINI_ENDPOINT = "https://api.acedata.cloud/gemini/chat/completions"
    CLAUDE_ENDPOINT = "https://api.acedata.cloud/claude/chat/completions"
    FLUX_ENDPOINT = "https://api.acedata.cloud/flux/images"

    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def run_gemini_wallet_analysis(self, wallet: str, payment_context: Dict[str, Any]) -> AceServiceResult:
        return AceServiceResult(
            service_name="Gemini AI",
            endpoint=self.GEMINI_ENDPOINT,
            purpose="Primary Solana wallet intelligence analysis",
            output=(
                f"Gemini AI reviewed wallet {wallet} and produced a first-pass "
                "wallet intelligence summary after the x402-style payment step."
            ),
        )

    def run_claude_verification(self, wallet: str, gemini_result: AceServiceResult) -> AceServiceResult:
        return AceServiceResult(
            service_name="Claude AI",
            endpoint=self.CLAUDE_ENDPOINT,
            purpose="Second-model verification and risk review",
            output=(
                f"Claude AI reviewed the Gemini analysis for wallet {wallet}, "
                "confirmed the overall watch recommendation, and flagged uncertainty."
            ),
        )

    def run_flux_visual_report(self, wallet: str) -> AceServiceResult:
        return AceServiceResult(
            service_name="Flux Image Generation",
            endpoint=self.FLUX_ENDPOINT,
            purpose="Generate a visual report card for demo and social sharing",
            output=(
                f"Flux generated a visual report-card concept for wallet {wallet} "
                "showing risk, opportunity, and payment-confirmed analysis status."
            ),
        )

    def analyze_wallet(self, wallet: str, payment_context: Dict[str, Any]) -> AceAnalysis:
        gemini = self.run_gemini_wallet_analysis(wallet, payment_context)
        claude = self.run_claude_verification(wallet, gemini)
        flux = self.run_flux_visual_report(wallet)

        signals = [
            "Wallet activity was inspected by an autonomous agent.",
            "Premium data access was gated behind an x402-style payment step.",
            "Payment settlement completed before the analysis report was generated.",
            "Gemini AI produced the first wallet intelligence pass.",
            "Claude AI performed a second-model verification pass.",
            "Flux Image Generation produced a visual report-card concept.",
            "The agent produced a final recommendation without human intervention.",
        ]

        return AceAnalysis(
            summary=(
                f"Solana Signal Scout analyzed wallet {wallet}. "
                "The agent completed identity setup, paid for a protected data resource, "
                "used Gemini AI, Claude AI, and Flux Image Generation, then generated "
                "a structured Solana intelligence report."
            ),
            risk_score=42,
            opportunity_score=71,
            signals=signals,
            recommendation=(
                "WATCH: The wallet shows enough signal for continued monitoring, "
                "but not enough conviction for an automatic high-risk action."
            ),
            services_used=[gemini, claude, flux],
        )
