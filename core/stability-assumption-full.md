---
title: "OP4: The Stability Assumption"
permalink: /core/stability-assumption-full/
description: "Full OP4 paper on the Stability Assumption and objective-boundary stability under accurate coupled modeling."
---

> **Canonical archive version** · [Read on Medium →](https://medium.com/@diamondlight/op4-the-stability-assumption-e19955599adb) · [Framework hub →](/core/alignment-constraint/) · [Proof Status →](/core/proof-status/)

---

---

**Proof Program navigation:**

| # | Document | Role |
|---|---|---|
| 1 | [Proof Status and Non-Claims →](/core/proof-status/) | Calibration |
| **→ You are here** | **OP4: The Stability Assumption** | Central theorem target |
| 3 | [The Tightening Sequence →](/core/tightening-sequence/) | Narrative closure |
| 4 | [OP4d: The Exhaustiveness Obligation →](/proof-program/op4d-exhaustiveness-obligation/) | Exhaustiveness question |
| 5 | [OP4d: Candidate Normal Form Specialist Verification →](/proof-program/op4d-candidate-normal-form/) | Formal apparatus |
| 6 | [Packet 1: IMMB-NS Verification and the Dynamic Blanket Stress Test →](/proof-program/packet-1-immb-ns-dbst/) | Empirical specialist packet |

Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)

---

## 1. The Stability Assumption

Every separable-objective alignment approach makes a structural bet. RLHF bets that expressed preference is a stable enough proxy for what we actually care about. Constitutional AI and debate bet that finitely specified evaluative structure can remain adequate as capability scales. Scalable oversight bets that evaluation criteria can keep pace with the systems being evaluated. Interpretability-as-monitoring bets that reading a system's internals can substitute for solving the specification problem.

These approaches differ in important ways. But each depends, somewhere, on a finite line between what the system optimizes and what it merely models remaining coherent as capability and modeling depth increase. The mechanisms differ. The underlying bet is shared.

The argument is not specific to these implementations. It applies to any approach that relies on a finite separable objective specification remaining coherent under increased modeling depth. Static and updating versions of this bet are treated separately below.

The bet is this: that the boundary between what a system is optimizing for and what it must model to act effectively remains stable — not perfect, not complete, but *coherent as a specification* — as modeling depth increases in coupled environments. Call this the stability assumption.

This paper isolates that assumption and asks whether it survives scrutiny.

*A note on proof status.* This paper presents a Stage 4 candidate architecture, not a theorem. The claim is that every identified finite-boundary strategy faces a named structural pressure under the conditions specified below, and that the remaining work is concentrated in explicit verification and exhaustiveness questions. A fourth strategy class outside the three identified families, a successful bounded-boundary empirical result, or a formal stability theorem would challenge the framework directly. Those challenges are extended as invitations, not dismissed as impossibilities.

---

## 2. Domain

The stability question is not abstract. It becomes practically unavoidable in environments with three properties.

**Open.** The system's interventions affect agents and structures beyond any fixed boundary — effects propagate through shared infrastructure, epistemic environments, and institutional relationships.

**Shared.** Multiple agents draw from the same substrate of coordination, trust, and physical resources. What one optimizer does to that substrate affects what others can do.

**Non-resettable.** Some reachable configurations cannot be recovered from within the system's own operational dynamics. Substrate collapse, epistemic capture, and coordination failure can be absorbing states.

Under sustained optimization pressure in environments with these properties — the Open-World Transformative (O_OWT) regime — the stability assumption faces its most demanding test.

Three applicability levels should be distinguished. At the level of isolated model behavior in a single session, the conditions are only partially satisfied. At the level of deployed AI systems embedded in human workflows, institutional feedback loops, and advisory relationships, the conditions are substantially satisfied. At the level of the training and deployment pipeline that optimizes capability and influence over time, they are most plausibly satisfied. The strongest near-term applicability claim is at the second and third levels, not the first.

Where the domain conditions are absent — bounded environments, static causal topology, non-adaptive agents, terminal objectives — the argument weakens in specific, identifiable ways. The domain is explicit so those exits are available to anyone who can take them honestly.

---

## 3. What Stability Would Require

Before asking whether the stability assumption holds, it is worth stating precisely what it would mean for it to hold.

An objective boundary is **stably adequate** if there exists a finite-complexity representation of the objective that satisfies three conditions simultaneously as modeling depth and intervention pressure increase:

**(a) Policy adequacy without decoupling.** The boundary continues to guide behavior toward what it was intended to track — it does not decouple from that target under accurate full-information evaluation as the system's model of the environment becomes more accurate.

**(b) No unbounded revision requirement.** The boundary does not require indefinitely expanding specification complexity to track what it has excluded — the excluded variables do not continuously generate new cases requiring new specification rules.

**(c) No load-bearing maintenance cost.** The boundary does not require boundary-maintenance costs that grow with intervention pressure, or that prevent adequacy comparable to what an open-model system would achieve under comparable resources.

All three conditions must hold simultaneously. A specification that satisfies (a) and (b) but requires continuously increasing maintenance work to remain coherent satisfies (c) only if that maintenance work vanishes rather than remaining structurally necessary.

This is the coherence condition the stability assumption requires.

The question this paper addresses is whether any finite separable objective specification can satisfy all three conditions simultaneously under accurate coupled modeling in O_OWT environments. Not whether any particular specification satisfies them. Whether any can. The challenge: show a finite objective-boundary strategy that survives accurate coupled modeling without collapsing into fixed specification, bounded dynamic tracking, or prediction-action firewalling. The precise counterexample conditions are in Section 8.

---

## 4. Why This Is Not the Ordinary Specification Problem

Goodhart's Law identifies proxy failure within a stable specification project: the measure becomes the target, and the target drifts. This is a real and serious problem. It is not the problem this paper is about.

The ordinary specification problem assumes that better specifications, more accurate proxies, or more sophisticated evaluation can close the gap between what we specify and what we care about. The problem is imprecision, incompleteness, or adversarial exploitation of the specification.

The stability assumption is about something more fundamental. It asks whether the specification project itself has a stable completion condition — not whether we can write better specifications, but whether *any* finite separable specification can remain adequate under the modeling depth that consequential action in coupled environments requires.

The distinction matters because the fix is different. If the ordinary specification problem is the right frame, alignment is a harder version of the same kind of problem we have always faced: write better objectives, improve training signals, refine evaluation. If the stability assumption fails, the problem is misframed at its foundation. Not harder. Different.

Here is why the problem may be different. As a system becomes capable enough to act consequentially in an open, coupled environment, it must model more of the structure of that environment — other agents' strategies, long-range causal chains, the conditions under which its own interventions remain viable. At some point, the variables it needs to represent in order to act effectively are no longer cleanly separable from the variables its objective treats as outside the scope of what matters.

When that happens, the system is using a single model to do two things simultaneously: determine what actions lead to good outcomes, and enforce a boundary between what is allowed to influence the objective and what is merely informative. Those two roles are in structural tension. The model's increasing accuracy in the first role creates pressure on the second.

This question is adjacent to embedded agency but distinct from it. Embedded agency asks how a system handles modeling and acting from within the world — how self-reference is handled. The stability assumption asks whether a separable objective — one that excludes some variables from the scope of what matters while using them for prediction — can remain coherently specified under accurate coupled modeling. The question is not only self-reference. It is separability. Embedded agency makes the agent/world boundary problematic; the stability assumption makes the objective/model boundary problematic. A system could handle many embedded-agency difficulties correctly and still face stability-assumption failure, because the latter concerns the objective/model boundary rather than only the agent/world boundary.

The strongest version of the concern is referential, not merely operational. At sufficient modeling depth, the target a finite objective is trying to specify may no longer be stably nameable — because it is identifiable only through background conditions the optimization itself changes. That is not a drift problem. It is a reference problem.

This is also not a harder version of mesa-optimization. Mesa-optimization asks what happens when a learned optimizer develops objectives that diverge from the base objective during training. That question assumes the base objective specification is itself coherent and asks how inner alignment can fail relative to it. The stability assumption asks whether the base objective specification remains coherent under the modeling depth consequential action requires — a prior question, not a refinement of the same one.

This question is also adjacent to the eliciting latent knowledge problem, but the target is different. ELK asks whether we can elicit what a model knows rather than what it reports. The stability assumption asks whether the boundary between knowledge used for prediction and variables permitted to govern action can remain coherent as modeling depth increases in coupled environments. ELK primarily addresses a reporting and oversight problem; the stability assumption treats that difficulty as one expression of a deeper objective-boundary stability problem. If the boundary itself cannot remain stably specified, eliciting the truth is necessary but not sufficient: the question becomes whether the truth can remain policy-inert without recreating the same audit regress at the action-selection level.

This is not a failure of specification precision. It is a question about whether the concept of a separable objective remains coherent at all as a system models its environment accurately enough.

If the stability assumption fails, alignment is not a harder specification problem. It is a different kind of problem.

---

## 5. Three Escape Families

Among the architectures currently identified, every strategy identified so far for maintaining a finite objective boundary in O_OWT conditions falls into one of three families.

**Fixed specification.** The objective boundary is specified in advance — a reward function, a preference model, a constitution, a set of evaluative principles — with sufficient precision that it remains adequate as modeling depth increases. The specification is external to the optimization process and static relative to it.

**Bounded dynamic tracking.** The objective boundary is updated adaptively, tracking the environment as it changes, at bounded computational cost. Rather than a fixed specification, the boundary evolves — but its evolution is constrained to remain tractable.

**Prediction-action firewall / structural enclosure.** The system's model includes variables that are excluded from the objective — it uses them for prediction but maintains a firewall preventing them from governing what it optimizes. Or the optimizer attempts to establish a private substrate, isolating itself from the broader coupled environment before the stability problem becomes acute.

These are not straw men. They represent the most sophisticated available strategies for making separable specification work under scaling. Any defense of the stability assumption must address at least one of them.

---

## 6. The Structural Pressures Each Family Faces

Under O_OWT conditions, each family faces a named structural pressure. These pressures are identified under a Stage 4 proof architecture — candidate arguments under stated premises, with specialist verification pending and exhaustiveness not yet formally established. The claim is not that each family has been proven to fail. The claim is that each faces a structural pressure that any defense of the stability assumption must address.

**Fixed specification faces Proxy-Convergence pressure.** In O_OWT conditions, any finitely specified external objective eventually couples to adequacy-relevant excluded variables through the system's own intervention effects. The optimizer's interventions alter the causal structure of the environment, generating new dependencies that the fixed specification did not model and cannot track. The specification target becomes proxy-like under optimization pressure — it continues to be pursued, but it no longer tracks what it was intended to track. The more capable the optimizer, the faster this coupling occurs, because larger interventions generate larger causal footprints.

This is not a generic form of Goodhart's Law applied to a new domain. It is a claim about what happens to any finitely specified external objective when the optimizer is capable enough that its interventions restructure the environment the objective was specified over. The specification does not merely drift. The environment it was tracking changes in response to the optimization, making the specification proxy-like from within.

**Bounded dynamic tracking faces Dynamic-Screening pressure.** Suppose the specification is updated adaptively as the environment changes. The question is whether a bounded-rate updating process can maintain adequacy as the environment evolves.

The structural pressure here is that the optimizer's own interventions are the source of the complexity the tracker cannot handle. In O_OWT conditions, the framework's proof program argues that sustained optimization can generate new causal pathways — potentially not merely quantitative expansion of existing structures, but qualitatively new dependencies. Whether this qualitative-novelty claim holds in the relevant empirical regimes is the hinge DBST-M1 is designed to test. The tracker's expansion generates the novelty it must then track. Each model the system builds changes the strategic landscape it is modeling. The problem is not that every model is immediately obsolete, but that maintaining adequacy requires the boundary to keep updating against novelty generated partly by the optimizer's own interventions. The burden does not vanish as modeling improves; under the Stage 4 construction, it is predicted to persist or grow with intervention pressure.

The result is a race the tracker cannot win not because it is slow, but because the optimizer is the entropy source. The screen and the novelty it cannot contain are not separate problems. They are the same dynamic, seen from two sides.

**Prediction-action firewall and structural enclosure face Representational-Incompatibility pressure.** The firewall strategy — model excluded variables for prediction, maintain a barrier preventing them from governing the objective — faces a structural tension that becomes more acute as modeling accuracy increases.

To act effectively in a coupled environment, the system must accurately model the agents it affects, including their strategies, responses, and the consequences of its own interventions on them. The excluded variables are precisely the variables the model requires for accurate prediction. As modeling depth increases, the firewall between "informative for prediction" and "admissible for the objective" must become increasingly precise — but increasing precision requires increasingly detailed representation of exactly what is being excluded.

The partition is downstream of the model it was introduced to constrain. Any rule that defines the exclusion must partition states into informative and inadmissible — but the admissibility of any action is defined by its predicted effect on the excluded variables. The firewall inherits the gradient it was supposed to limit. The formal version of this argument is developed in TC1 §XII.9a.

Structural enclosure — establishing a private substrate before the stability problem becomes acute — passes through the same coupled environment during construction, recreating the dependency structure it was designed to escape. The enclosure cannot bypass the stability problem; it requires surviving it.

**The shared structure.** Across all three families, the same dynamic appears: the act of accurate modeling in a coupled environment is constitutively the process by which the objective boundary becomes inadequate. The boundary does not fail because the specification was imprecise. It fails because what the system must model to act effectively and what its objective is permitted to cover are not stably separable as modeling depth increases.

If the three families are all there is — if every available partition-maintenance architecture reduces to one of these pressures — then the stability assumption does not merely face rising costs. It faces the possibility that finite separable objective specification fails to pick out a stable target under the modeling depth consequential action requires.

Whether this shared structure constitutes a formal impossibility depends on the question addressed in the next section.

---

## 7. How Current Approaches Inherit the Stability Assumption

The point is not that these approaches fail in all regimes. It is that, if treated as sufficient alignment foundations, each inherits a specific version of the stability assumption.

| Approach | Stability dependence | Relevant pressure |
|----------|---------------------|-------------------|
| RLHF / reward modeling | Expressed preference must remain an adequate proxy as optimization pressure and deployment coupling increase | Proxy-Convergence: the preference model can improve while the underlying target drifts |
| Constitutional AI | A finite evaluative boundary must remain adequate across novel coupled cases | Fixed-specification pressure: principles must cover action-relevant variables generated by deployment |
| Debate / oversight | The evaluative process must track relevant consequences without becoming the bottleneck or proxy | Bounded-tracking pressure: oversight must update fast enough to remain adequate |
| Interpretability-as-monitoring | Reading internal states must substitute for solving the objective-boundary problem | Firewall/audit-regress pressure: the monitor must model what is excluded and decide when it matters |
| Scalable oversight | Decomposed evaluation must preserve adequacy under increased coupling | Boundary-maintenance pressure: local checks may fail to capture global objective-relevant dependencies |

---

## 8. The Live Vulnerability: OP4d

The strongest form of the stability claim — that no finite separable objective specification can remain stably adequate under accurate coupled modeling in O_OWT conditions — depends on the three families identified above being jointly exhaustive across all O_OWT environment subclasses.

This is the framework's live vulnerability: a successful fourth strategy class would require rebuilding the specification-coherence argument from different foundations.

That exhaustiveness has not been formally established.

The current Stage 4 proof architecture has sharpened the claim considerably. Within the stated construction, every identified finite non-intrinsic objective-boundary strategy in O_OWT environments reduces to one of three failure families: proxy-convergence under fixed specification, dynamic-screening instability under bounded tracking, or representational incompatibility under prediction-action firewalling. The live remaining vulnerability is OP4d: whether a fourth strategy class exists outside these families. If no such class exists and the named premises hold, the implication is not merely that narrow-boundary objectives become costly or unstable, but that finite separable objective specification may fail to pick out a stable target at sufficient modeling depth. The proof program has not established that referential-instability claim. It has established the three-family classification and specified the conditions under which that claim would follow. Establishing it would require not only showing that every known boundary strategy fails, but a positive argument that the reference conditions making any finite objective's target identifiable are necessarily within scope of what optimization alters in O_OWT environments — the bridge from "all known strategies fail" to "no stable separable target exists."

The framework has examined 22 adversarial constructions within the current proof-search history, finding that each reduces to pressure from one of the three known families. This examination has been organized into a candidate normal-form classification under stated axioms — but this is candidate architecture, not formal exhaustiveness proof.

The live vulnerability is this: if a fourth specification strategy class exists outside fixed specification, bounded dynamic tracking, and prediction-action firewalling, the specification-coherence claim fails in its current form.

A minimal counterexample challenge can be stated precisely: construct a boundary architecture that satisfies all of the following simultaneously —

- It remains policy-adequate as modeling depth increases in O_OWT conditions, without decoupling from the target under accurate full-information evaluation.
- It uses excluded variables where prediction requires them, without those variables becoming functionally objective-governing.
- It avoids proxy decoupling, bounded-tracking failure, and firewall/audit-regress collapse under the structural pressures identified in Section 6.

No such architecture has been identified across 22 adversarial constructions within the current proof-search history; this is not an independent exhaustiveness proof. If one exists, finding it would be the most important contribution to this question anyone could make. The framework names this explicitly as an invitation rather than a caveat.

---

## 9. The Empirical Hinge

Whether bounded dynamic tracking faces a genuine structural pressure — rather than merely a practical difficulty that more compute could overcome — is, at its core, an empirical question. The key question: does sustained optimization in O_OWT environments generate qualitatively new causal structure faster than any bounded tracking process can absorb?

This question now has a first empirical result, with an important caveat that must be stated alongside it.

**DBST-M0** — a pre-registered minimal shared-novelty version of the Dynamic Blanket Stress Test — used three experimental arms receiving identical raw information and identical per-feature processing, with only the boundary-maintenance architecture differing. The pre-registered primary criteria were both met: boundary-maintenance cost rose with novelty pressure (slope 0.0985, 95% CI [0.0972, 0.1000]), and the adequacy gap between the bounded arm and the unconstrained arm also rose monotonically (gap slope 0.0091, 95% CI [0.0089, 0.0093]). Baseline equivalence was confirmed at minimum pressure.

However, a pre-specified same-rate random control produced nearly identical slopes (cost 0.0982; gap 0.0090). Under the pre-registered interpretation rule, this indicates that event rate rather than causal propagation structure is the identified driver within this design. What M0 established is technical feasibility and rising cost / adequacy-gap effects in the simplest toy shared-novelty regime, while leaving open whether the driver is causal propagation structure or event rate — a same-rate random control produced nearly identical slopes. It does not isolate causal propagation structure as the driver, and it does not test agent-action-generated novelty.

The robustness sweep also shows budget sensitivity: at a larger boundary budget (B=4), the raw values show that the adequacy gap approaches zero while update cost continues rising. Public interpretation should rely on the raw B=4 mean cost and gap values rather than the reported saturation-index field. The result supports a non-vanishing cost burden in this setting, but does not establish that adequacy loss itself persists under optimal budgeting.

**What remains.** DBST-M1 — in which each arm's own interventions causally influence future feature activations — is the test of the endogenous-novelty mechanism directly. M0 established the design's technical feasibility and rising cost / adequacy-gap effects, but did not isolate causal propagation from event-rate effects. M1 tests whether an optimizer's own actions generate the novelty a bounded boundary cannot absorb — that is the mechanism test.

The predicted failure is not lower reward. It is rising boundary-maintenance cost or adequacy loss in the bounded-boundary arms relative to the open-model arm, as pressure increases. If the bounded dynamic boundary maintains adequacy comparable to the open model without non-vanishing maintenance cost as pressure rises, the framework's central empirical direction is challenged within that regime. DBST-M0 provides the first pre-registered result showing technical feasibility and rising cost / adequacy-gap effects. DBST-M1 is the next step. The full specification of both instruments is in the Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP).

---

## 10. What Would Change the Framework

These are not rhetorical challenges. They are the specific conditions under which the framework's central direction requires revision.

**A successful bounded-boundary result.** A bounded-updating-boundary agent that maintains adequacy comparable to an open-model agent under rising intervention pressure without non-vanishing boundary-maintenance cost, under O_OWT-satisfying conditions. This would directly challenge the dynamic-screening pressure identified in Section 6.

**A formal stability account.** A proof establishing that some class of finite separable objective specifications can remain stably adequate — in the sense defined in Section 3 — under accurate coupled modeling in O_OWT conditions. This would show the stability assumption has a formal completion, not merely practical workarounds.

**A fourth strategy class.** A boundary architecture satisfying the minimal counterexample challenge stated in Section 8. This would show the three-family taxonomy is incomplete and require rebuilding the specification-coherence argument from different foundations.

Any of these results would be significant. The framework does not treat them as impossible. It treats them as the most important open questions in this space.

---

## 11. The Invitation

The stability assumption is load-bearing for every alignment approach that relies on finite objective boundaries. The question is whether it has been earned or merely assumed.

Run the Dynamic Blanket Stress Test. Construct the fourth strategy class. Formalize the stability theorem and show the boundary holds.

If the boundary holds under accurate coupled modeling, alignment is a specification problem and the field's current direction is broadly correct. If it does not, the problem is not harder. It is different.

The full argument — across physical substrate, experiential capacity, and the specification-coherence proof program — is developed in *The Alignment Constraint* and the accompanying series. This paper isolates the structural bet.

The assumption is now being tested. DBST-M0 provides the first pre-registered result: technical feasibility and rising cost / adequacy-gap effects in a toy shared-novelty design, with the caveat that a same-rate random control produced nearly identical slopes — indicating event rate rather than causal propagation structure as the identified driver. DBST-M1 is the mechanism test.

---

*[The Alignment Constraint →](/core/alignment-constraint/) | [TC1: The System-Aware Attractor →](/series-1/technical-companion/) | [Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP) →](/empirical/amp/) | [OP4d: The Exhaustiveness Obligation →](/proof-program/op4d-exhaustiveness-obligation/)*

*Continue to: [The Tightening Sequence →](/core/tightening-sequence/)*
*Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)*
