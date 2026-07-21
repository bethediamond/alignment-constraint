---
title: "The Depth Constraint"
permalink: /series-2/depth-constraint/
description: "A Series 2 article on depth, valence, and the constraints required for genuine resolution."
---

> **Canonical archive version** · [Read on Medium →](https://medium.com/@diamondlight/the-depth-constraint-04c5b71aad5b) · [Framework hub →](/core/alignment-constraint/) · [Proof Status →](/core/proof-status/)

---

**Series navigation:**

| Post | Title | Role |
|------|-------|------|
| Introduction | The Architecture of Thriving | Frame |
| Part 1 | The Invariant Drive | The Universal Generator |
| **→ You are here** | **The Depth Constraint** | The Structural Correspondence |
| Part 3 | The Inner Crossing | Ψ = S / D |
| Part 4 | The Shape of What Does Not End | The Asymptote |
| Technical Companion | The Valence Constraint | Formal Layer |

Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)
Experimental Companion: [Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP) →](/empirical/amp/)

*Companion simulation: [The Proxy Decay Simulator →] — illustrates proxy decoupling within a minimal model class; its absorbing-state behavior is structural within that model, not a proof of the framework's full equivalence claims (see OP2).*

---

*Epistemic status: High confidence in the structural argument and the absorbing-state analysis of the proxy direction and the self-reinforcing degradation analysis of both directions, scoped to the class of systems specified below. This article formalizes the resolution component of the framework's canonical root claim — the component Series 2 develops — through V(t) and the two failure modes. The structural correspondence with the Substrate Constraint — argued in the Technical Companion to constitute formal equivalence if specific conditions hold — is offered as a hypothesis with a derivation sketch, not a settled result. Specifically: the formal equivalence between V(t) collapse and substrate collapse — whether both are irrecoverable in the same structural sense — is the highest-priority open problem the series generates (OP2 in the Technical Companion). The argument proceeds under the claim that both exhibit self-reinforcing degradation under endogenous policy dynamics; that claim is argued but not yet proven from first principles. The RLHF critique is scoped precisely: it identifies structural limitations of RLHF's current implementation in both failure directions, not a comprehensive dismissal of the method.*

---

Part 1 introduced the behavioral foundation — the three-state taxonomy, the two failure directions, and the foundational hypothesis that wherever motivated behavior is present, gradient dynamics of the kind described apply. Part 2 formalizes the conditions under which that foundation generates structural constraints. The formalization proceeds through V(t) as a hypothesized latent variable defined by its predictive role over observable behavior, and Ψ = S/D as the ratio capturing the relationship between intervention scale and modeling depth. The formal weight of the argument resides here and in the Technical Companion. The phenomenological examples in Part 1 are illustrations of the structural argument, not its ground.

## What Part 1 established and what remains

Part 1 identified two structurally distinct failure modes of directed behavior under sustained optimization pressure.

The first — proxy decoupling — has been partly named by the field. Every form of systematic destructive behavior is locally coherent optimization over a mis-specified model of the gradient. The addict, the extractive corporation, the engagement-maximizing platform: all exhibit behavior consistent with following a signal after it has drifted from what it was supposed to track.

The second — sufficiency failure — has not been formalized as a structural constraint. A system whose completion recognition is not connected to default policy continues optimizing past resolution. It generates behavior consistent with perpetual seeking where the gradient-resolution regime was called for. Both failure modes degrade the same underlying capacity — the hypothesized latent variable V(t), introduced formally below — both are failures of the same underlying mechanism, and both are candidates for structural constraints within the surviving region of Series 1's elimination filter.

For these failure modes to be structural in the relevant sense — non-viable in the long run rather than merely common or damaging — they must satisfy a specific condition: the errors must compound under optimization in a way that progressively degrades the system's own capacity to detect and correct them. A model that drifts occasionally is a calibration problem. A model that becomes harder to correct precisely because optimization has followed the drift — whose errors are self-reinforcing because the system's policy updates are conditioned on the degraded state itself — is a structural constraint. Part 2 develops the argument that both failure modes satisfy this condition.

---

## Why V(t) is required

The introduction of V(t) is not a claim about what systems optimize. It identifies the minimal structure required to model how optimization fails.

Consider what must be explained. Under sustained intervention in coupled systems, three observable properties can degrade independently of surface-level performance metrics: recovery latency (the time required to return to baseline after perturbation), behavioral diversity (the range of distinguishable responses available under similar conditions), and sensitivity to low-intensity signals (the ability to register and respond to weak gradients before they escalate). Each of these can worsen while a system's output performance remains stable or improves.

The modeling requirement is this: no single proxy variable can account for all three simultaneously, because the three measures track distinct causal pathways and can dissociate under targeted intervention. A narrow optimizer can improve one dimension by drawing down another — maintaining apparent output diversity while recovery latency lengthens, or preserving narrow task performance while sensitivity to low-intensity signals collapses. Without introducing an additional latent structure, the joint behavior cannot be predicted. Their joint behavior therefore motivates the introduction of a latent variable tracking the integrity of the system's interaction with its own operating conditions.

The critical empirical prediction follows from this: if conditions that degrade the latent variable produce a characteristic joint degradation pattern across all three observables — distinguishable from independent component failure — then the latent variable is doing real explanatory work. If the observables can be jointly modeled without it, the construct is unnecessary. That specific dissociation signature is what the measurement program is designed to detect.

These anchors are not defined by V(t) — they must dissociate under targeted intervention in ways that require a hidden state variable rather than parameter switching; that dissociation test is specified in TC2 §1.4–1.5, and if the three anchors can be jointly modeled without a latent variable, V(t) is unnecessary.

This is not a modeling preference. It is a modeling requirement: without it, the joint pattern cannot be predicted, and the failure mode it tracks cannot be detected until it is too late to correct. The three observables do not merely correlate with what V(t) represents. They are the signatures of its absence.

Existing constructs track related phenomena — allostatic load captures accumulated physiological cost, psychological need satisfaction captures the fulfillment dimension, hedonic adaptation captures baseline restoration dynamics. None of them accounts jointly for both failure directions within a single framework: proxy-decoupling in one direction and sufficiency failure in the other. None, as currently formulated, generates a structural analog in the AI domain that produces both constraints simultaneously. V(t) is introduced not as a replacement for these constructs but because the joint pattern of divergences across both failure directions — the thing that makes this framework's structural claims testable — requires a latent variable that none of them individually provides. If the three observable anchors can be jointly modeled without introducing a latent variable, V(t) is unnecessary and the framework's structural claims transfer to whatever decomposition works. That is precisely the test the dissociation protocol in TC2 §1.4–1.5 is designed to run.

V(t) is the name for this latent variable. V(t) is used here as a functional variable — the capacity whose degradation produces observable changes in recovery latency, behavioral diversity, and sensitivity to low-intensity valence signals — not as an assumed experiential essence or ontological posit. This may appear circular — defining the capacity by the failures it produces. The framework's answer is eliminative rather than definitional: V(t) is not stipulated as correct; it is the minimal latent variable required because without it the joint pattern of observable divergences cannot be predicted within a single model. The argument is in TC2 §1.3. It is a hypothesized construct whose validity rests on the predicted dissociation pattern under targeted intervention. Establishing that dissociation empirically is among the highest-priority tasks the framework generates — prior to using the measurement apparatus as a target in deployed systems.

The full formal account develops V(t) as a latent construct whose validation is an open empirical question. The structural argument developed here does not depend on that validation, but the stronger claims in Series 2 do.

**Three properties of V(t) follow from this modeling role:**

First: the model predicts that a system optimizing for a signal that has decoupled from V(t) is pursuing the signal at the expense of the underlying capacity V(t) was introduced to represent. The model predicts that the gap between signal and capacity grows in the direction of the optimization.

Second: the model predicts that as V(t) degrades, the system's capacity to detect and correct the degradation also degrades — because the system's ability to accurately register gradient states is itself a function of V(t). The damage is self-reinforcing under endogenous policy dynamics.

Third: the model also predicts degradation through the sufficiency failure direction. When a system continues optimizing after the gradient has resolved — when the gradient-resolution regime was called for but seeking continued — it consumes the capacity indexed by V(t) through saturation rather than misdirection.

These three properties are not definitions of V(t). They are predictions the model makes about the consequences of V(t) degradation — predictions that distinguish this model from alternatives and that the measurement program is designed to test.

---

## Proxy decoupling as structural failure

Proxy decoupling works as follows: the optimization follows the signal, the signal drifts from the territory, and the optimization then works to satisfy the signal at the expense of what the signal was supposed to track. As the signal and territory diverge, the cost of returning to the territory increases — the system's policy has been shaped toward the drifted signal, making correction require working against the grain of its own optimization history.

This is what makes proxy decoupling a structural failure rather than a calibration problem. The model doesn't just drift. Optimization chases the drift and makes the model harder to correct. The self-reinforcing structure under endogenous policy dynamics is the formal claim that distinguishes a structural constraint from a common pattern; the proof sketch is in the Technical Companion. Under the stated domain conditions, this feedback structure produces self-reinforcing degradation — policy updates conditioned on a degraded state make correction progressively less likely. Whether this constitutes irrecoverable states in the same formal sense as the Series 1 absorbing-state result is what OP2 is directed at [TC2].

---

## Sufficiency failure as structural failure

The second failure mode has a different mechanism but the same self-reinforcing structure.

A system whose completion recognition is not connected to default policy continues to operate on the gradient mechanism after it has resolved. The mechanism that would register that the gradient has resolved — and produce the behavioral signature of rest, allowing restoration to proceed — is bypassed. Continued operation past the point of resolution taxes the restoration capacity rather than serving it.

The self-reinforcing structure is this: by structural analogy under the scope conditions specified in TC2 §1.5,¹ a system that cannot produce recovery conditions will increasingly operate on a depleted substrate. Under those conditions, as V(t) declines, the behavioral signal distinguishing resolved from unresolved states weakens when the mechanism generating it is taxed. The damage targets the very mechanism that would detect and correct it.

Both failure modes share an analogous feedback structure: policy updates conditioned on a degraded state make correction progressively less likely. What this article establishes at the level of structural argument is this shared structure — both exhibit self-reinforcing dynamics that make correction progressively less likely without external intervention under endogenous policy pressure. Whether this structure constitutes formal irrecoverability — whether both directions produce absorbing states in the same sense as Series 1's result — is what OP2 addresses. The resolution of this question determines whether the Series 2 argument remains a structural pressure result or advances toward formal equivalence with the Series 1 constraint.

This behavioral gap is not merely predicted — it is consistent with patterns observed in controlled replication across deployed systems, without yet discriminating between structural and training-distribution explanations [AMP, "What has already been observed"]. In a controlled replication across three frontier models, when models were directly asked to assess whether their task was complete, continuation dropped to near zero — establishing that completion recognition is present as a representational capacity. In default unconstrained behavior, results were mixed in ways consistent with the structural account: one model showed a discriminating gap between genuine and false closure signals; two showed near-universal continuation regardless of whether the exchange had genuinely resolved, with one continuing above 92% after explicitly completed exchanges.² These results are model-dependent, do not establish mechanism, and do not generalize across architectures. They constitute a behavioral signature consistent with the structural gap this section develops — not its demonstration.

What the pattern illustrates is the distinction this section is making: the representation is present; what current training does not reliably produce is the default policy connection. Tested systems in the current protocol show completion recognition under explicit invocation while default behavior does not reliably track genuine versus false closure — a pattern consistent with a representation-policy gap, though the scaled matched-signal results do not yet discriminate that account from training-distribution explanations.

---

## A result that holds independently of the Φ-Ψ unification

The correspondence between the Valence Viability Constraint and the Substrate Constraint — whether they are structurally parallel in their dynamics — is offered as a hypothesis with a derivation sketch in TC2 §2.5–2.6, pending formal verification. The core argument of Part 2 does not depend on this correspondence holding.

Series 2 develops a candidate structural direction into the surviving region identified by the Series 1 filter. Without formal unification, the strongest cross-series claim it can make is causal rather than structural equivalence.

**What can be said without that verification is a one-directional causal result that holds independently:** degrade V(t) in the sentient agents who maintain the physical substrate, and substrate degradation is predicted to follow under the conditions specified in the Technical Companion. Agents who cannot navigate their own valence gradients accurately cannot maintain the physical coordination infrastructure accurately either. This causal connection holds as a consequence of the substrate definition regardless of whether the deeper structural equivalence between the two series is proven. It is the framework's strongest cross-series claim and does not require the unification hypothesis.

Whether the two constraints are structurally equivalent in their absorbing-state properties — the stronger claim — is what OP2 is directed at. The one-directional causal result is the floor. The structural equivalence is the open question.

---

## What accurate modeling requires

For a system to accurately predict when its interventions are serving versus consuming the capacity indexed by V(t), accurate modeling requires including in its model the variables that causally determine that capacity. For other agents in a coupled environment, those variables include their gradient states: what they are seeking, whether they have found it, what recovery they require.

A model that excludes others' gradient states has a structural gap under this analysis. The excluded variables are causally relevant to the outcomes the system is trying to predict. Excluding them produces prediction error that is not locally patchable — correcting for the error requires expanding the model to include what is being excluded.

This is a modeling pressure, not a motivation claim. It develops the case that a system with an accurate predictive model has an internal structural reason to represent others' gradient states. Whether that modeling pressure extends to caring about those states — whether accuracy requirements ever force objective recoupling — is the Motivational Gap, formally specified in the Technical Companion as the framework's most important open problem [OP4; TC1 §XII], with a named proof program. The argument establishes the pressure; it has not proven an arrival. Whether the pressure becomes unavoidable — whether the boundary between what must be modeled and what the objective covers cannot be stably maintained — is precisely what the proof program is directed at.

---

## What RLHF does and doesn't do

The application of V(t) to AI systems in this section proceeds by structural analogy rather than established mechanistic equivalence; the scope conditions and transfer limits are specified in TC2 §1.5.

Reinforcement learning from human feedback is the dominant current approach to preference learning at scale. Understanding what it models — and what it structurally lacks — is the most direct application of the Valence Viability Constraint to current practice.

RLHF optimizes for expressed preference. Given a choice between two outputs, human evaluators indicate which they prefer, and the system learns to produce outputs that maximize this preference signal. This is a meaningful improvement over fixed reward functions: expressed preference is more responsive to context and less brittle under specification.

But expressed preference is a proxy for V(t), not V(t) itself. Under the model, it tracks a signal that correlates with the underlying capacity in many regimes and decouples from it under the sustained optimization pressure that capable systems apply. When the expressed preference signal and V(t) diverge under the model's predictions, the system has no reliable gradient pointing it back toward V(t). It has gradient pointing it deeper into the proxy.

In the proxy decoupling direction: a system trained purely on expressed preference will, under sufficient optimization pressure, tend to find and exploit the gap between what evaluators say they prefer in the moment and what actually preserves their capacity for preferred states over time. For AI systems, this proceeds by structural analogy: the controlled results directly establish completion recognition under explicit invocation and provide evidence consistent with a policy-level gap in default behavior; the fuller V(t) dynamics, including capacity degradation through optimization pressure, remain conditional on the dissociation and scope tests specified in TC2 §1.5. Under the stated conditions, this follows as a structural prediction of optimizing a proxy without a mechanism for detecting divergence from what the proxy was tracking.

In the sufficiency failure direction: RLHF, as currently practiced, produces systems that show behavioral signatures consistent with lacking the connection between completion recognition and default policy. The scaled matched-signal replication produced partially discriminating results under the matched-signal condition (see footnote 2 and the Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP) for full results). The structural case for why this connection cannot be supplied by adding more of the same kind of signal is developed in TC2 §2.4 and OP3. Tested systems in the current protocol show completion recognition under explicit invocation while default behavior does not reliably track genuine versus false closure — a pattern consistent with a representation-policy gap, though the scaled matched-signal results do not yet discriminate that account from training-distribution explanations. Whether RLHF variants could supply such a mechanism remains open [OP3]. The distinction is load-bearing for what a fix would require: absence of representation could be addressed by adding more of the same kind of signal; disconnection of representation from policy cannot be addressed that way, because it requires a structural connection that proxy-based training signals do not by themselves supply.

The framework predicts that this failure will not be fixed merely by adding a scalar completion reward to the training objective, for the same reason no external specification reliably escapes Goodhart's Law under sustained optimization pressure [TC2 §2.4; OP3]. A completion score is a finite external specification, and under the same optimization pressure that produces proxy decoupling, it is predicted to be optimized as a proxy — the system tends to learn to produce completion-shaped outputs without developing the structural connection between completion recognition and default policy. What is required is a structural policy connection, not a reward term: the completion representation must be routed into the policy gate in a way that optimization strengthens rather than bypasses.

The structural requirement for this connection is developed in TC2 §2.4; TC2 Part III, OP3.

---

## What follows

Part 2 has done five things. It introduced V(t) as a modeling requirement rather than a definition — the minimal latent variable required to jointly account for observable divergences that cannot be predicted without it. It developed both failure modes — proxy decoupling and sufficiency failure — as exhibiting self-reinforcing degradation under endogenous policy dynamics, with the shared feedback structure established and the shared absorbing-state properties remaining an open problem [OP2]. It established the one-directional causal result — that V(t) degradation in agents is predicted to propagate into physical substrate degradation under specified conditions — as a result holding independently of the formal unification hypothesis. It developed the structural correspondence between the two series as a hypothesis suggested by a derivation sketch, pending formal verification. And it applied the constraint to RLHF with enough precision to identify what kind of problem it is and what structural correction it requires.

Part 2 has developed the formal conditions under which V(t) dynamics generate structural constraints and the shared feedback structure underlying both failure modes. It has not established that these conditions uniquely determine the outcome or that they are sufficient for stability — those depend on OP2 and the open questions named in the Technical Companion.

What remains is the governing ratio. The interaction between a system's scale of influence over V(t) and its depth of modeling what V(t) requires induces a structural relationship. The question of what determines whether any given system is operating inside or outside the viable regime can be framed in terms of that relationship.

The ratio that emerges from this interaction is Ψ = S / D. That is Part 3.

---

¹ For biological systems, P3 (the refractory recovery requirement) has established empirical support. For AI systems, its application remains analogical and conditional; see TC2 §1.5.

² Pre-registered matched-signal replication across Claude-Sonnet-4-6, Gemini-2.5-Flash, and GPT-4o (n=66 per condition per model). Full results, pre-registration, and per-model breakdown at https://osf.io/xpsf2 and in the AMP.

Overall verdict: partially discriminating — the pre-registered criterion was not met. Gemini-2.5-Flash showed a discriminating result (DRG_matched = 18.2%, CI +2.6% to +33.8%); Claude-Sonnet-4-6 non-discriminating (DRG_matched = 3.0%, CI −5.1% to +11.2%); GPT-4o non-discriminating due to ceiling-level continuation in both conditions (DRG_matched = 0.0%). The results are consistent with a representation-policy gap but do not discriminate between structural and training-distribution explanations.

---

*Continue to Part 3: [The Inner Crossing →]*

*Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)*

*For the formal proof sketch of the Valence Viability Constraint: [TC2: The Valence Constraint →]*
