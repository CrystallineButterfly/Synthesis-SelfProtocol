"""Project-specific context for Private Human Gate."""

        from __future__ import annotations

        PROJECT_CONTEXT = {
    "project_name": "Private Human Gate",
    "track": "SelfProtocol",
    "pitch": "A privacy-preserving human verification layer that must approve high-impact agent actions before any treasury or exchange workflow is planned.",
    "overlap_targets": [
        "Venice Private Agents",
        "MetaMask Delegations",
        "ENS",
        "Lido stETH Treasury",
        "Uniswap Agentic Finance",
        "Status L2"
    ],
    "goals": [
        "discover a bounded opportunity",
        "plan a dry-run-first action",
        "verify receipts and proofs"
    ]
}


        def seed_targets() -> list[str]:
            """Return the first batch of overlap targets for planning."""
            return list(PROJECT_CONTEXT['overlap_targets'])
