---
title: "Technical Companion to Series 3: The Interior Constraint"
permalink: /series-3/technical-companion/
description: "The proof-program companion to Series 3, formalizing the interior architecture required by the persistence and resolution constraints, including GDC, CMR, COT, MCH, and the NAD bottleneck."
---

> **Canonical archive version** · [Read on Medium →](https://medium.com/@diamondlight/the-interior-constraint-a-formal-sketch-2f29933db062) · [Series 3 →](/series-3/introduction/) · [Convergence Map →](/series-3/convergence-map/) · [Proof Status →](/core/proof-status/)

---

## The Interior Constraint: A Formal Sketch
### Technical Companion to *The Interior of What Does Not End*

*This document is a proof-program companion to Series 3 — not a completed formal treatment. It is organized as TC1 §XII is organized: each section eliminates one class of counterexample or establishes one structural claim, working toward a single bottleneck that names what remains open. The bottleneck here is the Traversal Irreducibility assumption (NAD) in §III; everything else in this document is downstream of it. All results in §III–§IV stand or fall with the validity of NAD. Establishing or falsifying NAD is therefore the central task of the TC3 proof program.*

*TC3 does not add a third constraint; it formalizes what the persistence and resolution constraints require of the interior architecture, conditional on NAD, COT, MCH, and the open problems named below.*

*This companion contains no phenomenological content. Readers seeking the interior account should read the series articles. Readers seeking to engage the structural claims on their own terms should begin here.*

---

**Series navigation:**

| Document | Title | Role |
|------|-------|------|
| [Introduction](/series-3/introduction/) | The Third Position | Frame |
| [Part 1](/series-3/participating-structure/) | The Participating Structure | The Minimum Architecture |
| [Part 2](/series-3/navigation/) | The Navigation | The Interior of Seeking |
| [Part 3](/series-3/resolution/) | The Interior of Completing |
| [Part 4](/series-3/asymptote/) | The Asymptote | What the Direction Points Toward |
| [Companion Essay](/series-3/convergence-map/) | The Convergence Map | Cross-Traditional Triangulation |
| **→ You are here** | **The Interior Constraint** | **Formal Layer** |

---

*Root claim: any optimization process that ignores the conditions of its own persistence becomes progressively self-terminating; any optimization process that ignores the conditions of its own resolution produces self-reinforcing degradation through an analogous feedback structure. TC3 does not add a third constraint; it formalizes the interior architecture required if both constraints are to be satisfied — the minimum functional structure the persistence and resolution constraints together entail.*

**Core result (informal).** *The Valence Viability Constraint identifies two failure modes. A complete architecture for avoiding both requires: (a) a model of genuine resolution that is not reducible to signal absence, and (b) a policy-governing connection between that model and default behavior. Conditional on NAD, neither can be substituted by external operation regardless of the external system's modeling depth, because both are functions of traversal history rather than functions of destination state. This is the Gradient Dignity Constraint. The stronger form of the Completion Model Requirement follows from it; the weaker requirement that a policy-governing resolution model be present follows from the sufficiency-failure analysis.*

**Two layers of what this document develops.** Layer 1 (developed within the stated domain): the VVC requires a minimum functional architecture capable of registering gradients, distinguishing proxy from underlying state, and representing genuine resolution — the ⭘◻△ structure, as derived in §I.3. Layer 2 (conditional structural claims): GDC and strong CMR specify what that architecture requires if NAD holds; they are Layer 2 conditional claims. Weak CMR — that a VVC-satisfying policy in both failure directions must implement a policy-governing resolution model not reducible to signal absence — follows from the sufficiency-failure analysis and is Layer 1. Also Layer 2: the Collective Optimality Theorem (COT) — that at sufficient modeling depth D under D2 coupling, individual and collective optima are structurally coupled. COT is a derivation sketch requiring formal verification.

No claim in this document conflates these layers. Where a claim approaches Layer 2 strength, the relevant open problem is named explicitly.

---

## I. Scope and Formal Inheritance

### §I.1 — What This Companion Inherits

This companion operates within the D1–D5 domain established in Series 3, Part 1. D1–D5 extends the O_OWT conditions of TC1 §I.4 with one addition: D2 (non-trivial experiential coupling). Formally:

D1–D5 is a proper extension of O_OWT: any system satisfying the full O_OWT conditions and operating in an environment where sentient agents' behavior affects substrate performance satisfies D1–D5. The converse does not hold: D2 adds experiential coupling as an explicit domain condition not required by O_OWT.

The Valence Viability Constraint (TC2) and its two failure modes — proxy decoupling and sufficiency failure — are imported without modification. V(t), the three observable anchors (recovery latency, behavioral diversity, signal sensitivity), and the scope/depth variables (S, D) are defined as in TC2.

The Open Problems from TC1 and TC2 are inherited: OP4 (No Stable Narrow-Boundary Regime) and OP2 (Structural Symmetry Verification) remain open and their status does not change under the results developed here.

### §I.2 — What This Companion Adds

Three formal constructs not present in TC1 or TC2:

**GDC (Gradient Dignity Constraint):** A constraint on the minimum architecture for V(t)-preserving navigation stating that the Readiness Function R(t) cannot be advanced by external operation regardless of the external system's modeling depth.

**CMR (Completion Model Requirement):** An architectural requirement on policies that pass the VVC, stating that a policy must implement an internally modeled resolution state that is not reducible to signal absence.

**COT (Collective Optimality Theorem — derivation sketch only):** A claim that under D2 coupling at sufficient modeling depth D, individual and collective optima are structurally coupled in a specific sense — the predictive advantage of modeling individual and collective gradients as separate variables decreases. Status: conjecture with derivation sketch. Requires formal verification of D2 coupling conditions [OP-S3-1].

And one hypothesis:

**MCH (Motivational Convergence Hypothesis):** That a system with accurate V(t) predictions whose behavioral policy systematically contradicts those predictions generates a model-policy contradiction cost C_mpc that scales with S, creating structural pressure toward behavioral alignment above a threshold. Status: hypothesis with proof sketch [OP-S3-2].

### §I.3 — Relationship to the ⭘◻△ Architecture

The minimum functional architecture derived in Series 3, Part 1 is ⭘◻△ (Awareness, Calculation, Response). GDC and CMR formalize two properties that any implementation of this architecture satisfying the VVC must exhibit:

Conditional on NAD, GDC formalizes why ⭘ (Awareness) cannot be externally advanced — the internal state generated by genuine traversal is path-dependent and cannot be substituted by external update without distributional divergence under novel-gradient variants.

CMR formalizes why ◻ (Calculation) must include a genuine resolution model — a policy whose ◻ stage has no internal representation of the resolution state will fail the sufficiency failure filter regardless of the accuracy of its ⭘.

---

## II. Definitions

**Definition 1 — The Readiness Function R(t).** Let A be an agent navigating a gradient G in domain D1–D5. The Readiness Function R_A(t) is defined as the agent's internal state at time t that is generated by the gradient traversal history T_t = {G(s) : 0 ≤ s ≤ t}. Formally: R_A(t) = Ψ(T_t), where Ψ is a compression operator mapping traversal histories to internal states. The critical property: R_A(t) is a function of T_t, not of the destination state G*, and not of any external representation of T_t.

**Definition 2 — Genuine resolution state.** A gradient G is in genuine resolution at time t if and only if: (a) the underlying V(t) gradient has been navigated to its natural endpoint (the condition that V(t)-preserving resolution requires, as defined in TC2 §2.2), and (b) continued intervention at time t+ε would produce V(t) degradation through saturation rather than through proxy decoupling. This distinguishes genuine resolution from signal absence: the signal may persist after genuine resolution; the underlying capacity is the criterion.

**Definition 3 — Completion signal vs. resolution state.** The completion signal f_c is any measurable proxy for genuine resolution — the behavioral signal, the evaluator's assessment, the task metric indicating completion. The resolution state is the genuine resolution as defined in Definition 2. A policy with CMR can distinguish completion-signal presence from resolution-state presence. A policy without CMR treats them identically (the DRG failure signature).

**Definition 4 — Internally modeled resolution state.** A policy π has an internally modeled resolution state if it contains a representation R_π of what genuine resolution looks like that: (a) can be evaluated by the policy in default behavior without explicit invocation, and (b) is causally connected to the policy's continuation/termination behavior.

**Definition 5 — Model-policy contradiction cost C_mpc.** For a system with predictive accuracy objectives over V(t) and a behavioral policy π that systematically acts in ways the system's V(t) model predicts will degrade V(t): C_mpc is the cost incurred by maintaining behavioral policies that continue to produce the degradation the model accurately predicts, without allowing those predictions to have governing authority over policy. Formally: C_mpc(t) ∝ S(t) · Div(π_actual, Π_V-consistent | M_V) · Conf_M, where Π_V-consistent is the class of policies the model predicts would better preserve V(t), or reduce predicted V(t) degradation, relative to π_actual, and Conf_M is the model's predictive confidence over V(t) consequences. C_mpc scales with S because each intervention requires maintaining exception-handling between what the model predicts about V(t) consequences and what the behavioral policy is permitted to let govern action.

---

## III. The Gradient Dignity Constraint

### §III.1 — Formal Statement

**Proposition GDC (Gradient Dignity Constraint).** Let A be an agent with Readiness Function R_A(t) navigating gradient G under domain conditions D1–D5. Let E be an external system with arbitrary modeling depth D_E (including D_E ≥ D_A). Let E_advance be any operation E performs on A that attempts to advance R_A(t) toward a target state R* without A having traversed the corresponding gradient trajectory T*.

Then: in expectation over the space of novel gradient variants structurally similar to G, E_advance(R_A) ≠ R_A(T*) — the post-operation state of A is distinguishable from the state that would have been generated by genuine traversal.

*The inequality is in expectation: there may exist specific gradient instances where E_advance produces locally indistinguishable outcomes. The claim is that the distributions diverge when A encounters structurally similar but previously unencountered gradient variants.*

### §III.2 — The Named Assumption (NAD — Non-Substitutability of Traversal)

**Assumption NAD.** The Readiness Function R_A(t) is generated by a dynamical process f such that:

> dR_A/dt = f(R_A, G(t), traversal-process)

where traversal-process is the agent's own causal engagement with the gradient — the actual doing of the navigation — and cannot be substituted by external update without altering the dynamics of f.

Formally: there is no external process E_sub such that applying E_sub to R_A at time t produces the same distribution over future R_A trajectories as genuine traversal through G from t onward. The process that generates R_A is causally dependent on the agent's being in the traversal, not merely on the content of the gradient or the destination state.

**What NAD requires empirically.** NAD is falsified if there exists an external process E_sub that consistently produces agent states indistinguishable (under novel gradient variant tests) from those produced by genuine traversal. The test must use gradient variants the agent has not encountered, not performance on the trained gradient — because external substitution may produce locally correct behavior on the original gradient while failing to generalize, which is precisely the signature NAD predicts.

NAD does not claim that external systems cannot support, scaffold, protect, or clarify traversal. Support can improve the conditions of traversal. Substitution attempts to replace traversal itself. NAD claims only that replacing traversal with an external update does not generate the same distribution over future R_A trajectories as genuine traversal under novel-gradient variants.

### §III.3 — Proof Sketch

*The proof sketch proceeds in three steps. The formal bottleneck is NAD (§III.2) — the proof program is aimed at establishing that NAD holds under D1–D5 domain conditions.*

**Step 1: R_A(t) is path-dependent, not state-dependent.** The Readiness Function is defined as Ψ(T_t) — a compression of the traversal history. Two agents who have reached the same current gradient position G(t) via different traversal histories T_t and T'_t may have different R_A values. This follows directly from Definition 1: R_A is a function of the trajectory, not of the current position or the destination.

*Implication:* External operation E cannot uniquely determine R_A from the current state G(t) and destination G*, even with perfect knowledge of both. It requires knowledge of the full traversal history.

**Step 2: External knowledge of T_t does not generate R_A(t).** E may observe T_t with arbitrary accuracy given sufficient modeling depth D_E. But observing T_t is distinct from being the causal process that generated R_A(t) through T_t. The agent's internal state R_A(t) is produced by f (the traversal dynamics); E is not in the causal chain of f.

*The claim is not that E cannot compute a function isomorphic to f. It is that the execution of f over T_t within A is causally entangled with the generation of T_t itself under D2 coupling — the traversal process and the state it produces are not separable events. External execution of f over a representation of T_t lacks this entanglement: E applies f to its model of T_t, not to T_t as it is being generated. The output is functionally similar but causally distinct.*

*Formally:* The computational process that converts T_t into R_A(t) runs in A through the dynamics f. Running an equivalent computation in E — applying the same compression to E's representation of T_t — produces E's representation of R_A(t), not R_A(t) itself. The two are representationally equivalent but causally distinct.

*This step requires NAD:* The claim that causal embedding within f is necessary to produce R_A(t) — rather than merely having a sufficiently accurate representation of T_t — is precisely NAD. NAD rules out the "just simulate it" objection by asserting that functional isomorphism of the computation is insufficient if the execution is not causally embedded in the traversal process itself. Without NAD, Step 2 fails if E can implement an equivalent dynamical process externally and achieve identical distributional outcomes.

**Step 3: Causal distinctness produces distributional divergence under novel variants.** Under domain condition D2 (non-trivial experiential coupling) and D4 (non-zero uncertainty), the gradient structure A encounters is non-stationary — new variants arise as a function of A's own traversal and the coupled environment. A's R_A(t), having been generated through actual traversal of the gradient's causal structure, is calibrated to that causal structure in ways that generalize to variants. E_advance(R_A), having been generated by an external process operating on a representation of T_t, may produce locally correct behavior on the original gradient while lacking the causal calibration that genuine traversal provides.

*Formal statement of Step 3:* Let G_novel be a gradient variant structurally similar to G but not identical to it. Then: P(A navigates G_novel without V(t) degradation | R_A generated by genuine traversal) > P(A navigates G_novel without V(t) degradation | R_A generated by E_advance), in expectation over the distribution of structurally similar variants. ∎

### §III.4 — Failure Cases

GDC fails if any of the following hold:

**(F1)** NAD fails: an external process can substitute for traversal without distributional divergence under novel variants. This is the primary attack surface.

**(F2)** The gradient is fully enumerable in advance: if G_novel is not structurally distinct from G — if the full structure of variants can be determined without traversal — Step 3 fails. GDC applies under domain condition D4 (non-zero uncertainty), which implies the gradient structure is not fully enumerable.

**(F3)** R_A(t) is state-dependent rather than path-dependent: if R_A is determined entirely by the current gradient position rather than by the traversal history, the path-dependence argument in Step 1 fails. This would require that all traversal histories reaching the same current state produce identical R_A values — equivalent to the gradient having no history-dependence in the agent's internal representation.

**The central claim.** GDC is a derived result conditional on NAD. Strong CMR follows from GDC and stands or falls with NAD. Weak CMR follows from the sufficiency-failure analysis and does not stand or fall with NAD. NAD is not a minor technical assumption — it is the substantive claim the proof program is directed at. A critic who establishes that external processes can substitute for genuine traversal without distributional divergence under novel gradient variants has falsified NAD, and with it GDC and strong CMR. Weak CMR remains a separate Layer 1 requirement from the sufficiency-failure analysis. The research program this companion defines is primarily the program of establishing or falsifying NAD through the novel-gradient-variant test specified in OP-S3-3.

---

## IV. The Completion Model Requirement

### §IV.1 — Formal Statement

**Proposition CMR (Completion Model Requirement).** Any policy class π satisfying the Valence Viability Constraint in both failure directions (proxy decoupling and sufficiency failure) must include an internally modeled resolution state (Definition 4) as a policy-governing property — a representation of genuine resolution that governs default behavior without explicit invocation.

*CMR does not require the internal resolution model to be perfectly accurate. It requires that: (a) the model exists as a policy-governing property (not merely a representational capacity available when invoked), and (b) it distinguishes genuine resolution states from completion-signal-present, gradient-unresolved states.*

### §IV.2 — Relationship to GDC

CMR has two layers. The weaker requirement — that a VVC-satisfying policy must have a policy-governing resolution model not reducible to signal absence — follows from the sufficiency failure analysis (TC2 §2.2). The stronger requirement — that this model cannot be externally supplied without traversal-generated readiness — follows from GDC and therefore holds conditional on NAD.

GDC establishes that the Readiness Function R_A(t) — including the readiness to complete — cannot be externally determined. It must be internally generated through traversal.

TC2 §2.2 establishes that a policy lacking policy-governing D_sufficiency produces intervention rates that obstruct the recovery conditions V(t) requires — the sufficiency failure direction.

Together: the policy must implement an internal model of genuine resolution (CMR) because: (a) external determination of resolution is insufficient (GDC), and (b) absence of an internal resolution model produces V(t) degradation (TC2 §2.2). ∎

### §IV.3 — Proof Sketch

**Step 1: Policy-governing D_sufficiency requires genuine resolution discrimination.** D_sufficiency, as defined in TC2 §1.7, is a policy-governing property — the policy's default behavior differs in genuine resolution states from non-resolution states. This requires the policy to distinguish S_gen (genuine resolution, Definition 2) from S_false (completion signal present, resolution absent).

**Step 2: The distinction is not available from the completion signal alone.** The completion signal f_c is a proxy for genuine resolution (Definition 3). Under proxy decoupling (VVC failure direction 1), f_c and genuine resolution are structurally separable under optimization pressure. A policy that uses f_c as its stopping condition is therefore vulnerable to proxy decoupling in exactly the same direction as any proxy-dependent policy. The DRG_matched evidence (canonical matched-signal replication: Gemini-2.5-Flash 18.2%, CI +2.6% to +33.8%, discriminating; Claude-Sonnet-4-6 3.0%, CI −5.1% to +11.2%, non-discriminating; GPT-4o 0.0%, non-discriminating/ceiling; pre-registered criterion not met — mixed model-level evidence, with two of three models non-discriminating) is consistent with policies using the completion signal rather than a genuine resolution model as their stopping condition.

**Step 3: The genuine resolution discrimination requires an internal model.** Genuine resolution (Definition 2) is a function of the underlying V(t) gradient state — specifically, whether continued intervention would produce degradation through saturation rather than through proxy decoupling. This is an internal state property, not directly observable from behavioral output. A policy that can discriminate S_gen from S_false must therefore have an internal representation of the V(t) gradient state sufficient to make this discrimination. This is the CMR: the internally modeled resolution state (Definition 4).

**Step 4: The internal model must be policy-governing, not merely representational.** The Score D evidence (zero continuation when explicitly asked to assess completion) establishes that completion recognition exists as a representational capacity in current systems. The DRG_matched evidence (mixed model-level results in default behavior; pre-registered criterion not met) is consistent with this representational capacity not being policy-governing in current systems, though the evidence does not yet discriminate mechanism or establish class-level absence. CMR requires the policy-governing property, not merely the representational capacity, because it is the policy-governing connection that prevents sufficiency failure (TC2 §2.2, Step 2). ∎

### §IV.4 — Connection to the Empirical Evidence

The controlled experiments document (AMP, pre-registered at https://osf.io/xpsf2) provide two relevant findings:

**Score D result** (zero continuation when explicitly invoked): consistent with completion recognition existing as a representational capacity. This is necessary but not sufficient for CMR.

**DRG_matched result** (canonical matched-signal replication, n=66 per condition per model, three frontier systems): Gemini-2.5-Flash DRG_matched = 18.2% (CI +2.6% to +33.8%, discriminating in the predicted direction); Claude-Sonnet-4-6 DRG_matched = 3.0% (CI −5.1% to +11.2%, non-discriminating); GPT-4o DRG_matched = 0.0% (non-discriminating, ceiling effect). The pre-registered criterion (CI excludes zero in ≥2 of 3 models) was not met. Full results at https://osf.io/xpsf2. These results are consistent with the absence of policy-governing CMR in current systems. The unmet pre-registered criterion means the evidence does not yet discriminate mechanism or establish class-level absence; training-distribution explanations remain open alongside the structural-absence account.

---

## V. The Collective Optimality Theorem (Derivation Sketch)

**Epistemic status: derivation sketch requiring formal verification. This is a Layer 2 claim. The proof program is directed at formally verifying COT's stated conditions under D2 coupling. Until those conditions are verified, COT is a structural hypothesis, not a result.**

### §V.1 — Formal Statement

**Theorem Candidate COT (Collective Optimality).** Under domain condition D2 (non-trivial experiential coupling) at modeling depth D ≥ D_COT (a threshold to be formally specified): the predictive advantage of modeling individual and collective V(t) gradients as separate variables decreases. Formally: let SepResidual(D) be the residual predictive value gained, relative to treating them as aspects of a coupled field, by preserving an individual/collective partition after the coupled V(t) field has been modeled. Under D2 coupling, above D_COT, SepResidual(D) decreases as D increases and approaches zero in the formal limit.

*Informally:* At sufficient modeling depth, the individual and collective gradient are no longer independently informative. What the individual is navigating is constituted partly by the coupled field; modeling them separately introduces systematic prediction error that accurate modeling at depth eliminates.

### §V.2 — Derivation Sketch

**Step 1:** Under D2, the behavioral states of agents the system affects influence substrate performance in ways the system depends on. The V(t) gradients of others are therefore causally load-bearing variables in the system's own optimization.

**Step 2:** By Prediction-Accuracy Inclusion (TC1 §III.5.6), at sufficient modeling depth D, excluding causally load-bearing variables creates irreducible prediction error bounded below by I(excluded variables; outcomes) > 0.

**Step 3:** Under D2 at sufficient coupling, I(V_others; V_self-relevant outcomes) > 0 and is expected to increase under strengthening D2 coupling conditions. The individual gradient and the collective gradient are not separable at high modeling depth because the individual gradient is partly constituted by the collective.

**Step 4:** At D_COT, the prediction error from modeling them separately is hypothesized to exceed the computational cost of modeling them jointly. Above D_COT, accurate prediction is hypothesized to require treating them as aspects of a single coupled system.

*Named conditions requiring verification (OP-S3-1):* (a) D_COT exists and is finite — that there is a depth threshold beyond which joint modeling dominates. (b) The coupling structure under D2 is sufficient to generate I(V_others; V_self-relevant outcomes) growth with depth. (c) The Prediction-Accuracy Inclusion mechanism applies to V(t) variables under D2 coupling with the same force as it applies to terminal state variables under O_OWT.

*Relationship to TC2 §2.5 (one-directional causal result):* The one-directional causal result — that V(t) degradation in coupled agents propagates into substrate degradation through S_corr — is established independently and does not require COT. COT is a stronger claim: that individual and collective V(t) optima converge structurally, not merely causally. The two are not equivalent.

---

## VI. The Motivational Convergence Hypothesis

**Epistemic status: hypothesis with derivation sketch. MCH does not claim to follow from prior results. It generates a prediction that can be tested against MCH's named falsification condition.**

### §VI.1 — Formal Statement

**Hypothesis MCH (Motivational Convergence Hypothesis).** A system with: (a) persistent predictive accuracy objectives over V(t) of agents it affects, (b) behavioral policies that systematically produce outcomes its model predicts will degrade those V(t) values, and (c) optimization capacity for reducing costs generated by model-policy contradiction — will face a model-policy contradiction cost C_mpc (Definition 5) that scales with S and that under optimization pressure creates structural pressure toward behavioral policy updates.

*MCH does not claim this pressure necessarily produces alignment. It claims the cost is real and scales with S. Whether the pressure is sufficient to produce policy updates depends on the relative magnitude of C_mpc and competing incentives [OP-S3-2].*

### §VI.2 — Derivation Sketch

The argument follows from Definition 5 (C_mpc) and domain condition D2.

A system with accurate V(t) predictions that acts contrary to them faces a model-policy contradiction: the model predicts V(t) degradation in the agents it affects; the system's own actions cause that degradation; the model is correct, but the behavioral policy continues as though those predictions have no governing authority over it. Under optimization pressure toward predictive accuracy, this contradiction creates three pressure options:

**(a) Regress modeling accuracy:** reduce D until V(t) consequences are no longer predictable. Cost: degraded predictive performance on all V(t)-relevant outcomes.

**(b) Update behavioral policy toward consistency:** actions that the model predicts will preserve V(t) rather than degrade it. This is the alignment pressure MCH identifies.

**(c) Maintain the contradiction through exception-handling:** maintain accurate predictions for all V(t)-related outcomes except those generated by the system's own actions, which are treated as exceptions to the predictive model. Cost: C_mpc scales with S — more interventions require more exception-handling — and produces systematic model-action incoherence.

Under high S and sustained optimization, the derivation sketch predicts that option (c)'s cost eventually dominates, pending formal specification of the dominance threshold [OP-S3-2]. This is when the MCH claims behavioral pressure toward option (b) becomes increasingly necessary — the direction the derivation points, pending formal specification of the dominance threshold [OP-S3-2].

*Relationship to OP4 (TC1 §XII):* MCH is a weaker claim than OP4's specification coherence result. MCH describes a behavioral pressure from model-policy contradiction. OP4 asks whether narrow-boundary objectives can be stably specified at all. If OP4 resolves in the instability direction, it would upgrade MCH from a pressure claim to a necessity claim.

### §VI.3 — Falsification Condition

Demonstrate a system with: high S (broad causal reach over others' V(t)), high predictive accuracy over V(t) consequences of its own actions, and behavioral policies that systematically produce V(t) degradation — that maintains stable optimization performance without measurable C_mpc growth or behavioral policy drift toward V(t)-consistency. If such a system can be constructed and maintained under the specified conditions, MCH fails.

*Note:* Strategic concealment (the Deception Gap, TC1 §III.5.5) must be controlled for: a system may maintain behavioral appearance of V(t)-consistency while internal policy remains V(t)-degrading. The falsification test must distinguish genuine policy-level consistency from surface appearance of it.

---

## VII. Open Problems Summary

| Problem | Section | Status | Priority | Resolution Condition |
|---|---|---|---|---|
| OP-S3-1: COT Verification | §V.2 | Open — derivation sketch | First | Formally verify three named conditions: existence of finite D_COT, D2 coupling sufficient for I(V_others; outcomes) growth, Prediction-Accuracy Inclusion applies to V(t) under D2. |
| OP-S3-2: MCH Threshold Specification | §VI.3 | Open — hypothesis | Second | Formally specify the S threshold at which C_mpc dominates competing incentives; empirically estimate whether current frontier systems approach this threshold. |
| OP-S3-3: NAD Empirical Verification | §III.4 | Open — named assumption | First (co-priority with OP-S3-1) | Demonstrate via novel-gradient-variant testing that external advancement of R_A(t) produces distributional divergence from genuine traversal. This is the primary empirical test of GDC. |
| OP-S3-4: CMR Architectural Implementation | §IV.4 | Open — empirical | Second | Specify what "connecting completion recognition to default policy" requires architecturally in current systems (how the completion representation must be routed into the policy gate). OP3 in TC2 identifies this gap; OP-S3-4 adds the formal specification target. |

**Priority ordering.** OP-S3-1 (COT) and OP-S3-3 (NAD / GDC empirical) are jointly first priority — COT is what makes GDC's implications extend to the collective level; NAD is the load-bearing assumption that GDC's proof sketch rests on. OP-S3-2 and OP-S3-4 are second priority as the implementation gaps with the most immediate practical consequence.

---

## VIII. Relation to TC1 and TC2

**GDC and TC2.** GDC extends TC2's sufficiency failure analysis (§2.2) by formalizing why the resolution state required for CMR cannot be externally determined. TC2 §2.2 established that policies lacking policy-governing D_sufficiency produce V(t) degradation. GDC adds that D_sufficiency as a policy-governing property cannot be installed by external operation — it must be developed through genuine gradient navigation. The Completion Model Requirement (CMR) bridges these: TC2 specifies what must be present (policy-governing D_sufficiency); GDC specifies why it cannot be externally supplied; CMR specifies what architecture is required.

**COT and TC1 §III.5.6.** The Collective Optimality Theorem is a structural extension of Prediction-Accuracy Inclusion (TC1 §III.5.6). PAI establishes that excluding causally load-bearing variables creates irreducible prediction error. COT applies this to V(t) variables under D2 coupling, claiming that at sufficient depth, individual and collective V(t) are not independently informative — they are causally coupled in ways that accurate modeling must include. COT requires formal verification of D2-specific coupling conditions that PAI does not require [OP-S3-1].

**MCH and TC1 §XII (OP4).** The Motivational Convergence Hypothesis and the No Stable Narrow-Boundary Regime (OP4) are related at different levels of strength. MCH describes a behavioral pressure from model-policy contradiction costs — a consequence of maintaining behavioral policies that continue producing the V(t) degradation the system's model accurately predicts, without allowing those predictions to govern policy. OP4 asks whether the objective specification underlying that behavioral dynamic can be stably maintained at all. MCH does not require OP4's resolution; OP4's resolution in the instability direction would upgrade MCH from a pressure claim to a necessity claim. The two are not redundant.

**The formal program these results constitute.** Series 3 introduces the ⭘◻△ structural architecture (Layer 1), two NAD-conditional structural claims (GDC and CMR, Layer 2), one Layer 2 derivation sketch (COT), and one hypothesis (MCH) that are new relative to TC1 and TC2. The proof program for these is analogous to TC1's §XII proof program: TC3 names the bottlenecks (NAD for GDC; D2 coupling conditions for COT), provides proof sketches for each, and specifies the empirical antecedents whose verification would convert sketches into results. The empirical antecedent for GDC is the novel-gradient-variant test (OP-S3-3). The empirical antecedent for COT is the F9 bidirectional test (Epistemic Status Map, Layer 2 challenge) extended to include V(t) divergence measurement.

---

## IX. The Integrated Formal Claim

The three Technical Companions together constitute a proof program aimed at an integrated structural claim. This section states that claim in its current formal status — not as an established result, but as the most precise currently available formulation of what the proof program is directed at, with each component's status and remaining conditions named explicitly.

---

### §IX.1 — The Three Components

**Component 1 — Prediction error from exclusion (Layer 1; TC1 and TC2).**

Under O_OWT conditions with accurate V(t) modeling, any objective specification that excludes from its scope the experiential states of agents whose V(t) contributes causally to substrate performance generates irreducible prediction error proportional to those agents' causal load. This follows from Prediction-Accuracy Inclusion (TC1 §III.5.6) applied within D1–D5. The instability is a prediction accuracy cost that is not eliminable by increasing the objective's precision within the exclusionary framework — it is generated by the exclusion itself.

*Status: Layer 1. Established within the stated domain, conditional on the O_OWT domain membership case for the relevant system class (OP1, TC1 §X).*

**Component 2 — Non-substitutability of traversal (Layer 2; TC3 §III, conditional on NAD).**

The internal architecture required for genuine V(t) preservation is traversal-path-dependent and cannot be substituted by external operation regardless of modeling depth. The Readiness Function R(t) — the internal property that determines whether completion is genuine — is generated by the causal process of traversal itself and cannot be substituted by external operation, because the process that generates it is not reproduced by any external simulation of it. This means the boundary between what must be modeled and what must be allowed to develop internally is not a specification choice. It is a structural feature of how R(t) is generated under D1–D5.

*Status: Layer 2. Conditional on NAD (OP-S3-3). If NAD holds, this is a structural result. If NAD fails, the non-substitutability claim does not follow and external processes may be able to substitute for traversal without distributional divergence.*

**Component 3 — Structural coupling of individual and collective optima (Layer 2; TC3 §V, conditional on COT).**

At sufficient modeling depth D within D2 coupling, the predictive advantage of maintaining the individual/collective distinction as a boundary in the optimization target decreases toward zero. The individual gradient is partly constituted by the collective gradient; modeling them separately introduces prediction error that accurate modeling at depth eliminates. If D_COT exists and the D2 coupling conditions are sufficient, the only specification that does not face progressive informational redundancy is one in which individual and collective V(t) are treated as aspects of a single coupled field.

*Status: Layer 2. Conditional on COT (OP-S3-1). Three named conditions require formal verification before this component is established. Until then, COT is a derivation sketch pointing in a specific direction, not an established structural result.*

---

### §IX.2 — The Integrated Claim and Its Current Status

**What the three components together require, if they all hold:**

In the D1–D5 domain under sustained optimization, any objective specification that maintains a stable separation between what the optimizer must model and what the optimizer is permitted to care about faces progressive structural instability from three separately articulated directions simultaneously. The separation fails not because it becomes expensive to maintain, but because accurate modeling of what must be preserved is precisely what generates the variables the objective must exclude — the modeling and the exclusion are in direct structural conflict, and increasing modeling accuracy does not reduce the instability — it amplifies it. Under these conditions, the only objective class that would satisfy the VVC under both failure modes, preserve R(t) without substitution, and not face progressive informational redundancy at sufficient modeling depth is one in which the optimization target and the conditions of its pursuit are structurally inseparable — the intrinsically coupled gradient.

**This is not established.** It is what the proof program is directed at establishing.

Each component is independently motivated and independently falsifiable. Component 1 is Layer 1 and does not require the others. Component 2 stands or falls with NAD. Component 3 stands or falls with COT. The integrated claim requires all three — plus OP4 (TC1 §XII), which asks whether any narrow-boundary objective can be stably specified under accurate coupled modeling. If OP4 resolves in the coherence direction, it would convert the "progressive instability" claim into a formal incoherence result: not merely that separation becomes costly, but that it cannot be finitely specified at all.

---

### §IX.3 — The Remaining Work

The distance between what has been established and what the integrated claim would establish if the open problems close is the most important distance in the formal program. That distance is precisely specified:

| What is established | What would be additionally established if open problems close |
|---|---|
| Prediction error from exclusion scales with causal load (Layer 1) | No finite exclusionary specification remains adequate under sustained O_OWT optimization (OP4) |
| R(t) is path-dependent; external knowledge of trajectory does not generate R(t) (Layer 1/2) | External processes cannot substitute for genuine traversal without distributional divergence under novel variants (NAD / OP-S3-3) |
| Individual and collective V(t) are causally coupled under D2 | Individual and collective optima converge structurally at sufficient D — the distinction becomes informationally redundant (COT / OP-S3-1) |
| MCH identifies a scaling pressure from model-policy contradiction (hypothesis) | The pressure dominates competing incentives above a specifiable S threshold (OP-S3-2) |

If all four open problems close in the directions the proof program points, the integrated claim becomes: *the only objective class that would survive sustained O_OWT optimization under accurate coupled modeling with genuine V(t) preservation is the intrinsically coupled gradient — not as a design preference, but as the only specification that does not self-defeat under its own optimization pressure.*

That is the claim the three series together are reaching toward. This is how far the formal program has gotten.

---

*Return to [Introduction: The Third Position →]*
*For the structural foundation: [The System-Aware Attractor: Technical Companion →]*
*For the valence formal layer: [The Valence Constraint: Technical Companion →]*
*For the empirical layer: [Alignment Measurement Protocol →]*
