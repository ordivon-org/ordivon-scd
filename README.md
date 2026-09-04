> **Modification notice (Apache-2.0 §4(b)):** This file contains changes from an Apache-2.0-licensed upstream version in `ordivon-computing`.

# Semantics of Computational Descriptions — Research Core

Canonical owner/project: **Semantics of Computational Descriptions (SCD)**.

Historical alias: owner line S.

Current invariants:

- `Foundation0 = NONE`; `SCDF0` does not exist.
- `SCDF1–SCDF10` are immutable registry identities; number encodes identity only.
- FROZEN: `SCDF1`, `SCDF3`, `SCDF6`, `SCDF7`, `SCDF8`, `SCDF9`, `SCDF10`.
- OPEN at individual Foundation depth: `SCDF2`, `SCDF4`, `SCDF5`.
- `SCDF2 ↔ SCDF5 ↔ SCDF10 Boundary Architecture v1` is FROZEN.
- `FamilyMapLocalClosure = ADMITTED`.
- `WholeSExhaustiveComplete = UNKNOWN`.
- `ResearchOrderSCDF = UNKNOWN`.
- Canonical architecture: typed responsibility hypergraph, not a rooted Foundation tree.

Start with [OWNER-BOUNDARY-AND-STATUS](OWNER-BOUNDARY-AND-STATUS.md) and [SCDF-REGISTRY-AND-STANDING](SCDF-REGISTRY-AND-STANDING.md).

### Source horizon and `CURRENT.json`

For a present-tense claim about **current SCD owner research standing**, first resolve the canonical upstream repository `main` after explicitly observing remote freshness; in the current Git topology this is the fetched commit corresponding to `origin/main`. Only then should that source horizon's `authority/CURRENT.json` be consumed as the current owner `AuthorityVersionRef` pointer.

An exact historical checkout may contain a fully valid, digest-matching `authority/CURRENT.json`. That means the pointer was current **to that source horizon**; it does not by itself prove present owner currentness after `main` has advanced. Preserve that historical pointer and immutable publication rather than rewriting them. A local `refs/heads/main`, worktree `HEAD`, detached Runtime Workspace, or Workspace name can therefore establish exact-source identity without selecting the present source horizon.

The source-integration horizon and the publication's own `source.sourceRevision` are also distinct. The publication may deliberately fence the owner evidence at an earlier exact revision while a later `main` commit merely republishes or records the current pointer. Source integration chooses which `CURRENT.json` is authoritative now; the selected immutable publication then defines its own exact evidence/source boundary.

Current derived-theory candidate research:

- [TRAA — Derived-Theory Candidate / Live Dogfood Closeout — 2026-08-19](TRAA-DERIVED-THEORY-CANDIDATE-LIVE-DOGFOOD-20260819.md) — transformation-relative semantic substitutability, live Agent bridge-attractor dogfood, cross-owner replication, falsified rivals, and novelty boundary. `CANDIDATE / NOT_FROZEN`; does not alter the SCDF registry.

Consumption-oriented navigation:

- [Consumption-Oriented Map](CONSUMPTION-ORIENTED-MAP.md) — non-authoritative consumer view over current SCD owner standing, firewalls, negative history, TRAA claim ceilings, reopen gates, and candidate consumption order. It does not alter the SCDF registry or Foundation standing.
- [Environment / Habitat Census — Rounds 1–3](ENVIRONMENT-HABITAT-CENSUS.md) — empirical non-authoritative census of real description-mediated judgement boundaries, admitted positive habitats, already-sunk negative controls, candidates and reopen-only regimes through the current H8 round. It does not define a habitat ontology or production SCD environment.


Research instrumentation and applied evidence recovery:

- [Formalization & Canonical Falsification](formalization/README.md) — owner-native recovery of K0.2, CF-v0.1, external-theory mappings, responsibility matrix, negative G1–G4 investigations and the formal-gap closeout. These remain research instrumentation / negative evidence, not Foundation truth.
- [Applied SCD — Consumer Dogfood](applied/README.md) — owner-native recovery of A1–A8 and Cross-Consumer Findings v0.2. [External Revalidation — 2026-08-28](applied/CROSS-CONSUMER-FINDINGS-v0.2-REVALIDATION-20260828.md) separately records exact Host/Harness/Runtime current-to-source evidence. Historical dogfood bytes, present SCD synthesis standing, and foreign-owner currentness remain distinct; none changes SCDF standing.
- [`RECOVERED-RESEARCH-ARTIFACTS-20260827.json`](RECOVERED-RESEARCH-ARTIFACTS-20260827.json) records exact source revisions and byte digests for the recovered artifacts. The recovery fixes physical discoverability only; `semanticStandingChange=false`.

Mechanical owner recovery can be replayed without a package/runtime dependency plane:

```bash
scripts/owner-environment test
scripts/owner-environment cold-start
```

The gate only composes the existing owner-native recovery/firewall checks; it does not create an SCD runtime, semantic service, or new authority surface.
