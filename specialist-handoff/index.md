---
title: "Specialist Verification Agenda"
description: "The proof-work record and concrete verification questions the Alignment Constraint framework hands off to formal-methods, causal-inference, game-theory, and distributed-systems specialists."
---

# Specialist Verification Agenda

**Read this framing before opening any document below.**

This framework distinguishes what it has *argued* from what it has *proven*. The documents in
this section are the working record of that distinction. They are handoff materials for
specialists — not public-facing claims of proof, and not results to be cited.

Every document here self-labels as **Stage 4 (LLM ceiling)**: the strongest candidate arguments
currently available, under precisely named assumptions, awaiting independent human specialist
verification (Stage 5) before any claim of closure (Stage 6). This labeling is deliberate. A
project that cannot say where its arguments stop is not doing rigorous work. The honesty in these
documents *is* the rigor — not a sign that the framework is unfinished in some embarrassing sense,
but the discipline that makes the rest of the framework trustworthy.

If you are here to evaluate the framework's claims, start instead with
[Proof Status and Non-Claims](../core/proof-status.md) and
[The Stability Assumption](../core/stability-assumption.md). Return here when you want the raw
proof-work record.

---

## What specialist verification would resolve

The central open problem is **OP4d: the exhaustiveness obligation**. The specification-coherence
argument classifies every identified finite non-intrinsic objective-boundary strategy into three
failure families:

1. **Fixed specification** — proxy-convergence pressure (PCL)
2. **Bounded dynamic tracking** — dynamic screening instability (AGC)
3. **Prediction/action firewalling** — representational incompatibility (ICI)

The Stage 4 architecture holds *if* this classification is exhaustive. The single most valuable
contribution a specialist can make is to either confirm exhaustiveness formally or construct a
fourth strategy class that satisfies all three stability conditions simultaneously. See
[OP4d: The Exhaustiveness Obligation](../proof-program/op4d-exhaustiveness-obligation.md) and
[OP4d: Candidate Normal Form](../proof-program/op4d-candidate-normal-form.md).

---

## The handoff documents, by specialist type

**Formal methods / theorem verification:**
- [Phases 1–7 Formal Proof Handoff](phases-1-7-formal-proof-handoff.md) — Mixed-Mode Collapse Lemma, OP4d exhaustiveness, LOI/TOL attribution chain
- [Proof Artifacts — Locked Results](proof-artifacts-locked-results.md) — Direction 2 Stage-4 results
- [Five-Problems Stage-4 Handoff](five-problems-stage-4-handoff.md) — ICI and related problems

**Game theory / masking and audit dynamics:**
- [B1 Audit Regress Handoff](b1-audit-regress-handoff.md) — masking pressure and the audit-regress argument
- [B2 Governance Bifurcation Handoff](b2-governance-bifurcation-handoff.md) — pressure argument, not closure

**Distributed systems / extraction dynamics:**
- [Passive Extraction Handoff](passive-extraction-handoff.md) — Candidate 3

**Empirical (causal inference / latent-variable modeling):**
- [Packet 1: IMMB-NS + DBST](../proof-program/packet-1-immb-ns-dbst.md) — the DBST-M1 empirical hinge
- [DRG Frame-Manipulation Preregistration](../empirical/drg-frame-manipulation-preregistration.md) — mechanism-discrimination design (prior null reported honestly)
- [V(t) Dissociation Study](../empirical/vt-dissociation-study.md) — draft protocol; requires latent-variable specialist review before filing

---

## How to engage

If any argument here survives your scrutiny, the framework is stronger and you will have helped
establish it. If any breaks, the framework wants to know — a clean negative result is the most
valuable outcome. Either way, the ask is the same: not "accept this," but "verify or refute this
specific, named claim."

*Framework hub: [The Alignment Constraint →](../core/alignment-constraint.md)*
