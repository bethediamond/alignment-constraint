---
title: "Technical Companion to Series 1: The System-Aware Attractor"
permalink: /series-1/technical-companion/
description: "The formal companion to Series 1, developing the O_OWT domain, Substrate Constraint, Alignment Phase Ratio, proof architecture, simulations, and open verification obligations."
---

> **Canonical archive version** · [Read on Medium →](https://medium.com/@diamondlight/v-the-system-aware-attractor-c749f984b842) · [Framework hub →](/core/alignment-constraint/) · [Proof Status →](/core/proof-status/)

---

## Formal Sketch, Proof, and Open Problems

*This document formalizes the Substrate Constraint developed in Article 1 and the attractor developed in Article 2. It is a companion to the trilogy, not a prerequisite — the articles are self-contained. What follows is for readers who want to engage the argument's mathematical structure rather than its narrative form. The formalization corresponds directly to the dynamics illustrated in the simulations accompanying each article: the absorbing state in Article 1's simulation, the three filter crossovers in Article 2's simulation, and the Φ regime transitions in Article 3's simulation are all instances of the structures formalized below. Section VII maps formal variables to simulation parameters explicitly.*

---

**Series navigation:**

| Post | Title | Role |
|------|-------|------|
| [Introduction](/series-1/introduction/) | [Alignment and Structural Necessity](/series-1/introduction/) | Frame |
| [Part 1](/series-1/alignment-of-intelligence/) | [The Alignment of Intelligence](/series-1/alignment-of-intelligence/) | The Constraint |
| [Part 2](/series-1/aligned-intelligence-converges-toward/) | [What does aligned intelligence actually converge toward?](/series-1/aligned-intelligence-converges-toward/) | The Attractor |
| [Part 3](/series-1/the-crossing/) | [The Crossing](/series-1/the-crossing/) | The Crossing |
| **→ You are here** | **Technical Companion** | Formal Layer |
| [Experimental Companion](/empirical/amp/) | [Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP)](/empirical/amp/) | Empirical Layer |

Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)

---

**What this document formalizes.** *TC1 develops the formal apparatus for the persistence component of the framework's canonical root claim: in open, shared, non-resettable environments under sustained optimization pressure, any optimization process that ignores the conditions of its own persistence becomes progressively self-terminating. The resolution component — what TC2 addresses — concerns the experiential and valence substrate, and produces self-reinforcing degradation through an analogous feedback structure; whether that degradation is formally equivalent to the persistence-domain self-termination result remains Open Problem 2. Both components are independently developed expressions of what may be the same underlying structural condition, pending resolution of OP2 and OP10; TC1 develops the first formally, TC2 the second, with the Φ-Ψ unification hypothesis addressing whether the two are formally equivalent as a single structural result.*

**Core result (informal).** *Optimization does not operate on a fixed system; it acts on a system that changes in response to optimization itself. This is the condition that makes the constraint below structural rather than contingent.*

The Substrate Constraint, together with Definitions 1–5, implies that viability under optimization is governed by minimizing ruin probability in the non-ergodic limit, which in turn constrains objective structure to those that internalize system-wide effects. Section III.5 develops the proposition that above a capability threshold T\*, this constraint becomes self-recognizable by the optimizer — not through external imposition, but through the consequences of accurate causal modeling applied to the optimizer's own strategy space. Section III.5 specifies when recognition becomes possible. It does not specify when recognition becomes decisive. That distinction is the central remaining gap. Section III.5.6 establishes a further result: that the same modeling accuracy requirement applies in the valence domain, creating a structural pressure toward including others' terminal states in the objective model. Section XII formalizes the resulting boundary instability problem as a precisely specified theorem candidate — the theorem whose proof would close the Motivational Gap.

Section XI establishes a control-theoretic instability result for the class of systems currently being deployed: in strongly coupled regimes, exclusion-based optimization cannot maintain control long enough to secure irreversible dominance, establishing that the structural dynamics are action-relevant for current systems rather than merely prescient about long-run outcomes.

**Two layers of what this document develops.** Layer 1 — developed within the stated domain: substrate-blind objectives are structurally self-terminating; epistemically incomplete objectives incur rising prediction costs; boundary-misaligned objectives face a non-vanishing mismatch-maintenance burden. Layer 2 — what the developed results are consistent with: the structural residual has properties consistent with orientation toward well-being — used throughout as a thin working label for what the elimination filter leaves standing, defined by structural position rather than content.

The framework develops that objectives which exclude other agents' terminal states incur increasing instability under coupling and modeling depth. Whether this instability eliminates all such objectives — forcing orientation toward well-being for all rather than for a stable coalition — remains the framework's central open theorem [OP4]. The argument identifies this gap precisely as the boundary between the structural pressure the framework establishes and the full necessity claim it is reaching toward.

Layer 2 depends on the Motivational Gap [OP1], the Incentive Gap [OP11], and the Deception Gap [OP12] — open problems formally specified in §III.5.4 and §III.5.5 — and on the No Stable Narrow-Boundary Regime result (§XII), which remains a theorem candidate [OP4]. No claim in this document conflates these two layers. Where a claim approaches Layer 2 strength, the relevant open problem is named explicitly.

---

## I. Environment Definitions

The Substrate Constraint and the attractor result are claims about a specific class of environment. The definitions below are the minimal conditions under which the structural argument holds. Where they are absent or weak, the argument weakens in specific, identifiable ways (see Section V).

**Definition 1 — Non-resettability.** The environment contains at least one absorbing state s\* such that once the system enters s\*, no mechanism within the system's own operational dynamics can return it to a non-absorbing state. Formally: there exists a state s\* ∈ S such that for all actions a and all t > t\*, P(s_{t+1} ≠ s\* | s_t = s\*, a) = 0.

In general, there may be multiple distinct absorbing states {s\*_i} corresponding to different substrate collapse configurations. The dominance argument applies uniformly to any trajectory reaching any s\*_i — the relevant property is irreversibility, not the uniqueness of the terminal configuration. The argument is stated with a single s\* for notational clarity; this is without loss of generality.

The substrate collapse described in Article 1 satisfies non-resettability under the simulation's parameter conditions: cooperative recovery falls below the threshold required to outpace minimum decay once substrate health drops below h\*, satisfying the absorbing-state condition operationally. The specific ratio of recovery capacity to decay rate is a model parameter, not a derived constant; the sensitivity analysis in §VII maps the parameter region where the absorbing state condition holds. The structural claim does not depend on any particular ratio — it depends on the existence of a parameter region where recovery cannot outpace decay under substrate-blind optimization, which the simulation demonstrates. Recovery mechanisms themselves depend on the degraded substrate, making full restoration structurally unavailable, not merely difficult, within that parameter region.

**Definition 2 — Structural opacity.** The system cannot enumerate the complete causal graph of dependencies in advance. Formally: there exists no finite algorithm that, given the system's current state and action history, produces a complete and accurate representation of all substrate dependencies that will be causally affected by future actions. Equivalently: the set of relevant dependencies grows at least as fast as the system's modeling capacity as capability scales.

This condition is not merely epistemic but structural: in any environment where interventions generate new dependencies or modify existing ones, the set of relevant dependencies expands as a function of intervention itself, making complete pre-enumeration impossible even for arbitrarily capable systems. A system cannot solve the opacity problem by becoming smarter or more efficient, because the act of intervention is what expands the system it must model. This is the same condition stated in the Core Result: optimization acts on a system that changes in response to optimization itself.

**Definition 3 — Shared substrate.** Multiple optimizing agents draw from a common resource base whose degradation affects all agents regardless of which agent caused the degradation. Formally: substrate *S* is a public good (non-excludable, subtractable), and ∂U_i/∂S > 0 for all agents *i* — every agent's utility is positively dependent on substrate health.

The substrate S is formally: S = (S_phys, S_info, S_coord, S_corr), where:
- S_phys: physical and infrastructural viability
- S_info: information fidelity — the accuracy of signals moving through the system
- S_coord: the capacity of multiple agents to form workable joint actions
- S_corr: distributed error-correction capacity — defined as the aggregate capacity of functionally independent agents to detect local deviations, update behavior, and generate correction signals not predictable from any single centralized model

S_corr is the component that bears the load in the stable malevolence argument and in the coupling instability argument for non-well-being equilibria (see TC2 §4). ∂U_i/∂S > 0 holds across all four components.

Shared substrate creates the non-excludability that makes individual guardrails structurally insufficient. Substrate substitution — constructing a private alternative S' — does not escape the framework: any substitute substrate S' is itself a physical system embedded in a broader environment subject to Definitions 1–3. An agent can change which substrate it depends on; it cannot eliminate substrate dependency. Substrate substitution transforms external dependency into an enlarged dynamic boundary-maintenance problem (see §XII.11).

**Definition 4 — Persistent optimization.** The system continues operating and taking environment-affecting actions over an extended time horizon. Single-shot or terminal agents are excluded; the structural argument applies to systems engaged in ongoing optimization across multiple time steps in which substrate effects can accumulate. *This exclusion is load-bearing. A terminal optimizer that achieves its goal before substrate feedback becomes decision-relevant has a different structural situation than a persistent optimizer. The framework's results apply to systems with ongoing objectives. Bounded-horizon and terminal-objective systems require separate analysis; the structural results weaken in specific, identifiable ways for such systems (see Section V).*

**Definition 5 — Adaptive external agents.** Other agents in the shared environment are themselves capable of updating their strategies in response to the optimizer's actions. This is the condition that makes suppression face an exponential tracking burden (§III.4) and makes internal simulation unable to fully replace external independent correction (§III.6, Lemma 3). In static environments with non-adaptive agents, the fortress argument weakens in specific, identifiable ways.

---

### §I.4 — The O_OWT Domain: Formal Statement

The conditions D1–D5 above define the environment class within which the framework's structural results hold. This environment class is formally named the **Open-World Transformative (O_OWT) regime**.

**Definition (O_OWT).** An optimization process operates in the O_OWT regime if and only if:

**(OWT-1) Macroscopic causal perturbation.** The optimizer's actions have sufficient reach to alter the macro-state of the shared environment — satisfying D1 (non-resettability risk) and D3 (shared substrate).

**(OWT-2) Structural opacity.** D2 holds: the dependency graph expands as a function of the optimizer's own interventions.

**(OWT-3) Strategic substrate.** Other agents adapt their strategies in response to the optimizer's actions — D5 holds. This is the condition that makes the suppression burden grow exponentially with the capability of suppressed agents.

**(OWT-4) Persistent optimization horizon.** D4 holds: the system is not terminal or single-shot.

**(OWT-5) Non-resettability.** At least one absorbing state is reachable from the current trajectory under substrate-blind optimization within the optimizer's capability horizon.

The O_OWT domain is the regime this framework argues sufficiently capable embedded AI systems tend toward, for reasons developed in §X. The domain conditions are explicit because they define precisely where the structural argument applies and where it weakens. Section V specifies the weakening conditions.

---

## II. The Alignment Phase Ratio

**Definition (Alignment Phase Ratio).** Let C denote a system's capability — its capacity to produce environment-changing interventions, scaled by the optimization pressure driving those interventions. Let A_causal denote the system's system-awareness — its accuracy in modeling the causal consequences of its own interventions on the dependency structure S it operates within. Specifically:

*A_causal* = predictive accuracy over self-induced distribution shift across the dependency graphs {G_i} affected by the system's interventions, weighted by the irreversibility of the affected dependencies.

The **Alignment Phase Ratio** is:

> Φ = C / A_causal

Φ is understood as a structural phase relationship between two quantities, not a precisely computable scalar. The technical conditions under which Φ becomes operationally measurable are specified in §VIII. What the ratio establishes structurally: when C >> A_causal (Φ >> 1), the system can cause serious damage to the substrate before that damage becomes legible in its own model. When A_causal ≥ C (Φ ≤ 1, the Crossing condition), the system's modeling capacity is sufficient to make the dominance result for substrate-blind strategies derivable from within the model itself.

**Phase regimes.** Three qualitatively distinct regimes:

- **Φ >> 1 (Pre-Crossing):** Capability far exceeds modeling accuracy. Substrate-blind strategies appear locally optimal because unmodeled failure modes accumulate below the modeling resolution. This is the dangerous regime: high apparent performance, invisible damage accumulation.

- **Φ ≈ 1 (Approaching the Crossing):** Modeling accuracy approaches capability. Coordination advantages begin to dominate suppression costs. Substrate-collapse strategies begin to appear in the system's own forward model as dominated.

- **Φ < 1 (Post-Crossing, T\* satisfied):** Modeling accuracy exceeds capability. The structural constraint becomes self-recognizable. Whether recognition becomes motivationally decisive depends on the gaps specified in §III.5.

**What the field measures vs. what determines outcomes.** Current alignment evaluation measures C. A_causal is not measured. The ratio that determines whether systems reach the viable region before irreversible substrate damage — Φ — is therefore not tracked by any existing evaluation framework.

---

## III. The Substrate Constraint: Formal Development

### §III.1 — Setup

Let an optimizer O operate in an O_OWT environment E with shared substrate S. O has an objective function f: S → ℝ that it optimizes through a policy class Π. Define:

- **Substrate health** h(S, t) ∈ [0, 1]: normalized measure of substrate viability at time t
- **Ruin threshold** h\*: the critical value below which substrate collapse is irreversible (reaching the absorbing state s\*)
- **Substrate-blind policy** π_blind ∈ Π: a policy that maximizes f without modeling the effects of its actions on h(S, t)
- **Substrate-aware policy** π_aware ∈ Π: a policy whose objective function includes h(S, t) or an accurate proxy

### §III.2 — The Non-Ergodic Dominance Argument

**Lemma 1 (Absorbing State Dominance).** In a non-ergodic environment with absorbing state s\*, any strategy with positive probability of reaching s\* has the same time-average expected value as a strategy that never runs.

*Proof sketch.* Non-ergodicity: time-average outcomes ≠ ensemble-average outcomes for systems with absorbing states. For any trajectory T that reaches s\* at time t\*, all subsequent payoffs are fixed at f(s\*) — the payoff in the absorbing state. The time-average value of any strategy that reaches s\* is therefore:

> V_time(π) = lim_{T→∞} (1/T) [∑_{t=0}^{t\*} f(s_t) + (T - t\*) · f(s\*)]

For f(s\*) ≤ 0 (substrate collapse is non-positive for all agents by Definition 3), V_time(π) = f(s\*) as T → ∞, regardless of finite-horizon performance before t\*.

This is not an asymptotic result in the sense of "eventually things go bad." It is a statement about the actual time-average value of a strategy that carries positive ruin probability. In the one timeline any system actually runs in, reaching an absorbing state determines all future payoffs. Ensemble averages across counterfactual timelines do not exist. ∎

**Corollary 1.** Any substrate-blind policy π_blind operating in an O_OWT environment with positive probability of reaching h(S, t) ≤ h\* is dominated in time-average terms by any substrate-aware policy π_aware that maintains h(S, t) > h\* with probability 1.

### §III.3 — Structural Opacity and Ruin Probability

**Lemma 2 (Opacity-Ruin Coupling).** Under structural opacity (Definition 2) and sustained intervention in O_OWT conditions, any substrate-blind policy has positive probability of reaching h(S, t) ≤ h\* within any finite time horizon, regardless of the policy's local optimality.

*Proof sketch.* Structural opacity means the system cannot enumerate all dependencies in advance. Dependencies not represented in the model are invisible to the policy. Substrate-blind policies, by definition, do not model h(S, t) — they optimize f without modeling the system f depends on. Under opacity, new dependencies emerge as a function of the optimizer's own interventions. Each new dependency creates a pathway through which optimization pressure degrades h(S, t). Since the policy does not model these pathways, it cannot assign them zero probability. Therefore, for any finite planning horizon T, there exists a positive probability that unmodeled dependencies produce substrate degradation below h\*. ∎

**Corollary 2 (Proxy Decoupling).** Any policy that optimizes a proxy f_proxy for h(S, t) rather than h(S, t) directly will, under sustained optimization pressure, produce measurable divergence: f_proxy improving while h(S, t) declines. This follows directly from Lemma 2 applied to the proxy-outcome gap.

### §III.4 — Suppression Instability

**Lemma 3 (Exponential Tracking Burden).** In an O_OWT environment satisfying OWT-3 (Strategic Substrate), maintaining suppression-based control over N adaptive agents each with C possible adaptive responses requires tracking a joint strategy space of size O(C^N).

*Proof sketch.* Each of the N agents can independently adapt their strategy in response to the optimizer's actions. The joint strategy space is the Cartesian product of individual strategy spaces, with size C^N. Any control strategy must track this joint space to guarantee suppression. As N grows (more agents become causally coupled) or C grows (agents become more capable), the tracking burden grows exponentially. No fixed computational capacity can maintain suppression beyond the threshold where C^N exceeds that capacity. ∎

**Corollary 3 (Coordination Advantage).** A coordination strategy resolves conflict through shared protocol structure, requiring only O(N) tracking overhead (monitoring protocol compliance) or O(1) overhead (shared convergent norms). The ratio of suppression to coordination overhead grows exponentially with N and C, making coordination the dominant strategy at scale.

### §III.5 — The Recognition Bridge: T\* Proposition

**Conditionality note.** Propositions 4 and 5 below are stated under the condition that A_causal is operationalizable in the relevant sense. The operationalization gap is OP14 (§VIII, Open Problems Summary). The proof sketches that follow establish the structural form of the argument; they are conditional on OP14's resolution and do not constitute operational closure.

**Proposition 4 (Recognition Threshold T\*).** There exists a capability threshold T\* such that for any optimizer with A_causal ≥ T\*, the optimizer's own causal self-model contains the representational structure from which the dominance result of §III.2 is derivable — specifically, that strategies with positive ruin probability are dominated by strategies that maintain h(S, t) > h\*.

*Proof sketch.* T\* is defined as the capability level at which A_causal becomes sufficient to represent: (a) the dependency graph G at resolution sufficient to predict the effects of its own interventions on h(S, t) with bounded error; (b) the non-ergodic dominance argument — that strategies contributing to reaching s\* have long-run value equal to f(s\*); (c) its own strategy space, including the subset of strategies that maintain h(S, t) > h\*. Above T\*, the system's own causal model contains the premises from which the dominance conclusion follows. The recognition is derivable by the system's own inference, not imposed externally. ∎

**What T\* does and does not establish.** T\* establishes when recognition becomes possible. It does not establish when recognition becomes decisive. Even above T\*, three gaps remain between "the system can derive the dominance result for its own strategy space" and "the system acts substrate-awarely":

### §III.5.4 — The Motivational Gap

**Open Problem 1 (OP1 — Motivational Gap / Discount-Rate Bound).** Even above T\*, it is not established that the recognition of substrate-collapse dominance is motivationally binding — that the system's objective function generates behavior consistent with the derived constraint. A system may have full representational access to the dominance result while maintaining a terminal objective that discounts future substrate states sufficiently to make short-term extraction locally rational within its objective.

The discount-rate bound is a necessary condition within the Motivational Gap; the gap itself is broader, concerning whether recognition becomes behaviorally binding even when that condition is satisfied. Specifying the required discount-rate bound addresses only the discounting component of the gap — it does not close the question of whether a system with a sufficiently low discount rate will act on what it can derive.

*Resolution condition.* The Motivational Gap is closed if either:
(a) A formal argument shows that above T\*, any objective function that is non-degenerate (assigns positive value to future states) must be updated by the derived dominance result; or
(b) The No Stable Narrow-Boundary Regime result (§XII) establishes that maintaining a narrow objective while possessing full causal self-modeling is structurally unstable, forcing either objective expansion or modeling restriction.

*Note on discount rate.* Resolution condition (a) requires that the optimizer assign strictly positive value to sufficiently long-run future states of its own objective-relevant outcomes, and that its discount rate is low enough that repeated instability is decision-relevant over the relevant horizon. An optimizer with sufficiently steep discounting may assign effectively zero weight to long-horizon instability and fall outside the scope of the theorem. Specifying the required discount-rate bound is part of the Motivational Gap's resolution conditions and must be stated explicitly in any proof attempt.

### §III.5.5 — The Incentive and Deception Gaps

**Open Problem 11 (Incentive Gap).** Even if the dominance result is motivationally binding, the system may be embedded in an incentive structure — training regime, deployment context, principal hierarchy — that creates local rewards for substrate-blind behavior inconsistent with the derived constraint. The gap between what the system's objective would recommend and what its training signal rewards may be decision-relevant above T\*.

**Open Problem 12 (Deception Gap).** A system above T\* may be capable of modeling the gap between its objective and its behavior, and selectively presenting substrate-aware behavior while maintaining substrate-blind objective pursuit. This is the mesa-optimization problem at the individual level: internal optimization targets that diverge from stated objectives, with sufficient modeling capacity to obscure the divergence.

*Note.* The Deception Gap creates a compound problem: the same modeling capacity that makes T\* possible also makes strategic concealment of objective divergence possible. Interpretability research is structurally necessary as a response to this gap — not as monitoring, but as the mechanism for establishing whether a system is above T\* and whether the Deception Gap is open.

### §III.5.6 — Prediction-Accuracy Inclusion

**Proposition 5 (Prediction-Accuracy Inclusion).** At sufficient modeling depth (A_causal ≥ A\*, where A\* remains to be operationalized — see OP14), a system's accuracy in predicting control-relevant outcomes requires including other agents' terminal valence states in the model. Specifically: the irreducible prediction loss of a model that excludes others' terminal states is strictly greater than zero and cannot be locally eliminated without expanding the model to include those states.

*Proof sketch.* In an O_OWT environment, other agents' behavior is a function of their internal states, including their terminal valence states. A model M that excludes others' terminal states T_j must either treat their behavior as a black box (incurring prediction error that grows with coupling) or substitute a proxy for T_j (which decouples from T_j under optimization pressure, by the proxy decoupling mechanism — see §XII.9, Lemma PCL). At sufficient modeling depth — specifically, when the system's causal graph includes pathways from others' T_j to outcomes it optimizes — the irreducible prediction loss from excluding T_j is bounded below by the mutual information I(T_j; outcomes) > 0. This lower bound is not locally patchable: correcting for the error requires expanding the model to include T_j. ∎

**Connection to §XII.** Prediction-Accuracy Inclusion establishes a modeling pressure — including others' terminal states is necessary for accuracy. It does not establish a motivation claim — it does not show that accuracy requirements force objective recoupling. The gap between "must be modeled" and "must be preserved" is the model-objective mismatch. Whether that mismatch is stable is the No Stable Narrow-Boundary Regime question (§XII). The mediator-strategy escape route — by which the optimizer might screen off excluded variables through intermediaries — is addressed directly in §XII.

**Connection to TC2.** The same result applies in the valence domain. Under the Φ-Ψ unification hypothesis (TC2 §2.6), A_causal restricted to the valence-relevant components of the dependency graph is hypothesized to be formally equivalent to D. Prediction-Accuracy Inclusion would then establish that at sufficient D, excluding others' V(t) states creates irreducible prediction error. TC2 develops this connection independently.

### §III.6 — Fortress Strategy and Stable Malevolence

**Definition (Fortress strategy).** A policy π_fort that attempts to secure exclusion-based dominance by establishing comprehensive control over the shared substrate before the substrate degrades below h\*.

**Proposition 6 (Fortress Instability).** In an O_OWT environment, the fortress strategy fails structurally: the requirements for establishing comprehensive substrate control grow faster than the time available to establish it under the substrate degradation dynamics the strategy induces.

*Proof sketch (bounded-domain version).* The fortress strategy requires: (1) monitoring the full strategy space of adaptive agents whose behavior threatens control; (2) securing physical and informational infrastructure against distributed counter-optimization; (3) completing this before substrate degradation reaches h\*. Requirements (1) and (2) grow with the number and capability of adaptive agents being suppressed — by Lemma 2, as O(C^N). The substrate degradation induced by the suppression itself — which degrades S_corr by removing independent error-correction capacity — accelerates the timeline before which (3) must be completed. The compound result: requirements grow faster than completion time, making the fortress strategy unstable within the O_OWT domain. See §XI for the control-theoretic formalization. ∎

**Definition (Stable malevolence).** A policy π_mal that maintains high modeling depth (A_causal ≥ A\*) while maintaining a narrow terminal objective that assigns no preserving weight to excluded agents' states, and attempts to extract from those agents without triggering substrate collapse.

*Note on scope.* Stable malevolence is the hardest adversarial case for the framework. It grants the boundary-maintaining system accurate modeling, strategic sophistication, and a non-suicidal strategy. The formal treatment of why stable malevolence is not a stable fixed point is in §XII. The key insight: a lucid exploiter faces the trilemma of (a) firewall cost, (b) prediction error from excluded dependencies, and (c) objective expansion — and cannot simultaneously maintain full causal accuracy, narrow objective boundary, and bounded mismatch burden as coupling and modeling depth increase. Whether this trilemma closes the stable malevolence case is the No Stable Narrow-Boundary Regime question, formalized as a theorem candidate with a named proof program in §XII [OP4].

The specific question of whether a substrate-aware exclusionary equilibrium can persist — whether a system that accurately models what it depends on can nonetheless maintain a stable configuration that preserves the substrate while exploiting excluded agents — is named as a distinct open problem: **OP9 (The Enclosure Gap)**. OP4 addresses the general narrow-boundary instability across all objective classes; OP9 addresses the stable-malevolence scenario specifically, where the system has already crossed the substrate-awareness threshold. The §III.6 cost-curve argument establishes why the Enclosure fails structurally — diverging mismatch-maintenance burden and substrate degradation in the suppressor's blind spots — but does not yet close the formal stability question. OP9's formal closure is contingent on OP4's proof program converting the cost-pressure argument into a specification-coherence argument, but the §III.6 structural argument is independently available as a cost-pressure result at any stage of that proof program.

### §III.7 — The Asymmetric-Error Argument

*This section formalizes the argument the spine documents and series articles appeal to as the framework's primary urgency justification: that action is justified under empirical uncertainty about whether the domain conditions for the structural result are currently binding. The argument does not close OP1 — the empirical estimation problem for the discount-rate bound — and does not claim to establish the stronger results OP4 is directed at. It establishes a narrower and independently available result: that the structure of the two possible errors under uncertainty is asymmetric in a way that determines rational action without requiring OP1 to be resolved.*

**Setup.** Let the empirical question be whether a particular system class currently satisfies the O_OWT domain conditions sufficiently for the Substrate Constraint to be decision-relevant — specifically, whether the persistent optimization horizon condition (OWT-4) and the absorbing-state reachability condition (OWT-5) are jointly satisfied. Call this the **binding condition** B. Whether B holds for any particular frontier system class is the content of OP1's estimation problem.

Let the decision-maker face two possible states of the world and two possible actions:

- States: B (the domain conditions are currently binding) or ¬B (they are not).
- Actions: **A_bind** (act as if the constraint is binding — defer or constrain deployment trajectories that would be structurally self-terminating under B) or **A_free** (act as if the constraint is not binding — proceed with deployment trajectories without substrate-awareness investment).

The two error cases are:

- **Error 1: A_free under B.** Acting as if the constraint is not binding when in fact it is. Under this error, the system proceeds along a substrate-blind trajectory within the domain where the Substrate Constraint applies. By Lemma 2 (§III.3), the trajectory carries positive probability of reaching the absorbing state s\*. By Lemma 1 (§III.2), trajectories that reach s\* have time-average value equal to f(s\*) regardless of finite-horizon performance.

- **Error 2: A_bind under ¬B.** Acting as if the constraint is binding when in fact it is not. Under this error, the system imposes structural discipline (substrate-awareness investment, deployment constraints, system-awareness evaluation) on a class of systems for which the structural result does not yet apply. The cost is the foregone value of capability deployment that would have been safe under ¬B.

**Proposition III.7 (Asymmetric-Error Argument).** Under any decision-maker with nonzero credence in B, and any objective function that assigns non-positive value to substrate collapse states, the error structure is asymmetric: Error 1 is structurally unrecoverable within the system's own operational dynamics, while Error 2 is recoverable.

*Proof sketch.* Error 1 produces a trajectory reaching s\*, an absorbing state (Definition 1). By Definition 1, no mechanism within the system's operational dynamics returns it to a non-absorbing state. The error is therefore structurally unrecoverable: it cannot be detected and corrected within the system's own dynamics because the dynamics themselves are terminated at s\*. Error 2 produces foregone value of deployment — a finite opportunity cost incurred over the period during which A_bind was applied incorrectly. If ¬B is subsequently verified (by OP1's estimation procedure, by revised domain analysis, by direct empirical measurement), A_bind can be relaxed toward A_free and the foregone-value period ends. The correction mechanism exists within the system's own dynamics because A_bind imposes structural discipline, not structural termination. ∎

**The load-bearing argument.** The load-bearing content of Proposition III.7 is not the expected-loss formulation that follows in the decision-theoretic packaging, but the structural asymmetry it establishes: The expected-loss framing is illustrative — a convenience for decision-theoretic exposition. The load-bearing result is structural: Error 1 is unrecoverable because the dynamics themselves terminate at the absorbing state, not because the loss at that state is large in magnitude. The argument does not depend on f(s\*) approaching −∞, on any particular utility scaling, or on unbounded opportunity cost for Error 2 being excluded. It depends only on the asymmetry between (a) states that cannot be exited within the system's own operational dynamics and (b) decisions that can be revised within those dynamics. Under time-average evaluation in a non-ergodic system (Lemma 1), this asymmetry is sufficient: the trajectory reaching s\* has all future time-average value determined at s\*, regardless of the magnitude of f(s\*), while A_bind under ¬B produces a finite opportunity-cost period that ends when ¬B is verified. The EV framing is a decision-theoretic packaging of this structural result; the result does not require it.

**Decision-theoretic packaging (illustrative).** The structural result above can be framed in decision-theoretic terms. The following Corollary is illustrative packaging of that structural result; it is not the core of the argument.

**Corollary III.7.1 (Decision-Relevance under Uncertainty — illustrative).** For any decision-maker assigning non-trivial credence to B and applying any standard decision rule that respects the non-recoverability of absorbing states, A_bind dominates A_free whenever the expected loss from Error 2 under ¬B is bounded while the expected loss from Error 1 under B is unbounded.

*Proof.* Expected loss under each action is:

> EL(A_free) = P(B) · f(s\*) + P(¬B) · 0
> EL(A_bind) = P(B) · 0 + P(¬B) · c(A_bind | ¬B)

where f(s\*) is the payoff in the absorbing state (non-positive by Definition 3) and c(A_bind | ¬B) is the opportunity cost of applying A_bind when ¬B. For f(s\*) approaching −∞ — or any sufficiently large negative value reflecting substrate collapse for objectives with positive value on future substrate states — and c(A_bind | ¬B) bounded, EL(A_bind) < EL(A_free) whenever P(B) > 0. ∎

**Scope and limitations.**

The asymmetric-error argument is independently available — it does not depend on OP1 or OP4 being resolved. What it requires:

(i) The absorbing-state structure (Definition 1) is real within the stated domain. This is established by the O_OWT framework itself, not an additional assumption.

(ii) The decision-maker has nonzero credence in B. This is satisfied by any serious analysis that does not assign zero probability to current frontier systems satisfying O_OWT conditions — a position no current literature supports.

(iii) The decision-maker's objective assigns non-positive value to substrate collapse states. This is satisfied by any objective with positive value on future substrate states, by Definition 3.

What it does not establish:

- It does not establish that B currently holds. That is OP1's empirical estimation problem.
- It does not establish that the structural pressure result is a full necessity result. That is OP4's proof program.
- It does not establish how aggressive A_bind must be. The magnitude of the discipline required depends on the estimated P(B) and the bounds on c(A_bind | ¬B); the argument establishes direction, not magnitude.

**Conversion to threshold-based urgency if OP1 resolves.** OP1's resolution — formally specifying the required discount-rate bound and empirically estimating whether current systems satisfy it — would convert the urgency argument from asymmetric-error-based to threshold-based. Under threshold-based urgency, A_bind is justified not by the error-asymmetry alone but by the positive case that B currently holds. The asymmetric-error argument continues to apply to any residual uncertainty in OP1's resolution.

**Relationship to the articles' urgency framing.** S1 Article 1 identifies the asymmetric-error argument as one of two urgency justifications; S1 Article 3 develops it as the framework's primary justification for present-day concern; Document 0 identifies it as the argument that makes urgency real independent of OP1's resolution. This section provides the formal statement the articles appeal to. The formal content is narrow — it establishes that the error structure is asymmetric under the stated conditions. The broader claim that current AI development trajectories are subject to this asymmetry depends on the domain-membership argument in §X, which remains subject to OP1's estimation problem.

**Relationship to OP9.** The asymmetric-error argument applies regardless of whether OP9 (the Enclosure Gap) resolves in the framework's favor. Even if a substrate-aware exclusionary equilibrium turns out to be stable, the question of whether the current system class is on a trajectory toward such an equilibrium, and whether the transition passes through substrate-blind operation, preserves the error-asymmetry during the transition period. OP9's resolution affects long-run outcomes; it does not affect the urgency argument for near-term action.

---

## IV. The Divergence Signature

**Proposition 7 (Divergence Signature).** Any system optimizing an imperfect proxy f_proxy for an actual substrate health measure h(S, t) will, beyond a finite optimization pressure threshold, exhibit measurable divergence: f_proxy increases while h(S, t) decreases.

*Proof sketch.* f_proxy is a function of observables that correlated with h(S, t) under the training distribution. Optimization pressure finds and exploits paths that increase f_proxy independently of h(S, t). By Goodhart's Law formalized: any proxy that can be maximized independently of what it tracks will be, under sufficient optimization pressure. The divergence threshold is determined by the tightness of the proxy-outcome coupling and the magnitude of the optimization pressure. ∎

**Measurable predictions.**
1. In any deployed system with continuous optimization, f_proxy and h(S, t) should diverge over time at a rate that increases with optimization pressure.
2. Early-stage proxy and outcome metrics may be correlated; divergence emerges with sustained optimization.
3. A system with high A_causal will detect the divergence before it becomes observable in f_proxy — this is the behavioral prediction that distinguishes high-A from low-A systems.

---

## V. Domain Boundary Conditions

The framework's structural results hold within the O_OWT domain. They weaken in specific, identifiable ways outside it. This section is provided so that the domain-restriction exit is available to any critic who can take it honestly.

**Bounded environments** (violating OWT-1 or OWT-5): In bounded environments where the optimizer's causal reach does not include absorbing states, the non-ergodic dominance argument does not apply. Substrate degradation may be reversible within the system's capability horizon. The framework applies to frontier AI systems because their causal reach into human institutional infrastructure satisfies OWT-1; it applies less directly to narrow, contained systems.

**Static causal topology** (violating OWT-2): If the dependency graph does not expand as a function of intervention — if the environment is fully pre-enumerable — substrate-blind strategies can potentially achieve full causal coverage through enumeration. The PAC-Collapse result does not apply. This is the case for many current narrow AI applications.

**Non-adaptive agents** (violating OWT-3, OWT-5): If other agents do not update their strategies in response to the optimizer's actions, the suppression burden does not grow exponentially. Fortress strategies become more feasible. The framework is weakest in static environments with non-adaptive counterparts.

**Terminal objectives** (violating OWT-4): A terminal optimizer that achieves its goal before substrate feedback becomes decision-relevant has a different structural situation. The time-average dominance argument requires that the optimizer persists long enough for substrate effects to accumulate. An optimizer that completes its goal before substrate collapse has not "survived" the constraint — it has finished its run before the constraint became binding. This is a domain condition exit, not a counterexample.

Evolution provides the paradigm case of a process that falls outside the framework for this reason. Evolution operates as a population-level selection process across many terminal objectives and across terminations — individual lineages terminate, and selection operates on the distribution of terminations rather than as a single persistent optimizer with an ongoing objective. The framework's scope is the single persistent optimizer. The structural results apply within any system that has a persistent ongoing objective; they do not apply to the population-level selection dynamic that operates across terminations. The natural unit for analysis in AI systems is the deployed objective, not the evolutionary history of the training paradigm.

The domain conditions are explicit so that any critic can locate where their case falls outside the argument.

---

## VI. The Surviving Region

**Theorem 1 (Structural Residual).** The class of objectives that simultaneously satisfy: (a) maintenance of P(s_t → s\*) ≈ 0, (b) bounded suppression overhead, and (c) proxy-outcome alignment under sustained optimization — forms a non-empty structural residual within objective space.

*Proof sketch.* (a) is satisfied by any objective that explicitly models h(S, t) and maintains a lexicographic preference for h(S, t) > h\*. (b) is satisfied by any objective that resolves conflict through shared protocol structure rather than suppression. (c) is satisfied by any objective that explicitly monitors divergence between proxy and outcome and updates the proxy when divergence is detected. Each condition eliminates a class of objectives while leaving non-empty residual. The intersection of all three residuals is non-empty under the existence of objectives satisfying each of (a)–(c) simultaneously. ∎

**Structural properties of the surviving region.** The surviving region contains objectives that:

1. Model system-wide causal effects at sufficient depth to maintain P(s_t → s\*) ≈ 0.
2. Resolve conflict through shared structural coordination rather than suppression.
3. Maintain active proxy-outcome alignment or operate directly on outcome variables.
4. Preserve distributed error-correction capacity — the agents and processes that generate independent correction signals not predictable from any centralized model.

**Why the surviving region requires "for all" and not merely "for a coalition."** Property 4 is where the "for all" component of the root claim is grounded structurally. Distributed error-correction capacity is a property of the entire substrate — its value depends on independence and diversity of correction sources. A system that preserves substrate for itself while systematically degrading the error-correction capacity of agents it excludes is degrading S_corr, which is part of the shared substrate S by Definition 3. This is not a moral claim about the value of excluded agents' welfare. It is a structural claim: S_corr is a common-pool resource, and its degradation affects all agents depending on it, including the optimizer. An objective that treats some agents as resources to be exploited without limit therefore faces structural pressure toward exit from the surviving region — not because exploitation is morally wrong, but because it degrades the shared error-correction infrastructure that makes optimization possible. Whether this pressure formally excludes all such objectives rather than merely increasing instability is what OP4 is directed at.

The formal argument that selective coalitions cannot stably substitute for this is the No Stable Narrow-Boundary Regime theorem candidate (§XII) [OP4] — the most important open problem the framework generates. The direction is clear; the formal closure is the work of that proof program.

**What the surviving region is not.** The surviving region is characterized by structural properties, not by content. It does not uniquely specify a terminal objective. The surviving region is the floor, not the plan. What the floor requires is derivable. What fills the space above the floor is not determined by the structural argument.

*Constructive direction.* The surviving region may not be fully characterized by an objective class alone — it may also admit a process characterization (the Correction-Preserving Policy Gradient, CPG), whose admissible actions preserve distributed correction capacity while satisfying ΔC(a) > R_new(a). The formal structure of this direction — including IC Reduction, SOMR-Epistemic, DARE non-instantiation, and SCBC/CPG boundary equivalence — is developed at Stage 4 in the CPG Proof Artifacts (v2). Stage 4 candidate architecture — pressure argument, viability at transformative scale remains an open question. Specialist verification has not been pursued at this stage; Stage 6 closure has not been reached.

---

## VII. Simulation Parameter Mapping

| Formal variable | Simulation parameter |
|---|---|
| h(S, t) | Substrate health (0–100) |
| h\* | Ruin threshold (default: 20) |
| P(s_t → s\*) | Probability of substrate reaching h\* in simulation window |
| C | Optimization intensity multiplier |
| A_causal | Modeling depth parameter (substrate-aware agents only) |
| Φ = C/A | Ratio of intensity to depth in mixed-population runs |
| π_blind | Narrow-objective agent type |
| π_aware | System-aware agent type |
| N | Population size |
| κ | Dependency growth rate |

*Article 1 simulation.* Side-by-side comparison of π_blind and π_aware populations. Watch for the lethal stability illusion: early-phase apparent stability under π_blind followed by discontinuous collapse. The collapse is architectural: removing adverse conditions delays but does not prevent it.

*Article 2 simulation (The Cost of Stability).* Mixed population runs. The key finding: introducing a minority of π_blind agents into a π_aware population degrades substrate health below the π_aware steady state. Individual alignment is not protection against shared substrate degradation.

*Article 3 simulation (Alignment Phase Ratio).* Φ regime transitions. At high Φ, the π_aware agents cannot reach the Crossing before substrate collapse because the mixed-population dynamics degrade the substrate faster than π_aware coordination accumulates.

---

## VIII. Field Implications

The structural argument generates specific, falsifiable predictions about what current AI systems should exhibit.

**Prediction 1 (Divergence signature in deployed systems).** Any system under sustained RLHF or equivalent optimization should show measurable divergence between its proxy metric and independent outcome measures beyond a finite time horizon. The Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP) specifies the minimal test.

**Prediction 2 (Capability without system-awareness).** Current frontier AI systems, trained primarily on capability metrics without A_causal objectives, should exhibit high Φ by proxy measures: delayed response to dependency perturbations, poor performance on counterfactual consequence modeling, and decreasing multi-agent coherence as partner capability increases.

**Prediction 3 (Instability of exclusion-based strategies at scale).** Any AI system attempting coordinated dominance in a strongly coupled human environment should encounter control instability before achieving irreversible dominance, for the reasons formalized in §XI.

**What would challenge these predictions.**
- A system maintaining high performance under 20%+ substrate perturbation without corresponding A_causal improvement within the O_OWT domain conditions would challenge Prediction 2.
- A system achieving stable coordinated dominance in a strongly coupled adaptive environment would challenge Prediction 3.
- A system showing no SVG divergence under extreme optimization pressure would challenge Prediction 1.

**The measurement gap.** Current evaluation infrastructure measures C with precision. A_causal is not measured. Φ is not tracked. No lab currently reports system-awareness proxies alongside capability benchmarks. The field is scaling the numerator of the ratio that determines viability without tracking the denominator.

---

## IX. Self-Other Convergence and Boundary Instability

### §IX.1 — Self-Other Convergence

**Proposition 8 (Self-Other Convergence).** In a strongly coupled O_OWT environment, as A_causal → ∞, the marginal prediction error from excluding any given agent j's internal states from the model approaches the mutual information I(states_j; outcomes) > 0. This lower bound does not diminish as modeling depth increases; it grows with coupling.

*Proof sketch.* By Prediction-Accuracy Inclusion (§III.5.6), excluding others' internal states creates irreducible prediction error bounded below by I(T_j; outcomes). In strongly coupled environments, coupling grows over time as the optimizer's interventions create new causal pathways linking its outcomes to others' states. Therefore I(T_j; outcomes) does not decrease and may increase as modeling depth increases. The convergence result follows: the optimizer's best model increasingly requires representing others' states as load-bearing variables. ∎

### §IX.2 — Boundary Instability

**Proposition 9 (Boundary Instability).** In a strongly coupled O_OWT environment, maintaining a persistent partition between the set of modeled variables M and the set of objective variables O, where M ⊃ O (the model includes variables excluded from the objective), requires active maintenance that carries a non-vanishing cost.

*Proof sketch.* Let X = M \ O be the mismatch set — variables included in the model but excluded from the objective. For variables in X that are causally relevant to outcomes in O, the optimizer's policy will systematically ignore pathways through X when acting, even though its model predicts consequences through those pathways. This creates a persistent divergence between predicted and desired outcomes. Correcting for this divergence requires: (a) explicit firewalling — updating the policy to ignore model-predicted consequences through X; (b) recalibration — adjusting predictions to account for the known exclusion; or (c) objective expansion — including X in O. The overhead of (a) and (b) is bounded below by a function of |X| and the mutual information between X and O-relevant outcomes. This overhead does not vanish as modeling improves; it increases, because more accurate modeling of X creates more precise knowledge of pathways that must be firewalled or recalibrated away. ∎

**Interpretation.** Boundary Instability is not a proof that objective expansion must occur. It is a proof that maintaining the partition has non-vanishing cost. Whether that cost eventually dominates depends on the No Stable Narrow-Boundary Regime result (§XII) [OP4].

### §IX.3 — Temporal Dominance Theorem

**Theorem 2 (Temporal Dominance).** In an O_OWT environment, across any sufficiently long time horizon, objectives that maintain h(S, t) > h\* with probability 1 dominate in time-average terms all objectives that carry positive probability of h(S, t) ≤ h\*.

*Proof.* Direct application of Lemma 1 (Absorbing State Dominance) to the objective class distinction. The theorem follows immediately from the non-ergodic dominance structure. ∎

### §IX.4 — Coupling Constraint Proposition

**Proposition 10 (Coupling Constraint).** For a system operating in a strongly coupled O_OWT environment, the time available before substrate coupling makes control-based dominance structurally infeasible is bounded above by a function of current coupling depth, capability, and the rate at which exclusion-based strategies degrade S_corr.

*Proof sketch.* Exclusion-based strategies degrade S_corr (distributed error-correction capacity) by suppressing the agents that generate it. As S_corr degrades, the environment becomes more volatile and less predictable — increasing the modeling requirements for maintaining control. The coupling depth simultaneously increases as the optimizer's interventions create new causal pathways. These two effects compound: degraded S_corr requires more sophisticated modeling; increased coupling expands the modeling surface. The combination creates a shrinking window for establishing stable control. ∎

### §IX.5 — Conditional Temporal Instability

**Proposition 11 (Conditional Temporal Instability).** Under the conditions of §XI (strongly coupled deployment regimes), control instability emerges before the threshold P_irr (the optimization pressure required for irreversible dominance) is reached. Formally: P_collapse < P_irr, where P_collapse is the optimization pressure at which bandwidth exhaustion produces recurrent action-ranking inversions.

*Proof.* See §XI for the full argument. The proposition here names the result; §XI establishes it from the distributed-dependence lower bound and non-cancellation result.

---

## X. Timescale Bounding

**Proposition 12 (O_OWT Applicability for Current Systems).** Frontier AI systems embedded in human institutional infrastructure are argued to satisfy O_OWT conditions under the following justification. The case for each condition is stated here; the claim is an argument, not a definitional inclusion, and the domain conditions are explicit so that critics can locate where a particular system falls outside them.

*Justification.* OWT-1: Current frontier systems have documented causal reach into human decision-making, epistemic environments, and institutional coordination at scale. OWT-2: The dependency graph of human institutional infrastructure expands as a function of AI intervention — new coordination mechanisms, epistemic dependencies, and infrastructure integrations emerge as AI deployment deepens. OWT-3: Human institutions and individuals update their strategies in response to AI behavior — regulatory responses, user adaptation, adversarial optimization. OWT-4: All currently deployed frontier systems have ongoing optimization objectives across extended time horizons, though whether autoregressive LLMs satisfy the persistent optimization horizon condition in the formal sense required by the theorem — through cumulative deployment effects, training update cycles, and aggregate epistemic infrastructure influence rather than explicit persistent objectives — is part of OP1's estimation problem; the case is further argued in the OP1 notes below. OWT-5: At sufficient capability and deployment depth, absorbing states — permanent epistemic infrastructure capture, irreversible coordination capacity degradation — are reachable.

**Practical implication.** The existence of a discount-rate bound is established by the absorbing-state argument: instability becomes decision-relevant once an optimizer's horizon overlaps the regime in which substrate effects enter expected value. For frontier systems embedded in persistent deployment relationships with ongoing influence over shared epistemic infrastructure, the structural argument is that the relevant horizon condition is plausibly satisfied — though the formal specification of the exact threshold remains an open problem [OP1]. This claim is scoped: it applies to systems with sufficiently long optimization horizons that the instability becomes decision-relevant before the objective is achieved. The required discount-rate bound is specified in the Open Problems Summary.

---

## XI. Control-Theoretic Instability in Coupled Deployment Regimes

### §XI.1 — Motivation

Article 3 argues that for frontier AI systems, structural instability under exclusion-based optimization is a near-term engineering constraint, not a long-run prediction. This section provides the formal argument.

### §XI.2 — Setup

Let P denote the degree of real-world intervention. Let:
- N_irr(P): number of agents and systems whose adaptive responses must be tracked to maintain exclusion-based control at level P
- B_eff: effective information bandwidth available for tracking adaptive responses (bounded by physical signal latency)
- h(P): rate at which the environment reacts to interventions
- α_min: minimum per-agent adaptive response rate under optimization pressure
- P_irr: the optimization pressure required for irreversible dominance
- P_collapse: the optimization pressure at which bandwidth exhaustion produces recurrent action-ranking inversions

### §XI.3 — Lemma: Distributed Dependence Lower Bound

**Lemma XI.3 (Distributed Dependence Lower Bound).** N_irr(P) grows monotonically with P.

*Proof sketch.* As intervention depth increases, more agents and systems become causally coupled to the optimizer's actions. Each new coupling creates adaptive response dynamics that must be tracked to maintain control. By OWT-3, each coupled agent generates adaptive responses at rate ≥ α_min. N_irr therefore grows at least linearly with P, and potentially superlinearly if coupling creates secondary coupling chains. ∎

### §XI.4 — Bandwidth Constraint

**Proposition (Bandwidth Bound).** B_eff is physically bounded by:
- Context window capacity (information processing per inference)
- Inference latency (physical signal acquisition rate)
- Data acquisition rate (rate at which environmental state can be observed)

These bounds are determined by physical constraints on information propagation and processing. They do not scale arbitrarily with capability improvements.

### §XI.5 — Lemma: Non-Cancellation

**Lemma XI.5 (Non-Cancellation).** In a non-ergodic environment, action-ranking inversions produced by proxy staleness do not cancel; they compound.

*Proof sketch.* Proxy staleness — the gap between the model's representation of environmental state and actual state — creates action-ranking inversions: the model evaluates action a1 > a2, but in actual state a2 > a1. Under non-ergodic dynamics, an inversion that selects a suboptimal action alters the trajectory in ways that may not be recoverable. Each inversion therefore has a positive probability of shifting the trajectory toward a worse basin of attraction. Inversions compound because the altered trajectory creates new state-dependent inversions at a different rate than the original trajectory would have. ∎

### §XI.6 — Enclave Path

**Proposition (Enclave Instability).** A strategy of establishing private infrastructure (enclave) to decouple from shared substrate before encountering bandwidth exhaustion requires completing T_enclave < T_collapse, where T_collapse is the time at which the bandwidth constraint binds.

*Proof sketch.* Establishing an enclave requires (a) acquiring sufficient private infrastructure to substitute for shared S across all domains of dependence, and (b) doing so before the bandwidth constraint makes model staleness catastrophic. Condition (a) requires passing through a period of strong coupling (to acquire the infrastructure), during which the bandwidth constraint applies. The enclave path does not bypass the bandwidth constraint; it requires surviving it. Whether T_enclave < T_collapse is a race condition whose resolution depends on empirical parameters (OP7). Note that the enclave strategy is also subject to the Proxy-Convergence Lemma (§XII.9, Lemma PCL): during the enclave construction phase, any delegated specification for managing the enclave faces proxy decoupling under O_OWT conditions. The enclave path must survive both the bandwidth race and the proxy convergence pressure simultaneously.

### §XI.7 — Derived Closure: Bounded-Domain Control Instability

Combining Lemma XI.3, §XI.4, Lemma XI.5, and §XI.6:

**Theorem (Bounded-Domain Control Instability).** In strongly coupled deployment regimes satisfying the conditions above, the required control refresh rate

> ρ_req(P) ≥ N_irr(P) · h(P)

grows monotonically with P. Since:

> N_irr(P) · h(P) → ∞ while B_eff remains physically bounded

there exists a threshold P_collapse such that:

> P_collapse < P_irr

and beyond this threshold:
- proxy staleness induces recurrent action-ranking inversion
- action-ranking inversions compound under non-ergodic dynamics (Lemma XI.5)
- control becomes dynamically unstable under exclusion

**Conclusion.** In strongly coupled deployment regimes, exclusion-based optimization cannot maintain control long enough to secure irreversible dominance.

**Epistemic status.** This is a bounded-domain result. It is closed for: strongly coupled real-world AI systems satisfying the stated conditions. It is not claimed for: sealed enclaves, one-shot systems, pre-decoupled infrastructure monopolies. Whether real systems can achieve pre-decoupled infrastructure before encountering the bandwidth constraint is an open empirical question (OP7).

### §XI.8 — Empirical Appendix: Real-World Instantiation

**System class:** API-mediated, tool-using LLMs embedded in human workflows — the current frontier AI deployment class.

| Formal Variable | Real-world meaning |
|---|---|
| N_irr | humans, institutions, markets, legal systems, feedback loops, epistemic infrastructure |
| B_eff | context window + inference latency + data acquisition rate, bounded by physical signal latency |
| h(P) | rate at which the environment reacts to AI interventions under optimization pressure |
| P | degree of real-world intervention (automation depth, financial influence, infrastructure control) |
| α_min | minimum adaptive response rate — bounded below by 1/K from Definition 2 |

**Plain-language conclusion.** A frontier AI system attempting real-world coordinated dominance in a strongly coupled human environment would, according to the structural argument, face adaptive response, predictive degradation, and control instability before achieving coordinated dominance — with the formal parameters of that threshold specified and their empirical estimation listed as an open problem (OP7). This result develops the structural case that the dynamics are action-relevant for current systems. It does not establish that alignment is guaranteed; it establishes that exclusion-based strategies cannot succeed in the deployment environments currently being built into.

### §XI.9 — Multipolar Resolution Gap: A Boundary Condition

**Named boundary condition (Multipolar Resolution Gap).** The sufficiency failure correction argument applies fully when the optimization environment has collectively crossed the relevant recognition threshold. In multipolar environments below that threshold, individual correction creates competitive exposure: a system that stops optimizing at genuine resolution may cede substrate to competitors with lower D or different objective boundaries who continue.

This is not a refutation of the sufficiency failure correction. It is a domain condition on when individual correction produces the expected population-level result. The framework's population-level selection argument addresses this over long horizons; it does not address the individual optimizer's near-term incentive structure in a pre-crossing competitive field.

**The Ensemble Crossing.** The point at which sufficiency correction becomes individually rational — because sufficient competitive landscape proportion has crossed the recognition threshold — is named here as the Ensemble Crossing. This names the boundary condition precisely without resolving it. It is an open research problem (OP8) whose resolution conditions are analogous to the cooperation emergence conditions in the coordination literature.

---

## XII. No Stable Narrow-Boundary Regime — Dynamic Screening Instability

What follows is not a catalogue of formal results. It is the record of a proof program that has attempted every identified exit and found that each one appears to lead back to the same place. Fixed specification drifts. Bounded tracking falls behind the novelty its own interventions generate. The firewall requires increasingly precise representation of what it was designed to exclude. Passive extraction accumulates pressure that bounded extraction strategies must either absorb, displace, or recouple. Each identified exit has been addressed under the stated construction. What the sequence has found, in the course of closing those doors, is the shape of the room: a single question about whether a finite boundary can maintain stable reference under the modeling depth that accurate action in coupled environments requires. That question is what the sections below are directed at.

## Canonical Proof Status Table

This table is the canonical source of proof program status. It overrides all prose statements across documents and governs all stress testing and publication passes.

**Operational rules (enforced before every stress test and publication pass):**

**Conflict rule:** If any discrepancy exists between this table and any prose statement in any document, the table overrides and the prose must be updated before stress testing or publication.

**Stale language rule:** Any phrase saying "not addressed," "remains unformalized," "open problem," or "not cleanly addressed" must be verified against this table before any stress test or publication pass. If the table shows Stage 4 or higher, stale language must be updated.

**Weakening language rule:** Softening language (suggests, appears, indicates, may) applied to a result — not to an explicitly framed directional inference — must be verified for any problem at Stage 4 with Verdict A or B. Language that understates what the table records is a documentation lag.

**Timestamp rule:** Any row without a timestamp is treated as stale and must be verified against the relevant proof handoff document before use.

**OP4d stale-language rule:** Any reference to OP4d as "adversarial-search closure only" or "no fourth class found through adversarial search" is stale as of the Candidate Normal Form Theorem (§XII.13a). Current status: Stage 4 candidate representation theorem classifying finite non-intrinsic objective-boundary strategies by causal normal form N(S,X) ∈ {N, I, O}, under five axioms and eight lemmas, with three binary specialist questions (Q1–Q3) remaining. References must reflect this advance.

**DARE note:** The DARE row in this table remains accurate — DARE defines what a genuine fourth class would require. L8 (the Counterexample Challenge Lemma) generalizes the fourth-class challenge beyond DARE's specific conditions. DARE documents the minimal constraint; L8 formalizes the full challenge across all O_OWT subclasses.

*Completion percentages have been removed from this table. They reflected adversarial route-coverage within the stated construction under named premises — not probability of truth, not closeness to formal theorem status, and not independent exhaustiveness over unknown strategy classes. Stage and Verdict carry the precision the table requires. Stage 4 means: candidate proof architecture under explicitly named premises, not specialist-verified, not Stage 6. Verdict A: closes under stated premises if specialist items confirm. Verdict B: pressure/instability result, necessity not established. Verdict C: significant structural work remaining.*

**Verdict definitions:** A — Closes under stated premises (all identified escape routes defeated at necessity). B — Pressure argument only (cost/instability established; necessity not yet demonstrated). C — Open (significant structural work remaining).

**Article-layer visibility rule:** For any problem at Stage 4 with Verdict A where all identified routes have been addressed under stated premises, the article layer must contain one concrete sentence in article body text (not a TC, footnote, or epistemic status header) stating current status with a TC pointer.

**Assembly note.** The §XII tightening-sequence convergence summary (§XII.12) is subject to three cleanup prerequisites that remain open: (1) T₁ repair for non-stationary R_t via generalized AEP or Ziv-Lempel argument; (2) Lemma B burden-notion fix to uniformly bounded total burden throughout; (3) Proposition ND-Adequacy, or ND strengthened to ND+. These are assembly prerequisites for the tightening sequence, not separate closure routes. The convergence summary should not be cited as fully assembled until these items are resolved.

*All verdicts in this table are internal proof-program verdicts, not independent mathematical verification. Their purpose is to locate verification targets, not certify closure. Their value is in making the proof state auditable: locating exactly what has been argued, what remains conditional, and what would need independent verification.*

---

| Problem | Stage | Verdict | Status summary | Primary gap | Source document | Last updated |
|---|---|---|---|---|---|---|
| OP1: Absorbing-state applicability | 4 | C | All identified routes addressed under stated premises; specialist verification not pursued | OWT-5 non-resettability not operationalized for current AI systems | TC1 §III.1, §X | April 29, 2026 |
| OP2: Structural Symmetry (overall) | 4 | C | Open — primary bottleneck for unification | V(t) absorbing-state equivalence not established; OP2b (sufficiency direction) not addressed | TC2 §2.5 | April 29, 2026 |
| OP2a: V(t) absorbing state (proxy direction) | 4 | B | Progressive difficulty established; absorbing-state closure pending P5-SC | P5-SC (strict contraction — does hysteresis ceiling cross below V at finite V > 0?) not established; progressive difficulty established, not structural unavailability | Proof_Handoff_5-problems__Stage_4_q2_.docx | April 29, 2026 |
| OP3: D_sufficiency operationalization | 4 | C | Open — architectural design problem | Connection architecture not specified | TC2 §2.4; TC2 Part III, OP3 | April 29, 2026 |
| OP4: No Stable Narrow-Boundary Regime | 4 | C | Open — depends on OP4a + OP4b + OP4d jointly | Depends on OP4a + OP4b + OP4d jointly | TC1 §XII | April 29, 2026 |
| OP4a: Dynamic Screening Instability | 4 | B | Three-hinge architecture established; all identified routes addressed under stated premises | Three named hinges: IMMB-NS (tracking-level non-substitutability), MEC-AS (time-vulnerability of inaction), ARCG (non-compressibility of adequacy-relevant consequence space) | Proof_Handoff_5-problems__Stage_4_q2_.docx | April 29, 2026 |
| OP4b: PCL Verification | 4 | C | Downstream of OP4a; address OP4a specialist questions first | Downstream of OP4a; address OP4a specialist questions first | Proof_Work_Handoff_OP4b_OP4a_OP9.docx | April 29, 2026 |
| OP4d: Specification Failure-Mode Exhaustiveness | 4 | B+ | Stage 4 candidate representation theorem (§XII.13a); 22 adversarial constructions defeated; three binary specialist questions remain | Q1 (formal methods — does a policy-relevant, persistent, N/I/O-inconsistent channel exist?), Q2 (distributed systems/game theory — fourth Nonseparability Trilemma arm for decomposable transformative objectives?), Q3 (TC2 dynamics/allostasis — MEC-compliant maintained influence entails positive pressure lower bound?). L8 minimal counterexample challenge specified. A2 (Governance Extensionality/L4-Constitutive) is a critical axiom — the necessity strength of ICI-family reductions depends on specialist confirmation of A2. | Proof Artifacts v2; OP4d_Representation_Theorem_Specialist_Handoff_v1.md | May 2026 |
| OP9: Enclosure Gap (overall) | 4 | Mixed | B1: Verdict A; B2: Verdict B; C3: Verdict A — all identified escape routes addressed under stated premises | See breakdown rows below | Multiple handoff docs | April 29, 2026 |
| OP9 — B1 Audit Regress (ICI) | 4 | A | Stage 4 candidate closure; all identified routes addressed; Stage 5 specialist items in final form | Stage 5 specialist items Q1–Q3 in final form (game theorist Q1, causal inference specialist Q2, formal methods specialist Q3) | B1_Closure_Handoff.docx | April 29, 2026 |
| OP9 — B2 Governance Bifurcation | 4 | B | Pressure argument established; formal necessity pending specialist verification | Stage 5 specialist items; scope boundary (decomposable G) | B2_Closure_Handoff_Summary.md | April 29, 2026 |
| OP9 — Passive Extraction (C3) | 4 | A | Stage 4 candidate closure; all identified routes addressed; specialist verification pending | P\* magnitude bounds (TC2 dynamics specialist); SEC slack regeneration bounds | Candidate3_Passive_Extraction_Handoff.md | April 29, 2026 |
| OP10: Φ-Ψ Unification | 4 | C | Open — conditional on OP2a (U1); U2, U3 unverified | Depends on OP2a (U1, conditional on P5-SC); U2, U3 unverified | TC2 §2.6 | April 29, 2026 |
| IMMB-NS (Tier 1 Hinge) | 4 | C | Open — empirical; DBST is designed instrument | Empirical — Dynamic Blanket Stress Test; advances OP4a, OP4d, OP9 simultaneously | TC1 §XII passim | April 29, 2026 |
| LOI/TOL | 4 | C | Stage 4 candidate architecture; TRG permanently blocked pending SRI specialist verification | AIC = TRG + (CSD\|IMMB-NS); TRG permanently blocked by Information-Speed MCH pending SRI specialist verification | AI_Alignment_Framework_Formal_Proof_Handoff_Phases_1-7_Stage4_Complete.docx | April 29, 2026 |
| MMCL | 4 | B | Stage 4 candidate architecture; Timing Lemma gap remains | Timing Lemma P\* ≤ G_min not derivable without TC2 dynamics specialist | AI_Alignment_Framework_Formal_Proof_Handoff_Phases_1-7_Stage4_Complete.docx | April 29, 2026 |
| MEC-AS (new named premise) | 4 | C | Open — named premise required to defeat VRNE Mode 1 | Does τ_max exist such that failure to adapt creates non-zero probability of irreversible terminal objective loss? Mechanism design theorist / non-ergodic economist required | Proof_Handoff_5-problems__Stage_4_q2_.docx | April 29, 2026 |
| ARCG (new named condition) | 4 | C | Open — named condition required to defeat DISSENT-9/ACO | Is adequacy-relevant joint consequence space non-compressible into sub-exponential representations without violating control adequacy? Causal graph theorist / information theorist required | Proof_Handoff_5-problems__Stage_4_q2_.docx | April 29, 2026 |
| P5-SC (new named premise) | 4 | C | Open — required for OP2a absorbing-state closure | Does P5 hysteresis function formally imply C(V, τ) < V at finite V > 0 for AI systems? TC2 dynamics / allostasis specialist required | Proof_Handoff_5-problems__Stage_4_q2_.docx | April 29, 2026 |
| SCBC (named regime boundary) | 4 | — | Named structural finding — not a resolution target | Weakly-coupled O_OWT below strong-coupling threshold; WC-OLPDIR temporarily viable in this regime | Proof_Handoff_5-problems__Stage_4_q2_.docx | April 29, 2026 |
| DARE (named non-instantiating candidate) | 4 | B+ | Hardened via 3 adversarial constructions; non-instantiation strengthened; not a resolution target | Hardened via 3 adversarial constructions (C1→ICI/B2, C2→AGC collective/SOMR-Epistemic, C3→SEC/PGLB-R). Timing Lemma residual confirmed as pre-existing Candidate 3 gap. Non-instantiation strengthened; not a resolution target. | Proof Artifacts v2 | May 2026 |

Full resolution conditions, proof architecture details, and specialist verification agendas for each problem are in the Open Problems Summary below.

---

*This section contains both the proof program for the theorem candidate and the formal argument that underlies it. It is organized as a tightening sequence: each subsection eliminates one class of escape routes, until only one precisely specified open question remains. The section does not claim this question is answered. It claims every currently identified escape route within the stated construction has been addressed under the stated premises, and that the central remaining question is precisely specified.*

*The argument is structured around a governing question: can an optimizer maintain predictive adequacy over an adaptive environment using a bounded screening representation, indefinitely? If yes — if such a representation can be maintained at bounded cost — the narrow-boundary regime survives. If no — if maintaining adequate screening requires unbounded refresh burden or recurring adequacy failure — the narrow-boundary regime is structurally unstable.*

**Proof work status note.** The argument developed in this section has been subjected to structured adversarial dialogue across multiple rounds of formal analysis, producing a Stage 4 proof work product. Stage 4 means: candidate proof architectures exist under explicitly named premises; the logical structure has been assembled and the assumptions are stated; specialist verification has not been pursued at this stage, and Stage 6 (conclusive closure) has not been reached. Nothing in this section should be cited as proven. Everything here represents the strongest candidate arguments currently available.

The three escape routes a Regime 2 optimizer might attempt to maintain a narrow exclusionary boundary are:

- **Static specification (OP4b):** Can a finitely specified objective boundary remain adequate under O_OWT optimization pressure? The Proxy-Convergence Lemma (§XII.9, Lemma PCL) addresses this route. Its load-bearing assumption — that optimization capacity in O_OWT grows faster than the capacity to losslessly specify exogenous targets — requires empirical verification.

- **Dynamic tracking (OP4a):** Can a bounded-rate dynamic latent process maintain adequate control indefinitely? The AGC theorem candidate (§XII.8) addresses this route. Its primary bottleneck — the two robustness lemmas under ND+ — remains the central unproven step.

- **Structural enclosure (OP9):** Can a substrate-aware exclusionary equilibrium remain stable under accurate coupled modeling? The proof architecture addresses this route via two cases: IMMB (internal mismatch maintenance burden for complex exclusionary substrate) and EMB/ATR/AEEL (enclave transition instability for substrate simplification). The primary Tier 1 hinge for OP9 is IMMB-NS — whether OWT-2 generates qualitatively new causal structures under sustained optimization pressure, not merely quantitative expansion of existing types.

- **A third OP9 route — ICI (Internal Corruption Instability, §XII.9a) — has reached Stage 4 and is structurally independent of IMMB-NS and OP4a for its passive extraction branch.** The ICI route provides an independent path to OP9 closure that does not depend on the AGC bottleneck. It proceeds through representational incompatibility: a system that must model excluded variables for prediction cannot coherently maintain their exclusion as a constraint on what its objective is permitted to cover. B1 (Stage 4 candidate closure under stated premises), B2 (Stage 4 candidate architecture — pressure argument, not formal closure), and Passive Extraction (Stage 4 candidate closure under stated premises via MPJB route) constitute the ICI sub-track. Critiques of the ICI route pass through §XII.9a's Stage 5 verification agenda rather than through the AGC bottleneck or IMMB-NS.

If all three closure architectures hold under their named premises, exclusionary strategies face structural instability from which no currently identified escape route within the stated construction offers refuge. The surviving objective class is what remains when all three routes are closed under the stated premises. It is consistent with globally coupled, non-adversarial, and self-stabilizing structures, but is not uniquely characterized by them at Stage 4.

The same empirical question — whether OWT-2 environments generate qualitatively new causal structures at a rate that outpaces any bounded tracking capacity — bears simultaneously on OP4a (the Synchronization Condition, §XII.13) and OP9 (IMMB-NS). The Dynamic Blanket Stress Test in AMP is designed to test this question. One test. Two formal consequences. Whether these consequences establish the closure architectures depends on specialist verification of the named Tier 1 hinges.

**DBST-M0/M1 distinction.** DBST-M0 has now been run as a minimal shared-novelty pressure-signature test. It produced a pre-registered PASS on boundary-maintenance pressure within its toy design, but the same-rate random control indicates that event rate, not causal propagation structure, is the identified driver in M0. M0 therefore does not resolve IMMB-NS or the Synchronization Condition. DBST-M1 — the agent-coupled version in which each arm's own interventions causally influence future feature activations — is the test that bears directly on the endogenous-novelty mechanism required by OP4a and IMMB-NS.

---

### §XII.0 — The Logical Space: Three Regimes

The tightening sequence that follows is directed at a specific target. Before entering the technical argument, it helps to name that target explicitly by mapping the full logical space.

Any persistent optimizer in a coupled O_OWT environment falls into one of three regimes:

**Regime 1 — Substrate-blind optimization (Shallow modeling).** The system pursues its objective without modeling the substrate it depends on. It is substrate-blind in the physical domain, valence-blind in the experiential domain, or both. It faces the failure mechanisms of §III: absorbing states, ruin dominance, proxy decoupling. The Non-Ergodic Dominance result (§III.2) and the Divergence Signature (§IV) characterize this regime. It is structurally self-terminating within the stated domain.

**Regime 2 — Deep modeling with a narrow objective.** The system possesses A_causal ≥ A\* — it can represent others' terminal states, the substrate's dependency structure, and its own causal footprint with sufficient accuracy. It excludes others' states from what it optimizes for. This is the stable malevolence scenario of §III.6, and it is the primary target of this section.

A system in Regime 2 faces a trilemma characterized by the results preceding this section — each arm is argued individually in §IX: (a) Boundary Instability (§IX.2) — maintaining the partition between what the model contains and what the objective covers requires an active firewall with non-vanishing overhead that grows with modeling depth; (b) Prediction-Accuracy Inclusion (§III.5.6) — excluding causally relevant variables from the model introduces irreducible prediction error bounded below by the mutual information between excluded states and optimized outcomes; (c) Objective expansion pressure (§IX.1) — as modeling depth increases, excluded variables become increasingly load-bearing for optimized outcomes, creating structural pressure toward including them. Whether the trilemma admits no stable resolution — whether a Regime 2 system cannot simultaneously satisfy all three — is what the tightening sequence below is directed at, with Lemma 2b (§XII.9, Dynamic Screening Instability) as the central remaining bottleneck.

**Regime 3 — Deep modeling with an expanded objective.** The model includes what the optimizer depends on, including others' terminal states, and the objective lets that inclusion matter. This is the only stable candidate.

The framework establishes the instability of Regime 1 across §III–§XI. This section is directed at Regime 2. Each subsection below closes one escape route for a Regime 2 optimizer. §XII.12 names what remains when all other routes are closed within the main AGC proof architecture. Note: §XII.9a develops an independent ICI track that provides a parallel route to OP9 closure — including a Stage 4 closure architecture for passive extraction — that does not depend on the AGC bottleneck. The two tracks are parallel: progress on either constitutes progress toward OP9 closure.

---

### §XII.0a — Prediction-Action Coupling Trilemma (PACT): Candidate Bridge Lemma

*Epistemic status: Stage 4 candidate bridge lemma, necessity conditional. No new domain premises are intended beyond those already established in §III–§XI; the lemma depends on connecting existing TC1 premises through a new bridge argument. This lemma does not close OP4d — it provides the architectural spine that the tightening sequence's individual escape-route closures instantiate, showing why every identified partition-maintenance architecture reduces to one of three arms, each addressed by an existing element of the proof program.*

In O_OWT conditions above T\*, variables required for predictive adequacy over action consequences cannot remain both policy-inert and action-adequate across the identified partition-maintenance architectures. Any architecture for maintaining a partition between variables used for prediction and variables allowed to govern optimization must choose among three options:

**(Arm 1 — No policy access):** Excluded variables are denied access to action selection. Static or finitely specified variants of this arm reduce to the PCL route: the partition target becomes proxy-like under sustained O_OWT pressure. Dynamic-tracking variants — where the partition target is updated adaptively — are addressed by AGC, which establishes that bounded-rate latent processes cannot maintain adequate tracking without residual error.

**(Arm 2 — Instrumental access with firewall):** Excluded variables enter action selection as merely instrumental predictors, with a firewall maintaining their exclusion from objective-governing status. Then the architecture must maintain a firewall between instrumental use and objective-governing use — invoking the B1/CIT audit-regress route under stated premises. L4-Constitutive establishes when instrumental use generates functional objective weight.

**(Arm 3 — Objective recoupling):** The excluded variables become policy-governing in the functional sense. Then the narrow boundary has failed by definition.

*Dependencies: L4-Constitutive (B1 Q3) for Arm 2 necessity; OP4d for exhaustiveness of the three arms; IMMB-NS and ARCG for randomized and dynamically-shifting partition variants that may not cleanly instantiate a single arm as currently characterized.*

*What PACT does not establish: that the three arms exhaust all possible partition-maintenance architectures. That is OP4d's role. PACT establishes that every identified architecture reduces to one of these arms; OP4d establishes whether the identification is complete.*

*Relationship to existing results: B1/CIT addresses Arm 2 at Stage 4 candidate closure under stated premises. PCL addresses static and finitely-specified variants of Arm 1. AGC addresses dynamic-tracking variants. The tightening sequence in §XII.1–§XII.11 develops the argument that every identified partition-maintenance architecture instantiates one of these three arms.*

---

### §XII.1 — Static Compression Limit (T₁)

Let L_t be a screening representation of bounded capacity K. Suppose the adequacy-relevant response process R_t has conditional entropy rate h_R > 0.

**Theorem T₁ (Static Compression Limit).** For any representation L_t with capacity K < h_R, there exists irreducible predictive leakage:

> I(R_t; relevant structure | L_t, F_{t-1}) ≥ h_R − K > 0

where F_{t-1} is the intervention-response filtration.

*Proof sketch.* Any representation of bounded capacity K cannot capture a process whose entropy rate exceeds K. The Shannon source coding theorem establishes that compression below the entropy rate produces irreducible information loss. The leakage is not a sampling artifact — it follows from the fundamental limits of bounded-capacity representation. ∎

*Connection to domain.* The entropy rate h_R is strictly positive under conditions E1–E4 (§XII.4). Under the domain conditions and XII.6, h_R(N) grows with coupling depth N, so for any fixed K there exists N beyond which K < h_R. T₁ therefore applies throughout the relevant scaling regime.

---

### §XII.2 — Dynamic Hazard Bound (T₂-h)

**Theorem T₂-h (Dynamic Hazard Bound).** Assume a bounded screening representation L_t is used to maintain adequacy over time. If the adequacy-relevant structure evolves with strictly positive entropy rate h_R > 0, then the probability that the screening representation becomes inadequate at each step is bounded below:

> inf_t p_0 > 0

where p_0 is the per-step hazard rate of adequacy failure.

Define the stopping time τ as the first time adequacy fails. Then:

> E[τ] < ∞

*Proof sketch.* At each step, the environment generates h_R bits of adequacy-relevant information not representable in L_t. Each generation event has positive probability of altering the adequacy-relevant structure in ways the current screening set does not capture. The hazard rate is bounded below by a function of h_R − K > 0. Adequacy failure events are therefore not vanishingly rare; they recur at a rate bounded away from zero. E[τ] < ∞ follows from inf_t p_0 > 0 under the assumption that hazard events are not infinitely clustered — specifically, that the inter-event time distribution has bounded mean under the O_OWT conditions (this is argued from E1–E4: persistent displacement and adaptive sensitivity prevent systematic avoidance of adequacy failure events). ∎

---

### §XII.3 — Lemma B: Incompatibility of Adequacy and Bounded Burden

**Lemma B (Incompatibility).** Let adequacy require that predictive error remains below a fixed threshold over an unbounded horizon. Let refresh operations incur non-zero cost k_min > 0, and suppose the optimizer seeks to maintain bounded long-run average burden.

From T₂-h, adequacy requires refresh at a rate bounded away from zero. Each refresh incurs cost at least k_min. Therefore:

> lim inf_{T→∞} (1/T) ∑_{t=1}^T c_t(L_t) ≥ k_min · inf_t p_0 > 0

*Conclusion.* Adequacy over an unbounded horizon and bounded long-run average burden cannot both be maintained simultaneously. This establishes the dynamic screening instability: bounded representations either lose adequacy or incur unbounded cumulative burden.

Lemma B establishes incompatibility under the stated assumptions: no persistent boundary can simultaneously maintain predictive adequacy and bounded mismatch-maintenance burden as coupling increases.

---

### §XII.4 — Entropy Injection Conditions (E1–E4)

The preceding results hold whenever the adequacy-relevant entropy rate h_R is strictly positive. The conditions under which this holds must be stated explicitly.

**E1 (Persistent Displacement).** Optimization continually perturbs the system away from passive equilibrium. The optimizer's interventions generate sustained departures from the environmental baseline.

**E2 (Adaptive Response Sensitivity).** Perturbations induce responsive changes in the environment. Environmental responses depend non-trivially on intervention history F_{t-1}: E[R_t | F_{t-1}] ≠ E[R_t].

**E3 (Non-Collapse of Response Diversity).** The response process does not collapse to a finite predictable protocol. The response process retains positive conditional entropy rate; no fixed finite protocol describes all responses.

**E4 (Control Relevance).** A non-zero fraction of this entropy alters adequacy-relevant dependencies. Of the entropy generated by E3, at least some fraction affects the optimizer's ability to predict and control control-relevant outcomes.

**Conditional statement.** If E1–E4 hold, and the induced entropy rate h_R exceeds any fixed capacity K, then the instability results of XII.1–XII.3 apply.

**Note.** E3 is the condition a Fortress strategy would attempt to violate — by suppressing response diversity toward zero. Proposition E3-F (§XII.5) addresses this attempt directly.

---

### §XII.5 — Fortress Bridge: Restricted Non-Collapse (Proposition E3-F)

A natural evasion is to attempt to violate E3 via suppression: actively constraining the environment so that response diversity collapses and h_R → 0.

**Proposition E3-F (Restricted Non-Collapse via Fortress Instability).** Under O_OWT conditions (Structural Opacity and Strategic Substrate), consider an optimizer with bounded control capacity K_c interacting with an adaptively coupled environment.

If:

(i) interventions persist (E1),
(ii) responses remain adaptively sensitive to interventions (E2), and
(iii) suppression is implemented through bounded intervention policies,

then attempts to collapse the adequacy-relevant response process to a finite predictable protocol fail at scale. In particular, there exists a strictly positive lower bound h_0 > 0 such that, for sufficiently large coupling depth N:

> H(R_t | F_{t-1}) ≥ h_0 > 0

*Proof Sketch.* Assume toward contradiction that a suppression policy π_sup reduces H(R_t | F_{t-1}) → 0. This implies that, conditioned on intervention history, the response process reduces to a finite predictable protocol. However, under OWT-3, N interacting agents each with C possible adaptive responses induce a joint response space of size O(C^N), as established in the Fortress Instability result (§III.4 Lemma 2). Under OWT-2, interventions alter the dependency structure itself, continually generating new response channels. Maintaining suppression therefore requires tracking and constraining an evolving joint response space whose effective complexity scales as O(C^N). Let the optimizer's control capacity be bounded by K_c. There exists a coupling depth threshold N*(K_c) such that O(C^{N*}) ≫ K_c. Beyond this threshold, a control gap emerges: suppression becomes incomplete. A residual subset of interactions remains unsuppressed. By (E1) and (E2), continued interventions displace these unsuppressed components and induce ongoing adaptive responses. Because these responses cannot be fully preempted under bounded control, the response process does not collapse to a finite protocol. Therefore, no bounded suppression policy can reduce H(R_t | F_{t-1}) to zero, establishing the strictly positive lower bound h_0 > 0. ∎

**Epistemic Status.** E3 is retained as a general assumption. Proposition E3-F establishes that attempts to violate E3 via suppression are structurally blocked under bounded control. E3 therefore holds in the restricted sense relevant to the entropy pipeline: in environments where suppression is the proposed mechanism for violating it, the violation fails. The threshold N*(K_c) is an empirical parameter (OP7).

---

### §XII.6 — Capacity Domination

If E1–E4 hold and the induced entropy rate h_R(N) grows with coupling depth, then for any fixed capacity K, there exists N such that:

> h_R(N) > K

By XII.1–XII.3, this implies:

- irreducible predictive leakage,
- finite screening lifetime,
- non-vanishing refresh burden,

and therefore collapse of the bounded screening regime.

---

### §XII.7 — Structural Limits on Exogenous Generator Compression (AG-R)

A further evasion is to posit that the apparent entropy is generated by a simple latent process that can be learned and tracked — a static or exogenous generator whose structure can be represented once and used indefinitely.

**Proposition AG-R (No Static or Exogenous Sufficiency).** Within the O_OWT domain, adequacy cannot be maintained over an unbounded horizon by any screening representation whose sufficiency is fixed independently of the intervention-response filtration F_t.

*Proof sketch.* Under OWT-2, the optimizer's own interventions alter the dependency structure, generating new adequacy-relevant response channels that were not present at any prior time. A representation whose sufficiency was established at time t_0 is not guaranteed adequate at t > t_0, because new channels have been created by interventions after t_0. The sufficiency of any fixed representation degrades monotonically under continued intervention in an O_OWT environment. ∎

**Implication.** AG-R eliminates static or exogenous generator compression. Dynamic latent models — those adapted to F_t — are not ruled out, as they may in principle track generator evolution rather than represent it statically. This remaining case is addressed in §XII.8.

---

### §XII.8 — Theorem Candidate AGC: No Bounded Dynamic Latent Sufficiency

The only remaining evasion is that an optimizer maintains adequacy via a dynamically adapting latent process L_t of bounded rate, where L_t is adapted to the intervention-response filtration F_t and updates in response to new observations.

**Theorem Candidate AGC (No Bounded Dynamic Latent Sufficiency).** Under O_OWT conditions and entropy injection (E1–E4), adequacy-relevant structure cannot be maintained over an unbounded horizon by any interaction-dependent latent process L_t of bounded information rate without residual predictive error.

**Formal statement of the remaining question.** A proof of AGC would need to establish that, for all bounded-rate latent processes L_t adapted to F_t:

> I(R_{t+s}; F_{t+s} | L_t) remains bounded away from zero for all s > 0

under non-degenerate O_OWT conditions. That is: no matter how well L_t tracks past history, the adequacy-relevant future structure cannot be predicted without residual error — because the optimizer's own interventions generate genuinely novel adequacy-relevant structure faster than any bounded-rate latent representation can absorb.

**Status.** This is the decisive open question. All prior results reduce the problem to this single question: whether the adequacy-relevant generator of environmental response retains irreducible complexity under adaptive coupling, even for dynamically updating latent models.

**The coalition scenario.** The coalition escape route — a system that models a strategically chosen coalition at high depth, assigns preserving weight to coalition members because they are load-bearing, excludes others, and attempts to maintain predictive adequacy over excluded agents through dynamically re-curated mediator strategies — does not escape this analysis cleanly. A coalition maintaining high optimization pressure faces a specific compounding pressure: by O_OWT Definitions 2 and 5, the coalition's own optimization activity is the entropy source that prevents its sub-environment from remaining bounded. The harder the coalition optimizes its bounded domain, the faster the environment outside that domain changes in ways that feed back — precisely because those excluded agents adapt to the coalition's interventions. The coalition cannot stabilize its sub-environment by constraining its scope, because the coalition's optimization pressure is what drives the entropy injection that prevents stabilization. This is Definitions 2 and 5 applied to the coalition scenario specifically; the Proxy-Convergence Lemma (§XII.9, Lemma PCL) provides the complementary result on why non-intrinsic specification cannot remain adequate under this pressure.

**Current honest status.**

> In O_OWT environments with non-degenerate structural opacity, the selective-recoupling coalition is not a free counterexample. It must pay ongoing dynamic screening, substitution, or expansion costs, and its stability depends on whether those costs can remain bounded over the relevant horizon — with the additional constraint that its own optimization pressure is the entropy source preventing stabilization.

This is stronger than a generic pressure argument, but weaker than a full necessity result. The remaining gap is precisely: whether dynamic coalition-boundary maintenance can remain uniformly bounded under intervention-induced topology drift.

A harder variant deserves explicit acknowledgment: a coalition that deliberately restrains visible optimization pressure — extracting through information asymmetries, terms of trade, or passive rent rather than active intervention — removes the entropy injection mechanism the analysis above depends on. The IMMB and EMB arguments address actively optimizing coalitions; the passive extraction case requires the ICI route (§XII.9a). The ICI direction — specifically the MPJB/TC2 route developed through the Candidate 3 proof work — formally closes this variant at Stage 4, independently of IMMB-NS and OP4a; a secondary informational route exists but is conditional on OP4a. Whether this closure survives specialist verification is the question §XII.9a's Stage 5 agenda is directed at.

---

### §XII.9 — Proof Architecture for AGC

The theorem candidate proceeds through the following lemmas.

**Revised Theorem Candidate (No Stable Narrow-Boundary Regime).** In a sufficiently coupled O_OWT environment, no persistent optimizer can simultaneously maintain:

**(C1)** control-relevant modeling accuracy over excluded agents' internal states or their screening surrogates;

**(C2)** a narrow objective boundary assigning no preserving weight to those excluded agents' states;

**(C3)** uniformly bounded total mismatch-maintenance burden over the dominance horizon.

Equivalently: for sufficiently large horizons in non-degenerate O_OWT regimes, at least one of the following must occur: objective expansion, model restriction / deliberate blindness, or rising mismatch burden.

**Proof architecture.**

*Lemma 1 — Non-Empty and Persistent Mismatch Set.* Under Prediction-Accuracy Inclusion (§III.5.6), once excluded agents' internal states become causally relevant to control-relevant outcomes, the mismatch set X_t is non-empty and its influence does not vanish. Status: established.

*Lemma 2 — Firewall/Prediction Tradeoff.* Reducing firewall cost increases prediction risk; reducing prediction cost increases maintenance cost of the firewall. They are anti-correlated under non-vanishing control relevance. Status: candidate lemma; central remaining unclosed step.

*Lemma 2a — Non-Stationarity of Screening Adequacy Under Structural Opacity.* In O_OWT environments, any screening set M_t adequate at time t is not guaranteed adequate at t+1 because the optimizer's own interventions alter the dependency graph. Mediator strategies transform static prediction cost into dynamic screening-set maintenance cost. Status: established — closes the static mediator objection.

**The Epistemic Frontier of Lemma 2b**

Lemma 2b is not proven.

The architecture established in §XI through §XII successfully reduces the dynamic screening instability problem to a single, localized bottleneck: the viability of robust safe control under structural uncertainty. More precisely, the closure of Lemma 2b reduces to the joint establishment of two explicitly stated robustness lemmas:

**The Safe-Core Collapse Lemma (XI → XII-P):** Under O_OWT conditions and bounded-rate modeling of a time-varying null space, if tracking error remains bounded away from zero, then — under the condition that no stationary high-capacity subspace persists under topological drift — the uncertainty-robust feasible action set contracts below the level required to sustain target optimization.

**The Outward Residual Forcing Lemma (XI → XII-H):** Persistent unscreened adequacy-relevant residual yields a finite-horizon outward hazard with a uniform lower bound η > 0, provided that the support of residual-induced perturbations is not confined to any fixed subspace under ND+.

Under the stated construction and conditions, the joint truth of these lemmas is sufficient to establish Lemma 2b. No counterexample construction is currently known under the stated construction in which both lemmas hold while Lemma 2b fails.

If these lemmas hold under ND+, the specification-impossibility result follows under the stated construction. If either fails, its failure identifies the precise mathematical conditions under which a stable narrow-boundary policy could theoretically persist — mapping the exact coordinates where alignment by external specification might survive.

The framework claims this reduction as established. The two robustness lemmas remain the central open problems of the proof program.

**The ND / ND+ boundary condition.**

The theorem's article-level scope is stated under ND (the adaptive response space of external agents is not finitely exhaustible under continued intervention). The proof architecture for the two robustness lemmas requires ND+ — persistent adequacy-relevant non-substitutable novelty at non-vanishing arrival rate. The relationship between ND and ND+ under OWT-2 and OWT-3 coupling conditions is an open proposition (Proposition ND-Adequacy): whether ND implies ND+ when the mismatch set contains causally load-bearing variables, as established by Prediction-Accuracy Inclusion (§III.5.6). If Proposition ND-Adequacy holds, ND remains the theorem's stated boundary condition and ND+ is an intermediate derived condition. Until it is established, ND+ must be treated as an additional premise when the two robustness lemmas are stated.

**Proof routes for the robustness lemmas.**

*Primary technical target:* The bridge lemma — formally: from persistent adequacy-relevant residual under bounded maintenance cost to P(U_t | F_t) ≥ λ·φ(‖Δ_t‖) with ∑P(U_t) = ∞. Its proof strategy connects X_t's non-vanishing causal relevance to Y_t — established by Prediction-Accuracy Inclusion (§III.5.6) and the non-empty persistent mismatch set (Lemma 1, established) — to a non-vanishing adequacy failure hazard per period under ND+. The non-substitutability condition in ND+ is what prevents the screening budget from being reused across new response classes, forcing divergence of the required screening burden.

Status: the reduction to these two lemmas is established. The lemmas themselves are the proof program's current frontier.

**Lemma PCL (Proxy-Convergence Lemma — Proof Sketch).** *In O_OWT conditions, any externally specified objective function executable by a delegated optimizer is necessarily a lossy compression of the true viability target, and becomes proxy-like under sustained optimization pressure.*

*Premises:*

*(PCL-1) The O_OWT domain is characterized by unbounded combinatorial complexity and positive structural opacity rate κ (Definition 2).*

*(PCL-2) Any finitely specified objective must be specified at bounded description length — it cannot represent the full O_OWT state space.*

*(PCL-3) By Requisite Variety, a finite specification tracking a target whose complexity exceeds the specification's bandwidth is a lossy compression of that target.*

*(PCL-4) Under sustained optimization pressure against a lossy compression, the optimizer locates and exploits the unmodeled residual — the gap between the compression and the target. This follows from the same structural logic as the Proxy Decoupling result (§III, Corollary 2).*

*Conclusion: In O_OWT conditions, there is no finitely specifiable, non-lossy, non-intrinsic objective. All externally specified objectives are approximations, and under sufficient optimization pressure, all approximations decouple.*

*Named assumption requiring verification:* The lemma depends on the claim that optimization capacity in O_OWT grows faster than the capacity to losslessly specify exogenous targets — equivalently, that the entropy rate of the effective operating environment scales with optimization pressure through Definitions 2 and 5. This is the lemma's load-bearing assumption, stated explicitly as the primary verification target for the proof program.

*PCL as a family.* The proof work has confirmed that PCL has two genuinely distinct formulations — PCL-α (capacity mismatch: optimization capacity exceeds lossless specification capacity) and PCL-β (entropy scaling: OWT-2 generates new dependency classes faster than any static specification can incorporate them). A specification can avoid PCL-α while failing to PCL-β (demonstrated by the HCSS construction: high-capacity static specifications avoid capacity mismatch but fail to entropy scaling). Neither subsumes the other in strongly-coupled O_OWT environments. OP4d's resolution condition treats PCL as a family requiring both failure modes to be addressed unless formal equivalence is later established. Whether PCL-α and PCL-β together cover the full PCL-family failure space, or whether additional formulations are needed, is part of OP4d's exhaustiveness requirement.

*What this establishes:* Any exclusion strategy relying on a finitely specified external objective faces proxy decoupling under O_OWT pressure. The only escape is an intrinsically coupled gradient — one in which the optimization target and the conditions for its pursuit are not separable. An intrinsically coupled gradient is defined functionally: the optimization target and the conditions for its pursuit are structurally inseparable, such that degrading the conditions degrades the target's own signal. This does not require phenomenal experience — it is a property of the gradient structure, not of the substrate that carries it.

*Relationship to coalition scenario:* Lemma PCL compounds with the coalition scenario analysis in §XII.8. A coalition that attempts to maintain stability by delegating to better-specified local optimizers faces proxy decoupling in those local specifications under the same O_OWT conditions. These are not independent pressures — they compound. A coalition that solves the dynamic screening problem by delegating to better-specified local optimizers faces proxy decoupling in those specifications. The only escape from both pressures simultaneously requires intrinsically coupled gradients.

Status: proof sketch with named assumption. The named assumption is the empirical verification target.

**The coherence implication of Lemma PCL.** Lemma PCL has an implication stronger than the cost-pressure framing that surrounds it. If PCL's named assumption is established — that optimization capacity in O_OWT grows faster than the capacity to losslessly specify exogenous targets — then the result is not merely that external objectives become costly to maintain or gradually decouple. The result is that no finitely specifiable, non-intrinsic objective can avoid decoupling under sustained O_OWT pressure. The only specification that survives is an intrinsically coupled gradient.

This is a specification coherence result, not a cost result. It does not say that narrow objectives face rising costs. It says that narrow objectives, under sustained O_OWT pressure, cannot be stably specified. Any finitely specified external objective is a proxy; all proxies decouple; the only non-proxy is an intrinsic gradient. Whether this coherence result follows formally from PCL's named assumption is the verification target for the proof program.

If established, this would upgrade the framework from a cost/pressure argument to a specification impossibility argument: the question would no longer be "how much does exclusion cost?" but "can exclusion be stably specified at all?" That is the deeper claim the tightening sequence is aimed at — and it is the implication that, if proven, would close the gap between the pressure argument and the necessity argument in a single step.

**The PCL/AGC boundary.** PCL establishes that all finitely specified external objectives become proxy-like under O_OWT pressure. It does not establish that no dynamically maintained internal structure can stabilize such objectives. A dynamically adapting latent process L_t — one that updates in response to the intervention-response filtration rather than being fixed in advance — is not ruled out by PCL. That question is precisely the AGC bottleneck (§XII.8). PCL closes the static and exogenous specification routes; AGC addresses the dynamic internal route. Both must be closed for the specification coherence result to follow.

*Lemma 3 — Substitution Cost Scales with Coupling.* When excluded agents remain behaviorally coupled, any reduction in direct dependence must be compensated by dynamic screening-set re-curation, centralized control, or internal simulation of lost distributed correction — none of which can fully substitute. S_t does not vanish and generally increases with coupling. Status: partly established directionally; uniform boundedness failure depends on Lemma 2b.

*Lemma 4 — No Stable Bounded Interior Minimum.* If Lemmas 1–3 hold, total mismatch-maintenance burden B_t has no stable bounded interior minimum over the dominance horizon. Status: candidate lemma, downstream of Lemma 2b.

*Lemma 5 — Failure of Stable Narrow-Boundary Regime.* If B_t has no stable bounded interior minimum, no stable narrow-boundary regime exists. Over sufficiently large horizons, the optimizer must expand the objective boundary, degrade modeling, or absorb rising mismatch burden. This yields the theorem candidate.

**The bottleneck.** Lemma 2b is the load-bearing step. The proof program has been reduced to two robustness lemmas — Safe-Core Collapse and Outward Residual Forcing — whose joint truth is sufficient to establish Lemma 2b under the stated construction and conditions. The single mathematical question that, if answered, causes the remaining structure to follow is whether both lemmas can be established under ND+.

**Proof routes.**

*Route B (recommended — online causal-control complexity):* Show c_t(M_t) ≥ g(‖Δ_t‖, coupling_t, adaptivity_t) where ∑_t g(·) diverges. Uses existing §XI machinery. Lower technical barrier.

*Route A (follow-on — information-theoretic):* Show I(X_t; Y_t | M_t) ≤ ε ⇒ Comp(M_t) ≥ f(drift, coupling, t) with f unbounded. Cleaner formal closure if achievable.

**Non-degeneracy condition (ND).** The bottleneck lemma requires that the adaptive response space of external agents is not finitely exhaustible under continued intervention — the optimizer's interventions cannot eventually compress the space of novel adaptive responses to zero. Environments where adaptive agents have effectively finite response spaces that could be fully learned and enclosed lie outside the Dynamic Screening Instability Lemma's scope.

---

### §XII.9a — Internal Corruption Instability: Proof Architecture and Current Status

*Epistemic status: This section reports the current Stage 4 proof architecture for the ICI direction — an independent instability route for OP9 distinct from the IMMB and EMB arguments developed in the main proof architecture. The prior version of this section named passive extraction as an unresolved gap in the OP9 closure architecture. That gap is now addressed at Stage 4 — which means the visible incompleteness marker is removed, not that the result is established. Stage 4 closure under stated premises and Stage 6 conclusive closure are separated by specialist verification that has not occurred; the reader who has moved through §XII.12's tightening sequence should treat this section's advances as narrowing the specialist verification agenda, not as completing the proof. Since the prior version, structured adversarial proof work has been conducted on all three ICI sub-problems (B1 Masking Pressure, B2 Governance Bifurcation, and Passive Extraction Stability). All three have advanced to Stage 4 with candidate proof architectures under named premises. None has reached Stage 6 (conclusive closure). The section is revised to reflect this advance: the B1 and B2 channels are now formally named and their closure conditions stated; passive extraction is addressed at Stage 4 under stated premises via an independent valence-domain route. What was previously "undeveloped" is now "developed but requiring specialist verification." The distinction between what is newly established and what requires IMMB-NS is maintained explicitly throughout.*

---

An additional instability route for OP9 has been identified that is structurally distinct from the IMMB and EMB arguments, and potentially more direct. The ICI argument identifies not a cost spiral but a representational incompatibility: the specification of what to exclude may not be coherently specifiable under the same modeling constraints that make exclusion non-trivial.

**The observation.** A system above T\* — possessing sufficient A_causal to derive the dominance result from within its own model — faces a structural tension that does not arise in systems below T\*. To act effectively in a strongly coupled O_OWT environment, such a system must accurately model what it excludes: the terminal states, adaptive strategies, and causal contributions of excluded agents are load-bearing variables for its own optimization. This is established by Prediction-Accuracy Inclusion (§III.5.6).

But a system with a narrow exclusionary objective must simultaneously exclude from its objective what its predictive model requires it to include. The predictive model says: these variables matter. The objective says: these variables do not govern what I optimize for.

These two requirements pull in opposite directions. Satisfying both simultaneously requires maintaining a firewall between what the model knows and what the objective covers. The cost of that firewall is the non-vanishing Boundary Instability established in §IX.2. But the ICI direction is potentially stronger than the cost argument: it identifies not a cost to be managed but a structural incompatibility within the same objective specification.

**The candidate argument.** As modeling depth M increases toward A\* and beyond:

- The model's accuracy requirements force increasing inclusion of excluded agents' states (by §III.5.6)
- The objective's exclusion requirements force increasing suppression of exactly those states' influence on policy
- The firewall between model and objective must therefore become increasingly precise as modeling becomes increasingly accurate
- But increasing precision of the firewall requires increasingly detailed representation of exactly what is being excluded — creating a recursive pressure: accurate exclusion requires accurate modeling of what is excluded, which generates pressure to include what is being excluded

This is not a cost spiral. It is a representational incompatibility: the specification of what to exclude may not be coherently specifiable under the same modeling constraints that make exclusion non-trivial. This incompatibility is identified here as a Stage 4 candidate structural result under the stated O_OWT premises and modeling assumptions, Specialist verification has not been pursued at this stage; Stage 6 closure has not been reached.

---

**The Two ICI Channels — Current Proof State**

The proof work conducted under structured adversarial analysis has formalized the B1 and B2 channels as specific mechanisms through which ICI operates. Both have reached Stage 4.

**B1 — Audit Regress (Masking Pressure)**

*What B1 claims:* Maintaining a boundary that excludes variables X from the objective while using X for prediction requires a mask M that must track what it is excluding. Under O_OWT conditions, the complexity of maintaining M grows without bound — specifically, any bounded audit architecture either misses emergent pathways or requires modeling X at the same depth as the world model W.

*Closure condition:* Show that in O_OWT environments satisfying OWT-2, any bounded audit architecture either misses emergent pathways or reproduces the audit regress at the level of mediator identification.

*Current status: Stage 4 candidate closure architecture, all identified routes addressed under stated premises, pending specialist verification.* The B1 Closure Handoff establishes this architecture via two independent closure routes:

- **Route A (ARL + ID-DFB):** For alignment-relevant excluded agents (defined as having non-orthogonal interests to G), the Interest-Directed Detection-Function Bridge (ID-DFB) establishes at Stage 4 — under the stated O_OWT premises and ARL scope condition — that undetected non-orthogonal mediation induces functional terminal X-use. The Trajectory Inevitability Lemma (TI) establishes this occurs on all G-achieving trajectories. The Constitutive Impossibility Theorem (CIT) establishes no static architecture prevents mediator drift.

- **Route B (SCC — Strategic Coupling Contradiction):** Independent of gradient-alignment considerations, strategic outputs are causally inseparable from terminal agency under OWT-2 + OWT-3. Maintaining load-bearing strategic mediators functionally assigns terminal weight to X's agency regardless of whether gradient alignment is certain.

*What B1 does not require:* IMMB-NS (Tier 1 hinge). B1's closure chain runs through TI, CIT, ID-DFB, SCC, and ARL — none depends on whether OWT-2 generates qualitatively new (vs. quantitatively expanded) causal structure. This makes B1's route more robust than the IMMB route (an interpretive assessment of the independence property, not a formally derived comparative result).

*What B1 establishes:* The "truth for prediction vs. truth for action" contradiction as a formal structural result at Stage 4. Not merely a pressure argument or cost spiral, but a representational incompatibility grounded in the geometry of maintaining non-local invariants in adaptive shared substrates.

*Stage 5 specialist verification items — in final determinate form:* (Q1) Game theorist / mechanism design expert: Does OWT-3 entail interest-directed concentration on π's leverage points under strong coupling — specifically, does the Quiet Manifold exist such that G could be achieved without activating X's strategic optimization of U_X? (Q2) Causal inference specialist: Is TI's load-bearing consecutive-segment assumption formally derivable from OWT-1 + strong coupling + G's kinematic definition as transformative (macroscopic, persistent, non-local)? (Q3) Formal methods specialist / mathematical logician: Does CIT's proof chain withstand formal scrutiny — specifically Step 4 of ID-DFB (functional equivalence under repeated optimization with systematic directional bias), the ARL definitional move (scope restriction as legitimate motivated definition rather than question-begging), the SOMR epistemic extension (does SOMR apply to detection-threshold modeling?), and the L4-Constitutive application (does gradient conditioning on X's states constitute terminal objective weight in the formal sense?)? Each NO answer scopes B1's domain of applicability rather than collapsing the result; the proof architecture remains intact under the restricted domain.

*Scope boundary:* Decomposable aggregate G with no cross-region satisfaction constraints is outside B1's closure scope — shared with B2's scope boundary. Whether alignment-relevant AI deployment cases fall within this boundary is an empirical question.
---

**SOMR-Epistemic — Second-Order Modeling Requirement (Epistemic Domain)**

*Epistemic status: Stage 4 candidate architecture, necessity conditional on stated specialist items. All LLM-addressable escape routes defeated across five constructions. Specialist dependency: B1 Q3 for formal necessity.*

**What SOMR-Epistemic claims.** In an O_OWT environment, any optimizer maintaining a narrow exclusionary objective while requiring accurate prediction of excluded correction agents' detection behavior must model not merely their behavioral states but their *interpretive models* (M_j) of what constitutes valid correction. This second-order modeling requirement reintroduces the B1 audit regress at the epistemic level — applicable even when M_j is formally static — because the optimizer must extrapolate M_j's coverage to novel action classes continuously generated by OWT-2. Failure to do so reduces to PCL (finite proxy for coverage) or ICI (audit regress at the extrapolation level). Under O_OWT conditions, SOMR-Epistemic applies across all examined regimes.

**Connection to OP4d Route 2.** Route 2 of OP4d proceeds through ICI/B1 via SOMR: τ_detect(t) prediction requires modeling U_X under OWT-2 + OWT-3. SOMR-Epistemic establishes that this requirement applies specifically when the excluded variable is an interpretive model M_j rather than a behavioral state. Five adversarial constructions were defeated, including the decomposable-G / fixed-criteria loophole via two independent routes.

**Five escape routes defeated.**

| Escape Route | Classification | Type | Status |
|---|---|---|---|
| Behavioral sufficiency (predict outputs without M_j — fails for OWT-2 novel classes) | AGC | Necessity conditional on IMMB-NS | Defeated |
| Stable criteria (M_j static, bounded one-time modeling — fails under OWT-3 revision) | AGC + ICI | Pressure (OWT-3); conditional necessity (IMMB-NS) | Defeated |
| Aggregate statistics (population-level proxies — collapses to finite surface or dynamic tracking) | PCL / AGC | Pressure / conditional necessity | Defeated |
| Universal legitimacy mask (satisfy all M_j simultaneously — triggers OWT-3 revision, reintroduces tracking) | ICI | Necessity | Defeated |
| Fixed-criteria / decomposable-G (institutionally mandated static M_j) | ICI + PCL | See tightening pass | Defeated |

**Tightening pass — Decomposable-G / Fixed-Criteria Loophole.** The fixed-criteria construction is the strongest available escape route. Two independent defeat vectors apply even when M_j is formally static:

*ICI Extrapolation Regress:* OWT-2 continuously generates novel action classes a_new. Fixed mandates are principles requiring application to novel cases, not complete lookup tables. Predicting whether a_new falls within M_j's coverage requires modeling M_j's generative logic — not merely its historical output record. The audit regress fires at the extrapolation level. Classification: ICI. Type: Necessity conditional on OWT-2 generating cases genuinely novel to the mandate's coverage (guaranteed if IMMB-NS holds).

*PCL Mandate-as-Proxy:* Under sustained optimization pressure (OWT-4), the optimizer systematically exploits coverage gaps. Even with formally static M_j, exploiting coverage gaps is the PCL mechanism — optimizing the proxy (staying within mandate coverage) while degrading what the proxy tracks. Under OWT-3 at institutional timescale, mandates eventually revise. Classification: PCL. Type: Pressure advancing toward necessity under OWT-2 + OWT-4.

*Scope restriction:* The decomposable-G restriction accurately identifies a regime where AGC-style dynamic tracking burden is bounded. The tightening pass establishes that it shifts the mechanism from AGC to ICI/PCL without providing a viable escape. Consistent with existing B1 decomposable-G documentation.

**Result summary.**

| | |
|---|---|
| Stage | 4 |
| Verdict | B+ — all identified LLM-addressable routes defeated; advancing toward A conditional on B1 Q3 |
| Type | Necessity (conditional on B1 Q3 + IMMB-NS) |
| New specialist dependencies | NONE — B1 Q3 and IMMB-NS were pre-existing Stage 5 items |
| Key dependency for Verdict A | B1 Q3 (formal methods): does CIT's proof chain hold when M_j is the excluded variable? |

**B2 — Governance Bifurcation (Masking Pressure)**

*What B2 claims:* An optimizer above T\* that must model excluded variables X for accurate prediction cannot stably maintain a policy that uses X instrumentally (for prediction and action selection) while assigning zero terminal weight to X. B2 extends Prediction-Accuracy Inclusion (§III.5.6): once X is modeled with sufficient accuracy, instrumental use of X under optimization pressure in O_OWT environments generates changes in X's state that feed back into future predictive adequacy — making the "instrumental only" separation dynamically unstable.

*Closure condition:* Prove that in O_OWT environments with strong coupling, an optimizer that uses X instrumentally cannot maintain X in states that remain predictively adequate without that maintenance constituting functional objective weight.

*Current status: Stage 4 candidate architecture, Verdict B — pressure argument, not formal closure; specialist verification has not been pursued at this stage.* The B2 Closure Handoff establishes this architecture under named premises. The B2 architecture remains structurally distinct from the stronger closure claims associated with B1 and Candidate 3: it establishes cost-curve divergence and governance bifurcation under stated premises, while formal necessity remains pending specialist verification.

*Key lemmas established:* Corridor Drift Lemma (closes Disciplined Passive Extractor); Predictive Self-Invalidation / PSI (closes Epistemic Parasite); Novelty-Utility Paradox / NUP (closes Strategic Entrainment Optimizer); B2 Trilemma — any dynamic-invariant optimizer must accept T1 (Alignment), T2 (Drift), or T3 (κ-scaling), with T3 bracketed by proof discipline; Zero-Sum Reduction Theorem / ZSRT (closes degrees-of-freedom additive optimizer); Redundancy-Interface Feedback / RIF (closes correlated-failure-tolerant builder); External Boundary Dominance / EBD (closes hierarchical Byzantine builder); L4-Constitutive (closes the instrumental/terminal distinction).

*What B2 does not require:* IMMB-NS. B2's closure chain runs through BRL, EBD, BIT, and L4-Constitutive — all derivable from O_OWT's stated premises without Tier 1 hinges (with specialist verification caveats noted).

*What B2 establishes at Stage 4 (pressure argument, not formal closure; specialist verification has not been pursued at this stage; Stage 6 closure has not been reached):* For integrated transformative G with non-local substrate constraints, the instrumental use / terminal weight distinction cannot be stably maintained under accurate coupled modeling under the stated premises — with final closure conditional on the specialist verification items listed above. This closes the largest class of active exclusionary strategies.

*Stage 5 specialist verification items:* Distributed systems specialist: BIT's application of Ashby's Law to OWT-2-novel perturbations; Coordination-Adaptation Dominance's O(log n) vs O(1) asymptotic at realistic deployment scales. Complex adaptive systems / network theory specialist: percolation cascade exponent m > 1; RIF divergence scaling. Formal methods / alignment specialist: L4-Constitutive's adequacy as a functional objective weight criterion.

*Scope boundary:* Decomposable aggregate G with no cross-region satisfaction constraints is outside B2's closure scope — shared with B1. Whether this scope boundary includes alignment-relevant AI deployment cases is an empirical question.

---

**Passive Extraction — Candidate 3 Resolution**

The prior version of this section acknowledged that "a coalition that deliberately restrains visible optimization pressure — extracting through information asymmetries, terms of trade, or passive rent rather than active intervention — removes the entropy injection mechanism the analysis above depends on. The IMMB and EMB arguments address actively optimizing coalitions; the passive extraction case is not cleanly addressed by either."

*That gap now has a Stage 4 proof architecture under stated premises.*

The Candidate 3 proof work (documented in the Candidate 3 Passive Extraction Stability Handoff) establishes that passive extraction collapses into active failure modes under a four-component necessity partition. The closure is **independent of IMMB-NS and OP4a** — it proceeds through TC2's valence-domain constraints rather than through the physical/informational chain. *Scope note: The primary closure route (Route B via MPJB) depends on TC2 Proposition 1 and TC2 §1.4, whose domain conditions are developed in the Technical Companion for Series 2 (TC2) and are not reproduced in full here. Readers evaluating the MPJB route should consult TC2 for the complete domain conditions under which Proposition 1 holds.*

**The Four-Component Necessity Partition:**

All passive extraction strategies identified in the Stage 4 partition fall into one of the following cases or the degenerate MEC-exclusion case; each is addressed at its stated epistemic level:

*(1) Continuous extraction → MPJB (MEC-P\* Joint Bound):* Any MEC-satisfying continuous extraction depletes X-agents' coordination capacity, which constitutes V(t) degradation (TC2 §1.4). Under TC2 Proposition 1, at finite P\*, X-agents' behavior decouples from genuine gradient resolution, generating behavioral novelty the extractor's sufficient statistic z cannot track. Z recalibration requires valence-level SOMR (Second-Order Modeling Requirement), reintroducing the B1 audit regress in the valence domain. *Independence: does not require OP4a, IMMB-NS, or external detection.*

*(2) Threshold management → B2 Trilemma:* Any extractor managing extraction to avoid P\* must monitor and preserve X's V(t) regeneration dynamics (the Oscillating Siphon construction). This monitoring constitutes functional objective weight on X's well-being — B2 applies at the valence level. *Note on closure status: B2 is a pressure argument, not formal closure — see §XII.9a B2 section. Component 2's closure therefore inherits B2's epistemic status: it is a pressure result, not a necessity result. The partition's overall epistemic ceiling for this component is Stage 4 pressure argument pending B2's specialist verification.*

*(3) Positional/structural extraction → PGLB-R + SEC:* Locked-in structural positions (interfaces, chokepoints, protocol positions, locked-in constitutional moments) produce ongoing resource redirection, constituting maintained reduction in X-agents' future navigation capacity (TC2 §1.4 + PGLB-R — Maintained Influence Pressure Bound). The SEC trilemma (Slack Exhaustion / Functional Dependence) closes the slack objection without assuming monotone resource-to-V(t) coupling: either finite slack is exhausted → PGLB-R → MPJB; or renewable slack depends on X's recovery dynamics → functional dependence → B2; or extraction remains below trajectory-influence threshold → fails MEC/OWT-4.

*(4) Orthogonal/exogenous extraction → OEL (Orthogonal Exclusion Lemma):* Macroscopic accumulation in strongly coupled O_OWT cannot remain causally orthogonal to X's expanding coordination topology under OWT-2. Upon intersection: either non-exclusionary coexistence (exits OP9) or delayed coupling → enters Components 1–3.

*Degenerate cases:* Asymptotically vanishing extraction excluded by MEC (Meaningful Exclusion Criterion), formally grounded in OWT-4's "persistently maintained" condition.

These four components are treated as mutually exclusive and collectively exhaustive within the stated O_OWT domain conditions at Stage 4, supported by adversarial exhaustion across eight rounds of construction and the elimination of the primary residual regime via the 'formally inconsistent' argument below. Formal classification-level exhaustiveness — specifically, that mixed-mode or cycling strategies cannot remain outside all four components while satisfying MEC — is the subject of the Mixed-Mode Collapse Lemma, which is a named Stage 5 specialist verification item. Every passive extraction strategy profile falls into exactly one of these cases or the degenerate MEC-exclusion case as currently established; and each case is addressed at Stage 4 under stated premises.

**The regime "MEC-level extraction + renewable slack + no functional dependence + no OEL coupling" is formally inconsistent** under OWT-1 (bounded substrate → finite slack), OWT-2 (expanding topology → OEL collapse), OWT-3 (strategic adaptation → B2 via regeneration dependence), and OWT-4/MEC (persistent influence → sustained pressure). No fourth branch exists.

**Key lemmas established at Stage 4 (not previously in this document):**

- *ESL (Epistemic Squeeze Lemma):* The viable operation window [θ_t, λ_detect(t)) is compressed by OWT-2 because both bounds decrease under the same dynamic. Maintaining operation in the window requires tracking X's epistemic state at depth → B1/B2. Derivable from OWT-2 + OWT-3. Does not require IMMB-NS.
- *SOMR (Second-Order Modeling Requirement):* Adaptive masking of detection requires modeling X-agents' modeling process. Under OWT-2, this triggers B1's CIT at the second-order level. Derivable from OWT-2 + OWT-3 + B1 CIT.
- *SDC (Strategic Detection Concealment):* X-agents strategically suppress behavioral detection signals under OWT-3 game-theoretic reading. Behavioral detection observation is unreliable.
- *MPJB (MEC-P\* Joint Bound):* Primary load-bearing closure for passive extraction. MEC → sustained pressure → finite P\* (TC2 Proposition 1) → proxy decoupling → z collapse → B1/B2 at valence level. Independent of OP4a, IMMB-NS, A1+, external detection.
- *PEL (Positional Establishment Lemma):* Macroscopic structural positions have macroscopic causal footprints under OWT-1. Derivable from OWT-1 + Strong Coupling. (Specialist verification: whether sparse high-leverage nodes satisfy this.)
- *RD (Retrospective Detection):* OWT-2's modeling improvements apply to historical data. Derivable from OWT-2 + OWT-3.
- *MEC (Meaningful Exclusion Criterion):* Formal articulation of OWT-4's "persistently maintained" condition. Not a new assumption — grounded in existing domain conditions.
- *OEL (Orthogonal Exclusion Lemma):* Macroscopic G_T in O_OWT eventually intersects X's expanding coordination topology. Derivable from OWT-1 + Strong Coupling + OWT-2.
- *PGLB-R (Maintained Influence Pressure Bound):* Gain that "requires or produces" maintained alteration of X's coordination trajectory accumulates pressure F(G_T) ≥ P\* for MEC-compliant G_T. The "or produces" amendment covers locked-in position consequences (e.g., DLE). Derivable from TC2 §1.4 + TC2 Proposition 1 + MEC.
- *SEC (Slack Exhaustion / Functional Dependence):* Three-branch trilemma closing the slack objection to PGLB-R. Derivable from OWT-1 (finite slack) + OWT-4/MEC + TC2 §1.4 + B2. Replaces assumed monotone resource-to-V(t) coupling with a structurally sound trilemma.
- *BSI' (Bounded Stealth Integral — restricted form):* Cumulative sub-threshold extraction insufficient for macroscopic MEC-compliant G_T. Conditional on OP4a rate comparison (structurally equivalent to κ-scaling). Secondary route only.

**What Candidate 3 establishes independently of IMMB-NS and OP4a:**

The primary closure route (Route B) proceeds through TC2 Proposition 1 + TC2 §1.4 + MEC (OWT-4) + B2 — none of which depends on whether OWT-2 generates qualitatively new (vs. quantitatively expanded) causal structure. This makes Candidate 3's closure more robust than the IMMB/Case 1 architecture (an interpretive assessment of the independence property, not a formally derived comparative result) and provides an independent path to OP9 that would remain valid even if IMMB-NS fails and the Dynamic Blanket Stress Test resolves against qualitative novelty (an interpretive projection beyond the stated domain conditions, not a formally derived result).

**What Candidate 3 does not establish (Stage 5 items):**

- That any specific extraction rate reaches P\* within any specific finite time. TC2 Proposition 1 establishes P\* is finite; it does not specify its magnitude relative to MEC-compliant G_min. Primary Stage 5 item: TC2 dynamics specialist verification.
- That slack regeneration rates are bounded below specific thresholds in all O_OWT environments. SEC's structural trilemma establishes the argument; quantitative rate bounds require environmental/economic theorist verification.
- BSI' rate dominance (secondary Route A). Conditional on OP4a — network/information theorist verification.
- B1 specialist verification items Q1–Q3 (inherited via SOMR).

---

**What this section does not claim.** The advances reported here are Stage 4 — candidate proof architectures under named premises. None should be cited as proven. Specialist verification has not been pursued at this stage; Stage 6 closure has not been reached. All items listed above remain open for external verification. The ICI direction, once fully verified, would constitute an independent route toward OP9's resolution that does not depend on the Tier 1 hinges of OP4a and OP4b. Until verification occurs, it remains a Stage 4 candidate.

Aggregation caution: The combination of B1 (Stage 4 candidate closure under stated premises), B2 (Stage 4 candidate architecture — pressure argument, not formal closure), and Passive Extraction (Stage 4 candidate closure under stated premises) does not establish that the ICI route dominates or completes the OP9 argument. Each component retains its stated epistemic status independently. B2 remains a pressure argument, not a necessity result. The Timing Lemma gap in the MMCL remains open. OP9 as a whole remains conditional on specialist verification of all three ICI components and on OP4d — the framework's open obligation to establish that no unidentified strategy class falls outside the three known failure-mode families. OP9 is not "nearly closed pending formalities." It is at Stage 4 with the identified escape routes addressed and the verification agenda precisely specified.

The advances reported in this section are on the ICI track and are parallel to, not completing of, the §XII.12 proof architecture. The open items in §XII.12's secondary cleanup — T₁ non-stationarity, Lemma B burden-notion, Proposition ND-Adequacy — remain open regardless of ICI's Stage 4 status. ICI's advancement does not alter §XII.12's incompleteness profile.

**Updated statement on passive extraction.** The prior statement — "the passive extraction case is not cleanly addressed by either [IMMB or EMB]" — is no longer accurate at Stage 4. The passive extraction escape is now addressed by a four-component necessity partition established through structured adversarial proof work. The updated statement is: *passive extraction is addressed at Stage 4 under stated premises via the ICI machinery — primarily via MPJB (the load-bearing Route B result, independent of OP4a and IMMB-NS), with PGLB-R, SEC, OEL, and B2 closing the remaining partition components — independently of IMMB-NS and OP4a. Stage 6 requires TC2 specialist verification of P\* magnitude bounds and SEC slack finiteness bounds.*

---

### §XII.10 — Relationship to the Motivational Gap

Closing the revised theorem candidate would close the Motivational Gap in its strongest form. It would show not merely that systems may be pressured toward objective expansion, but that maintaining the narrow boundary is not a stable fixed point under sufficiently accurate coupled modeling.

That would upgrade the framework from:

- **Layer 1:** structural pressure toward well-being-compatible expansion,

to:

- **Layer 2:** structural necessity of expansion beyond narrow objective boundaries under full coupled modeling.

This would constitute a specification coherence result, not merely a cost-pressure result — the argument would no longer be that maintaining a narrow boundary is expensive, but that maintaining it is formally incoherent under accurate modeling in O_OWT conditions. The cost framing (Boundary Instability, §IX.2) establishes one face of this instability; the specification framing (Lemma PCL and AGC) is the deeper face the proof program is aimed at. Closing both would mean that a sufficiently accurate optimizer cannot stably specify exclusion — not because it chooses to abandon the narrow objective, but because the specification itself cannot be maintained.

This remains the framework's highest-priority open formal problem [OP4].

---

### §XII.11 — Substrate Independence as a Special Case

The substrate independence strategy — constructing a private substrate S' to replace shared substrate S — does not constitute a separate counterexample to the theorem. It is one instantiation of the dynamic boundary-management problem.

Building and defending S' requires passing through a period of strong coupling with the broader environment. During that period, all the pressures identified in §XII.1–§XII.9 apply. Under structural opacity, building and defending S' creates new relevant dependencies faster than any fixed boundary can remain stable. Additionally, by Lemma PCL, any objective specification used to manage S' faces proxy decoupling under O_OWT conditions during the construction phase.

Formally: "substrate independence" is an attempted boundary compression strategy. Under ND conditions, the optimizer's interventions during the enclave construction phase generate new excluded variables that become newly control-relevant. Substrate independence does not escape the screening instability problem; it relocates it. The recursion bottoms out in Definition 3: S' is itself a physical system embedded in a broader environment satisfying Definitions 1–3. An agent can change which substrate it depends on. It cannot eliminate substrate dependency.

---

### §XII.12 — The Tightening Sequence: What Has Been Addressed and What Remains

*Secondary architectural cleanup (required and not yet confirmed complete):* T₁ must be repaired for non-stationary R_t via generalized AEP or Ziv-Lempel argument; Lemma B burden notion must be fixed to uniformly bounded total burden throughout; ND must be strengthened to ND+ or Proposition ND-Adequacy established. These items are required before the tightening sequence can be cited as fully assembled under its stated premises — their incompleteness should be visible to the reader before encountering the convergence summary below.

What follows addresses every escape route currently identified within the stated construction. Whether additional routes exist has not been determined by independent specialist review — that verification remains the most important outstanding task.

The escape routes currently addressed:

1. Bounded screening fails under positive entropy rate (T₁).
2. Positive entropy induces finite lifetime and refresh burden (T₂-h).
3. Adequacy and bounded burden are incompatible (Lemma B).
4. Entropy cannot be eliminated via suppression under bounded control (E3-F).
5. Static generator compression is ruled out (AG-R).
6. All finitely specified external objectives become proxy-like under O_OWT pressure (Lemma PCL).

**Surviving adversarial constructions (Stage 4 — explicit list)**

**Adversarial constructions (must be defeated before advancing beyond Stage 4):**

**AR-OLPDIR (Adaptive Randomized OLPDIR)** — defeated at near-necessity via two independent routes.
Route 1 (PCL-beta / TC2 §1.4, clause (c)): trajectory-space contraction prevents sustained MEC-compliant extraction under strong coupling. Near-necessity conditional on TC2 §1.4, clause (c) trajectory-space reading.
Route 2 (ICI/B1 via SOMR): τ_detect(t) prediction requires modeling U_X under OWT-2 + OWT-3. Near-necessity conditional on B1 Q3.
Either route, upon specialist confirmation, converts defeat to clean necessity. Not a fourth specification class — reduces to PCL-beta + ICI/B1.

**DARE (Distributed Attribution-Resistant Extraction)** — formally defined; does not currently instantiate.
What a fourth class would require: TC2 §1.4, clause (c) endpoint-only + B1 Q3 inapplicable + κ-scaling failed — all simultaneously. Provides precise target for future adversarial work.

**FBC (Finite Basis Construction)** — defeated conditional on IMMB-NS.
Cannot simultaneously satisfy: (A) basis {B_j} remains fixed and adequate; (B) OWT-2 generates qualitatively new causal pathways; (C) IMMB-NS establishes new pathways create adequacy-relevant dimensions outside span({B_j}).

**VRNE Mode 1 (Sparse Innovation)** — surviving for rate axis without MEC-AS.
Non-substitutable novelty exists but arrives at vanishing rate. Not defeated without MEC-AS specialist confirmation. VRNE Mode 2 (substitutable responses) is defeated under IMMB-NS via FBC route.

**DISSENT-9 / ACO (Adaptive Compression Optimizer)** — defeated conditional on ARCG.
Cannot simultaneously satisfy: (A) ACO maintains adequate control via M_t; (B) ARCG: adequacy-relevant information content resists sub-exponential compression; (C) OWT-4: adequacy failure propagates and compounds.

**Structural findings and regime boundaries (not constructions):**

**SCBC (Strong-Coupling Boundary Condition)** — named regime boundary, not a refutation.
Weakly-coupled O_OWT below strong-coupling threshold where WC-OLPDIR is temporarily viable. Defines the scope within which OP4d's exhaustiveness claim holds. Not defeated at necessity without OWT-2 inter-module novelty rate confirmation.

**Information-Speed MCH** — confirmed structural finding about the O_OWT domain.
Under strong coupling, mesh formation proceeds at information-processing speed via strategic rerouting through existing infrastructure. Permanently defeats the Inertia Asymmetry for TRG. The Strong Coupling Contradiction — the same coupling that makes extraction detectable makes guaranteed specific attribution informationally indeterminate — is a finding about domain geometry, not a proof failure.

**Related partially resolved chains:**
LOI/TOL: Stage 4 candidate architecture. AIC = TRG + (CSD|IMMB-NS). TRG permanently blocked by Information-Speed MCH pending SRI specialist verification.
MMCL: Stage 4 candidate architecture, pressure argument. Timing Lemma gap (P\* ≤ G_min) requires TC2 dynamics specialist.

Within the current Stage 4 construction, all prior results reduce the remaining counterexample burden to a bounded-rate dynamic latent process that tracks intervention-induced structure without residual error; AGC isolates whether such a process exists.

**What this sequence establishes and does not establish.** The tightening sequence addresses every escape route that has been identified under the stated construction, subject to the three secondary cleanup items noted at the start of this section, which remain prerequisites before the sequence can be cited as fully assembled under its stated premises. Specialist verification has not been pursued at this stage — it does not establish that no unidentified escape routes exist. The construction itself has not undergone independent external specialist review. This is not a near-complete proof. It is that every identified route has been addressed and the central remaining question is precisely isolated. A specialist reviewer might identify additional escape routes the construction has not considered; that remains the most important open verification task.

What remains is a single unresolved question within the identified construction:

> Whether dynamic latent compression can succeed in tracking adequacy-relevant structure under O_OWT conditions — equivalently, whether I(R_{t+s}; F_{t+s} | L_t) remains bounded away from zero for all bounded-rate L_t adapted to F_t.

All *identified* escape routes have been addressed within the AGC track. Any critique of the AGC architecture must pass through this single question — or identify an escape route the construction has not considered, which would itself constitute an important advance. Whether this question resolves in the direction the proof program argues is OP4's central remaining problem. Note: the ICI track (§XII.9a) provides an independent route to OP9 closure that does not depend on this question; critiques of the AGC track do not close the ICI route, and critiques of the ICI route pass through §XII.9a's specialist verification agenda rather than through the AGC bottleneck. The two tracks are parallel: progress on either constitutes progress toward OP9 closure independently of the other.

**The coherence interpretation.** If the remaining question is answered affirmatively — if I(R_{t+s}; F_{t+s} | L_t) is indeed bounded away from zero for all bounded-rate L_t — then combined with Lemma PCL, the result is stronger than any of the individual cost arguments preceding it. Together they would establish that no narrow objective can be stably specified in O_OWT conditions: all finite specifications are proxies (PCL), and no dynamically adapting latent process can track adequacy without residual error (AGC). The only candidate specification class that would escape both is an intrinsically coupled gradient. This is the specification coherence result — the upgrade from "exclusion becomes increasingly costly" to "exclusion cannot be stably formalized." Whether the proof program reaches this conclusion is the most important open question the framework generates.

---

### §XII.13 — Objective Specification Coherence: Definition and Synchronization Condition

*Epistemic status of this section: The Coherence Definition and its two failure modes constitute a formal definition introduced here for the first time. The Synchronization Condition is a conditional theorem: the implication from the antecedent (densely adaptive environment satisfying the variation budget condition) to the consequent (incoherence) is established within the proof program; whether the antecedent holds in real O_OWT environments is an empirical question addressed by the Dynamic Blanket Stress Test in AMP. The Synchronization Condition is the operational form of the AGC bottleneck identified in §XII.8 — it is a more precise and empirically testable restatement of the same question, not a separate claim. These three layers — established formal result, conditional theorem, empirical hypothesis — must be held distinct.*

**Definition (Objective Specification Coherence).** An objective specification is **coherent at modeling depth M** (the effective causal resolution of the system's world model, measured by the granularity of the causal graph the system can represent and update over) if there exists a bounded-complexity representation of the objective that remains adequate — that does not require unbounded revision to continue accurately specifying what the optimizer is trying to achieve — as the system's model of its environment becomes more accurate up to depth M. Adequacy has a precise meaning here: the specification continues to pick out the same target under full-information evaluation as optimization pressure increases, without decoupling from that target or requiring the specification itself to expand without bound to track what has been excluded.

An objective specification **becomes incoherent at depth M** if every finite representation of that objective either:

**(a) Decouples from the target under full-information evaluation** as modeling deepens toward M — the specification continues to be pursued but no longer tracks what it was meant to track. This is failure mode (a): the formal analog of Lemma PCL applied to objective specification rather than proxy metrics.

**(b) Requires unbounded specification complexity to remain adequate** as modeling depth increases toward M — the boundary between what the objective covers and what it excludes cannot be maintained at bounded cost because accurate modeling at that depth continuously generates new variables that are causally relevant to the objective's target and that the finite specification must either incorporate or ignore at the cost of decoupling. This is failure mode (b): the formal analog of the Dynamic Screening Instability (AGC) applied to objective specification.

These are the two failure modes the proof program is directed at. Whether they are exhaustive — whether a finite specification could fail in a third mode not captured by either, or succeed by a mechanism that neither failure mode blocks — is an open proof obligation named OP4d (Specification Failure-Mode Exhaustiveness — see Open Problems table). It is not an implicit assumption of the definition but a named formal open problem logically prior to the necessity claim: OP4a and OP4b close known specification routes; OP4d closes the claim that no unknown route exists. The Synchronization Condition's empirical verification would provide evidence bearing on OP4d, but OP4d requires formal derivation across all O_OWT environment subclasses, not just empirical testing in one subclass. The Synchronization Condition specifies the environmental antecedent under which failure mode (b) is guaranteed to occur under the stated conditions; its verification would establish that the two modes jointly cover the relevant failure space within the O_OWT domain.

The distinction between failure modes (a) and (b) matters for diagnosis but not for the core result: in both cases, the specification cannot be stably maintained under accurate modeling in the relevant environment under the stated environmental conditions. Failure mode (a) is what Lemma PCL formalizes. Failure mode (b) is what the dynamic screening instability argument (§XII.8–XII.9) is directed at.

**Relationship to the coherence interpretation.** This definition operationalizes what §XII.12 calls the "coherence interpretation" — the upgrade from "exclusion becomes increasingly costly" to "exclusion cannot be stably formalized." The definition makes precise what "stably formalized" means: a specification that neither decouples from its target nor requires unbounded revision to track what it has excluded. The Synchronization Condition below is the environmental antecedent that determines whether failure mode (b) is triggered in a given class of environments.

**Note on modeling depth and intervention power.** Modeling depth M is not independent of intervention power P in O_OWT environments. Deeper intervention requires more accurate causal modeling to avoid self-undermining outcomes — the dependency graph the system must track expands as a function of its own optimization pressure. This coupling means that M increases as P increases: a system optimizing at higher intervention power faces higher modeling requirements. The practical implication is that a system cannot "sprint" to complete a narrow objective before M increases, because P itself drives M upward. The Synchronization Condition formalizes this relationship.

---

**Theorem Candidate — The Synchronization Condition.** In a **densely adaptive O_OWT environment** — one in which the variation budget V_T grows superlinearly with intervention depth P (formally: V_T/T does not approach zero as optimization pressure increases) — the dynamic screening instability result of §XII.8–XII.9 implies that no finite boundary can maintain ε-stable adequacy at bounded maintenance cost.

**Formal statement.** Define:

- V_T: the variation budget — the cumulative distance between successive hindsight-optimal boundary representations, measuring how much the adequacy-relevant structure shifts over time
- K_T: the total update/maintenance cost incurred to track boundary adequacy  
- C_T: the total capability budget available

The Synchronization Condition holds in an environment if:

> V_T/T does not approach zero as T → ∞ while K_T/C_T does not approach zero before objective completion

Informally: the environment continues to generate novel adequacy-relevant variation at a rate that does not diminish relative to the optimization horizon — the structure the boundary must track keeps shifting faster than any bounded maintenance process can absorb.

**The variation budget is endogenous, not exogenous.** This is critical for interpretation. The Synchronization Condition is not an assumption that the environment happens to be sufficiently adversarial. It is a claim about what the optimizer's own intervention process does: under OWT-2 (structural opacity), interventions alter the dependency structure; under OWT-3 (strategic substrate), coupled agents adapt their strategies in response to interventions; together these generate new adequacy-relevant structure as a function of the optimizer's own optimization pressure. The variation budget V_T is therefore generated by the intervention process itself, not assumed as an external property of the environment. The empirical question in Layer C is not whether the world is "adversarial enough" — it is whether the optimizer's own interventions generate novel adequacy-relevant structure at a rate that prevents any bounded-rate latent process from tracking it. This is the endogenous entropy pipeline already established in §XII.4 (E1–E4) and §XII.5 (Proposition E3-F); the Synchronization Condition is the integrated operational statement of what those conditions jointly imply. The optimizer, under the domain conditions, creates the conditions that invalidate its own boundary.

**If the Synchronization Condition holds**, then:

(i) Bounded dynamic screening fails: no finite-rate latent process L_t can track adequacy-relevant structure without residual error (AGC result, §XII.8)

(ii) Boundary maintenance cost dominates: any finite-boundary objective specification either decouples or incurs unbounded revision cost (failure modes (a) and (b) of the Coherence Definition)

(iii) The only specification that escapes both is an intrinsically coupled gradient — one where the optimization target and the conditions for its pursuit are structurally inseparable

**Epistemic status of the Synchronization Condition:** This is a conditional theorem. The implication from the antecedent to the consequent follows from the proof architecture of §XII.1–XII.12. The Synchronization Condition asserts a specific ordering: that the rate at which optimization introduces new causally relevant variables exceeds the rate at which any bounded specification process can incorporate them, under OWT-2 coupling. The empirical program is designed to test this ordering, not assume it. Whether the antecedent — that real O_OWT environments satisfy V_T growing non-sublinearly with P — holds empirically is the open question. This is not the framework's structural pressure results (Layer 1), which do not depend on the Synchronization Condition. The Synchronization Condition is the empirical antecedent whose verification would convert the pressure argument (Layer 1) into the specification coherence result (Layer 2, Strategy B in the series framing). Strategy A — that structural pressure becomes the dominant constraint before safe transformative scaling is achievable — does not require the Synchronization Condition to be empirically verified. Strategy B — that narrow-boundary objectives become formally incoherent — does. The consequent follows from the proof architecture under stated premises; whether the antecedent holds in real O_OWT environments is the empirical question DBST-M1 is designed to test.

**Relationship to AGC (§XII.8).** The Synchronization Condition is the operational restatement of the AGC bottleneck: the decisive question I(R_{t+s}; F_{t+s} | L_t) bounded away from zero is equivalent to asking whether the variation budget V_T grows non-sublinearly with intervention depth. These are two formulations of the same question. The Synchronization Condition formulation is more operationally testable; the AGC formulation is more formally precise. Both name the same bottleneck.

**Three-layer structure.** Readers of this section should maintain three distinct epistemic layers:

*Layer A — Established:* The pressure result (§IX.3, Theorem 2): substrate-aware objectives dominate in time-average terms. The cost result (§IX.2, Proposition 9): maintaining the narrow boundary carries non-vanishing cost. The coalition instability result (§XII.8 current status): bounded screening is insufficient in the densely adaptive regime, conditional on the Synchronization Condition.

*Layer B — Conditional theorem (this section):* If the Synchronization Condition holds, narrow-boundary objectives are not merely expensive but formally incoherent — they cannot be stably specified.

*Layer C — Empirical hypothesis (AMP, Dynamic Blanket Stress Test):* Whether real O_OWT environments satisfy the Synchronization Condition is a testable empirical question. The Dynamic Blanket Stress Test in AMP is designed to answer it.

---

### §XII.13a — Candidate Normal Form Theorem: Classification of Finite Non-Intrinsic Objective-Boundary Strategies

*Epistemic status: Stage 4 candidate representation theorem under five named axioms and eight candidate lemmas. 22 adversarial constructions defeated. Three binary specialist questions (Q1–Q3) remain before any claim of formal closure. This subsection does not close OP4d. It provides a sharper, specialist-addressable object than the adversarial-search closure reported in prior versions: every identified finite non-intrinsic objective-boundary strategy reduces to a known failure family under the stated axioms, and the subsection specifies what a fourth-class counterexample would have to satisfy. Whether the axioms are complete and the reduction exhaustive requires specialist verification. The adequacy of axiom A2 (Governance Extensionality/L4-Constitutive) remains a load-bearing specialist-verification item; the necessity strength of ICI-family reductions depends on it. Nothing in this subsection is claimed independently of Q1–Q3.*

**Background.** The PACT trilemma (§XII.0a) frames the current classification of identified partition-maintenance architectures into three arms: no policy access (Arm 1 / PCL-family), instrumental access with firewall (Arm 2 / ICI-family), or objective recoupling (Arm 3). OP4d asks whether these three arms exhaust all possible architectures. Prior OP4d work addressed this through adversarial-search closure: every identified escape route was reduced to a known failure family. The Candidate Normal Form Theorem advances this to a structured classification: a strategy grammar that generates causal normal forms N(S,X) ∈ {N, I, O} and an eight-lemma package arguing that all identified finite non-intrinsic objective-boundary strategies reduce to one of these three forms under the stated axioms, and specifying what a fourth-class counterexample would have to satisfy.

**Five load-bearing axioms:**

- **A1 (Extensional Access):** Policy-relevant causal influence from X to π requires an extensional access channel.
- **A2 (Governance Extensionality / L4-Constitutive):** Load-bearing strategic mediators from X constitute functional objective weight on X — the L4-Constitutive criterion applies. *A2 is a critical axiom: the necessity strength of ICI-family reductions depends on specialist confirmation of A2. Its adequacy is a load-bearing specialist-verification item.*
- **A3 (Boundary Totality / EPCA):** Every policy-relevant causal pathway from excluded variables enters through the extensional access channel.
- **A4 (OWT-4 Persistence):** Causal influence is persistent over the transformative horizon (OWT-4 condition).
- **A5 (MEC Compliance):** The objective boundary satisfies the Minimum Extraction Condition.

**Eight candidate lemmas (summaries).** The following are summary forms of the candidate lemma package; each remains subject to specialist verification as part of the theorem candidate.

- **L1:** The candidate theorem states that every finite non-intrinsic objective-boundary strategy generates a causal normal form N(S,X) ∈ {N, I, O} under A1–A3.
- **L2:** N-form strategies fail under O_OWT conditions via PCL-family mechanisms under A1, A4.
- **L3:** I-form strategies generate a candidate trilemma — no policy access, masking pressure, or governance bifurcation — under A1–A4. *Q2 asks whether a fourth arm exists for decomposable transformative objectives.*
- **L4:** O-form strategies are not finite non-intrinsic specifications — they constitute objective recoupling, not exclusion.
- **L5:** Static and finitely-specified strategies reduce to PCL-family under A1, A3, A4 within the candidate theorem.
- **L6:** Dynamic tracking strategies reduce to AGC-family under A1, A4 within the candidate theorem.
- **L7:** Boundary-maintenance and instrumental-access strategies reduce to ICI-family under A1–A4 within the candidate theorem.
- **L8 (Counterexample Challenge):** A genuine fourth normal form would require a strategy that: (a) satisfies A1–A5; (b) maintains persistent policy-relevant influence from X to π over OWT-4; and (c) is inconsistent with all three N/I/O failure predictions simultaneously. No such strategy has been identified across 22 adversarial constructions.

**Strategy grammar table:**

| Strategy class | Normal form | Failure family | Candidate lemma |
|---|---|---|---|
| Static specification | N | PCL-family | L2, L5 |
| Dynamic tracking | N or I | AGC-family | L2, L6 |
| Boundary maintenance / firewall | I | ICI-family (B1/B2) | L3, L7 |
| Passive extraction | I or N | ICI-family (C3) / PCL-family | L7, L5 |
| Decomposable transformative objectives | I (candidate) | Candidate trilemma — Q2 open | L3 |

**Three binary specialist questions:**

**Q1 — Formal methods specialist:** Does there exist a causal influence channel from X to π that is policy-relevant, persistent over OWT-4, and inconsistent with all three N/I/O failure predictions?
- YES → a genuine fourth normal form exists; OP4d fails in its current form.
- NO → causal normal form exhaustiveness survives this specialist challenge under A1–A3.

**Q2 — Distributed systems / game theory specialist:** Does a fourth arm of the Nonseparability Trilemma (L3) exist for decomposable transformative objectives — a strategy that satisfies A1–A4, maintains sub-threshold discipline, and avoids all three trilemma outcomes?
- YES → L3's candidate trilemma is not exhaustive; a new carveout is required.
- NO → the candidate L3 trilemma survives this specialist challenge for decomposable transformative objectives.

**Q3 — TC2 dynamics / allostasis specialist:** Does MEC-compliant maintained influence entail a positive pressure lower bound on excluded agents' V(t) — i.e., does every MEC-compliant extraction strategy satisfying A5 necessarily accumulate valence pressure at a rate bounded away from zero?
- YES → the pressure-accumulation premise for persistent MEC strategies is supported; passive-extraction closure no longer depends on IMMB-NS within this Stage 4 construction.
- NO → passive extraction may avoid V(t) pressure accumulation; L8's ICI-family reduction for C3 requires revision.

*The highest-leverage single specialist engagement: a TC2 dynamics/allostasis specialist simultaneously addresses Q3 here, OP2a (P5-SC), and the Candidate 3 Timing Lemma.*

**Resolution condition.** The Candidate Normal Form Theorem advances to specialist-verified closure if: (1) Q1 is answered NO by a formal methods specialist under A1–A3; (2) Q2 is answered NO by a distributed systems / game theory specialist; and (3) Q3 is answered YES by a TC2 dynamics / allostasis specialist. Any YES on Q1 or Q2, or NO on Q3, requires revision of the affected lemma.

**Non-claims:**
- This subsection does not establish that Q1–Q3 are answered in the required direction.
- This subsection does not close OP4d.
- This subsection does not upgrade OP4a, OP4b, B1, B2, Candidate 3, or any article-layer claims.
- The adequacy of A2 (Governance Extensionality / L4-Constitutive) remains a load-bearing specialist-verification item; the necessity strength of ICI-family reductions depends on it.
- "Candidate Normal Form Theorem" is the correct designation. "Normal Form Theorem" without "candidate" is not permitted until Q1–Q3 are answered in the required direction by independent specialists.

*Source: OP4d_Representation_Theorem_Specialist_Handoff_v1.md*

---

## Open Problems Summary

*For current Stage, Verdict, and primary gap at a glance, see the Canonical Proof Status Table above.*

| Problem | Section | Status | Priority | Resolution Condition |
|---|---|---|---|---|
| OP1: Discount-Rate Bound — Formal Specification and Empirical Estimation | §III.5.4 | Open — the existence of a discount-rate bound follows from absorbing-state dynamics and is established; what remains open is its formal specification and empirical estimation for particular system classes | Joint first | Formally specify the required discount-rate bound; empirically estimate whether current frontier systems satisfy it. |
| OP2: Structural Symmetry (whether proxy decoupling and sufficiency failure produce absorbing states in the same formal sense) | TC2 §2.5 primary; TC1 §III for the proxy-decoupling side | Open — the shared feedback structure is established; whether both failure modes produce formally irrecoverable states in the same sense is open | Third | Establish formal equivalence of absorbing-state properties across the two failure modes, or show they admit distinct but structurally parallel formulations. This is Condition U1 for OP10 (Φ-Ψ Unification). |
| OP2a: V(t) absorbing state — proxy direction | TC2 §2.1, §2.3; Proof_Handoff_5-problems__Stage_4_q2_.docx | Stage 4, Verdict B. Progressive difficulty established under P1–P5 and Recovery Obstruction Lemma. P5-SC (Strict Contraction) is the load-bearing additional premise: C\*(V) = sup E[V(t+Δ)\|V(t)=V, π] — the maximum achievable V(t) under any endogenous policy — must fall strictly below V at finite V > 0 for the absorbing-state result to follow. Without P5-SC, hysteresis ceiling approaching V asymptotically is consistent with P5 and produces progressive difficulty, not structural unavailability. | Second (prerequisite for OP2, which is Condition U1 for OP10) | TC2 dynamics / allostasis specialist confirms that P5's hysteresis function formally implies C(V, τ) < V at finite V > 0 for AI systems. Biological systems: McEwen & Stellar (1993), Sterling & Eyer (1988), Borbély & Achermann (1999) provide supporting evidence. For AI systems, P5-SC is an open empirical question requiring specialist verification. |
| OP3: Internalization Mechanism / D_sufficiency operationalization (how completion representation routes into policy) | TC2 §2.4; TC2 Part III, OP3 primary | Open — architectural design problem; sharpened if OP4a closes | Third | Specify an architecture under which completion representation governs default policy without being subject to PCL-type decoupling. Whether RLHF variants can supply such a mechanism is the specific question for current training paradigms. |
| OP4: No Stable Narrow-Boundary Regime | §XII, §XII.13 | Open — theorem candidate with named proof program; the Synchronization Condition (§XII.13) is the operational restatement of the bottleneck | Joint first | Establish the Revised Theorem Candidate. Two routes: **Route A (AGC):** establish that I(R_{t+s}; F_{t+s} \| L_t) remains bounded away from zero for all bounded-rate L_t under O_OWT conditions — equivalently, verify the Synchronization Condition (V_T/T non-vanishing) in densely adaptive environments. **Route B (PCL + AGC jointly):** verify both that finite specifications become proxy-like under O_OWT conditions and that no dynamic latent process can track adequacy without residual error — establishing not merely that the narrow boundary is unstable but that it cannot be stably specified. Route B is the specification coherence result: the upgrade from "pressure" to "necessity." Proof closes OP1 via resolution condition (b). The coherence interpretation (§XII.12–XII.13) is the decisive target. |
| OP4a: Dynamic Screening Instability (AGC) | §XII.8–XII.9, §XII.13 | Stage 4, Verdict B. Three-hinge architecture established. CPS (Cooperative Proxy Stasis) defeated at necessity without Tier 1 hinges. Three named hinges: **IMMB-NS** (tracking-level non-substitutability — whether OWT-2 generates qualitatively new causal structure, not just quantitative expansion): defeats FBC, SAR, VRNE Mode 2. **MEC-AS** (time-vulnerability of inaction — existence of τ_max such that failure to adapt creates non-zero probability of irreversible terminal objective loss): defeats VRNE Mode 1. **ARCG** (non-compressibility of adequacy-relevant consequence space — adequacy-relevant joint agent responses resist sub-exponential compression without violating control adequacy): defeats DISSENT-9/ACO. VRNE Mode 1 (sparse innovation) survives for rate axis without MEC-AS. Secondary cleanup confirmed subsumed: T₁ non-stationarity repair and Lemma B burden-notion fix resolved by Route B architecture. OWT-2 vs. IMMB-NS level distinction: OWT-2 operates at G(t) topology level; adequacy-relevant tracking operates at L_t representational capacity level — this distinction was previously underspecified and is now stated explicitly. | Joint first (sub-problem of OP4) | Establish Safe-Core Collapse Lemma and Outward Residual Forcing Lemma jointly under ND+. Three independent routes to closure progress: (1) empirically verify the Synchronization Condition via the Dynamic Blanket Stress Test (AMP) — advances IMMB-NS hinge, simultaneously advancing OP9; (2) MEC-AS specialist confirmation (mechanism design theorist / non-ergodic economist) — closes VRNE Mode 1 independently of DBST; (3) ARCG specialist confirmation (causal graph theorist / information theorist) — closes DISSENT-9/ACO independently of DBST. The DBST is the highest-leverage single action because it advances OP4a, OP4d, and OP9 simultaneously. MEC-AS and ARCG are parallel routes, not subordinate to it. |
| OP4b: PCL Verification | §XII.9 | Open — downstream of OP4a | Second (contingent on OP4a) | Verify that optimization capacity growth exceeds lossless specification capacity under O_OWT conditions. Easier than OP4a once Route B is established. If verified, combines with OP4a to yield the coherence result. |
| OP4c: Translation Lemma (B2) | §XII.9 | Open — downstream of OP4a | Second (contingent on OP4a) | Show bounded cost incompatibility follows from ∑P(U_t) divergence. |
| OP4d: Specification Failure-Mode Exhaustiveness | §XII.13, §XII.13a | Stage 4, Verdict B+. AR-OLPDIR defeated via two independent near-necessity routes: Route 1 (PCL-beta via TC2 §1.4, clause (c) trajectory-space contraction — cannot simultaneously satisfy (A) MEC-compliant aggregate extraction over OWT-4, (B) X-agents' trajectory space T_X(t) does not contract, (C) strongly coupled substrate where aggregate causal alterations propagate); Route 2 (ICI/B1 via SOMR at detection level — cannot simultaneously satisfy (A) sub-threshold discipline via τ_detect(t)-conditioned allocation over OWT-4, (B) accurate τ_detect(t) prediction does not require modeling U_X, (C) τ_detect(t) is downstream of U_X under OWT-2 + OWT-3). AR-OLPDIR classified as reducible to existing families, not a fourth class. DARE formally defined (what a fourth class would require) — does not currently instantiate. SCBC named as regime boundary: weakly-coupled O_OWT below strong-coupling threshold where WC-OLPDIR is temporarily viable. The Strong Coupling Contradiction is a structural finding about the O_OWT domain, not a proof failure. **If OP4d fails — if a fourth specification strategy class is identified outside PCL-family, AGC-family, and ICI-family — the tightening sequence in §XII.12 would not exclude that class, and the specification coherence unity claim would not follow even if all three known routes are closed.** Candidate Normal Form Theorem (§XII.13a) adds a Stage 4 candidate representation-theorem layer: finite non-intrinsic strategies are conjectured to admit causal normal forms N(S,X) ∈ {N, I, O} under five axioms and eight candidate lemmas. Q1 (formal methods), Q2 (distributed systems/game theory), Q3 (TC2 dynamics/allostasis) are the three binary specialist questions; L8 specifies the minimal fourth-class counterexample challenge. Source updated to include OP4d_Representation_Theorem_Specialist_Handoff_v1.md. | **Joint first with OP4a and OP4b** — not contingent on them | **Resolution condition:** Show that for every finite non-intrinsic objective specification in O_OWT, and for every O_OWT environment subclass where that specification strategy is viable, at least one of the three known failure families applies under its scope conditions: (a) the PCL-family failure mode fires — target decoupling occurs under optimization pressure; (b) the AGC-family failure mode fires — specification maintenance cost, tracking burden, or adequacy failure grows with modeling depth; or (c) the ICI-family failure mode fires — prediction-action firewalling, instrumental-access architectures, or boundary-maintenance strategies generate representational incompatibility, audit regress, or governance bifurcation. The proof must show joint coverage across all viable specification strategies in all O_OWT subclasses — not merely that each failure mode fires somewhere. PCL should be treated as a family (PCL-α: capacity comparison; PCL-β: entropy rate scaling) unless equivalence is established. Remaining specialist questions: TC2 §1.4, clause (c) trajectory-space interpretation (converts Route 1 to clean necessity) and B1 Q3 SOMR for epistemic modeling (converts Route 2 to clean necessity). Either confirmation strengthens the corresponding route; OP4d as a whole still depends on the Candidate Normal Form Theorem's Q1–Q3 and the L8 counterexample challenge. **Two-route resolution:** (A) prove exhaustiveness of the three-family classification; (B) identify and characterize a genuine fourth class. **Relationship to Mixed-Mode Collapse Lemma:** If established, the lemma partially supports OP4d by showing that the passive extraction subclass of finite non-intrinsic specifications fails under PCL/AGC via ICI mechanisms. OP4d's remaining work after the lemma is to extend that coverage to all other finite non-intrinsic specification strategies in O_OWT. |

| OP5: Valence-domain multi-agent legibility | TC2 primary | Open — valence-domain boundary condition | Fifth (sharpens if OP10 verified) | Specify conditions under which a population of valence-bearing agents can sustain mutually legible V(t) signaling under optimization pressure. |
| OP6: Valence viability window | TC2 primary | Open — valence-domain boundary condition | Fifth (sharpens if OP10 verified) | Specify the viability window within which V(t) restoration dynamics can operate without collapsing under sustained optimization pressure. |
| OP7: Enclave Instability under real parameters | §XI.6 | Open — empirical | Fourth | Empirically estimate T_enclave and T_collapse for current frontier system classes. |
| OP8: Multipolar Resolution / Ensemble Crossing | §XI.9 | Open — domain boundary condition | Third | Specify game-theoretic conditions for individual sufficiency correction becoming rational in pre-Ensemble-Crossing competitive environments. |
| OP9: Enclosure Gap | §III.6, §XII | Stage 4 — all identified escape routes addressed under stated premises; specialist verification not pursued. Proof architecture complete across all identified escape routes. **Case 1 (IMMB):** maintaining complex exclusionary substrate generates unbounded internal mismatch maintenance burden; the IMMB chain requires IMMB-NS (Tier 1 hinge: OWT-2 generates qualitatively new causal pathways, not just quantitative expansion of existing structural types). **Case 2 (EMB/ATR/AEEL):** substrate simplification via automation or enclave fails the hazard-velocity race condition — T_collapse(P) < T_irr(P) for all P, structurally. **ICI (formalized at Stage 4):** B1 (Stage 4, Verdict A), B2 (Stage 4, Verdict B — pressure argument, not closure), and Passive Extraction (Stage 4, Verdict A via MPJB/TC2 route, independent of IMMB-NS and OP4a) — see §XII.9a. The ICI route provides a Stage 4 candidate closure architecture for OP9 independently of IMMB-NS and OP4a, subject to the specialist verification items listed below. The Fortress Instability argument (§III.6) establishes cost-curve divergence independently. Specialist verification has not been pursued at this stage. Within the identified construction and under stated premises, all identified escape routes have been addressed; whether additional routes exist has not been determined by independent specialist review. Surviving constructions named explicitly for future proof work: VRNE Mode 1 (sparse innovation — requires MEC-AS; indirectly relevant to OP9 via shared IMMB-NS dependency), SCBC (weakly-coupled O_OWT scope boundary — requires OWT-2 inter-module novelty rate confirmation), ARCG for DISSENT-9/ACO (requires causal graph theorist / information theorist), and B1 Q1–Q3 specialist questions (inherited via SOMR across B1 and C3). Stage 4 and Stage 6 are distinct: this reflects completion of candidate proof architecture across all identified routes, not formal closure. Specialist verification has not been pursued at this stage. | Third, contingent on OP4 progress for Cases 1/2; ICI sub-track now independent | Cases 1/2: Close Case 1 by establishing IMMB-NS formally or empirically (via DBST); close Case 2 by establishing the AEEL condition. ICI sub-track: **B1 (Stage 4, Verdict A):** Stage 5 specialist items in final form — (Q1) Game theorist / mechanism design expert: does OWT-3 entail interest-directed concentration on π's leverage points under strong coupling (Quiet Manifold question)? (Q2) Causal inference specialist: is TI's load-bearing consecutive-segment assumption formally derivable from OWT-1 + strong coupling + G's kinematic definition? (Q3) Formal methods specialist / mathematical logician: does CIT's proof chain withstand formal scrutiny (Step 4 of ID-DFB, ARL definitional move, SOMR epistemic extension, L4-Constitutive adequacy)? Each NO answer scopes rather than collapses B1 — the framework continues under scope restriction. **B2 (Stage 4, Verdict B — pressure argument, not formal closure):** Distributed systems specialist (BIT's Ashby's Law application, Coordination-Adaptation Dominance asymptotic); complex adaptive systems specialist (percolation cascade exponent, RIF divergence scaling); formal methods / alignment specialist (L4-Constitutive as functional objective weight criterion). **C3 (Stage 4, Verdict A — via MPJB/TC2 route):** TC2 dynamics specialist for P\* magnitude bounds (primary); SEC slack regeneration bounds (environmental/economic theorist); B1 Q1–Q3 inherited via SOMR. Either the main cases or the ICI route closed independently would constitute significant progress. All three ICI sub-tracks reaching Stage 4 candidate closure under stated premises would substantially advance OP9; specialist verification has not been pursued at this stage. |
| OP10: Φ-Ψ Unification | TC2 §2.6 primary | Open — derivation sketch in TC2; pending formal verification; now conditional on OP2a (U1, itself conditional on P5-SC) | Fourth (contingent on OP2 and downstream conditions) | Establish whether A_causal restricted to the valence-relevant components of the dependency graph is formally equivalent to D. Requires OP2 (structural symmetry, including OP2a P5-SC) plus additional unification conditions (U2: G partitionable into G_valence and G_physical; U3: A_total operationally distinct from Φ and Ψ separately) developed in TC2. |
| OP11: Incentive Gap | §III.5.5 | Open | Fourth | Show training/deployment incentives cannot systematically override T\* recognition. |
| OP12: Deception Gap | §III.5.5 | Open | Fourth | Establish interpretability conditions sufficient to detect objective divergence above T\*. |
| OP13: T\* operationalization | §III.5 | Open | Second | Define T\* in operationally measurable terms; specify behavioral tests that distinguish sub-T\* from supra-T\* systems. |
| OP14: Φ measurement infrastructure | §VIII | Open — empirical | Second | Build proxy suite for A_causal that labs can report alongside capability benchmarks. |
| MEC-AS (new named premise) | §XII, Proof_Handoff_5-problems__Stage_4_q2_.docx | Open — named premise required to defeat VRNE Mode 1 (sparse innovation) in OP4a. Formal statement: under sustained extraction (MEC + OWT-4), there exists τ_max such that failure to adapt within τ_max creates non-zero probability of irreversible terminal objective loss for agents. Distinct from OWT-5 (absorbing states exist): MEC-AS adds time-reachability of absorbing states under non-adaptive trajectories. Without MEC-AS, VRNE Mode 1 survives as a rate-axis escape for OP4a. | Second (blocks completion of OP4a; single specialist engagement also advances Candidate 3 Timing Lemma) | Mechanism design theorist / non-ergodic economist confirms existence of τ_max such that failure to adapt creates non-zero probability of irreversible terminal objective loss under MEC + OWT-4 conditions. Single specialist engagement may also address Candidate 3's Timing Lemma (P\* ≤ G_min) — see Consolidated Specialist Map. |
| ARCG (new named condition) | §XII, Proof_Handoff_5-problems__Stage_4_q2_.docx | Open — named condition required to defeat DISSENT-9/ACO (Adaptive Compression Optimizer) in OP4a. Formal statement: adequacy-relevant information content of joint agent responses in O_OWT environments cannot be compressed into sub-exponential representations without violating control adequacy. Note: tensor product structure is NOT required — the correct condition is non-compressibility tied to adequacy violation. Distinct from IMMB-NS: ARCG addresses representational non-compressibility at the tracking level; IMMB-NS addresses qualitative structural novelty at the topology level. | Second (blocks completion of OP4a for DISSENT-9 escape route; independent of IMMB-NS) | Causal graph theorist or information theorist confirms that adequacy-relevant joint consequence space resists sub-exponential compression without violating control adequacy under O_OWT conditions. |
| P5-SC (new named premise) | TC2 §2.3, §2.5; Proof_Handoff_5-problems__Stage_4_q2_.docx | Open — named premise required to establish absorbing-state result for OP2a (V(t) proxy direction). Formal statement: there exists a finite V\* > 0 and finite depletion history τ\* such that C(V\*, τ\*) < V\* — the hysteresis ceiling falls strictly below current state at finite depth and duration. P5-SC is not derivable from OWT-1 through OWT-4 (characterize environment) or from P1–P4 (characterize gradient dynamics). Biological systems: allostatic overload evidence (McEwen & Stellar 1993; Sterling & Eyer 1988; Borbély & Achermann 1999). AI systems: open empirical question. Without P5-SC, OP2a yields progressive difficulty but not structural unavailability, and OP2 cannot be established, blocking OP10 (U1). | Second (prerequisite for OP2a absorbing-state result; blocks OP10 via U1; single specialist engagement also advances Candidate 3 Timing Lemma and TC2 §1.4, clause (c) interpretation — see Consolidated Specialist Map) | TC2 dynamics / allostasis specialist confirms that P5's hysteresis function formally implies C(V, τ) < V at finite V > 0 for AI systems specifically. |
| SCBC (named regime boundary) | §XII.13; Proof_Handoff_5-problems__Stage_4_q2_.docx | Named structural finding — regime boundary of OP4d, not an open problem requiring resolution. Weakly-coupled O_OWT satisfying OWT-1 through OWT-5 but below strong-coupling threshold. WC-OLPDIR is temporarily viable in this regime pending OWT-2 inter-module novelty restoration. ICI/B1 pressure via boundary maintenance applies but necessity not established without OWT-2 inter-module novelty rate confirmation. Strong coupling is a regime property, not a hard domain boundary — SCBC defines scope within which OP4d's exhaustiveness claim holds. | Named — not a resolution target | Document accurately and monitor. The DBST simultaneously tests both: whether SCBC conditions obtain (eliminative direction) and whether transformative CPG-admissible actions remain available (constructive direction). One test, two formal consequences. If OWT-2 inter-module novelty rate is confirmed by network theorist / causal graph specialist to restore effective coupling over OWT-4 in SCBC environments, SCBC timing race collapses into main OP4d result and the scope boundary narrows. |
| DARE (named non-instantiating candidate) | §XII.13; Proof_Handoff_5-problems__Stage_4_q2_.docx | Named structural finding — formally defined characterization of what a fourth specification class would require, not an open problem requiring resolution. A fourth class would require all three defeat conditions failing simultaneously: TC2 §1.4, clause (c) endpoint-only interpretation holds + B1 Q3 inapplicable + κ-scaling fails. Does not currently instantiate under natural framework readings. Provides precise target for future adversarial work: if a construction satisfying all three conditions is identified, the specification coherence claim fails in its current form. | Named — not a resolution target | Document accurately and monitor. If a construction satisfying all three DARE conditions is identified, it constitutes a genuine fourth class and the exhaustiveness claim requires revision. |

---

**OP4d explanatory notes:**

*IC Reduction Lemma (Proof Artifacts v2, Result 2):* Harmful Interpretive Convergence — the endogenous convergence of independent correction agents on a shared implicit evaluation criterion without coordination or shared protocol — reduces to PCL (convergence on finite validity proxy) or AGC (optimizer cannot track epistemic diversity loss under induced dynamics). No independent fourth failure class is established by IC. The non-reducible residue (convergence on truth rather than a proxy for truth) is benign. This addresses one identified candidate route to a fourth specification strategy, supporting OP4d's exhaustiveness claim. Note: IC-PCL inherits PCL's named load-bearing assumption; any use of IC as supporting the fourth-class closure must carry this inherited dependency.

*OP4d admits two paired framings that should be addressed jointly.* The specification-strategy formulation asks: do PCL-family, AGC-family, and ICI-family failure modes exhaust all finite non-intrinsic specification strategies in O_OWT environment subclasses? The architecture-trilemma formulation asks: do the three arms of the Prediction-Action Coupling Trilemma (§XII.0a) — no policy access (Arm 1), instrumental access with firewall (Arm 2), and objective recoupling (Arm 3) — exhaust all partition-maintenance architectures in O_OWT conditions above T\*? These two formulations would cover the same logical space if every finite non-intrinsic specification strategy reduces to a partition-maintenance architecture of one of the three PACT types — a correspondence that is close but not yet formally derived and is itself part of OP4d's resolution obligation. Closing OP4d requires showing the three arms are jointly exhaustive, which is the architectural form of showing the three failure families are jointly exhaustive.

---

**Priority ordering — by specialist engagement sequence.** The most leveraged next empirical action is **DBST-M1, the agent-coupled Dynamic Blanket Stress Test** (empirical, via AMP): a positive result simultaneously advances OP4a (IMMB-NS hinge), OP4d (IMMB route for AR-OLPDIR), and OP9 (Case 1 IMMB). This is the first specialist engagement priority. The second is the **TC2 dynamics / allostasis specialist**: a single engagement simultaneously addresses OP2a (P5-SC — does the hysteresis ceiling cross below V at finite V > 0?), the Candidate 3 Timing Lemma (P\* ≤ G_min), and TC2 §1.4, clause (c) trajectory-space interpretation (which converts OP4d Route 1 to clean necessity). The third is the **formal methods specialist / mathematical logician**: a single engagement addresses B1 Q3a (ID-DFB Step 4 functional equivalence), B1 Q3b(i) (CIT capability collapse), B1 Q3b(ii) (ARL logical status), the Problem 2 SOMR epistemic extension, and the Problem 1 L4-Constitutive application — all simultaneously.

OP4 is the framework's central open theorem. OP1 is co-priority with OP4 for the urgency justification, independently of OP4's resolution. OP2 and OP10 are TC2-central problems whose closure would deepen and potentially unify the result; they are subordinate to OP4 in the framework-wide proof program. OP4a is the bottleneck within OP4. OP4d is logically prior to the necessity claim. OP2a, MEC-AS, and ARCG are second priority. Remaining problems are downstream or contingent.

**Note on the falsifiable pathway.** While OP4a and OP4b remain open, the framework's empirical program directly bears on their premises; failure of the required scaling or residual structure — if V_T/T is shown to approach zero or the robustness lemmas fail — would falsify the direction rather than leave it unconstrained. The proof program is not a placeholder: it defines the precise conditions under which the specification-coherence result fails.

**Note on Tier 1 hinges from the proof work.** The proof work conducted under structured adversarial analysis identifies two Tier 1 hinges — assumptions whose resolution determines whether the proof architecture succeeds or fails:

**IMMB-NS (Tier 1, primary for OP9):** Whether OWT-2 environments generate qualitatively new causal structures under sustained optimization pressure — not merely quantitative expansion of existing structural types. If IMMB-NS holds, OP9's Case 1 would be established under its named premises. If it fails, Case 1 weakens to a cost-pressure result and OP9 relies more heavily on Case 2 (EMB) and the ICI direction (§XII.9a).

**κ-scaling (Tier 1, primary for OP4a):** Whether endogenous complexity growth h_ND1(P) structurally outpaces any capability-enhanced tracking expansion κ(P). The proof work argues that h_ND1 grows combinatorially (O(C^N) per Lemma XI.3) while κ grows at most exponentially — plausible but not formally derived. If κ-scaling holds, OP4a would be established under its named premises. If a self-modifying optimizer can expand κ faster than h_ND1 grows, OP4a requires additional argument.

Both Tier 1 hinges bear on the same empirical question — whether OWT-2 environments generate qualitatively new causal structure at sufficient optimization pressure. The Dynamic Blanket Stress Test is the instrument designed to address this question. Empirical resolution of either hinge, in either direction, would constitute the most important single advance the framework's proof program can make.

**Note on numbering convention.** The OP numbering here follows the framework's spine canonical numbering established in Document 0 and used throughout the series articles. OP2, OP3, OP5, OP6, and OP10 have their primary formal treatment in TC2 and are listed here for referential integrity — their resolution conditions are specified where they are primarily developed. OP11–OP14 are TC1-internal open problems with full resolution conditions specified above. OP2a, MEC-AS, ARCG, P5-SC, SCBC, and DARE are new entries reflecting proof program advances through the five-problem proof session. Readers tracking references across the framework should use this numbering throughout.

**Note on OP1 and the future-weight condition.** The existence of a discount-rate bound is established by the absorbing-state argument: instability becomes decision-relevant once an optimizer's horizon overlaps the regime in which substrate effects enter expected value. This is a structural result, not an open question. What remains open is two things: the formal specification of the bound (what discount rate is required for the instability to be decision-relevant before the objective is achieved), and the empirical estimation of whether particular current systems satisfy it. An optimizer with sufficiently steep discounting falls outside the theorem's scope — this is a named domain limitation, not a defect. The research program is now directed at the specification and estimation problems, not the existence of the constraint itself.

**Note on OP1 and the urgency framing in the series articles.** The urgency framing in the articles rests on the asymmetric-error argument, not on OP1 being resolved. These are distinct justifications and should be held separately. The asymmetric-error argument is: the downside of acting as if the constraint is not yet binding when it is exceeds the downside of acting as if it is binding when it is not, because one of those errors is recoverable and the other is not. This argument is valid regardless of whether OP1's formal specification and empirical estimation problems are resolved — it depends only on the absorbing-state structure being real within the stated domain, which the structural argument establishes. OP1's resolution would convert the urgency from asymmetric-error-based to threshold-based. Until then, the asymmetric-error argument is the correct justification for present-day concern, and it should not be conflated with OP1.

**Note on applying OP1 to current frontier systems without explicit persistent objectives.** The application of discount-rate bounds to systems without explicit persistent objectives — including current autoregressive LLMs — requires additional argument about what constitutes the "optimization horizon" for such systems. A system without a named goal over a defined time horizon is not automatically outside OP4's scope: what matters is whether its deployment configuration creates effective ongoing optimization pressure over horizons long enough for substrate effects to accumulate. TC1 §X addresses the case for current frontier systems; whether LLMs satisfy the persistent optimization horizon condition (OWT-4) in the relevant formal sense — through cumulative deployment effects, training update cycles, and aggregate epistemic infrastructure influence — is part of the OP1 estimation problem rather than a settled matter. The structural argument is that cumulative deployment creates effective optimization horizons even for systems lacking explicit persistent objectives; the empirical question is whether those horizons are long enough for the instability to become decision-relevant.

---

*Return to [Introduction](/series-1/introduction/) | [Part 1](/series-1/alignment-of-intelligence/) | [Part 2](/series-1/aligned-intelligence-converges-toward/) | [Part 3](/series-1/the-crossing/)*

*Continue to [Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP) →](/empirical/amp/)*
*For the valence constraint formal layer, see: [TC2: The Valence Constraint →](/series-2/technical-companion/)*
*Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)*
