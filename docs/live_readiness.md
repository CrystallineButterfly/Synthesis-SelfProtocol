# Live readiness

- **Project:** Private Human Gate
- **Track:** SelfProtocol
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:18+00:00`

## Trust boundaries

- **SelfProtocol** — `rest_json` — Gate sensitive actions behind privacy-preserving proofs.
- **Venice** — `rest_json` — Run private reasoning over sensitive inputs.
- **MetaMask Delegations** — `contract_call` — Enforce delegation scopes, expiries, and intent envelopes.
- **ENS** — `contract_call` — Publish human-readable coordination and identity receipts.
- **Lido** — `contract_call` — Route staking yield through guarded treasury actions.
- **Uniswap** — `rest_json` — Quote swaps and bounded liquidity moves.
- **Status L2** — `rest_json` — Prepare gasless relay bundles for Status L2.

## Offline-ready partner paths

- **MetaMask Delegations** — prepared_contract_call
- **ENS** — prepared_contract_call
- **Lido** — prepared_contract_call

## Live-only partner blockers

- **SelfProtocol**: SELF_PROTOCOL_API_KEY, SELF_VERIFICATION_URL — https://docs.self.xyz/
- **Venice**: VENICE_API_KEY, VENICE_CHAT_COMPLETIONS_URL, VENICE_MODEL — https://docs.venice.ai/
- **Uniswap**: UNISWAP_API_KEY, UNISWAP_QUOTE_URL — https://developers.uniswap.org/
- **Status L2**: STATUS_RPC_URL, STATUS_RELAYER_URL — https://status.app/

## Highest-sensitivity actions

- `selfprotocol_zk_verify` — SelfProtocol — Use SelfProtocol for a bounded action in this repo.
- `venice_private_analysis` — Venice — Use Venice for a bounded action in this repo.
- `metamask_delegations_delegate_scope` — MetaMask Delegations — Use MetaMask Delegations for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for SelfGateRegistry.
- Run python3 scripts/run_agent.py to produce a dry run for self_gate.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
