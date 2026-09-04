> **Modification notice (Apache-2.0 §4(b)):** This file contains changes from an Apache-2.0-licensed upstream version in `ordivon-computing`.

# SCD Provenance

## Canonical continuity

- `task:scd-research-core-consolidation-branch-20260818` — revision 3, completed; immediate consolidation baseline for this materialization.
- `task:computational-semantics-owner-line-handoff-20260818` — revision 16, completed canonical owner-line handoff referenced by consolidation.
- `task:semantics-of-computational-descriptions-post-closeout-handoff-20260818` — later current SCD continuity referenced by consolidation.

Historical owner-line-S family-map tasks remain provenance only when their local naming/status predates canonical SCD materialization.

## Repository materialization base

Materialization was built in an isolated detached worktree from committed base:

`1a9cc7b3a9144751b6f3d38650f42f0ea7340148`

No claim in this directory is established merely by being present in Git. Host continuity and owner-native evidence remain the semantic authority chain.


## 2026-08-27 owner-native research-artifact recovery

The standalone owner cutover exposed a recovery gap: current authority publications still name K0.2, CF-v0.1 and A1–A8 applied evidence as current research instruments/evidence, while their full texts had remained on historical `ordivon-computing` research branches and were not reachable from standalone `ordivon-scd` main.

This repair restores the exact source-fenced texts without changing their semantic standing:

- formalization source revision: `bc1aba930ab6de64680ac2b8fab4d29fe2aa0348` (`research/scd-gap-investigations-20260818`; includes the corpus originally materialized at `0591128af1668df22750ab5b76cad73621d45ecd`);
- applied source revision: `9424ed240da1c6d13a12266897384fb848434aa6` (`research/scd-applied-dogfood-20260818`).

Exact recovered-path digests are recorded in `RECOVERED-RESEARCH-ARTIFACTS-20260827.json`. Historical branch commits remain immutable lineage. This is a physical/recovery sedimentation repair only: it does not mint new authority, update the existing AuthorityVersionRef, close/open any SCDF, or rewrite historical publications.
