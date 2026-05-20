from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, Any


@dataclass
class PaymentReceipt:
    resource: str
    amount_usdc: float
    network: str
    status: str
    settled_at: str
    facilitator: str


class X402Client:
    """
    x402-style payment adapter.

    In production, this is where the agent would:
    1. Request a protected data resource
    2. Receive HTTP 402 payment requirements
    3. Sign payment authorization
    4. Submit through the facilitator
    5. Retry the resource request with payment proof

    For this bounty demo, the behavior is deterministic and local so judges
    can run it without private keys.
    """

    def __init__(self, private_key: str):
        self.private_key = private_key

    def pay_for_resource(self, resource: str, amount_usdc: float) -> PaymentReceipt:
        return PaymentReceipt(
            resource=resource,
            amount_usdc=amount_usdc,
            network="solana-mainnet-demo",
            status="settled",
            settled_at=datetime.now(timezone.utc).isoformat(),
            facilitator="ace-x402-facilitator-demo",
        )

    def get_payment_context(self, resource: str) -> Dict[str, Any]:
        receipt = self.pay_for_resource(resource=resource, amount_usdc=0.01)
        return {
            "resource": receipt.resource,
            "amount_usdc": receipt.amount_usdc,
            "network": receipt.network,
            "payment_status": receipt.status,
            "settled_at": receipt.settled_at,
            "facilitator": receipt.facilitator,
        }
