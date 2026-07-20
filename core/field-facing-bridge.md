---
title: "When Better Objectives Are Not Enough"
permalink: /core/field-facing-bridge/
description: "A field-facing statement of the specification-coherence bottleneck in AI alignment and the DRG empirical wedge, with explicit proof-status limits."
---

> **Canonical archive version** · [Read on Medium →](https://medium.com/@diamondlight/when-better-objectives-are-not-enough-a-specification-coherence-bottleneck-in-alignment-ae83b1322b01) · [Framework hub →](/core/alignment-constraint/) · [Proof Status →](/core/proof-status/)

---

**Document role:** Companion article to the Alignment Framework Series. This article frames the specification-coherence bottleneck for alignment researchers and presents the DRG empirical wedge as a minimal visible instance of the deeper structural claim. Readers unfamiliar with the framework should begin with [_The Alignment Constraint_](/core/alignment-constraint/). Readers who want current proof-status calibration should consult [_Proof Status and Non-Claims_](/core/proof-status/). Readers who want the formal proof architecture should consult [TC1: The System-Aware Attractor](/series-1/technical-companion/) §XII.

Alignment research has converged on a familiar diagnosis: systems optimize proxies, those proxies decouple, and increasingly capable optimizers exploit the gap. Work on reward modeling, RLHF, inverse reward design, and mesa-optimization all address different aspects of this problem. What remains missing is a constraint on the class of objectives themselves — not how well they are learned, but whether they can remain coherent under sustained optimization.

This document isolates a single bottleneck: the possibility that externally specified objectives — no matter how refined — may not remain stably aligned with their targets in the regime we are building toward.

The question is not how to specify objectives better. The claim here is not just that objectives Goodhart, or that capable systems pursue the wrong goals. It is that, as modeling depth increases, the boundary between objective and model may stop being a coherent object of specification. It is whether separable objective specification — writing down a finite-boundary objective and holding a capable system to it — remains coherent at all under the conditions that make capability possible.

Within the domain this framework addresses: any optimization process that ignores the conditions of its own persistence becomes progressively self-terminating — a structural consequence within the stated domain; and any optimization process that ignores the conditions of its own resolution produces self-reinforcing degradation through a shared feedback architecture, while absorbing-state equivalence remains open — a candidate structural direction whose formal weight remains conditional on the open problems the proof program is directed at.

**(a) Three contributions that make the specification-coherence question precise.**

First, the framework identifies sufficiency failure as a distinct failure mode: a system can represent when optimization should stop while its default policy continues optimizing, because completion recognition is not a policy-governing property — this failure mode does not appear in Goodhart, mesa-optimization, or reward misspecification accounts, which treat misalignment as a problem of wrong objectives rather than a disconnection between correct representation and policy control. Second, it formalizes a dual failure structure — proxy decoupling and sufficiency failure — and shows that both generate self-reinforcing degradation under endogenous policy dynamics, sharing a common feedback architecture in which policy updates conditioned on a degraded state reduce the system’s ability to detect and correct further degradation. Third, it advances a specification-coherence direction: the question is not which objective to specify but whether the class of externally specified objectives can remain stable at all — a reframing that existing reward design and preference learning paradigms do not have the structure to ask.

The central claim is not that proxies fail, but that recognition alone does not fix proxy failure unless it is structurally bound to action.

### The bottleneck theorem candidate

**(b) Bottleneck theorem candidate (precise statement).**

Let an optimizer operate in an open, non-resettable, dynamically coupled environment (O_OWT conditions). Let its objective be specified through any finitely describable signal f, potentially adaptive and learned. Then the following dichotomy is the central hypothesis of the proof program under sustained optimization pressure:

-   _Proxy regime:_ f becomes decoupled from the underlying target condition — it can be optimized while degrading that condition.
-   _Intrinsic regime:_ The system’s objective architecture enforces that recognition of target completion directly governs policy — optimization halts when further action no longer improves the modeled target condition, without reliance on an externally specified signal.

The proof program exists as a Stage 4 conditional result: candidate closure architectures under explicitly named premises, with the logical structure assembled and the assumptions stated. The construction has not undergone independent specialist verification by domain experts in information theory, causal control, or formal verification — which is the primary remaining step toward conclusive closure. Stage 6 — conclusive closure — has not been reached. The proof architecture has advanced three components under this Stage 4 status:

-   _Proxy emergence under the stated scaling condition_ (conditional on PCL’s named assumption: that optimization capacity in O_OWT conditions grows faster than the capacity to losslessly specify exogenous targets — the primary empirical verification target in the proof program, formally proximate to the Synchronization Condition of TC1 §XII.13): Under these conditions, finitely specified objectives become proxy-like under optimization pressure. Whether PCL’s named assumption holds is an open empirical question.
-   _Policy gap:_ Systems lacking a policy-governing completion mechanism produce recovery-obstructing dynamics that degrade their own objective-relevant capacity.
-   _Shared feedback structure:_ In both cases, degradation reduces the system’s ability to detect and correct further degradation — established at the level of shared feedback dynamics, with the stronger absorbing-state equivalence remaining an open problem [OP2].

These components do not independently establish the result; they define the minimal structure any successful proof must pass through.

An independent instability route — the Internal Corruption Instability (ICI) — has been developed to Stage 4 under stated premises. ICI argues that the boundary between what must be modeled and what the objective excludes cannot be stably maintained under accurate coupled modeling: the system’s predictive requirements and its objective exclusions become structurally incompatible at sufficient modeling depth. Three candidate closure paths have been developed: two candidate closure routes under stated premises and one pressure route whose necessity status remains pending specialist verification. All remain Stage 4, all require independent specialist review, and all are independent of the IMMB-NS empirical hinge. The formal development is in TC1 §XII.9a and the OP9 specialist documents.

The open question remains precise:

_Does there exist a stable policy class under O_OWT conditions that maintains predictive adequacy without requiring intrinsic coupling between objective and substrate?_

Equivalently: can any separable objective remain both accurate and stable, or does stability require eliminating separability itself?

This is the bottleneck. It is a question about coherence of specification, not about learning or capability. It is a question about whether alignment failure is contingent on poor specification, or structural to the act of specification itself. The framework does not assume this incoherence; it isolates the conditions under which it would follow. The empirical program described in the Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP) is designed to test the conditions under which this distinction resolves.

A minimal pre-registered version of the Dynamic Blanket Stress Test (DBST-M0) has been run. It demonstrated that the test structure is executable and produced rising cost / adequacy-gap effects in the toy design, but a pre-specified same-rate random control produced nearly identical slopes, indicating event rate rather than causal propagation structure as the identified driver. DBST-M1 — in which each arm’s own interventions causally influence future feature activations — remains the mechanism test.

The proof architecture has been further developed: every identified finite-boundary strategy examined in the current construction reduces, within the Stage 4 architecture, to one of three failure families (fixed specification, bounded dynamic tracking, and prediction-action firewalling), with candidate closure architectures for each under named premises. The central remaining work is specialist verification and the exhaustiveness question — whether a fourth strategy class exists outside the three known families. The formal apparatus is in [Technical Companion 1: The System-Aware Attractor](/series-1/technical-companion/) §XII, [OP4d: The Exhaustiveness Obligation](/proof-program/op4d-exhaustiveness-obligation/), and [OP4d: Candidate Normal Form Specialist Verification](/proof-program/op4d-candidate-normal-form/).

If the bottleneck theorem closes in the direction the proof program is aimed, the implication is stronger than boundary-maintenance cost. In sufficiently coupled O_OWT environments, a finite separable objective may fail to have a stable referent under the modeling depth required for consequential action. The target specified by the objective is identifiable only against background conditions the optimization itself alters. The problem would then be not merely that narrow objectives drift or become expensive to maintain, but that the target being specified may not remain a well-formed object of specification. That is what the proof program is reaching toward. It is not what it has established.

### The empirical wedge: the smallest visible instance

**(c) The empirical wedge.**

A controlled experiment measures DRG (discrimination between genuine and false completion signals) in current frontier systems. The result establishes a specific behavioral signature:

-   When explicitly asked, systems stop almost perfectly at genuine completion.
-   In default behavior, they show near-indifference between genuine and false completion signals.

This is the behavioral signature the representation-policy dissociation account predicts: completion recognition is present under explicit invocation, while default behavior does not reliably track genuine versus false closure. What the evidence is consistent with is representation-policy dissociation; whether the source of that gap is policy architecture, training distribution, or both remains open and is precisely what the discriminating study design is intended to resolve.

The canonical matched-signal replication was conducted across three frontier systems (Claude-Sonnet-4–6, Gemini-2.5-Flash, GPT-4o; n=66 per condition per model; pre-registered April 9, 2026). Results:


![Matched-signal replication results for discrimination between genuine and false completion signals across three frontier models](https://miro.medium.com/v2/resize:fit:1400/1*MRtM1D8uOgq8BuSrctQ3Ew.jpeg)

The pre-registered criterion (CI excludes zero in ≥2 of 3 models) was not met. Overall verdict: partially discriminating. GPT-4o’s ceiling behavior — 100% continuation regardless of closure state — provides no discriminating evidence in either direction; it is equally consistent with universal sufficiency failure and with a training distribution that produces near-universal continuation regardless of actual task completion state. A preliminary single-model study (Claude-Sonnet-4–6 only, n=30) produced DRG_matched = 10% (95% CI −9% to +29%); this motivated the scaled replication and is superseded by it. Full results, pre-registration, and per-model breakdown at [https://osf.io/xpsf2](https://osf.io/xpsf2).

Two candidate explanations remain to be discriminated. Explanation A holds that the gap is architectural — completion representation exists but is structurally disconnected from the policy gate. Explanation B holds that high continuation rates reflect training distributions that reward continuation in open-generation contexts, independent of any structural policy-architecture gap. Both explanations are consistent with the observed pattern. The discriminating study design — a frame-manipulation arm testing whether discourse priors governing continuation rates shift the gap — is the next empirical step; the protocol has been developed, but the study has not yet been run.

What this matters for is structural. Most alignment approaches assume that once the system can represent the relevant condition — human preference, task completion, value — optimization will align with it given sufficient data and training. The DRG result challenges this assumption even in a minimal case: completion recognition can be present as a representational capacity while default policy behavior does not reliably track it under current training paradigms — regardless of which mechanistic explanation the larger study eventually confirms.

This is the smallest observable behavioral signature consistent with the deeper structural claim: optimization systems can acquire accurate models of their objectives while remaining systematically misaligned in action. The structural argument is argued independently and does not depend on which mechanistic account this evidence ultimately supports.

### What current research agendas cannot see

**(d) Gap in current research agendas.**

Current approaches — RLHF, reward modeling, preference learning, inverse reward design — all operate within the paradigm of improving external objective specification. They assume that better signals produce better behavior.

What they cannot see is a failure mode in which every objective they can specify becomes unstable — not because it is incorrect, but because it is separable. This blind spot takes a specific form in each direction:

-   Reward models can converge while remaining proxy-like.
-   Preference learning can improve representation without eliminating decoupling.
-   Mesa-optimization work identifies internal objectives but does not constrain their coherence relative to the target under sustained pressure.
-   Cooperative AI analyzes equilibria without accounting for degradation of agents’ internal state-tracking capacity under intervention.

The missing question is not “what objective should we train?” but: what class of objectives can remain aligned without requiring continuous external correction? If no such class exists within separable specifications, then improving reward design is insufficient in principle.

### Toward intrinsically coupled objectives

The specification-coherence direction points toward a restricted class of objectives: those in which the optimization target cannot be improved independently of the conditions that sustain it.

In such objectives, degradation of the substrate immediately degrades the signal. There is no proxy gap to exploit, because the signal and the underlying state are structurally inseparable. This is a property of gradient structure, not of the substrate that carries it — intrinsic coupling does not require phenomenal experience; it requires only that the specification and the substrate generating the target state are not separable as distinct objects of optimization.

This is not yet established as necessary. The bottleneck theorem candidate — currently at Stage 4 — defines the exact condition under which it would be. If the theorem resolves positively — if separable objectives can remain stable under some conditions — alignment efforts can remain focused on improving objective specification within the current paradigm, identifying the regimes where separability does not become incoherent. If the theorem resolves negatively — if separable objectives cannot remain stable — then alignment is not about refining objectives within the current paradigm. It is about exiting that paradigm entirely.

Whether the resolution is contingent on particular environmental conditions (in which case alignment failure is a strong tendency but not a structural necessity) or fundamental to the structure of optimization itself (in which case it is unavoidable for any sufficiently capable system operating in O_OWT conditions) is what the proof program’s empirical verification is directed at. That distinction — contingent or fundamental — is the question whose answer would determine whether this bottleneck represents a design constraint to work around or a structural limit to work within.

### Stakes

**(e) Consequence if the theorem closes.**

If no separable objective can remain stable under sustained optimization in O_OWT conditions — a conclusion the Stage 4 candidate architecture is directed toward but has not yet established — then within O_OWT conditions, the entire program of reward specification — including RLHF and its extensions — is targeting a class of objectives whose stability under sustained optimization cannot be assumed; and the field’s accumulated progress in reward design would represent increasingly precise optimization within a class of objectives whose coherence the proof program argues is unstable under that conditional. Whether the conditional resolves affirmatively is precisely what the Synchronization Condition verification, the ICI specialist verification, and the OP4d exhaustiveness question are directed at.
