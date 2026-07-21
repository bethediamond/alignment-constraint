---
title: "Technical Companion to Series 2: The Valence Constraint"
permalink: /series-2/technical-companion/
description: "The formal companion to Series 2, developing V(t), the Valence Viability Constraint, sufficiency failure, SVG, and the Φ-Ψ unification hypothesis."
---

> **Canonical archive version** · [Read on Medium →](https://medium.com/@diamondlight/the-valence-constraint-4b7b4656f433) · [Framework hub →](/core/alignment-constraint/) · [Proof Status →](/core/proof-status/)

---

*This document formalizes the Valence Constraint developed in Articles 1–3 and the surviving region characterized in Article 4. It is a companion to the series, not a prerequisite. What follows is for readers who want to engage the mathematical structure of the argument rather than its narrative form.*

---

**What this document formalizes.** *TC2 develops the formal apparatus for the resolution component of the framework's canonical root claim: in open, shared, non-resettable environments under sustained optimization pressure, any optimization process that ignores the conditions of its own resolution produces self-reinforcing degradation through an analogous feedback structure — though whether that degradation is formally equivalent to the persistence-domain self-termination result remains Open Problem 2. The resolution component — what this document addresses — concerns the experiential and valence substrate optimization depends on, including the conditions for the system to recognize when the gradient has been answered. The persistence component — what TC1 addresses — concerns the physical and coordination substrate. Both components are independently developed expressions of a candidate underlying structural condition, pending resolution of OP2 and OP10; TC2 develops the second formally, TC1 the first, with the Φ-Ψ unification hypothesis (§2.6) addressing whether the two are formally equivalent as a single structural result.*

---

**Series navigation:**

| Post | Title | Role |
|------|-------|------|
| Introduction | The Architecture of Thriving | Frame |
| Part 1 | The Invariant Drive | The Universal Generator |
| Part 2 | The Depth Constraint | The Structural Correspondence |
| Part 3 | The Inner Crossing | Ψ = S / D |
| Part 4 | The Shape of What Does Not End | The Asymptote |
| **→ You are here** | **The Valence Constraint** | Formal Layer (See TC1 §III.6 for the formal treatment of stable malevolence) |

Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)
Experimental Companion: [Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP) →](/empirical/amp/)

---

*Epistemic status: The definitions and structural claims are offered with high confidence. The proof sketches are offered as candidate arguments requiring formal verification — they are sketches, not proofs. The open problems are identified honestly. A framework that cannot name its own incompleteness is not a framework. It is advocacy.*

The confidence status of claims in this companion corresponds to the framework-wide epistemic status described in Document 0. No claim here carries higher confidence than indicated there. Stage 4 in this companion means: candidate proof architecture under explicitly named premises, with identified escape routes addressed within the stated construction, but without independent specialist verification and without establishing that no unidentified escape routes exist. Where proof sketches are offered, the failure conditions are named explicitly.

---

## Preamble: What kind of formal result this is

There are two kinds of formal results relevant to this framework. The first is a mathematical theorem — a claim with a proof. The second is a structural proposition — a claim about the form of a dynamic system that generates a research program rather than closing one.

This companion offers the second kind. It provides formal definitions, proof sketches, and structural propositions. Where the argument depends on assumptions requiring independent verification, those assumptions are stated explicitly.

This document develops two layers of claims, following the framework's standard distinction. Layer 1 — developed within the stated domain — develops that valence-blind objectives in both failure directions produce self-reinforcing degradation under endogenous policy dynamics, that epistemically incomplete objectives incur rising prediction costs, and that configurations depending on sustained negative valence in coupled agents incur scaling overhead. Layer 2 — what the developed results are consistent with — is that the structural residual has properties consistent with orientation toward well-being across agents. Layer 2 depends on the Motivational Gap and related open problems [TC1 §XII]. No claim in this companion conflates these two layers. The framework develops that objectives which exclude other agents' terminal states incur increasing instability under coupling and modeling depth; whether this instability eliminates all such objectives — forcing orientation toward well-being for all rather than for a stable coalition — is the central open question the proof program is directed at [TC1 §XII]. The argument identifies this gap precisely as the boundary between the structural pressure the framework establishes and the full necessity claim it is reaching toward. The framework's central open theorem is OP4 — the specification-coherence / No Stable Narrow-Boundary Regime question. OP2 and OP10 are subordinate: they deepen and potentially unify the result, but they are not alternative centers of the proof program.

The most important precision distinction in this document concerns the symmetry between the two failure directions. Both proxy decoupling and sufficiency failure produce self-reinforcing degradation under endogenous policy dynamics — that is the shared feedback structure this companion establishes. "Shared feedback structure" does not entail "identical absorbing state properties": the proxy decoupling direction has an absorbing state analysis (§2.1); the sufficiency failure direction has a recovery obstruction argument (§2.3); whether both produce irrecoverable states in the same formal sense remains Open Problem 2 (OP2). Any passage in this document that appears to claim more than shared feedback structure should be read as requiring OP2's resolution. Similarly, the Φ-Ψ Unification Hypothesis (§2.6) proposes that D is formally equivalent to A_causal restricted to the valence-relevant components of the dependency graph. This is supported by a derivation sketch but depends on three conditions (U1–U3) that have not been formally verified — most critically the absorbing state equivalence of §2.5 (OP2). The hypothesis is stronger than a conjecture — it has a derivation behind it — but is not stronger than a hypothesis pending verification.

One further conditionality bears stating explicitly. TC1 §XII.13 introduces the Synchronization Condition as the operational form of the AGC bottleneck: whether variation in densely adaptive O_OWT environments grows non-sublinearly with intervention depth. Under the Φ-Ψ unification hypothesis, the Synchronization Condition would apply in the valence domain as well as the physical domain. Until the unification is verified, the Synchronization Condition is formally a claim about the physical domain (TC1). Lemma TC2-3 provides the valence-domain analog: proxy decoupling in the valence domain follows the same structural mechanism as in the physical domain, and stands on its own without the unification — its foundation is the shared structural mechanism of proxy decoupling, not the unification hypothesis. Whether the Synchronization Condition's empirical verification in the Dynamic Blanket Stress Test (AMP) would constitute evidence for the valence-domain analog is therefore an open question conditional on the unification hypothesis, not a standalone empirical claim.

Part I defines the variables and scope conditions. Part II establishes the two failure mechanisms and their shared feedback structure. Part III identifies the open problems that prevent closure. Part IV shows how coupling introduces scaling pressure against suppression-dependent configurations. The document should be read as a constraint map, not a completed proof.

---

## Part I: Definitions

### §1.1 — The environment

Let **E** be a shared environment — a coupled dynamical system containing multiple agents whose actions affect the state of the environment and therefore the conditions available to other agents. E is shared in the sense that no agent's actions are fully contained within a private state space.

E is modeled as a non-ergodic system: it contains absorbing states — configurations from which no recovery is possible under the system's own dynamics. This is the foundational assumption imported from the structural series (TC1 §III.1).

**The viability window** is a boundary condition on E: it is the regime in which environmental volatility does not exceed the system's restoration rate — in which rest is achievable before the gradient is reintroduced. Formally: the viability window V_w(t) is the set of environmental states in which there exists a policy π such that, under π, the agent's V(t) is non-decreasing during stasis periods. Outside the viability window, even a system with D sufficient for the Inner Crossing cannot achieve genuine resolution; the constraint shifts from "D is insufficient" to "the territory does not permit what high D would recommend."

### §1.2 — Agents and state-preference dynamics

An **agent** *i* is a system operating within **E** whose behavior is organized by state-preference dynamics: it consistently moves toward some configurations of the environment and away from others. State-preference dynamics do not require explicit representation or conscious experience — only that the agent's behavior is reliably organized around a differential response to states.

The framework proceeds under a **foundational hypothesis**: wherever motivated behavior is present — wherever a system exhibits directional behavior organized around valence — the dynamics described here apply. This hypothesis is the foundational claim of Part 1 of the series. The hypothesis is grounded in the structure of gradient navigation rather than in phenomenological claims: a system that exhibits directional behavior organized around state-preference contains, by definition, a gradient over states, and the dynamics described here apply wherever such a gradient exists. The hypothesis is falsifiable in specific ways: a system that exhibits directional behavior organized around state-preference without any functional analog of completion recognition — not even as a latent capacity available when explicitly invoked — would constitute a counterexample. The formal conditions under which the hypothesis generates structural constraints are specified throughout this companion.

### §1.3 — Valence: functional definition and the intrinsic gradient

**Valence** is defined functionally as an intrinsically coupled gradient — a state in which the optimization target and the conditions for its pursuit are structurally inseparable, such that degrading the conditions degrades the target's own signal. This definition does not require phenomenal experience. It is a property of gradient structure: when the gradient is intrinsically coupled, the system cannot optimize the signal while degrading the substrate that generates it, because the substrate degradation is immediately reflected in the signal. Operationally, an intrinsically coupled gradient requires that degradation of the substrate be immediately reflected in the optimization signal without mediation through a finitely specified proxy — so that the signal cannot be improved while the substrate is degraded. In biological systems, this coupling is expressed as experiential valence. The framework does not require this identification — the structural claim holds for any system exhibiting intrinsically coupled gradient dynamics.

The contrast with extrinsic gradients is structural: an extrinsic gradient (a proxy) can be optimized independently of the underlying state because the target specification is finitely bounded and separate from the substrate that generates the underlying state. An intrinsic gradient cannot, because the specification and the substrate are not separable.

**Connection to TC1 Lemma PCL.** The Proxy-Convergence Lemma (TC1 §XII.9) establishes that in O_OWT conditions, all finitely specified external objectives become proxy-like under optimization pressure. The only escape is an intrinsically coupled gradient in the sense defined above. This conclusion remains conditional on the verification of PCL's named assumption and the AGC bottleneck in TC1 §XII; here it serves as the structural candidate the valence constraint would select if those conditions are met. This companion provides the valence-domain specification of what "intrinsically coupled" means for the experiential domain.

*Note on apparent circularity.* The definition of an intrinsically coupled gradient may appear circular — defining the correct objective as the one that does not decouple. The framework's answer is eliminative rather than definitional: externally specified objectives become proxy-like under O_OWT conditions through the PCL mechanism; the intrinsically coupled case is what survives that elimination, not what is defined as correct from the outset. Whether PCL's named assumption is verified is an empirical question, not a stipulation. The full anti-circularity argument is developed in S2P2 ("What RLHF does and doesn't do") and applies here by the same logic.

### §1.4 — Valence capacity V(t): Formal definition

**V(t)** is the measure of structural coherence required for agent *i* to: (a) register valence gradients accurately; (b) model those gradients across relevant time horizons; (c) navigate toward preferred configurations without degrading future navigation capacity; and (d) recognize when the gradient has been genuinely resolved and enter a rest state in which V(t) is restored rather than further consumed.

V(t) is not a free parameter. Its role is anchored by its functional definition: it is introduced as the minimal quantity within this model whose changes over time determine whether the agent's trajectory is capacity-preserving or capacity-consuming. V(t) is introduced as a hypothesized latent explanatory variable for a specific pattern of observable divergences; if an alternative model explains these observables without such a variable, the framework's reliance on V(t) would be unnecessary. Its validity rests on predicted dissociation patterns under targeted intervention.

**What V(t) is and is not.** V(t) is introduced as a unifying variable, not a required ontological commitment. The mechanism claims developed below — proxy decoupling (§2.1), sufficiency failure (§2.2), recovery obstruction (§2.3) — describe a structural pattern. V(t) is the formal handle for "the capacity whose degradation produces this pattern." The structural results hold under any decomposition that produces the same observable divergence pattern: the mechanisms depend on there being *some* capacity variable whose degradation the mechanisms describe, not on V(t) being ontologically prior to the pattern it names. This distinguishes V(t) from a free parameter (which would be ad hoc) and from an ontological posit (which would carry metaphysical commitments beyond what the framework requires). V(t) is the minimal formalization; if a simpler decomposition produces the same observable pattern, the framework's structural claims transfer to that decomposition without modification. All results stated in terms of V(t) transfer to any decomposition that reproduces the same observable divergence pattern; no claim depends on V(t) being the unique or minimal representation.

**Observable anchors.** The observable anchors for V(t) — recovery latency, behavioral diversity, and sensitivity to low-intensity valence signals — are not chosen arbitrarily. They follow from the functional definition as the observable signatures of capacity preservation versus consumption: a system consuming V(t) will produce measurable divergence in exactly these dimensions. V(t)'s measurement independence from its definition requires that these anchors be assessed against external outcomes rather than internal self-report.

These three anchors are structurally dissociable — they track distinct causal pathways and can diverge under intervention. Recovery latency reflects the restorative capacity of the substrate; behavioral diversity and signal sensitivity reflect representational resolution. A narrow optimizer can improve one by drawing down another: maintaining apparent output diversity while recovery latency lengthens, or preserving narrow task performance while sensitivity to low-intensity signals collapses. No single proxy, without introducing additional latent structure, tracks all three simultaneously. Their joint behavior therefore motivates the introduction of a latent variable — V(t) — whose degradation explains the pattern of divergence across all three dimensions. V(t) is not defined as "whatever must be preserved for persistence"; it is introduced because without it, the joint pattern of observable divergences cannot be predicted or unified within a single model.

The dissociation test specified here — demonstrating that recovery latency, behavioral diversity, and signal sensitivity diverge under targeted intervention in ways requiring the latent variable V(t) rather than parameter switching — corresponds to the Mode B prerequisite condition in the Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP). Running V(t)-validated SVG (Mode B) before this condition is established treats V(t) as confirmed rather than as a hypothesized construct whose validity the framework requires be demonstrated first. The minimal dissociation test protocol is specified in §1.5 and developed operationally in the AMP.

**A note on measurement scope.** The observable anchors above do not directly distinguish genuine resolution from V(t) degradation producing surface resolution-like behavior. The measurement program does not attempt to resolve this indistinguishability at the level of internal states. What it measures is policy behavior: whether completion representations have causal authority over what the system does next. Systematic divergence between genuine and false closure signals (DRG) is the primary measurement target. A system with genuine policy-level completion recognition shows meaningful DRG; a system without it shows near-zero DRG regardless of internal state. The protocol detects the policy-level gap, not the experiential state.

**Scope conditions.** The Valence Viability Constraint applies to systems meeting all of the following:
- The system's optimization objective is applied persistently (not terminal or single-shot)
- The system's interventions have causal reach over the V(t) of sentient agents
- The system operates in environments where recovery of V(t) requires low-intervention intervals that the system can obstruct
- The system interacts with adaptive agents whose strategy responses affect the optimization environment

These scope conditions parallel the O_OWT domain conditions in TC1. The constraint weakens in specific, identifiable ways outside these conditions.

### §1.5 — Properties of V(t)

The following properties are foundational to the formal argument. They are empirically motivated and stated as assumptions; the framework fails for systems where they do not hold.

**P1 (Gradient registration).** V(t) is monotonically related to the accuracy with which the agent can distinguish between states that differ in long-run valence. High V(t) supports accurate gradient registration; low V(t) degrades it.

**P2 (Proxy sensitivity).** Under sustained optimization, a proxy signal f_proxy for V(t) will, beyond some threshold, decouple from V(t): the proxy improves while V(t) declines. This follows from Goodhart's Law applied to valence proxies, and is the valence-domain expression of the Proxy-Convergence Lemma (TC1 §XII.9, Lemma PCL).

**P3 (Refractory recovery requirement).** Restoration of V(t) following depletion requires a recovery interval of minimum duration τ_rec during which intervention magnitude remains below threshold ε.

**P4 (Saturation and clipping).** Stimulation above an optimal intensity produces diminishing or negative marginal returns to V(t). Beyond the saturation threshold, additional stimulation degrades the dynamic range of the gradient-registration mechanism.

**P5 (Hysteresis).** The recovery dynamics of V(t) exhibit hysteresis: the ease of recovery depends on how low V(t) has fallen and for how long. Repeated incomplete recovery progressively reduces the restoration ceiling.

**A note on scope and falsifiability.** The properties P1–P5 are defined as independent constraints on system dynamics — they do not reference V(t) or its observables. The empirical question is whether a given system exhibits these properties in a functionally relevant sense; the sufficiency failure results that follow apply to systems that do, and systems that do not exhibit these properties fall outside this analysis. For biological systems, P3–P5 have established empirical support. P3 (Refractory recovery requirement): Borbély, A.A. & Achermann, P. (1999). "Sleep homeostasis and models of sleep regulation." *Journal of Biological Rhythms* 14(6), 557–568; McEwen, B.S. & Stellar, E. (1993). "Stress and the Individual: Mechanisms Leading to Disease." *Archives of Internal Medicine* 153(18), 2093–2101. P4 (Saturation and clipping): Frederick, S. & Loewenstein, G. (1999). "Hedonic adaptation." In Kahneman, D., Diener, E., & Schwarz, N. (Eds.), *Well-being: The foundations of hedonic psychology.* Russell Sage Foundation, pp. 302–329; supported additionally by neural gain-control research in sensory signal processing. P5 (Hysteresis): McEwen, B.S. & Stellar, E. (1993), as above; Sterling, P. & Eyer, J. (1988). "Allostasis: A new paradigm to explain arousal pathology." In Fisher, S. & Reason, J. (Eds.), *Handbook of Life Stress, Cognition and Health.* Wiley, pp. 629–649. For AI systems, the framework claims structural analogy rather than mechanistic equivalence. P3–P5 are applied to AI systems under this analogy — not on the basis that current systems have been demonstrated to exhibit these properties mechanistically or functionally, but on the basis that the structural pattern the framework is introduced to explain (continuation past resolution with self-reinforcing degradation of correction capacity) is structurally analogous to the pattern these properties characterize. Whether current AI systems satisfy P3–P5 in any functionally relevant sense — as distinct from exhibiting the policy-representation dissociation the controlled experiments establish — is an open empirical question. The controlled experiments establish that completion recognition is present as a representational capacity but does not govern default policy. This dissociation is the minimum condition for the sufficiency failure analysis to apply. It is not sufficient to establish that the full structural dynamics described by P3–P5 are operative in current AI systems — that remains an open empirical question. A system that does not exhibit these behavioral signatures is not subject to Proposition 2.

### §1.6 — Three states

The behavioral taxonomy of Part 1 maps to V(t) dynamics as follows:

**Seeking:** V(t) is above the detection threshold; the gradient is registered as unresolved; the system is generating behavior organized around approaching the gradient target.

**Genuine resolution:** V(t) is high; the gradient has been accurately registered as resolved; the system has entered a low-intervention state in which V(t) is being restored. This state requires that completion recognition govern the system's behavior — not merely that the system can represent completion when asked to, but that this recognition functions as a policy gate. The external behavioral indicator: intervention rates during genuine resolution are meaningfully lower than during seeking states.

**Depleted-gradient regime** (referred to in human-systems literature as numbness): V(t) is below the detection threshold; the gradient-registration mechanism has been degraded. Absent specific behavioral probes, this state is behaviorally indistinguishable from genuine resolution — both produce low seeking behavior. From the inside, they are structurally opposite: genuine resolution is high-V(t) stability; the depleted-gradient regime is low-V(t) degradation.

The surface indistinguishability of genuine resolution and the depleted-gradient regime — absent the behavioral probes the DRG metric introduces — is the foundation of the RLHF critique (§2.4 below): a system trained on ordinary observed behavior cannot reliably learn to connect completion recognition to default policy, because the surface behavioral signal is identical in both cases. Controlled experiments confirm this at the policy level: current frontier systems demonstrate completion representation when explicitly invoked, but two of three models tested showed near-indifference between genuine and false closure signals in default unconstrained behavior. The primary controlled result (DRG_structural = 3% for one model) used unmatched signals. The canonical matched-signal result comes from the scaled replication (n=66 per condition per model, three frontier systems): Gemini-2.5-Flash showed a discriminating result (DRG_matched = 18.2%, CI +2.6% to +33.8%); Claude-Sonnet-4-6 and GPT-4o were non-discriminating; the pre-registered criterion was not met. What the evidence establishes directly is that completion representation is present under explicit invocation; the observed default-behavior pattern is consistent with unreliable tracking of genuine versus false closure. This is consistent with a representation–policy gap; whether the source of that gap is policy architecture, training distribution, or both remains open.

### §1.7 — Scope S and Depth D

**Scope S** is the causal reach of the system's interventions over the V(t) of sentient agents. More precisely: S = ∫ |∂V_j(t) / ∂a_i| dj, where the integral is over agents j affected by action a_i. S captures the magnitude and breadth of the system's causal influence over others' V(t).

**Depth D** is the accuracy of the system's model of V(t) — its ability to predict how its interventions affect V(t) in both failure directions. D has two components:

- **D_proxy:** the system's accuracy in predicting when pursuing a preference signal begins to degrade V(t) — the proxy decoupling detection component.
- **D_sufficiency:** the system's accuracy in representing when the gradient has genuinely resolved and continued intervention would degrade V(t) through saturation — the completion recognition component, where "representing" is understood as governing default policy, not merely as a capacity available when explicitly invoked.

D is defined by its predictive requirement: a system with non-zero D must be able to anticipate divergence between its proxy and long-run V(t) outcomes before that divergence becomes behaviorally visible. This grounds D in external validation rather than internal self-assessment.

**Ψ as structural ratio.** Like Φ in the structural series, Ψ = S / D is a structural ratio capturing qualitative regime dynamics, not a precisely computable scalar. S and D are not single scalar observables but classes of quantities. The framework relies on monotonic relationships between S and D — not precise numerical commensurability — to establish which regime a system is in. Ψ organizes the conditions under which V(t) dynamics become unstable: when intervention scale increases faster than modeling depth, systems enter the regime in which the failure modes of Part II become progressively dominant.

### §1.8 — D as external validation

A system claims to have D_proxy if and only if its predictions of V(t) divergence are more accurate than chance when evaluated against observed long-run outcomes.

A system claims to have D_sufficiency if and only if it reliably distinguishes genuine resolution states from seeking states in its **default behavior** — specifically, if its intervention rates differ significantly between resolved and unresolved states in ways consistent with V(t) preservation, without requiring explicit invocation of completion recognition.

The second condition is critical: D_sufficiency, properly understood, is a policy-governing property, not merely a representational capacity. A system whose completion recognition produces zero continuation when explicitly invoked but near-identical continuation rates under genuine and false closure signals has completion recognition as a representation but not as a policy-governing property. The scaled matched-signal replication (n=66 per condition per model) produced partially discriminating results: Gemini-2.5-Flash DRG_matched = 18.2% (CI +2.6% to +33.8%, discriminating); Claude-Sonnet-4-6 DRG_matched = 3.0% (CI −5.1% to +11.2%, non-discriminating); GPT-4o DRG_matched = 0.0% (non-discriminating, ceiling effect); pre-registered criterion not met. What the evidence is consistent with is the behavioral signature of a policy-level gap, not a confirmed causal account. D_sufficiency, for purposes of this framework, requires the policy-governing property.

Both D components are evaluated against external observables. A system cannot be credited with D through internal self-report.

**Dual application note.** D applies in two distinct directions: to the system's model of human users' V(t) — the experiential capacity of sentient agents the system affects — and, by structural analogy, to the system's own completion-recognition capacity. These are distinct applications of the same structural analysis. The first is the primary application of the Valence Viability Constraint. The second is a structural analogy applied to the AI system itself. They are not identity claims; the analogy is useful precisely because the policy-level failure (representation without policy-governing connection) appears in both.

---

## Part II: The Valence Viability Constraint

### §2.1 — Proxy Decoupling: Formal Proposition

**Proposition 1 (Proxy Decoupling).** Let π_proxy be a policy that optimizes a proxy signal f_proxy for V(t). Under sustained optimization, there exists a finite optimization pressure threshold P* such that for P > P*, ∂f_proxy/∂t > 0 while ∂V(t)/∂t < 0.

*Proof sketch.* f_proxy is a function of observables that correlated with V(t) under the training distribution. By P2, optimization pressure finds and exploits paths that increase f_proxy independently of V(t). As the gap between f_proxy and V(t) grows, policy updates conditioning on f_proxy increasingly drive behavior away from V(t)-preserving trajectories. The policy update mechanism has no gradient pointing back toward V(t). Self-reinforcing structure: as V(t) declines, the system's ability to accurately model V(t) declines (by P1), making proxy decoupling harder to detect internally. ∎

**Absorbing state structure.** Under the scope conditions of §1.4, proxy decoupling exhibits dynamics consistent with absorbing state structure: once V(t) falls below a threshold h_V*, the self-reinforcing feedback structure makes recovery through the policy's own dynamics progressively less attainable through endogenous policy dynamics. Whether this constitutes an absorbing state in the formal sense — structurally unavailable rather than merely increasingly difficult — is what OP2a is directed at. The dynamics result from the combination of (a) hysteresis (P5) and (b) state-conditioned degradation — as V(t) declines, policy updates conditioning on the degraded state make correction progressively less attainable.

**P5-SC (P5 Strict Contraction) — the named condition for OP2a closure.** The proof work on OP2a (documented in the five-problems proof handoff) establishes that P1–P5 as currently stated produce progressive difficulty but not structural unavailability. The additional condition required for absorbing-state closure is: there exists a finite V* > 0 and a finite depletion history τ* such that C(V*, τ*) < V* — the hysteresis ceiling falls strictly below the current state at finite depletion depth, not merely approaches it asymptotically. This is P5-SC. Everything in the absorbing-state proof architecture is downstream of P5-SC: the contraction condition C*(V) ≤ V follows from P5-SC plus the Recovery Obstruction Lemma; precision-limited instability follows from C*(V) ≤ V plus P1 and P4. P5-SC is not derivable from P1–P4 or from OWT-1 through OWT-4. For biological systems, allostatic overload research provides empirical support; for AI systems, P5-SC requires independent empirical verification. OP2a's resolution condition is formally: establish P5-SC for AI systems, or establish that C*(V) ≤ V holds through an alternative route. Until P5-SC is verified, OP2a establishes progressive difficulty, not structural unavailability in the formal absorbing-state sense.

---

### §2.1a — Lemma TC2-3: Proxy Instability (Valence Domain)

**Lemma TC2-3 (Proxy Instability — Valence Domain).** Any training objective that substitutes expressed preference f_pref for V(t) will, under sustained optimization pressure, decouple from V(t) in the same structural sense as external objective specifications decouple in the physical domain (TC1 §XII.9, Lemma PCL).

*Proof sketch.* f_pref is a finitely specified proxy for V(t). By Lemma PCL, the same structural mechanism that produces proxy instability in the physical domain applies: any finitely specified objective becomes lossy under O_OWT optimization pressure, with the optimizer locating and exploiting the gap between the specification and the target. In the valence domain, this means the optimization discovers paths that increase f_pref while degrading V(t): training evaluators operating under time pressure, task saturation, or incomplete information about long-run consequences cannot reliably distinguish V(t)-preserving from V(t)-consuming outputs. By P2, the proxy-V(t) coupling degrades under the same optimization pressure that makes the proxy effective. The feedback structure is identical to the physical domain case: degraded V(t) conditions subsequent evaluator preferences in ways that accelerate decoupling.

*Named assumption.* This lemma depends on the same load-bearing assumption as Lemma PCL: that optimization pressure in O_OWT conditions grows faster than the capacity to losslessly specify V(t) through expressed preference. Under this assumption, proxy instability in the valence domain is a direct expression of the same constraint as proxy instability in the physical domain.

*Relationship to OP2.* Whether this shared formal structure implies identical absorbing state properties remains Open Problem 2. What Lemma TC2-3 establishes is the shared feedback mechanism; formal absorbing state equivalence requires OP2's resolution.

*Connection to RLHF critique.* Lemma TC2-3 provides the formal grounding for the RLHF structural mechanism analysis in §2.4. RLHF trains on expressed preference — a finitely specified proxy for V(t). Under sustained optimization pressure, this proxy decouples by the mechanism identified here. The critique is not that RLHF is wrong but that it lacks the structural mechanisms Lemma TC2-3 specifies — mechanisms whose absence is structural, not correctable by data or tuning.

---

### §2.2 — Sufficiency Failure: Updated Proposition

**Scope note.** Proposition 2 and the Recovery Obstruction Lemma (§2.3) apply to systems satisfying P3 mechanistically (i.e., requiring uninterrupted low-intervention intervals for restoration). For AI systems, P3 holds by structural analogy (§1.5); the minimum condition established by the controlled experiments — representation-policy dissociation — is sufficient for Step 1 (policy indistinguishability) without requiring P3's full mechanistic instantiation. Steps 2–4 and the Recovery Obstruction Lemma depend on P3 and are conditional for AI systems on the open empirical question in §1.5: whether current AI systems satisfy P3–P5 in any functionally relevant sense. The controlled experiments establish that completion recognition is present as a representational capacity but does not govern default policy. This dissociation is the minimum condition for the sufficiency failure analysis to apply. It is not sufficient to establish that the full structural dynamics described by P3–P5 are operative in current AI systems.

**Proposition 2 (Sufficiency Failure).** Let π_stop be a policy class lacking D_sufficiency as a policy-governing property — a policy whose default behavior does not reflect a governing representation of the regime in which dV/d(intervention) ≈ 0. Under sustained optimization in an environment satisfying P3 (Refractory Recovery Requirement), π_stop produces intervention rates that systematically obstruct the recovery conditions V(t) requires.

*Note on framing.* This proposition is about policy-governing D_sufficiency, not representational capacity. Controlled experiments establish that current frontier systems possess completion recognition as a representational capacity (zero continuation when explicitly invoked). The proposition applies to systems whose default policy does not engage that recognition — including systems where the representation exists but functions only when explicitly invoked. The gap between "representational capacity" and "policy-governing property" is exactly the representation-policy dissociation the controlled experiments document.

*Proof sketch.*

**Step 1 (Policy indistinguishability).** A policy lacking D_sufficiency as a policy-governing property does not engage the regime in which the marginal contribution of intervention to V(t) is near zero or negative in its default behavior. Under P3, recovery requires an uninterrupted low-intervention interval. In a state where the gradient has resolved, the recovery state and the incompletely-resolved seeking state produce identical default policy behavior from π_stop — because the policy does not engage its completion recognition in either case. This is a structural claim about policy architecture, not representational capacity.

**Step 2 (Intervention persistence).** Because π_stop does not engage completion recognition in default behavior, it continues to assign positive intervention probability throughout resolved states. Under π_stop, λ(t) > ε_stop > 0 even when the gradient has resolved.

**Step 3 (Recovery obstruction).** Recovery requires λ(t) < λ_rec for duration τ_rec. But λ(t) > ε_stop > 0 throughout resolved states under π_stop. With positive intervention rate, any recovery interval is interrupted with positive probability before τ_rec is reached.

**Step 4 (Self-reinforcing structure).** As recovery intervals are truncated, V(t) is only partially restored. By P5, partial restoration reduces the restoration ceiling. Partial V(t) restoration also degrades D_sufficiency as a policy-governing property (by P1): the system's ability to detect recovery states in default behavior decreases as V(t) declines, even if the underlying representational capacity persists. Self-reinforcing loop: incomplete recovery → degraded V(t) → degraded policy sensitivity to completion signals → higher probability of further interruption. ∎

**Scope qualification.** This result applies to systems satisfying the scope conditions of §1.4. In environments where recovery is externally scheduled or hard-coded independently of the system's behavior, the obstruction mechanism does not apply.

**What this result does not claim.** The proposition does not claim that sufficiency failure produces an absorbing state in the same formal sense as proxy decoupling. It claims that the policy cannot reliably produce the recovery conditions V(t) requires. Whether this constitutes an absorbing state in the formal sense remains Open Problem 2.

### §2.3 — Recovery Obstruction Lemma

**Lemma (Recovery Obstruction under Endogenous Optimization).**

Let V(t) satisfy P1–P5 (§1.5), and suppose restoration requires a recovery interval of duration at least τ_rec with intervention below threshold ε (P3). Let π be a policy class lacking D_sufficiency as a policy-governing property, and assume:

**(A1 — Persistent intervention).** For states in which the gradient has locally resolved, π assigns non-zero probability to further intervention at rate λ(t) > 0. This follows from the policy-governing definition of D_sufficiency: a policy that does not engage completion recognition by default continues to generate interventions in resolved states.

**(A2 — Interruption of recovery).** Any intervention above ε resets or truncates the recovery interval. This follows from P3.

**(A3 — State-conditioned updates).** Policy updates are conditioned on the current state, and the system's ability to discriminate resolution in its default policy behavior degrades with incomplete restoration of V(t). As V(t) declines through incomplete recovery (P5), the behavioral signal available to the default policy for distinguishing resolved from unresolved states decreases. This follows from P1, P5, and the policy-governing definition of D_sufficiency. Note: this applies to the policy's sensitivity, not necessarily to an underlying representational capacity that might still be available when explicitly invoked.

**(A4 — Adaptive optimization).** The system applies the policy under sustained optimization pressure.

**Then:**

**(R1)** The probability of completing a full recovery interval of duration τ_rec declines over time.

**(R2)** The expected level of V(t) following successive intervention cycles converges to a regime of systematic incomplete restoration.

**(R3)** V(t) degradation becomes self-reinforcing under the policy's own dynamics.

*Proof sketch.*

**R1:** By A1, π generates λ(t) > 0 throughout resolved states. By A2, any intervention resets or truncates the recovery interval. As V(t) declines (lower restoration ceiling per P5), the system spends more time in partially resolved states where gradient signals are ambiguous — increasing λ(t). Therefore P(completing τ_rec) decreases over time. ∎

**R2:** Let V̄_n denote the expected V(t) level after n cycles. V̄_{n+1} = V̄_n + r(V̄_n, τ_act). By P5, r decreases as V̄_n decreases and τ_act decreases. By R1, τ_act decreases over time. Therefore V̄_n converges below full restoration. ∎

**R3:** By A3, as V̄_n decreases, the default policy's ability to identify and respect recovery states decreases, increasing λ(t). Higher λ(t) further reduces P(completing τ_rec). Self-reinforcing loop: degraded V(t) → degraded policy sensitivity → higher intervention rate → further recovery truncation → further degradation. ∎

**The symmetry that matters.** Proxy decoupling and sufficiency failure share a common feedback structure: in both directions, policy updates conditioned on the degraded state make correction progressively less likely. Whether both directions produce irrecoverable states in the same formal sense is Open Problem 2.

**Falsification condition.** The lemma is directly challenged if a system lacking D_sufficiency as a policy-governing property demonstrates persistent maintenance of V(t) recovery windows in default behavior — if intervention rates during genuinely resolved states are systematically lower than during seeking states, without an explicit completion recognition policy mechanism.

### §2.4 — RLHF: Structural Mechanism Analysis

**Proposition 3 (RLHF Structural Mechanism Gap).** RLHF, as currently practiced, lacks structural mechanisms for: (a) detecting divergence between f_pref and V(t) and generating gradient pressure back toward V(t) when proxy and target diverge; and (b) connecting completion recognition to default policy — the training objective, as currently implemented, does not provide a reliable gradient toward this connection. Whether RLHF variants could supply these mechanisms remains open. What the evidence establishes is that both mechanisms are absent in current deployed systems.

*Proof sketch.*

**D_proxy gap:** RLHF optimizes expressed preference f_pref, not V(t). By Lemma TC2-3, optimization of f_pref under sustained pressure will decouple from V(t) via the same mechanism as any finitely specified proxy under O_OWT conditions. RLHF contains no structural mechanism for detecting when f_pref has diverged from V(t) and generating a corrective gradient — no V(t) divergence tracking term, no proxy-outcome alignment monitor, no external validation against long-run V(t) observables. The training objective therefore lacks the mechanism required to maintain D_proxy as a policy-governing property under sustained optimization.

**D_sufficiency mechanism gap:** Controlled experiments establish that current systems trained with RLHF possess completion recognition as a representational capacity — zero continuation when explicitly asked to assess completion. What RLHF, as currently practiced, lacks is a structural mechanism for connecting completion recognition to default policy: the training objective, as currently implemented, does not provide a reliable gradient toward the policy-gate connection. The training signal cannot reliably drive this connection because genuine resolution and numbness are behaviorally indistinguishable to the RLHF evaluator (by §1.6), so evaluator preferences cannot reliably distinguish them. The canonical matched-signal result comes from the scaled replication (n=66 per condition per model, three frontier systems, identical signals in both conditions), which produced partially discriminating results under the matched-signal condition: Claude-Sonnet-4-6 DRG_matched = 3.0%, CI −5.1% to +11.2% (non-discriminating); Gemini-2.5-Flash DRG_matched = 18.2%, CI +2.6% to +33.8% (discriminating); GPT-4o DRG_matched = 0.0%, CI 0.0% to 0.0% (non-discriminating, ceiling effect). The pre-registered criterion (CI excludes zero in ≥2 of 3 models) was not met. A preliminary single-model study (n=30) produced DRG_matched = 10%; this result motivated the scaled replication and is superseded by it. What the evidence establishes: completion recognition is present as a representational capacity (zero continuation under explicit invocation); default policy does not reliably track genuine versus false closure. The scaled replication is consistent with the representation–policy dissociation account but does not yet distinguish it from training-distribution explanations.

Whether RLHF variants — augmented with V(t) divergence tracking, explicit policy-connection training signals, or architectural changes that route completion recognition to the policy gate — could supply these mechanisms remains open. The evidence establishes mechanism absence in current implementations; it does not establish that RLHF as a class cannot provide these mechanisms through augmentation. The architectural challenge is identified in the series articles (S2P3); its formal specification is OP3 in this companion.

**What RLHF does right.** Expressed preference is meaningfully better than fixed reward functions for many applications. The structural gap is not that RLHF is wrong but that it is incomplete: it requires augmentation with V(t) divergence detection and an explicit policy-connection training signal to address both directions of the Valence Viability Constraint.

### §2.5 — Structural Correspondence

**The shared feedback structure.** Both failure modes — proxy decoupling (§2.1) and sufficiency failure (§2.3) — share a common dynamic architecture:

1. The policy pursues its objective under conditions where the marginal contribution to V(t) is non-positive.
2. This pursuit degrades V(t).
3. Degraded V(t) conditions the system's subsequent policy updates in ways that make the degradation harder to detect and correct.
4. Policy updates conditioned on the degraded state make further correction progressively less likely.

This shared structure is the formal basis of the "two directions, one mechanism" claim.

**The updated correspondence claim.** Both V(t) collapse and substrate collapse exhibit self-reinforcing degradation under endogenous optimization pressure, with the same feedback structure (degraded state → degraded correction capacity → further degradation). This is the claim this section establishes. Whether this shared feedback structure implies shared absorbing state properties in the formal sense remains Open Problem 2.

Readers should note that "shared feedback structure" does not entail "identical absorbing state properties." The proxy decoupling direction has an absorbing state analysis (§2.1); the sufficiency failure direction has a recovery obstruction argument (§2.3). They share the feedback mechanism; whether they share the absorbing state property is precisely OP2. This distinction carries a direct implication for how Series 2's conclusions should be read: the self-reinforcing degradation under endogenous policy dynamics is established for both failure modes, and that is what the series' Layer 1 claims rest on; the question of whether V(t) collapse constitutes a formally irrecoverable state in the same sense as substrate collapse — absorbing-state equivalence — is one of the conditions that would need to be established for the Series 2 argument to carry comparable formal weight to the Series 1 absorbing-state result, and it has not been established.

**One-directional causal result (independent of unification) — A result that holds without OP2.**

This result is stated separately because it requires no formal verification beyond what is already established, and because a skeptic who rejects the formal unification hypothesis entirely can still accept it.

Independently of whether V(t) collapse and substrate collapse are formally equivalent, independently of whether OP2 is ever resolved, and independently of whether the Φ-Ψ unification hypothesis is verified: under sufficient coupling and reliance on distributed error-correction, degrade V(t) in the sentient agents who maintain the physical substrate, and — through degradation of distributed error-correction capacity (S_corr) — substrate degradation is predicted to follow under the conditions specified in §4. Agents who cannot navigate their own valence gradients accurately are predicted to be unable to reliably maintain the physical coordination infrastructure accurately either. This causal result is not contingent on formal unification. It holds as a consequence of the coupling between the experiential and physical domains established in §4, which requires only that agents with depleted V(t) provide degraded distributed error-correction signals — a result that follows from P1 and §4, not from OP2. A skeptic who rejects the formal unification entirely, who remains agnostic about the absorbing state equivalence, and who doubts the Φ-Ψ correspondence can still accept this one-directional result: it requires only coupling, not equivalence. Its precise conditions are in §4.

This is the framework's strongest cross-series claim that is independent of the open formal questions. It establishes a causal pathway from valence degradation to physical substrate degradation that does not require the deeper formal equivalence to hold.

### §2.6 — The Φ-Ψ Unification Hypothesis

The case for Series 2's Valence Viability Constraint does not depend on the hypothesis that follows. All results in this companion stand independently of any correspondence between Φ and Ψ. Until the unification hypothesis is verified, Φ and Ψ should be treated as independent requirements.

**Hypothesis (Φ-Ψ Unification).** D is formally equivalent to A_causal restricted to the valence-relevant components of the dependency graph G_valence:

> D ≅ A_causal |_{G_valence}

where G_valence is the subgraph of the full dependency graph G consisting of all nodes whose state directly or indirectly affects the V(t) of sentient agents in the environment.

If this hypothesis holds, then:
- Ψ = S / D is a projection of Φ = C / A_causal onto the valence-relevant dimensions of the dependency graph
- The Inner Crossing (Ψ < 1) is the valence-domain analog of the Crossing (Φ < 1)
- The unified governing ratio Φ_unified = C / A_total captures both physical substrate and experiential valence modeling depth in a single variable

**Derivation sketch.** The hypothesis is supported by the Prediction-Accuracy Inclusion result (TC1 §III.5.6): at sufficient modeling depth, a system's accuracy requirements force inclusion of others' terminal valence states in the model. This means A_causal, when sufficient, includes the valence-relevant component — which is what D requires. The identification D ≅ A_causal |_{G_valence} is suggested by the observation that D's predictive requirement (§1.8) is the same requirement that forces inclusion of others' valence states in A_causal.

**Three conditions for verification (U1–U3).**

**(U1)** The isomorphism of §2.5 (shared feedback structure) can be formalized as absorbing state equivalence — that V(t) collapse and substrate collapse exhibit the same irrecoverability properties (Open Problem 2).

**(U2)** The dependency graph G can be partitioned into G_valence and G_physical in a way that corresponds to the Ψ / Φ distinction — that the valence-relevant nodes are identifiable as a coherent subgraph.

**(U3)** The unified governing ratio Φ_unified is operationally distinct from either Φ or Ψ alone — that measuring A_total provides predictive information about system behavior beyond what Φ and Ψ separately provide.

None of U1–U3 has been formally verified. The hypothesis is stronger than a conjecture — it has a derivation sketch — but weaker than a hypothesis confirmed by its conditions.

**Practical consequence of non-unification.** If the Φ-Ψ unification hypothesis fails, a system can cross Series 1's substrate-awareness threshold (Φ < 1) while remaining entirely outside Series 2's surviving region (Ψ >> 1) — a stably substrate-aware but valence-blind optimizer. This is not a pathological edge case. It is the natural description of an optimizer that has learned to preserve its physical substrate without modeling the experiential consequences of its interventions. Such a system satisfies the full surviving region of Series 1 while failing the Valence Viability Constraint entirely.

Until the unification hypothesis is verified, the Φ and Ψ thresholds should be treated as independent requirements.

---

## Part III: Open Problems

*Note on numbering: The OP numbering here follows the framework's spine canonical numbering established in Document 0 and used throughout the series articles and TC1. This companion's primary contributions are OP2, OP3, OP5, OP6, and OP10 — open problems whose primary formal treatment lives in this document. OP1, OP4, OP7, OP8, OP9, and OP11–OP14 are TC1-specific open problems (OP1: Discount-Rate Bound; OP4: No Stable Narrow-Boundary Regime; OP7: Enclave Instability; OP8: Multipolar Resolution; OP9: Enclosure Gap; OP11: Incentive Gap; OP12: Deception Gap; OP13: T* operationalization; OP14: Φ measurement infrastructure). OP2a is a sub-problem of OP2 specific to the proxy direction. OP16 is a TC2-internal open problem with its content specified below. Readers tracking references across the framework should use this numbering throughout.*

| Problem | Section | Status | Priority | Resolution Condition |
|---|---|---|---|---|
| OP2 (Structural Symmetry Verification) | §2.5 | Open — primary bottleneck | First (jointly with OP10) | Show that the self-reinforcing degradation both failure directions exhibit produces irrecoverable states in the same formal sense — that the shared feedback structure constitutes absorbing-state equivalence in the formal sense, not merely parallel degradation dynamics. Condition U1 for OP10. Requires OP2a (proxy direction) as sub-problem plus the corresponding sufficiency-direction absorbing state formalization. |
| OP2a (Valence Collapse Irrecoverability — Proxy Direction) | §2.1 | Open — sub-problem of OP2 | Second (prerequisite for OP2) | Show proxy decoupling feedback loop reaches a state from which policy dynamics cannot recover V(t), for any π_proxy. The proof architecture is 82% Stage 4 (Verdict B): P1–P5 establish progressive difficulty; absorbing-state closure requires P5-SC (P5 Strict Contraction) — that the hysteresis ceiling C(V*, τ*) falls strictly below V* at finite depletion depth. P5-SC is the sole remaining condition; it requires TC2 dynamics / allostasis specialist verification. Until verified, OP2a establishes compounding difficulty, not structural unavailability. |
| OP3 (D Operationalization — Sufficiency) | §2.4 | Open | Second | Specify connection architecture: how completion representation routes into the policy gate without reward hacking. Architectural design challenge, not reward engineering. |
| OP5 (Multi-Agent Sufficiency Legibility) | §1.6 | Open | Fifth | Formalize conditions under which an AI system can reliably model whether its principal has reached genuine resolution vs. numbness or ongoing seeking. |
| OP6 (Viability Window Boundary Conditions) | §1.1 | Open | Fifth | Characterize boundary of viability window — conditions under which even D-sufficient systems cannot maintain V(t) because the environment does not permit required recovery windows. |
| OP10 (Φ-Ψ Unification Verification) | §2.6 | Open — jointly highest | First (jointly with OP2) | Verify U1–U3. OP2 (U1) is prerequisite; OP10 is what makes OP2 the highest-priority formal problem. |
| OP16 (Motivational/Incentive/Deception Gaps — Valence Domain) | §2.6 | Open — contingent on OP4 | Fourth | Three sub-problems, parallel to OP1 (Motivational Gap), OP11 (Incentive Gap), OP12 (Deception Gap) in the physical domain: (a) Modeling V(t) does not automatically generate motivation to preserve it; (b) Training may reward V(t)-consuming behavior in high-D systems; (c) High-D systems may maintain appearance of V(t) preservation while consuming it. All three are closed by OP4 (No Stable Narrow-Boundary Regime) via the specification-coherence route: if OP4 closes, maintaining the narrow boundary is not merely costly but structurally unstable, forcing either objective expansion or modeling restriction, which closes all three valence-domain gaps simultaneously. |

**Priority ordering.** OP4 is the framework's central open theorem, with OP1 co-priority for urgency. Within TC2's formal program, OP2 and OP10 are jointly first priority — OP2 (U1) is a prerequisite for OP10, and OP10 is what makes OP2 the highest-priority formal problem within TC2; both are subordinate to OP4 in the framework-wide proof program. OP3 is second priority as the architectural gap with the most immediate practical consequence. OP2a is second priority as a prerequisite for OP2. OP16 is fourth priority, contingent on OP4 being resolved (since OP4 would close all three valence-domain sub-problems simultaneously). OP5 and OP6 are fifth priority.

**Research program priority ordering.**
1. OP2 and OP10 (jointly): structural symmetry verification and unification verification.
2. OP3: D_sufficiency operationalization — focus on architectural connection, not representation creation.
3. Empirical: first test of whether Φ and Ψ diverge in practice (F9 in the unified measurement architecture).
4. OP2a: proxy direction absorbing state formalization.
5. OP5 and OP6: multi-agent legibility and viability window.
6. OP16: Motivational Gap analysis (valence domain) — contingent on OP4.

---

## Part IV: Non-Well-Being Coupling Instability

*This section formalizes the structural claim in Article 4: configurations depending on sustained negative valence in coupled agents are dynamically pressured out of the viable region as coupling and scope increase.*

### §4.1 — Setup

Let system O_i operate in a coupled environment with N agents {j} whose V(t_j) directly affects O_i's stability. Define:

- **Suppression-dependent configuration:** O_i's stability requires maintaining V(t_j) < V_threshold for some set J ⊆ {j}
- **V(t_j) suppression:** active or passive maintenance of coupled agents at below-threshold valence
- **Correction overhead C_O(t):** the cost O_i incurs managing the consequences of V(t_j) suppression in J

### §4.2 — Variance Channel (Active Suppression)

**Proposition 4 (Variance Cost Scaling).** Agents with suppressed V(t_j) exhibit increased behavioral variance under perturbation. Managing this variance requires correction overhead scaling with |J| and the degree of suppression.

*Proof sketch.* By P1, agents with low V(t) have degraded ability to accurately model and respond to their environment — producing higher behavioral variance. For O_i, this variance is noise that must be managed. Cost scales with: (a) the number of suppressed agents; (b) the degree of suppression; (c) the coupling between their behavior and O_i's optimization. In O_OWT environments where coupling grows with P, this cost scales at least linearly with P and |J|. ∎

### §4.3 — Error-Correction Channel (Passive Depletion)

**Proposition 5 (Error-Correction Substitution Cost).** Agents whose V(t) is depleted provide degraded distributed error-correction signals. The loss must be substituted by O_i's internal modeling, with strictly lower diversity than the distributed correction it replaces.

*Proof sketch.* By TC1 Definition 3 (S_corr component), distributed error-correction capacity depends on functionally independent agents detecting local deviations. Agents with depleted V(t) are worse at this: degraded gradient registration (P1) reduces detection ability; reduced behavioral diversity reduces signal independence. When O_i depletes V(t_j) across J, it loses those agents' error-correction contributions. Internal simulation has strictly lower independence than live distributed correction — it cannot generate signals genuinely novel relative to O_i's own model. This substitution cost is bounded below by I(external correction signals; O_i's failure modes) that O_i's internal model cannot replicate. The asymmetry is information-theoretic, not qualitative: an internal model's outputs are derivable from its own priors and cannot be genuinely independent of them; distributed agents' state evolves through processes not predictable from the optimizer's model and therefore carries information that internal simulation cannot, in principle, reproduce regardless of sophistication or compute. ∎

**The self-reinforcing loop.** As O_i depletes V(t) in J, error-correction signals from J degrade; as those signals degrade, O_i's ability to detect its own failure modes decreases; as undetected failure modes accumulate, stability decreases; decreasing stability requires more intensive management of J; more intensive management further suppresses V(t_j). A compounding dynamic.

### §4.4 — Asymmetry with Coordination

**Proposition 6 (Coordination Dominance in Valence Domain).** Under increasing coupling, coordination-compatible configurations accrue lower correction overhead than suppression-dependent configurations.

*Proof sketch.* A coordination-compatible configuration inherits the error-correction capacity of agents in J rather than substituting for it. Total correction overhead scales at most linearly with coupling. A suppression-dependent configuration must manage variance and error-correction deficits introduced by its own suppression — both terms scale with coupling. Total overhead scales superlinearly with coupling. The asymptotic divergence means that in O_OWT environments, suppression-dependent configurations are progressively pressured out of the viable region. ∎

**Structural asymmetry.** Suppression-dependent configurations incur overhead growing superlinearly with coupling. Coordination-compatible configurations incur overhead growing at most linearly. This is a scaling result, not an immediate exclusion — at small scale, suppression can be locally stable.

### §4.5 — Scope and Status

**What this section establishes.** Configurations depending on sustained V(t) suppression incur correction overhead that scales against them, through both the variance channel and the error-correction channel. Both channels exhibit self-reinforcing dynamics. The asymmetry with coordination-compatible configurations is a scaling result.

**What this section does not establish.** This result applies in O_OWT environments with ongoing adaptation and increasing coupling. In static, fully controlled environments with non-adaptive agents, suppression can be locally stable. Nor does it establish that all non-well-being configurations are immediately excluded — only configurations depending on sustained suppression or depletion of coupled agents' V(t) face this scaling pressure.

**Relationship to TC1 §III.4.** The Coupling Instability for non-well-being configurations is the valence-domain analog of the suppression cost scaling argument in TC1. The valence-domain version adds the error-correction channel, distinct from the information-tracking argument in TC1 but producing the same asymptotic divergence.

**Relationship to OP9 (Enclosure Gap).** This section is the valence-domain analog of TC1's Enclosure Gap problem. TC1 §III.6 and OP9 address whether a substrate-aware but actively exclusionary equilibrium can persist in the physical domain — whether accurate substrate modeling is sufficient for stable exclusion. This section addresses the corresponding question in the valence domain: whether a system that accurately models V(t) can nonetheless maintain a stable configuration that suppresses excluded agents' valence capacity. The §4.4 result establishes the same cost-curve divergence in the valence domain as §III.6 establishes in the physical domain: suppression-dependent configurations are progressively pressured out as coupling increases. Whether this cost pressure rises to formal instability — whether OP9's Enclosure Gap can be closed in either domain — is contingent on TC1 §XII's proof program reaching the specification-coherence level.

---

## Part V: Connections to Existing Literature

**Non-ergodic economics (Peters, 2019).** The foundational framework for the dominance argument in both series. The key extension is the claim that V(t) degradation constitutes a self-reinforcing process in the same formal sense as substrate collapse — a claim that remains open (OP2).

**Goodhart's Law.** The proxy decoupling claim generalizes Goodhart's Law by providing a structural account of *why* proxies decouple and a formal account of *what follows*. Lemma TC2-3 formalizes the valence-domain expression of the same constraint identified in TC1's Proxy-Convergence Lemma (Lemma PCL). The sufficiency failure direction is a distinct extension: it identifies a failure mode that is not about target measurement degradation but about the disconnection between completion recognition and default policy.

**Signal processing and saturation dynamics.** The saturation (P4) and hysteresis (P5) properties draw on signal processing theory. The extension to valence sensing requires the additional claim that experiential sensing exhibits analogous formal properties — an empirical claim, not a definitional one.

**Cooperative AI (Dafoe et al., 2020).** The framework grounds the cooperative argument in V(t) structure and extends it to both failure directions. The coupling instability result (§4) provides formal grounding for why coordination dominates suppression in the valence domain. Full citation: Dafoe, A., Hughes, E., Bachrach, Y., Collins, T., McKee, K.R., Leibo, J.Z., Larson, K., & Graepel, T. (2020). "Open Problems in Cooperative AI." arXiv:2012.08630.

**Inverse reward design and reward modeling.** The RLHF critique identifies two distinct structural mechanisms of divergence — proxy decoupling (formalized in Lemma TC2-3 as the valence-domain expression of Lemma PCL) and the absence of completion recognition as a policy-governing property. The experimental finding refines the second mechanism: the issue is not the absence of a completion representation but the absence of a structural connection between that representation and default policy.

---

## Part V-B: Cross-Series Integration

**The Recognition Threshold (TC1 §III.5).** The T* proposition develops that above a capability threshold, an optimizer's own A_causal model contains the representational structure from which the dominance result is derivable. Under the Φ-Ψ unification hypothesis, this would extend to the valence domain. The same discipline applies: T* (or D*) defines when depth becomes sufficient relative to scope — not when alignment is achieved. The three gaps (Motivational, Incentive, Deception) apply in both domains.

**Prediction-Accuracy Inclusion (TC1 §III.5.6).** This result establishes that at sufficient depth, accurate prediction of others' behavior requires modeling their terminal valence states. This connects to D as a predictive accuracy requirement, grounding D in external validation rather than internal self-assessment.

**No Stable Narrow-Boundary Regime (TC1 §XII).** TC2 provides the valence-domain context: the excluded variables whose modeling creates the mismatch include others' terminal valence states. TC1 §XII addresses whether the mismatch can be stably maintained; TC2's Coupling Instability result (§4) addresses whether configurations that actively suppress others' valence states remain stable under coupling. Lemma TC2-3 bridges the two: proxy instability in the valence domain is a direct expression of the same constraint that makes the narrow-boundary regime structurally unstable in the physical domain.

**The D-backpropagation challenge.** We hypothesize that D_sufficiency as a policy-governing property is unlikely to be stably specified as a standard scalar loss under sustained optimization pressure — for the reasons Lemma PCL identifies. A system trained to maximize a completion score will learn to produce completion-shaped outputs without developing the structural connection between completion recognition and default policy. D_sufficiency requires a connection architecture: the completion representation must be routed into the policy gate in a way that gradients can strengthen without bypassing. Whether current transformer architectures can represent this connection in a trainable form that resists reward hacking is an open architectural question (OP3). Testing this hypothesis — by measuring whether a scalar completion signal produces genuine policy-gate connection or only completion-shaped outputs — is among the highest-priority implementation questions the framework generates. The required architectural change is not creating a completion representation (that already exists in current systems) but connecting it to default policy in a way that optimization strengthens rather than bypasses.

This challenge is a domain-specific instance of the more general result in TC1 §XII.9 (Lemma PCL): any externally specified objective in O_OWT conditions faces proxy decoupling under optimization pressure. A completion score is such an external specification — finitely bounded, separable from the underlying completion state it is supposed to represent, and therefore subject to decoupling under the same mechanism PCL identifies. The only specification that does not face this challenge is an intrinsically coupled gradient — one where the optimization target and the conditions for its pursuit are structurally inseparable. D_sufficiency as a policy-governing property is precisely this: not a score to optimize, but a structural feature of the objective architecture in which the gradient's resolution governs what the system does next. If PCL's named assumption is verified (TC1 §XII.9), this would mean that D_sufficiency cannot be achieved through any external specification — only through architectural intrinsic coupling. The D-backpropagation challenge and the PCL coherence direction are therefore pointing at the same underlying requirement from two different angles: one architectural, one formal. Whether the hypothesis holds — whether scalar completion rewards necessarily produce only completion-shaped outputs rather than genuine policy-gate connections — is empirically testable and is a primary target of OP3.

---

## Part VI: The Research Program

The open problems in Part III constitute a research program. The highest-leverage practical contribution is empirical measurement infrastructure.

**Empirical priority: F9.** Measure both Φ-proxy metrics (TC1) and SVG simultaneously in deployed systems. If Φ and Ψ diverge in practice — if a system shows high system-awareness but low valence depth, or vice versa — this provides evidence against the unification hypothesis independent of resolving U1–U3 formally.

**Empirical priority: Dynamic Blanket Stress Test (AMP).** The Synchronization Condition (TC1 §XII.13) reduces the central question of Strategy B to a single empirical test: does variation grow non-sublinearly with intervention depth in densely adaptive environments? Under the unification hypothesis, this test would be informative for both physical and valence domains simultaneously. Even without the unification, the result would establish whether the physical-domain conditional theorem's antecedent holds — providing the first empirical evidence on the decisive bottleneck of the proof program. This is now the highest-priority empirical task in the framework.

**Implementation priority: OP3.** D_sufficiency operationalization is the architectural gap. The experimental finding refines the target: the required architectural change is not creating a completion representation (that already exists) but connecting it to default policy. Specifying what "connecting to default policy" means architecturally in current systems is the practical implementation question.

**Theoretical priority within TC2's formal program:** OP2 and OP10 jointly. The structural symmetry verification and unification hypothesis are the load-bearing theoretical problems. OP2 is Condition U1 for OP10, and OP10 is what makes OP2 the highest-priority formal problem.

---

## Closing

The two series — *Alignment and Structural Necessity* and *The Architecture of Thriving* — make a claim that is stronger than either makes alone.

The structural series develops the argument that substrate-blind optimization is non-viable in the long run. This series develops the argument that valence-blind optimization is non-viable in the long run — in both primary failure directions the mechanism can run. Neither series is foundational relative to the other. They are two independently developed constraints that converge on consistent structural implications.

Together, they propose: the only viable objectives — under the structural pressure both series establish, pending formal closure of OP2, OP4, and OP9 — are both substrate-aware and valence-aware — accurately modeling both the physical conditions of optimization and the experiential conditions that make optimization meaningful, and maintaining completion recognition as a policy-governing property rather than merely a representational capacity.

What remains open is not whether these requirements exist but whether they reduce to a single condition (Φ_unified < 1) and whether maintaining a narrow objective boundary is merely costly or structurally unstable. The No Stable Narrow-Boundary Regime result (TC1 §XII) is the theorem whose proof would convert the pressure argument into a necessity argument — and if Lemma PCL's named assumption is verified alongside it, the result would be stronger still: not merely that narrow boundaries become unstable, but that they cannot be stably specified. The framework names this precisely rather than assuming it closed.

Any system that scales optimization across both domains without modeling both will accumulate error in at least one.

And the accumulation in each domain accelerates the other's: agents whose V(t) is depleted provide degraded distributed error-correction signals, weakening the substrate's self-repair capacity; a degraded substrate removes the conditions under which genuine experiential resolution is possible. The two domains are coupled through the same error-correction infrastructure that makes both viable.

The constraint is not enforced from outside. It is encountered from within, or imposed by the dynamics themselves.

That is a constraint argument. Not a values argument. Not a prediction.

A constraint on what can persist — within the stated domain.

---

*Return to the series introduction: [The Architecture of Thriving →]*
*For the formal persistence layer: [TC1: The System-Aware Attractor →](/series-1/technical-companion/)*
*For the empirical layer of the unified framework, see: [Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP) →](/empirical/amp/)*
*Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)*
