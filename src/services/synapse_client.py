from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class AgentProfile:
    agent_id: str
    name: str
    purpose: str
    created_at: str


class SynapseClient:
    """
    Lightweight OOBE/Synapse-style agent identity adapter.

    The demo uses this adapter to create a clear autonomous-agent identity
    without requiring live mainnet credentials during local judging.
    """

    def __init__(self, agent_id: str, agent_name: str):
        self.agent_id = agent_id
        self.agent_name = agent_name

    def register_agent(self) -> AgentProfile:
        return AgentProfile(
            agent_id=self.agent_id,
            name=self.agent_name,
            purpose="Autonomous Solana research and signal generation",
            created_at=datetime.now(timezone.utc).isoformat(),
        )
