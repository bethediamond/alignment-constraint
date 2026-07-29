---
title: "Specialist Verification Agenda"
permalink: /specialist-handoff/
description: "The proof-work record and concrete verification questions the Alignment Constraint framework hands off to formal-methods, causal-inference, game-theory, and distributed-systems specialists."
---

**Read this framing before opening any document below.**

This framework distinguishes what it has *argued* from what it has *proven*. The documents in
this section are the working record of that distinction. They are handoff materials for
specialists — not public-facing claims of proof, and not results to be cited.

Every document here is a **Stage 4 specialist handoff**: it records candidate proof architecture
under precisely named assumptions, without independent specialist verification and without theorem
closure. Stage 5 is independent specialist verification; Stage 6 is closure. This labeling is deliberate. A
project that cannot say where its arguments stop is not doing rigorous work. The honesty in these
documents *is* the rigor — not a sign that the framework is unfinished in some embarrassing sense,
but the discipline that makes the rest of the framework trustworthy.

If you are here to evaluate the framework's claims, start instead with
[Proof Status and Non-Claims](/core/proof-status/) and
[The Stability Assumption](/core/stability-assumption/). Return here when you want the raw
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
[OP4d: The Exhaustiveness Obligation](/proof-program/op4d-exhaustiveness-obligation/) and
[OP4d: Candidate Normal Form](/proof-program/op4d-candidate-normal-form/).

---

## The handoff documents, by specialist type

**Formal methods / theorem verification:**
- [Phases 1–7 Formal Proof Handoff](/specialist-handoff/phases-1-7-formal-proof-handoff/) — Mixed-Mode Collapse Lemma, OP4d exhaustiveness, LOI/TOL attribution chain
- [Proof Artifacts — Locked Results](/specialist-handoff/proof-artifacts-locked-results/) — Direction 2 Stage-4 results
- [Five-Problems Stage-4 Handoff](/specialist-handoff/five-problems-stage-4-handoff/) — ICI and related problems

**Game theory / masking and audit dynamics:**
- [B1 Audit Regress Handoff](/specialist-handoff/b1-audit-regress-handoff/) — masking pressure and the audit-regress argument
- [B2 Governance Bifurcation Handoff](/specialist-handoff/b2-governance-bifurcation-handoff/) — pressure argument, not closure

**Distributed systems / extraction dynamics:**
- [Passive Extraction Handoff](/specialist-handoff/passive-extraction-handoff/) — Candidate 3

**Empirical (causal inference / latent-variable modeling):**
- [Packet 1: IMMB-NS + DBST](/proof-program/packet-1-immb-ns-dbst/) — the DBST-M1 empirical hinge
- [DRG Frame-Manipulation Preregistration](/empirical/drg-frame-manipulation-preregistration/) — mechanism-discrimination design (the preregistered multi-model criterion was not met; one model discriminated in the predicted direction and two were non-discriminating or ceiling-limited)
- [V(t) Dissociation Study](/empirical/vt-dissociation-study/) — draft protocol; requires latent-variable specialist review before filing

---

## How to engage

If any argument here survives your scrutiny, the framework is stronger and you will have helped
establish it. If any breaks, the framework wants to know — a clean negative result is the most
valuable outcome. Either way, the ask is the same: not "accept this," but "verify or refute this
specific, named claim."

*Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)*
