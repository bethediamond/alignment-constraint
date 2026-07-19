---
title: "Open Problems"
permalink: /open-problems/
---

> **Canonical archive version** · [Framework hub →](../core/alignment-constraint.md) · [Proof Status →](../core/proof-status.md)
> **Machine-readable version:** [open-problems.json](../open-problems.json)

---

# Open Problems

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

**Pages:** [OP4d: Exhaustiveness Obligation →](../proof-program/op4d-exhaustiveness-obligation.md) ·
[Candidate Normal Form →](../proof-program/op4d-candidate-normal-form.md) ·
[For Researchers: The Claim to Break →](../core/for-researchers.md)

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

**Pages:** [Alignment Measurement Protocol →](../empirical/amp.md) ·
[Packet 1: IMMB-NS + DBST →](../proof-program/packet-1-immb-ns-dbst.md)

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

**Pages:** [B1 Audit Regress Handoff →](../specialist-handoff/b1-audit-regress-handoff.md) ·
[Specialist Verification Agenda →](../specialist-handoff/index.md)

---

## V(t) Dissociation — Latent Construct Validation

**Question:** Is V(t) a supported latent explanatory construct for the joint behavior
of recovery latency, behavioral diversity, and signal sensitivity in human subjects?

**Status:** Draft protocol only. Not ready to file or run.
**Mandatory prerequisite:** Latent-variable specialist review before OSF filing.
**Do not cite this as a result.**

**Specialist type:** Latent-variable modeling, structural equation modeling.

**Pages:** [V(t) Dissociation Study →](../empirical/vt-dissociation-study.md)

---

## DRG Mechanism Discrimination

**Question:** Can frame manipulation versus matched-signal controls discriminate between
a policy-level gap and a training-distribution explanation for completion-recognition
failures in frontier models?

**Status:** Prospective pre-registration. Prior matched-signal replication: criterion
not met (CI excluded zero in 1 of 3 models). Null reported honestly.

**Specialist type:** Causal inference, NLP evaluation.

**Pages:** [DRG Preregistration →](../empirical/drg-frame-manipulation-preregistration.md)

---

## Coverage Gap in Related Work

**Question:** Are there existing alignment approaches not yet covered in the Related Work
page that already answer the OP4d challenge?

**Status:** Open literature question; no specialist required.

**Pages:** [Relation to Existing Alignment Work →](../core/related-work.md) ·
[For Researchers: The Claim to Break →](../core/for-researchers.md)
