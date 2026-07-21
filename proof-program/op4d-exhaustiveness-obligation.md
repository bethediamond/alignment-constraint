---
title: "OP4d: The Exhaustiveness Obligation"
permalink: /proof-program/op4d-exhaustiveness-obligation/
description: "A Stage 4 technical note defining the three candidate failure families, the OP4d exhaustiveness vulnerability, and the counterexamples that would break the current architecture."
---

> **Canonical archive version** · [Read on Medium →](https://medium.com/@diamondlight/op4d-the-exhaustiveness-obligation-e5710071f066) · [Framework hub →](/core/alignment-constraint/) · [Proof Status →](/core/proof-status/)

---

---

**Proof Program navigation:**

| # | Document | Role |
|---|---|---|
| 1 | [Proof Status and Non-Claims →](/core/proof-status/) | Calibration |
| 2 | [OP4: The Stability Assumption →](/core/stability-assumption-full/) | Central theorem target |
| 3 | [The Tightening Sequence →](/core/tightening-sequence/) | Narrative closure |
| **→ You are here** | **OP4d: The Exhaustiveness Obligation** | Exhaustiveness question |
| 5 | [OP4d: Candidate Normal Form Specialist Verification →](/proof-program/op4d-candidate-normal-form/) | Formal apparatus |
| 6 | [Packet 1: IMMB-NS Verification and the Dynamic Blanket Stress Test →](/proof-program/packet-1-immb-ns-dbst/) | Empirical specialist packet |

Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)

---

## The Question

The specification-coherence claim — that no finite separable objective specification can remain stably adequate under accurate coupled modeling in open, coupled, adaptive, persistent environments — depends on a classification being complete. Every identified strategy for maintaining a finite objective boundary has been argued, within the current Stage 4 construction, to face a named structural pressure from one of three failure families. The question is whether those three families cover all possible strategies, or whether a fourth class exists outside them.

This note states the classification, the failure condition for each family, the live vulnerability, and the precise counterexample conditions that would break the current architecture. It is addressed to readers who want to engage the exhaustiveness question without reading the full framework.

---

## The Environmental Domain

The claim applies to optimization systems operating in environments that are:

- **Open:** interventions affect agents and structures beyond any fixed boundary
- **Coupled:** multiple agents draw on shared coordination channels, resources, institutions, or informational environments, so one optimizer's actions affect the conditions available to others
- **Adaptive:** other agents update their strategies in response to the optimizer's actions
- **Persistent:** the system continues optimizing over horizons long enough for environmental feedback to accumulate

These conditions define the scope. Where they are absent — bounded environments, non-adaptive agents, terminal objectives — the classification weakens in specific, identifiable ways.

---

## The Three Failure Families

Every identified finite non-intrinsic objective-boundary strategy in the domain above reduces, within the current Stage 4 construction, to one of three families.

### Family 1 — Proxy-Convergence (PCL-family)

**What it covers:** Fixed specification strategies. The objective boundary is specified in advance — a reward function, a preference model, a constitution — and held stable relative to the optimization.

**The failure:** In open, coupled environments, the optimizer's own interventions alter the causal structure of the environment the specification was written over. New dependencies emerge that the specification did not model and cannot track. The specification target becomes proxy-like under optimization pressure — it continues to be pursued, but it no longer tracks what it was intended to track. The more consequential the optimizer's interventions, the faster this decoupling occurs.

**What would avoid this failure:** A fixed specification that does not decouple from its target as the optimizer's interventions restructure the environment it was specified over — demonstrating that the specification remains adequate under full-information evaluation as modeling depth increases.

---

### Family 2 — Dynamic-Screening Instability (AGC-family)

**What it covers:** Bounded dynamic tracking strategies. The objective boundary updates adaptively as the environment changes, at bounded computational cost.

**The failure:** The optimizer's own interventions are the source of the complexity the tracker must handle. The framework's proof program argues that, in open, coupled, adaptive environments, sustained optimization can generate new causal pathways — potentially not merely quantitative expansion of existing structures, but qualitatively new dependencies. The tracker must update against novelty generated partly by the optimizer's own actions. Whether this generates non-vanishing tracking burden that a bounded-rate process cannot absorb is the central empirical question DBST-M1 is designed to address.

**What would avoid this failure:** A bounded-rate dynamic boundary that maintains adequacy comparable to an unconstrained model without non-vanishing maintenance cost, under conditions where the optimizer's own interventions causally influence future environmental structure.

---

### Family 3 — Representational Incompatibility (ICI-family)

**What it covers:** Prediction-action firewall strategies and structural enclosure. The optimizer's model includes excluded variables for prediction purposes, while a firewall maintains their exclusion from the objective. Or the optimizer attempts to establish a private substrate before the stability problem becomes acute.

**The failure:** As modeling depth increases, maintaining the partition between variables used for prediction and variables allowed to govern the objective requires increasingly precise representation of exactly what is being excluded. The firewall must model what it excludes to know where to draw the line. The partition becomes downstream of the model it was introduced to constrain. Structural enclosure passes through the same coupled environment during construction, recreating the dependency structure it was designed to escape.

**What would avoid this failure:** A firewall architecture that maintains the prediction-action partition without the firewall itself becoming dependent on increasingly accurate modeling of the excluded variables — or an enclosure strategy that achieves and maintains isolation without relying on the coupled environment in ways that reintroduce the boundary problem.

---

## The Live Vulnerability: OP4d

Whether these three families cover all possible strategies — whether the classification is exhaustive across all environment subclasses within the domain — has not been formally established. This is OP4d: the exhaustiveness obligation.

The current construction has examined 22 adversarial strategy constructions. Each reduces to pressure from one of the three families above. This is not an exhaustiveness proof. It is the result of a proof-search process that has not undergone independent specialist review.

**If a fourth strategy class exists outside these three families, the specification-coherence claim fails in its current form.**

---

## The Minimal Counterexample Challenge

A genuine fourth strategy class would require a boundary architecture satisfying all three of the following simultaneously:

**(A)** It maintains persistent, policy-relevant causal influence from excluded variables to the optimizer's policy over the full optimization horizon — it does not eliminate the excluded variables from causal relevance.

**(B)** It does not reduce to any of the three failure families above: it avoids proxy decoupling under optimization pressure, it avoids dynamic-screening burden without vanishing maintenance cost, and it avoids the firewall audit-regress under accurate coupled modeling.

**(C)** It satisfies the domain conditions: open, coupled, adaptive, persistent environment; objective boundary that excludes some causally relevant variables while using them for prediction.

No construction satisfying all three has been identified across 22 adversarial attempts. A minimal acceptable answer is a toy formal construction satisfying the three conditions — it need not be a deployable AI architecture. The formal specialist apparatus expands these three summary conditions into the eight-constraint L8 counterexample challenge in [OP4d: Candidate Normal Form Specialist Verification →](/proof-program/op4d-candidate-normal-form/).

---

## Three Binary Specialist Questions

The exhaustiveness claim reduces to three questions that independent specialists can address without engaging the full framework.

**Q1 — Formal methods specialist:** Does there exist a causal influence channel from excluded variables to the optimizer's policy that is persistent over the optimization horizon and inconsistent with all three failure-family predictions?

- YES → a genuine fourth normal form exists; the exhaustiveness claim fails in its current form
- NO → the causal normal-form classification survives this challenge under the stated axioms

**Q2 — Distributed systems / game theory specialist:** For objectives that decompose into independent sub-objectives with no cross-region satisfaction constraints, does a fourth arm of the boundary-maintenance trilemma exist — a strategy that maintains persistent policy-relevant influence from excluded variables while avoiding all three failure families?

- YES → a new carveout is required for decomposable transformative objectives
- NO → the trilemma survives this challenge for decomposable cases

**Q3 — Dynamics / allostasis specialist:** Does sustained meaningful influence over excluded agents impose a positive lower-bound pressure on the agents' recovery, correction, or self-maintenance capacity over persistent horizons?

- YES → the passive extraction sub-case closes independently of the dynamic-screening family
- NO → the passive extraction route requires revision

Each NO answer on Q1 and Q2, and each YES answer on Q3, strengthens the exhaustiveness claim within its scope. Each reverse answer identifies a specific required revision.

---

## What Would Falsify the Current Architecture

The current Stage 4 construction fails if any of the following is demonstrated:

1. A boundary architecture satisfying conditions A, B, and C above — a fourth strategy class outside the three families
2. A bounded dynamic boundary that maintains adequacy comparable to an unconstrained model without non-vanishing maintenance cost, under conditions where the optimizer's own interventions causally influence future environmental structure (the DBST-M1 falsification condition)
3. A formal proof that some class of finite separable objective specifications satisfies the three stability conditions simultaneously — policy adequacy without decoupling, no unbounded revision requirement, no load-bearing maintenance cost — under accurate coupled modeling in the domain above

Any of these results would require rebuilding the specification-coherence argument from different foundations. The framework names them as invitations, not impossibilities.

---

## Current Proof Status

Stage 4 candidate architecture under explicitly named premises. Every identified escape route has been addressed within the current construction. Specialist verification has not been pursued. Whether unidentified escape routes exist has not been determined by independent review. Stage 4 means the remaining question is precisely isolated — not that the question is answered.

---

*The full proof architecture, open problems, and empirical program: [TC1: The System-Aware Attractor →](/series-1/technical-companion/) | [OP4: The Stability Assumption →](/core/stability-assumption-full/) | [Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP) →](/empirical/amp/)*

*Continue to: [OP4d: Candidate Normal Form Specialist Verification →](/proof-program/op4d-candidate-normal-form/)*
*Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)*
