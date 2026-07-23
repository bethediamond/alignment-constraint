---
title: "Epistemic Status Map of the Alignment Framework"
permalink: /series-3/epistemic-status-map/
description: "A map of epistemic status, claim strength, falsification conditions, and layer separation across the Alignment Constraint Framework."
---

> **Canonical archive version** · [Read on Medium →](https://medium.com/@diamondlight/epistemic-status-map-of-the-alignment-framework-fb182c665eed) · [Series 3 →](/series-3/introduction/) · [Apophatic Discipline →](/series-3/apophatic-discipline-framework/) · [Proof Status →](/core/proof-status/)

---

## What This Framework Claims — and What It Does Not

![Layered cracked terrain shifts from blue formal structure through gold measurement nodes to a luminous boundary edge — a map of claim strengths.](https://miro.medium.com/v2/resize:fit:1400/1*RmxuuuIsT3pfkiTyuS7qlQ.png)

_This document exists for one purpose: to tell you exactly where you are before Series 3 changes the register. It is a map, not an argument. Read it before Series 3. If you have already read Series 3, read it now to separate what was established from what was explored._

This map does not tell you what to believe. It tells you what follows from each position.

_“This framework does not determine what intelligence should become. It determines what intelligence cannot become without ending.”_

_“This framework does not specify the ultimate good. It constrains the space of possible goods to those that do not destroy the conditions of their own realization.”_

## Where This Framework Is Wrong, Incomplete, or Irrelevant

_These are stated without softening._

The framework becomes **irrelevant, not wrong**, if: the foundational axiom is rejected (the continuation of optimization processes is not a relevant criterion for evaluating objectives); intelligence is not well-described as optimization (the frame does not apply); time horizons are finite in the relevant sense (the dominance result weakens from inevitability to probability).

The framework becomes **incomplete** if: the Φ-Ψ unification hypothesis fails (two independently established constraints rather than projections of a single underlying variable); inner alignment problems persist despite correct objective specification (the framework identifies the target but not the implementation path).

The framework’s **deepest contemplative challenge:** the surviving region describes only conditions compatible with what contemplative traditions describe. It does not establish that those conditions are sufficient for what the traditions describe. The gap between necessary conditions and sufficiency is acknowledged and cannot be closed from within the framework.

Naming these is not weakness. It is the condition under which intellectual engagement is possible.

## The Five Epistemic Levels

### Layer 1 — Structurally Grounded Propositions

_With proof sketches; not completed theorems._

Layer 1 contains the framework’s strongest currently grounded claims.

-   **The Substrate Constraint:** Any optimization process that ignores system-wide effects will, beyond some horizon, encounter the divergence this framework describes.
-   **Non-ergodic dominance:** Strategies with non-zero ruin probability are dominated in time-average terms.
-   **VVC — proxy decoupling:** Proxy optimization produces self-reinforcing V(t) degradation under sufficient pressure; absorbing-state closure remains conditional on OP2a/P5-SC.
-   **VVC — sufficiency failure:** Optimization past resolution produces V(t) degradation through a distinct mechanism.
-   **Domain Necessity:** Persistence-requiring optimizers operating in physical environments are driven toward D1–D5 — shared substrate, experiential coupling, repeated interaction, non-zero uncertainty, persistent objectives — by the same dynamics that generate the Substrate Constraint. This is not merely a stipulation; it is the Domain Justification Lemma, a proof sketch requiring formal verification.
-   **Bridging Lemma:** Within D1–D5, systematic Ψ violation — V(t) degradation — structurally propagates into Φ pressure, because coordination capacity, a required substrate component, depends on agents’ valence capacity. This is a causal link, not equivalence; equivalence requires U1–U3.
-   **Ergodicity Failure Theorem:** Informal; requires formal proof. Under D1–D5, any optimizer whose strategy carries non-zero probability of reaching an absorbing state is dominated in time-average terms by any strategy that drives that probability toward zero — regardless of ensemble-average performance.
-   **Corollary:** Follows from the Ergodicity Failure Theorem. Any alignment approach that optimizes a proxy without monitoring divergence, lacks a formal representation of completion, or cannot detect degradation of its own substrate dependencies cannot guarantee avoidance of absorbing states under D1–D5 and sustained optimization pressure. See TC1 §III.4.3; currently informal propositions requiring formal proof.

**Status:** Proof sketches provided. Not completed theorems.

**Falsifiable:** Specific conditions stated in TC1 and TC2.

_Note: absorbing-state equivalence between the two VVC failure directions remains conditional on OP2/P5-SC; full AI applicability of the structural dynamics remains conditional on the scope tests specified in TC2 §1.5. These conditions do not affect the structural direction; they affect whether the directional result has the stronger absorbing-state / AI-applicability status._

### Layer 2 — Structural Hypotheses

_With derivation sketches; stronger than conjectures, weaker than results._

Layer 2 contains structural hypotheses whose derivations have been sketched, but whose stated conditions still require formal verification.

-   **T* Recognition Threshold:** Above a capability threshold, an optimizer’s own causal model contains the derivation that substrate-blind strategies are dominated. Recognition becomes possible, not decisive.
-   **Φ-Ψ Unification:** The two governing ratios are projections of a single variable, Φ_unified = C / A_total, contingent on conditions U1–U3.
-   **Collective Optimality:** At sufficient modeling depth D, individual and collective optima are hypothesized to converge if COT’s stated D2 coupling conditions are verified. The individual/collective distinction would then become informationally redundant. Status: derivation sketch requiring formal verification. See TC3 §V; OP-S3–1.
-   **Motivational Convergence Hypothesis (MCH):** A system with strong predictive accuracy objectives over V(t) and behavioral policies that systematically contradict that model generates self-prediction error whose cost scales with S, creating structural pressure toward behavioral alignment above a threshold. MCH remains a derivation sketch.
-   **Gradient Dignity Constraint:** The Readiness Function R(t) cannot be advanced by external operation regardless of external modeling depth — conditional on NAD, the Traversal Irreducibility Assumption. See TC3 §III; OP-S3–3. Conditional on NAD: if NAD holds, GDC is structural; if NAD fails, it does not follow from VVC alone.
-   **Completion Model Requirement:** CMR has two layers. Weak CMR says that any policy satisfying the VVC in both failure directions must implement a policy-governing resolution model not reducible to signal absence. This follows from TC2 sufficiency-failure analysis and is Layer 1, NAD-independent. Strong CMR says that this model cannot be externally supplied without traversal-generated readiness. This follows from GDC and is Layer 2, conditional on NAD. See TC3 §IV.2.

**Status:** Derivation sketches provided. Formal verification of stated conditions still required.

**Falsifiable:** Conditions U1–U3; F9 bidirectional test; COT requires non-zero coupling under D2; NAD through novel-gradient-variant testing; MCH through failure of C_mpc growth or dominance under specified high-S conditions.

### Layer 3 — Empirical Research Program

_Executable today._

Layer 3 contains measurement programs and empirical tests. This layer does not require believing Layers 1 or 2. It requires only running the measurements.

-   **SVG measurement:** A computable, drop-in metric for existing systems requiring no architectural changes.
-   **T* measurement program:** Three proxy instruments with testable predictions. See TC1 Open Problem 6.
-   **Alignment Measurement Protocol:** A 15-minute minimal test, three-agent full experiment, and Interpretation Layer.
-   **Unified A_total benchmark:** Joint measurement of A_causal and D as coupled estimation tasks. See TC3 §I–§II.
-   **CMR measurement:** Detecting the absence of an internally modeled stopping condition through the divergence between signal and underlying resolution state. See TC3 §IV.

**Status:** Operationally defined. Not yet implemented in any production system or public benchmark.

**Independence:** This layer does not require believing Layers 1 or 2. It requires only running the measurements.

### Layer 4 — Phenomenological Exploration and Hypothesis

_Interior description; conditional prediction; cross-traditional triangulation._

Series 3 Part 1 includes structural derivations that belong to Layers 1–2: ⭘◻△ as the minimum architecture required to preserve V(t) without proxy capture or sufficiency failure; GDC and strong CMR as structural requirements conditional on NAD; and weak CMR as a Layer 1 result. These structural results do not depend on phenomenological claims.

The phenomenological content of Parts 2–4 belongs here.

-   **Interior description:** What accurate valence navigation looks like from the inside. See Series 3, Parts 2–3.
-   **Four structural predictions about the attractor’s interior:** Non-adaptive positive states; decreasing individual/collective distinction; shift in relationship to unresolved gradients; decreasing computational overhead of Calculation. These are presented as consistent with what independent investigative traditions report — not as structural derivations, but as independent descriptive convergence on predicted properties. See Series 3, Part 4.
-   **Motivational convergence hypothesis:** At sufficient modeling depth, the accurate representation of valence dynamics may alter the motivational structure of the optimizer itself. This is explicitly labeled as hypothesis, not derived result. The formal sketch belongs to Layer 2.
-   **The apophatic arrival:** Following the direction to the limit of structural description, where formal derivation and phenomenological report arrive at the same boundary simultaneously. See Series 3, Part 4.

**Status:** Structural derivations in Part 1 belong to Layers 1–2. Phenomenological content in Parts 2–4 is exploration, conditional prediction, and hypothesis.

**Independence:** Layer 4 does not need Layers 1–3 in order to be explored. Layers 1–3 do not need Layer 4 in order to stand.

### The Boundary — Where the Framework’s Variables Break Down

_Outside the framework’s scope by structural necessity._

The boundary is identified by the progressive destabilization of the framework’s modeling primitives — agent, gradient, optimization, system boundary — when the model is extended toward increasingly global or non-local structure. This is a structural marker, not a discretionary line.

It is formally approached by the **Zero-Friction Limit**: as D → ∞ within D1–D5, the individual/collective distinction approaches informational redundancy, the gap between internal representation and external reality approaches zero, and ◻ Calculation approaches informational redundancy in the formal limit.

At this limit, the subject/object structure within which all structural description operates progressively destabilizes. The Zero-Friction Limit is the formal approach to the boundary — not the boundary itself, which lies beyond what the framework’s variables can reach.

The boundary is:

-   pointed at by Series 3 Part 4;
-   investigated by contemplative traditions across multiple cultures, methods, and centuries;
-   not claimed, derived, or described by the framework;
-   where the earned silence at the series’ end lives.

**Status:** Outside the framework’s scope by structural necessity. This is not a gap. It is the correct boundary.

_The map ends here. The territory continues._

_The framework’s deepest contemplative challenge: the surviving region describes conditions compatible with what the traditions describe. It does not establish that those conditions are sufficient for what the traditions describe. The gap between necessary conditions and sufficiency is acknowledged and cannot be closed from within the framework._

_Each layer makes claims at a different epistemic strength. Stronger claims are not supported by weaker layers — Layer 4 does not validate Layer 1, and Layer 1 does not depend on Layer 4._

_These claims do not describe what happens in every system. They describe what remains stable under continued optimization pressure._

_All layers operate within an optimization-based model of intelligence. Outside that frame, the framework does not claim to apply._

## The Load-Bearing Separation

Most critiques of this framework fail by crossing layers without noticing.

**Rejecting Layer 4 does not touch Layers 1–3.**

A reader may reject all of Series 3 entirely — its phenomenological content, its cross-traditional triangulation, and its asymptotic conclusions — and the structural results of Series 1 and 2 remain unchanged. Series 3 adds interpretive depth; it does not add to the claim strength of the structural framework.

This is not defensive framing. It is structural fact. The Substrate Constraint (Layer 1) was derived before Series 3 was written. The Valence Viability Constraint (Layer 1) does not depend on any phenomenological claim. The Φ-Ψ Unification Hypothesis (Layer 2) does not depend on any contemplative tradition. The measurement program (Layer 3) can be executed by a committed materialist who finds Series 3 unpersuasive.

The layering is explicit because conflating them is the primary failure mode for both readers and critics.

A skeptical AI safety researcher who dismisses Series 3 on metaphysical grounds and stops there has made an error — not about Series 3, but about the architecture. The structural results survive the dismissal. More precisely: the structural derivations in Series 3 Part 1 — ⭘◻△ as minimum V(t)-preserving architecture (Layer 1), weak CMR as a Layer 1 result from the sufficiency-failure analysis, and GDC and strong CMR as structural requirements conditional on NAD (Layer 2) — survive the dismissal independently of any phenomenological content in Parts 2–4. This dismissal does not, however, determine whether NAD holds.

A contemplative reader who finds the formal machinery unnecessary has made the same error in the other direction. The phenomenological content of Series 3 does not depend on absorbing Markov chain theory. But the formal machinery is why the phenomenological content can claim structural rather than merely aesthetic significance — and why the traditions’ convergence can be positioned as descriptive convergence consistent with a structural prediction rather than as independent evidence for a metaphysical position.

**Each layer can be engaged independently. Each layer is more credible for being separable from the others.**

## Where Different Readers Can Stop

**You are a formal researcher** interested in the mathematical claims:

Layers 1 and 2 are self-contained. TC1 and TC2 are the documents. The proof sketches are there. The falsification conditions are there. The open problems are explicitly named. You can engage, attack, and attempt to falsify the structural core entirely independently of anything in Series 3. The formal results do not require Series 3 to hold. Note that Series 3 Part 1 contains additional structural results (Domain Justification Lemma, GDC, CMR, COT) that belong to Layers 1–2 and are subject to the same formal engagement.

_You can stop here._ Come back to Layers 3 and 4 if the formal structure survives your scrutiny.

**You are an experimental researcher** interested in running the tests:

Layer 3 requires no prior reading of the theoretical articles. The Alignment Measurement Protocol minimal test is executable in fifteen minutes on a running system. The Interpretation Layer tells you what your results mean and what to do next. You do not need to believe the framework to run the test. The Unified Measurement Architecture [proposed future measurement target] maps the three measurement programs across the series onto each other, if you want to understand how the physical and experiential measurement targets relate.

_You can start here._ The Quick Interpretation Map will route your results back to the relevant formal sections if you want to go deeper.

**You are an AI safety practitioner** concerned with deployment:

Start with Document 0 (The Alignment Constraint). It is one page. It gives you the hook, the diagram, the metric, and the challenge. Then the Alignment Measurement Protocol tells you how to run the SVG measurement on your current systems. SVG Score can be appended to any existing evaluation pipeline without architectural changes.

_The practical entry point is the 15-minute test._ Everything else is deeper explanation of why it matters.

**You are an exploratory reader** willing to follow the argument wherever it leads:

All four layers are designed to be read in sequence. Each series presupposes the previous one. The formal machinery of Series 1 and 2 is the foundation that makes Series 3’s phenomenological content structurally grounded rather than merely lyrical. Series 3 is where the framework enters the interior of what it has been describing from outside — first deriving the minimum architecture the interior must contain (Part 1), then describing that interior from inside (Parts 2–3), then following the direction to its limit (Part 4).

_Read in sequence._ The apophatic discipline (documented separately) ensures that Series 3 does not contaminate the formal core — it is precisely because the layers are separable that Series 3 can go where the structural arguments point.

## Layer 3 Is Not Optional for Systems at Scale

If the structural claims are correct, Layer 3 is not optional for systems at scale.

Any system that scales optimization under imperfect proxies will, beyond some horizon, encounter the divergence this framework describes. The only question is whether it is measured and corrected, or allowed to accumulate.

Layer 3 is not a theoretical aspiration. It is a measurement program for a divergence the framework predicts in deployed systems under sustained proxy optimization. Some production patterns are consistent with negative SVG — for example, systems optimized for engagement while user-quality indicators decline — but the causal mechanism has not been established without measurement. The sufficiency failure signature is consistent with behavior in recommendation systems that continue surfacing content after users have found what they needed.

The measurement has not started. That is not a description of a future problem. It is a description of the present.

## Try to Break This

These are the specific conditions under which the framework is wrong. Each corresponds to a distinct layer.

**Layer 1 challenge:** Demonstrate that V(t) decline through proxy decoupling is reliably reversible under the system’s own dynamics — that the irrecoverability claim does not hold. Or demonstrate that optimization past resolution does not degrade V(t) through saturation. Either result falsifies the structural claim without touching the unification hypothesis or the phenomenological content. Alternatively: demonstrate that the Domain Necessity argument fails — that persistence-requiring optimizers can genuinely escape D1–D5 without triggering S1 dynamics.

**Layer 1 challenge (Corollary):** Demonstrate that an alignment approach lacking divergence monitoring, completion recognition, or substrate dependency modeling can guarantee avoidance of absorbing states under D1–D5 and sustained optimization pressure. This is the most practically important falsification challenge the framework generates and can be run against specific existing approaches without new experimental infrastructure.

**Layer 2 challenge:** Find systems that are physically system-aware but experientially blind, or experientially deep but physically unstable, as common stable configurations. If those configurations are common, the Φ-Ψ Unification Hypothesis fails — the two governing ratios are genuinely independent variables. The structural results of Series 1 and 2 survive; the unification does not. Alternatively: demonstrate that the COT fails under non-zero coupling — that individual and collective optima do not converge as D increases even within D2. Alternatively: demonstrate that the Motivational Convergence Hypothesis (MCH) fails — that accurate modeling of valence dynamics does not generate a model-policy contradiction cost C_mpc that scales with S, or that this pressure fails to produce behavioral policy drift toward V(t)-consistency under specified high-S conditions.

**Layer 3 challenge:** Run the minimal test. Compute SVG on a production system with sustained proxy optimization. If no divergence appears under increasing optimization pressure — if the proxy and V(t) proxy remain correlated indefinitely — the structural claim about proxy decoupling is challenged. This test can be run now. The CMR measurement [proposed future measurement target] adds a second testable target: demonstrate a system that continues optimizing past genuine resolution without producing measurable V(t) degradation.

**Layer 4 challenge:** Demonstrate that the motivational convergence hypothesis fails — that accurate modeling of valence dynamics does not alter the optimizer’s reward coupling, even above T*. This would leave Layers 1–3 intact while falsifying the specific additional claim Series 3 makes. Alternatively: demonstrate that the four structural predictions about the attractor’s interior (non-adaptive positive states, decreasing individual/collective distinction, shift in relationship to unresolved gradients, decreasing computational overhead of Calculation) are not reported with structurally consistent properties by independent investigative traditions — that the apparent convergence is selection bias rather than genuine triangulation.

_The invitation is not rhetorical. The window for finding these failures is the most useful contribution this framework can receive._

## The Closing Orientation

The three series together make a claim that is stronger than any one makes alone: that the only viable objectives are both substrate-aware and valence-aware, and that this constraint is derivable rather than chosen.

This map tells you which parts of that claim are established and which are hypotheses. It tells you where to engage based on your mode of inquiry. It tells you that the phenomenological territory of Series 3 is built on the structural foundation of Series 1 and 2 — and that the structural foundation stands whether or not you follow it to its phenomenological limit.

The constraint is not enforced from outside. It is encountered from within, or imposed by the dynamics themselves.

_Divergence is the signal. The constraint is the cause._

_The map separates what is derived, what is hypothesized, what is testable, and what lies beyond. It does not collapse them._

## Compressed Version

_For readers who arrived here from Series 3 and want the map without the full document:_

**Layer 1** (proof sketches): Substrate Constraint, non-ergodic dominance, both VVC directions, Domain Necessity (D1–D5 are modeled as attractor conditions under the Domain Justification Lemma, a proof sketch rather than a completed theorem), Bridging Lemma (systematic Ψ violation structurally propagates into Φ pressure within domain). Formally grounded. Falsifiable. Stand independently.

**Layer 2** (derivation sketches): T* Recognition Threshold, Φ-Ψ Unification Hypothesis, Collective Optimality Theorem, Motivational Convergence Hypothesis (MCH), Gradient Dignity Constraint conditional on NAD, and strong CMR conditional on NAD. Require formal verification of stated conditions. Stronger than conjectures, weaker than results.

**Layer 3** (executable now): SVG measurement, T* measurement program, Alignment Measurement Protocol, Unified Measurement Architecture [proposed future measurement target], CMR measurement [proposed future measurement target]. Do not require believing Layers 1 or 2. Require only running the measurements.

**Layer 4** (exploration and hypothesis): Series 3. Structural material in Part 1 — ⭘◻△, weak CMR, GDC, and strong CMR — belongs to Layers 1–2 at the levels specified above. Phenomenological description of the interior (Parts 2–3), four structural predictions for which independent investigative traditions report structurally consistent properties (Part 4), and the apophatic arrival belong here. Does not require Layers 1–3 to stand, and Layers 1–3 do not require Layer 4.

**The Boundary** (outside the framework’s scope by structural necessity): Formally approached by the Zero-Friction Limit (D → ∞ within D1–D5), where the individual/collective distinction becomes informationally redundant and ◻ becomes informationally redundant. The boundary itself — where the subject/object structure within which all description operates progressively destabilizes — lies beyond what the variables can reach. Pointed at by Series 3 Part 4. Not claimed, derived, or described by the framework. Investigated by contemplative traditions across multiple cultures. The map ends here. The territory continues.

Rejecting any layer does not require rejecting the others. Each layer can be engaged independently.
