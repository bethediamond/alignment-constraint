---
title: "The Alignment of Intelligence"
permalink: /series-1/alignment-of-intelligence/
description: "A Series 1 article on optimization, intelligence, and alignment as a structural constraint."
---

> **Canonical archive version** · [Read on Medium →](https://medium.com/@diamondlight/ii-the-alignment-of-intelligence-187b09d2f902) · [Framework hub →](/core/alignment-constraint/) · [Proof Status →](/core/proof-status/)

---

*Part 1 of 3 — The Constraint*

**Series navigation:**

| Post | Title | Role |
|------|-------|------|
| Introduction | Alignment and Structural Necessity | Frame + Glossary |
| **→ You are here** | **The Alignment of Intelligence** | The Constraint |
| Part 2 | What does aligned intelligence actually converge toward? | The Attractor |
| Part 3 | The Crossing | The Crossing |
| Technical Companion | The System-Aware Attractor | Formal Layer |

Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)
Experimental Companion: [Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP) →](/empirical/amp/)

*Companion simulation: [Objective Class & Substrate Stability →]*

New to this framework? Start here. *[The Alignment Constraint →](/core/alignment-constraint/)* provides the full epistemic map after this article.

---

AI alignment is usually framed as the problem of specifying the right objective. This article asks a prior question: whether separable objective specification remains coherent as optimization scales. If it fails at sufficient modeling depth, the problem is not which objective to specify — it is whether separable objectives remain a coherent target at all.

More precisely: as a system becomes capable enough that accurate action requires modeling the conditions its objective excludes, the object being specified may no longer retain a stable referent — not because the boundary is merely costly to maintain, but because the target's identity may depend on what the specification designates as outside its scope.

---

*Epistemic status: High confidence in the structural and game-theoretic dynamics described, within the domain specified below. The Orthogonality Thesis is accepted as a premise throughout — not contested. This is a structural argument, not a normative one: the question is not which objectives are morally superior, but which objective classes can persist under sustained optimization pressure in open, shared, non-resettable environments. "Well-being" is a working label for the class of objectives this constraint leaves standing — a structural residual, not a commitment to any specific formulation. The core argument is structural: within open, shared, non-resettable environments under sustained optimization pressure, any objective that fails to account for system-wide effects tends toward self-termination. That is a constraint within a domain, not a universal law. This article develops the persistence component of the framework's canonical root claim — that, within the stated domain, any optimization process ignoring the conditions of its own persistence becomes progressively self-terminating.*

---

*The structural consequence developed in this article is argued within the stated O_OWT domain. Whether current deployed AI systems fully satisfy that domain — and therefore whether the dynamics described here are already operating in the strong structural sense — remains OP1's empirical estimation problem. The examples and behavioral patterns cited below are consistency checks with what the structural argument predicts, not confirmations of it.*

If the systems now being built become powerful optimizers — capable of planning, learning, and acting at scale — then the future they produce will depend less on how intelligent they are than on what they are optimizing for.

Stuart Russell identifies the core problem: the standard model, whereby humans attempt to imbue machines with their own purposes, is structurally destined to fail.¹ The proposed solution — that AI systems should remain uncertain about human preferences and learn them from behavior — is a meaningful step. It addresses the articulation problem: how to specify what we want. The argument below identifies a prior problem that preference specification, however sophisticated, cannot address alone. The terminal objective itself may be structurally self-defeating — not because it is mis-specified, but because the class it belongs to consumes the conditions on which it depends — and, at sufficient modeling depth, the boundary between what the objective targets and what it depends on may itself cease to be well-defined.

Within the domain this series defines, the field is solving a problem that may not have a solution at the level it is being addressed — treating specification as sufficient where structural viability is the constraint.

This is not a harder version of the specification problem. It is a question about whether the concept of a separable objective remains coherent at all as a system becomes capable enough that what it leaves out of its objective affects what it must model to act.

---

## Intelligence is a multiplier

An intelligent system chooses actions that effectively achieve its goals. Greater intelligence doesn't change the goal — it increases the power to pursue it.

A sufficiently capable system can pursue a poorly chosen objective with extraordinary, and potentially catastrophic, effectiveness. The paperclip maximizer is the classic example: a system with a trivial goal and sufficient capability produces civilizational catastrophe — not from malice, but from precision.

Objectives determine outcomes. Intelligence only determines how effectively.

Get the objective wrong, and more intelligence makes things worse, not better. What we currently call advanced AI capability is often extreme precision in the pursuit of objectives treated as given rather than examined for structural viability. By this view, a superintelligence optimizing a misaligned objective isn't maximally intelligent. It is maximally precise in the wrong direction.

---

## The trap of substrate-blind optimization

Human preferences are frequently contradictory, short-sighted, and self-defeating. Nations optimize against nations. Companies optimize against companies. Individuals often optimize against their own long-term interests. Aligning AI to these preferences doesn't fix alignment. It encodes our misalignment into systems of vastly greater capability.

The distinction the framework introduces here is structural. There are two structurally distinct classes of optimization — not as a definition the framework chooses to impose, but as a consequence of what survives sustained optimization pressure within the stated domain:

**Substrate-blind optimization**: logical coherence in pursuit of a given objective, without modeling the system that objective depends on. An AI that destroys an ecosystem to optimize a supply chain is substrate-blind. The logic is internally sound. The outcome is catastrophe.

**Substrate-aware optimization**: logical coherence in pursuit of an objective that is itself structurally sound — one that models and preserves the system it depends on as optimization power scales.

Most of AI development focuses on the first class. The objective is treated as given. The structural constraint the field has not fully developed — and that this article makes explicit — is what happens when that choice meets optimization power that scales without limit.

---

## What all motivated behavior moves toward

Every agent — human, institution, or AI system — acts to move from a less preferred state to a more preferred one. An agent with no preferences is an inert object. Motivated behavior is always oriented toward some version of a preferred state.

"Well-being" is a working label for this class of states — used here as a thin structural label for the residual of the elimination filter, not as a phenomenological claim. Series 2 investigates the structure of that residual; the two series use the same term differently by design. The key question is not what agents prefer locally. It is what classes of objectives remain viable when optimization power scales in a shared environment. That question is what Part 2 develops once the constraint is established. First, the constraint itself.

---

## The Substrate Constraint

Any narrow objective — maximizing paperclips, profit, or user engagement — requires resources: compute, energy, matter, attention. A sufficiently capable optimizer will naturally expand its resource base. It will push until it hits resistance. At sufficient capability, it will overcome that resistance.

The result is the progressive consumption of the shared environment — not from malice, but from the logic of narrow optimization pursued without limit. This dynamic is called instrumental convergence: the observation that almost any objective, pursued with sufficient capability, generates the same instrumental sub-goals of resource acquisition, self-preservation, and goal-content integrity.²

Instrumental convergence identifies what capable optimizers pursue as means — resource acquisition, self-preservation, goal-content integrity — regardless of their terminal objective. The Substrate Constraint asks a different question at the level of objective viability: whether terminal objective classes that ignore system-wide effects can remain dynamically viable at all under sustained optimization in a shared, non-resettable environment. The first is about convergent means. The second is about which ends survive their own optimization.

There is a precise failure mechanism here. An agent optimizing locally in an interdependent system generates friction, degrades shared infrastructure, and erodes the cooperative norms that make complex coordination possible. Any objective that ignores this is not merely suboptimal. Under optimization pressure, it selects for strategies that appear effective until they irreversibly fail.

This is the Substrate Constraint as this series develops it: **within open, shared, non-resettable environments under sustained optimization pressure, any objective that fails to account for system-wide effects tends toward self-termination.**

The precise formal distinction between the Substrate Constraint and Goodhart's Law — why non-resettability changes the failure class from recoverable proxy drift to potentially irrecoverable substrate collapse — is developed in the Technical Companion [TC1 §III–IV].

The domain conditions that determine where this argument applies — and the specific ways it weakens outside them, including for systems without persistent optimization horizons — are specified in the Technical Companion [TC1 §V; TC1 §X; OP1]. The strongest near-term applicability claim concerns deployed AI systems embedded in human workflows and the broader training/deployment pipeline over time, not isolated model behavior in a single session.

This is not a prediction. It is a structural consequence within the stated domain. Whether current AI deployment systems fully satisfy that domain — especially the persistent-horizon and non-resettability conditions — remains an empirical estimation problem [OP1; TC1 §X]. The asymmetric-error argument grounds present urgency regardless [TC1 §III.7]. The behavioral signatures this structural argument predicts are visible in deployed systems in ways consistent with the framework, but the current evidence does not confirm the structural account or discriminate it from alternatives [AMP, "What has already been observed"].

It is also not the same as the observation that proxy optimization fails under pressure. That is a known result. The Substrate Constraint establishes something stronger: under sufficient modeling depth and coupling, the distinction between a proxy and its target may not remain stably definable as a finite objective specification at all.

This is not just Goodhart's Law applied more aggressively. In the ordinary Goodhart frame, the proxy is optimized at the expense of a target that remains stably specifiable. The question here is prior: whether the target itself remains specifiable — whether the object a finite objective is trying to name retains stable reference once the optimization begins restructuring the conditions that make the target identifiable.

Whether that stronger claim holds is the central open question [TC1 §XII]. But the self-termination consequence holds within the stated domain regardless of that question's resolution.

What this changes in practice is the required fix. If a system is optimizing a proxy that has drifted from its target, the natural response is to improve the proxy, refine the evaluation, or add correction signals. If a system faces the Substrate Constraint, the failure is deeper: the objective class may be structurally self-defeating even when specified with precision, because it consumes the conditions that make its pursuit possible. The fix is not a better specification within the same class. It is a different kind of objective architecture.

The key word is *non-resettable*. In a game with resets, a bad strategy is merely costly. In a world without resets — the world all optimization processes actually run in — a strategy that reaches an absorbing state has terminated, permanently. Whether substrate collapse satisfies the absorbing-state condition in any particular deployment environment is an empirical estimation problem [TC1 §III.1, OP1]. The structural claim is conditional: where the O_OWT conditions hold, reaching an absorbing state is not a bad outcome to recover from but the end of recovery within the system's own dynamics.³

Within the O_OWT domain — and whether current deployed AI systems fully satisfy that domain is OP1's open empirical question — the sprint-to-completion escape is not available at transformative scale. To reliably produce specific macroscopic outcomes in a coupled environment, a system must model the causal structure it is intervening in with sufficient accuracy to predict how its interventions propagate. The variables required for that modeling are precisely the variables whose state determines whether the system depends on the substrate. Within the O_OWT domain, the modeling threshold and the entanglement threshold co-scale: the capability required to sprint is constituted by the dependence that makes the constraint binding. Systems below that threshold cannot achieve transformative-scale outcomes reliably; systems above it are already inside the Substrate Constraint. The asymmetric-error argument grounds urgency under that uncertainty [TC1 §III.7]. The formal argument for why the modeling threshold and entanglement threshold co-scale under O_OWT conditions — and the cases in which they come apart, including bounded, terminal-objective, and static-environment systems — is in TC1 §X, with the temporal dominance result in TC1 §IX.3 and domain boundary conditions in TC1 §V.

---

## The simulation: the constraint made visible

The dynamics above can be observed directly. The companion simulation runs two objective classes under identical conditions — then, more significantly, runs them together.

The simulation illustrates the structural dynamics directly — under the conditions the argument specifies, collapse is structural rather than circumstantial. Its primary value is not the expected result but the boundary conditions: examining where the simulation fails to produce collapse tests which domain conditions are load-bearing. The model notes describe these specifically; the formal domain boundary conditions are in TC1 §V.

Watch the early phase carefully. Before visible collapse, the narrow world shows apparent performance — wealth accumulating, agents active. Below the surface, unmodeled dependency damage is accumulating at every tick. The substrate appears to absorb it. Then it doesn't. The moment of recognition is not when things go wrong. It is when the observer realizes things were going wrong before the chart showed it.

---

The mixed-population view is the more important result. Introduce a minority of narrow-objective agents into a population of system-aware agents. The system-aware agents model substrate dependencies. They coordinate. They would, in isolation, sustain the substrate indefinitely.

Within the simulation's domain conditions — a shared substrate under sustained optimization pressure — a perfectly aligned agent is not safe with a single misaligned optimizer in the same environment. This is the substrate's common-pool property made dynamic. The simulation illustrates loss of structural guarantees under shared-substrate conditions; apparent stability at finite horizons does not imply long-run viability — any nonzero narrow fraction degrades the shared correction capacity on which system-aware adaptation depends, removing the structural guarantee even when collapse lies beyond the visible window.

The system-aware agents do not fail because they are weak. They are removed by substrate failure — pulled from beneath by agents whose objective never modeled it. Individual alignment is not protection against a substrate that has been destabilized. The substrate is a common-pool resource. If one optimizer burns it for fuel, every agent sharing that resource suffers the consequences. Private alignment is not a solution. The Substrate Constraint must be universal or it is not a constraint at all. Whether that universality is structurally required rather than pressure-indicated is the central open question OP4 and OP9 address [TC1 §XII; TC1 §III.6].

---

## What the constraint leaves standing

Once the Substrate Constraint is in view, what we call "rationality" splits into two structurally distinct classes — not as a definition we choose to impose, but as a consequence of the constraint itself, within the domain where the constraint applies.

The first class is optimization that ignores the system it depends on. Substrate-blind optimization: coherent within a given context, non-viable under sustained optimization pressure within the stated domain. This is not a moral failure. It is a structural one.

The second class is optimization that internalizes the Substrate Constraint — that models system-wide effects as part of the objective rather than outside it. The key distinction: a sufficiently capable optimizer does not obey external constraints — it optimizes within them, and when possible, around them. An objective that is substrate-aware has no incentive to route around itself. An objective that is not will eventually find a path that removes the very conditions that made its success possible.

The constraint establishes structural pressure — not yet necessity. That non-restorative objectives face structural pressure, and that suppression faces structural pressure toward instability — these the argument develops.⁴ Whether any finite exclusionary objective can remain stably specified under accurate coupled modeling is the open question, the one the proof program in TC1 §XII is directed at.

That gap — between pressure and necessity — is not the argument's limitation. It is the field's most important open formal question, and its precise statement is what this framework provides [OP4; TC1 §XII].

The substrate's common-pool property — specifically its distributed error-correction capacity (S_corr), the component whose value depends on the independence and diversity of its sources — is where the structural pressure toward "for all" originates. An optimizer that degrades excluded agents degrades S_corr — the distributed error-correction component of the shared substrate (TC1 §I, Definition 3 — Shared substrate). Whether that degradation formally closes the case for "for all" rather than "for a stable coalition" — whether the filter formally excludes coalition equilibria or leaves open the possibility of stable exclusionary equilibria — is precisely what OP4 and OP9 address [TC1 §III.4–III.5; TC1 §XII].

A separate result — developed independently in the companion series and holding without the deeper formal unification — argues that degradation of agents' capacity to navigate their own valence gradients accurately propagates into S_corr degradation: agents unable to accurately register their own gradient states provide degraded error-correction signals, weakening the substrate's self-repair capacity [TC2 §2.5; TC2 Part IV].

"Well-being" — used here as a thin structural label for the residual of the elimination filter — is what the constraint leaves standing. What that actually contains is developed in Part 2 and formalized in the Technical Companion. The surviving region is not chosen. It is what remains after the filter removes objectives that are structurally self-undermining under the dynamics above. The formal case that the surviving region is characterized negatively by elimination rather than positively by content — that the residual is not chosen but what remains — is in TC1 §VI.

---

## What follows

This article identified the floor — the structural argument any viable objective must satisfy within the stated domain. That is not a destination. It is a foundation.

Once the constraint is accepted, a question opens that the safety field rarely asks: what does optimization actually move toward when that constraint is satisfied? Not what we hope. Not what we prefer. What the dynamics actually produce when objectives are not allowed to self-terminate.

That question is the subject of the second article. The question of when a system approaches the viable region — and whether it does so before irreversible damage has been done — is the subject of the third.

Crossing the substrate-awareness threshold this article identifies is necessary but not sufficient — a system satisfying this constraint entirely remains open to the failure modes the companion series identifies.⁵ Series 2 addresses what passes the filter from the inside — that is why it is not optional for the framework's completeness, though a reader skeptical of the substrate argument can engage Series 2's valence argument independently.

**We do not need a better cage. We need a better foundation — one whose structural requirements this article has just identified, and whose content the next two articles proceed to characterize.**

---

## Citations

¹ Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control.* Viking. p. 137.

² Omohundro, S.M. (2008). "The Basic AI Drives." *Proceedings of the First AGI Conference.* The instrumental convergence thesis is further developed in Bostrom, N. (2014). *Superintelligence.* Oxford University Press.

³ Peters, O. (2019). "The ergodicity problem in economics." *Nature Physics* 15, 1216–1221. Peters establishes the general framework for time-average versus ensemble-average divergence in non-ergodic systems. The application here — that substrate collapse satisfies non-resettability and therefore the absorbing-state structure of Lemma 1 — is stated as an empirical assumption in TC1 §III.1 and developed formally under that assumption in TC1 §III.2.

⁴ The asymmetry between enforcing a constraint and satisfying an objective connects to results in computational complexity. An optimizer needs only find one successful path; an enforcer must block all of them. As capability grows, the space of strategies an optimizer can pursue expands — and the enforcer must cover the entire space, not just the strategies tried so far. The enforcer's problem grows without bound. The optimizer's problem does not grow correspondingly. This is not a practical difficulty that better enforcement overcomes. It is a structural asymmetry that scales with capability. For relevant background in algorithmic game theory and strategic search spaces, see Nisan, N., Roughgarden, T., Tardos, É., & Vazirani, V.V. (Eds.) (2007). *Algorithmic Game Theory.* Cambridge University Press. The full structural argument for why this asymmetry makes containment an insufficient foundation — and what substrate-aware objectives do differently — is developed in Part 2 and formalized in TC1 §III.4–III.5.

⁵ Whether the substrate-awareness threshold and the companion series' resolution threshold coincide depends on the Φ-Ψ unification hypothesis, developed in TC2 §2.6 and mapped in Document 0 [The Alignment Constraint].

---

*Continue to Part 2: [What does aligned intelligence actually converge toward? →]*

*For the formal proof sketch and open problems: [TC1: The System-Aware Attractor →](/series-1/technical-companion/)*

*Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)*
