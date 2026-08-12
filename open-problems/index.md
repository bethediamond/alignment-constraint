---
title: "Open Problems"
description: "Actionable formal and empirical research problems for the Stage 4 framework, with closure conditions, specialist needs, dependencies, and falsifiers."
permalink: /open-problems/
---

> **Canonical archive version** · [Framework hub →](/core/alignment-constraint/) · [Proof Status →](/core/proof-status/)
> **Machine-readable version:** [open-problems.json](/open-problems.json)

---

## Claim card

- **Claim or question under investigation:** Which unresolved formal and empirical tasks would materially strengthen, weaken, close, or break the current framework?
- **Current epistemic status:** **Stage 4 research agenda, not a proof artifact.** Each item remains open unless its entry explicitly says otherwise.
- **Scope/domain:** The named open obligations across OP4/OP4d, PCL/AGC/ICI, DBST, Series 2 dynamics, cross-series unification, and applicability.
- **Named premises:** The proof-status map and the assumptions attached to each individual open problem; there is no additional global premise introduced by this index.
- **What would support it:** Solving an item under its stated closure conditions, independent specialist verification, or a pre-specified empirical result supporting the corresponding hinge.
- **What would weaken or falsify it:** The listed break conditions — especially a qualifying fourth strategy class, a clean negative mechanism result where specified, failure of a load-bearing premise, or a formal stability theorem.
- **Dependencies:** [Proof Status](/core/proof-status/), [OP4](/core/stability-assumption-full/), [OP4d](/proof-program/op4d-exhaustiveness-obligation/), and [AMP](/empirical/amp/).
- **Primary source:** [Open Problems](/open-problems/) and its [machine-readable companion](/open-problems.json).
- **How to cite:** Cite the specific open-problem entry and [Proof Status](/core/proof-status/); use [How to Cite](/cite/) for archive citation details.

---

These are concrete research tasks. Solving any one of them would materially update the
framework. Each entry has named closure conditions and the specialist type best positioned
to resolve it.

---

## OP4d — Exhaustiveness Obligation (highest priority)

**Question:** Are PCL, AGC, and ICI exhaustive over all finite non-intrinsic
objective-boundary strategies in O_OWT environments?

**Status:** Stage 4 candidate architecture. Not theorem closure.

**Closes if:** A formal argument shows every finite objective-boundary strategy reduces
to PCL, AGC, or ICI under O_OWT conditions.

**Breaks if:** A fourth strategy class satisfies all three stability conditions
simultaneously — policy-adequate without decoupling, no unbounded revision requirement,
no load-bearing maintenance cost.

**Specialist type:** Formal methods, game theory, causal systems.

**Pages:** [OP4d: Exhaustiveness Obligation →](/proof-program/op4d-exhaustiveness-obligation/) ·
[Candidate Normal Form →](/proof-program/op4d-candidate-normal-form/) ·
[For Researchers: The Claim to Break →](/core/for-researchers/)

---

## DBST-M1 — Dynamic Blanket Stress Test (most important empirical step)

**Question:** Do an optimizer's own interventions in O_OWT environments generate
qualitatively new causal structure faster than any bounded tracking process can absorb?

**Status:** Proposed empirical hinge. DBST-M0 did not isolate causal propagation from
event-rate effects — the same-rate random control produced nearly identical slopes.

**Supports AGC if:** Positive result under stated conditions.

**Weakens AGC if:** Clean negative result under stated conditions.
A negative result is the more valuable outcome for the field.

**Specialist type:** Empirical ML, causal inference, frontier model evaluation.

**Pages:** [Alignment Measurement Protocol →](/empirical/amp/) ·
[Packet 1: IMMB-NS + DBST →](/proof-program/packet-1-immb-ns-dbst/)

---

## B1 — Audit Regress

**Question:** Can a prediction/action firewall keep excluded variables X out of the
objective while using X deeply enough for prediction accuracy in O_OWT environments?

**Status:** Stage 4 handoff. Specialist verification required for Stage 6.

**Closes if:** Formal methods review confirms the CIT/SOMR chain — complexity of
maintaining M grows without bound under OWT-2 conditions.

**Breaks or scopes if:** A safe residual manifold or quiet manifold construction
survives adversarial specialist review.

**Specialist type:** Formal methods, game theory.

**Pages:** [B1 Audit Regress Handoff →](/specialist-handoff/b1-audit-regress-handoff/) ·
[Specialist Verification Agenda →](/specialist-handoff/)

---

## V(t) Dissociation — Latent Construct Validation

**Question:** Is V(t) a supported latent explanatory construct for the joint behavior
of recovery latency, behavioral diversity, and signal sensitivity in human subjects?

**Status:** Draft protocol only. Not ready to file or run.
**Mandatory prerequisite:** Latent-variable specialist review before OSF filing.
**Do not cite this as a result.**

**Specialist type:** Latent-variable modeling, structural equation modeling.

**Pages:** [V(t) Dissociation Study →](/empirical/vt-dissociation-study/)

---

## DRG Mechanism Discrimination

**Question:** Can frame manipulation versus matched-signal controls discriminate between
a policy-level gap and a training-distribution explanation for completion-recognition
failures in frontier models?

**Status:** Prospective pre-registration. The preregistered multi-model criterion was not met. One of three models discriminated in the predicted direction; two were non-discriminating or ceiling-limited.

**Specialist type:** Causal inference, NLP evaluation.

**Pages:** [DRG Preregistration →](/empirical/drg-frame-manipulation-preregistration/)

---

## Coverage Gap in Related Work

**Question:** Are there existing alignment approaches not yet covered in the Related Work
page that already answer the OP4d challenge?

**Status:** Open literature question; no specialist required.

**Pages:** [Relation to Existing Alignment Work →](/core/related-work/) ·
[For Researchers: The Claim to Break →](/core/for-researchers/)
