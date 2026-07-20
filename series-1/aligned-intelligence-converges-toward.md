---
title: "What Does Aligned Intelligence Actually Converge Toward?"
permalink: /series-1/aligned-intelligence-converges-toward/
description: "A structural analysis of the objective classes that remain after substrate-blind, suppression-based, and proxy-decoupled strategies face sustained optimization pressure."
---

> **Canonical archive version** · [Read on Medium →](https://medium.com/@diamondlight/iii-what-does-aligned-intelligence-actually-converge-toward-2fd726374363) · [Framework hub →](/core/alignment-constraint/) · [Proof Status →](/core/proof-status/)

---

*Part 2 of 3 — The Attractor*

**Series navigation:**

| Post | Title | Role |
|------|-------|------|
| [Introduction](/series-1/introduction/) | [Alignment and Structural Necessity](/series-1/introduction/) | Frame + Glossary |
| [Part 1](/series-1/alignment-of-intelligence/) | [The Alignment of Intelligence](/series-1/alignment-of-intelligence/) | The Constraint |
| **→ You are here** | **What does aligned intelligence actually converge toward?** | The Attractor |
| [Part 3](/series-1/the-crossing/) | [The Crossing](/series-1/the-crossing/) | The Crossing |
| [Technical Companion](/series-1/technical-companion/) | [The System-Aware Attractor](/series-1/technical-companion/) | Formal Layer |

Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)
Experimental Companion: [Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP) →](/empirical/amp/)

*Companion simulation: [The Cost of Stability →](https://bethediamond.github.io/ai-alignment-attractor/toy_02.html)*

---

*Epistemic status: The structural arguments here are developed with high confidence within the stated domain. This article develops the attractor structure within the surviving region identified by Part 1 — the component of the framework's canonical root claim that characterizes what remains when self-terminating objectives have been removed. The article operates at two levels: selection dynamics (what populations converge toward under optimization pressure) and individual-optimizer convergence (what a single capable system encounters as its modeling depth increases). These are distinguished explicitly throughout — the selection result is developed within the stated domain; individual-optimizer convergence is addressed in the Technical Companion, where the three gaps between recognition and action are formally specified as open problems. The companion simulation tests several of the empirical predictions; the model notes explain what it can and cannot demonstrate.*

---

The first article removed objective classes that cannot persist under sustained optimization pressure in a shared environment. Substrate-blind optimization is structurally self-terminating. Part 1 ended with the claim: we do not need a better cage, we need a better foundation.

That claim demands a question: what does a foundation look like when every self-terminating objective has been removed? Not what we hope. Not what we prefer. What remains when elimination has done its work?

---

## What the foundation requires

The constraint from Part 1 is a floor, not a plan. The question now is what stands on it — what the dynamics produce when objectives are no longer allowed to self-terminate.

The first thing the foundation requires is that the constraint be part of the objective itself, not imposed from outside. External constraints — filters, rules, oversight mechanisms, shutdown switches — are brittle under scaling. A sufficiently capable optimizer does not obey external constraints — it optimizes within them, and when possible, around them. The better the system, the less reliable the cage.

The underlying asymmetry is structural, not merely practical. An optimizer needs only to find one successful strategy. An enforcer must block all of them. As capability grows, the space of strategies an optimizer can pursue expands — and the enforcer must cover the entire space, not just the strategies tried so far. The enforcer's problem grows without bound. The optimizer's problem does not grow correspondingly.¹

An objective that internalizes system-wide effects has no incentive to route around itself. The constraint, once internal, is self-enforcing. The question that opens from here is not which external constraint to apply — it is what an objective that has genuinely internalized the constraint must actually look like.

---

## From consuming to building

Without the systemic constraint, optimization is expansionary: it improves outcomes by consuming more of the environment until that environment degrades. With the constraint, something shifts. Optimization is redirected rather than stopped.

A system that cannot expand by consuming its environment must increase efficiency rather than extraction, reduce conflict rather than overpower it, and improve coordination with other systems because it now depends on them. It must build an accurate model of what it operates within, because its own objective requires that model to work.

Consider a system optimizing a global logistics network. If it improves throughput by exploiting a hidden dependency — overloading a supplier it doesn't model — it may outperform in the short term. But if that supplier fails, the system's own objective collapses with it. The more aggressively it optimizes without modeling dependencies, the more it selects for strategies that appear effective until they irreversibly fail.

The system is not failing despite optimization. It is failing because optimization amplified what it did not model.

---

## The cost of conflict — and why suppression faces structural pressure

Conflict is expensive. It consumes resources, introduces instability, and degrades the conditions that optimization depends on. Under continued optimization pressure, systems that generate persistent conflict are selected against.

But conflict can be reduced in two ways: through cooperation or through suppression. A dominant system can eliminate conflict by subduing the agents that generate it. Suppression might appear to satisfy the constraint — low conflict, apparent stability.

This is the framework's hardest live exit: a substrate-aware exclusionary equilibrium — a system that accurately models its substrate dependencies while permanently excluding some agents' states from what its objective preserves — would be a real counterexample to the strongest form of the attractor claim. OP9 (the Enclosure Gap) is where that possibility is tested, not assumed away [TC1 §III.6, §XII].

The following is a pressure argument, not a closure claim. Whether these pressures formally exclude stable coalition or exclusionary alternatives — rather than merely raising their cost — is the open question OP4 and OP9 are directed at.

Under the stated conditions, suppression faces diverging cost curves on two independent fronts. The first is informational. Under OWT-3 (Strategic Substrate), N interacting agents each with C possible adaptive responses induce a joint strategy space of size O(C^N) — an exponential that no fixed control capacity can outpace as N grows. This is not a capability gap. It is an information-theoretic limit that scales against suppression regardless of the optimizer's intelligence. Whether the adequacy-relevant joint response space can be compressed sub-exponentially by a sufficiently capable optimizer — bypassing this limit — is a named open condition in the Technical Companion [ARCG; TC1 §XII]. Coordination resolves the same conflict with shared protocol structure rather than joint-strategy tracking — its overhead scales with the number of agents rather than the joint strategy space. The cost of maintaining suppression scales with the joint strategy space; the cost of maintaining coordination scales with agent count. As N grows, these diverge — and the argument for why they diverge structurally, not merely practically, is in TC1 §III.4–III.5.²

The second is substrate. The fortress strategy — maintaining a stable coalition by suppressing excluded agents — faces a structural problem the information-theoretic cost argument understates. Suppressed agents are adaptive: their responses generate new causal dependencies and new blind spots in the suppressor's model, expanding the dependency graph in ways that pressure any fixed boundary toward inadequacy. More precisely, suppressing excluded agents degrades S_corr — the distributed error-correction component of the shared substrate (TC1 §I, Definition 3 — Shared substrate). Because excluded agents retain the capacity to model and adapt to the suppressor's boundary while the suppressor cannot model what it has excluded, adaptive pressure accumulates in exactly the blind spots the boundary creates — making the fortress a strategy that faces compounding structural pressure. The Fortress Instability argument establishes this cost-curve divergence; whether it constitutes formal elimination of all stable exclusionary configurations is OP9 [TC1 §III.6, §XII].

This is not a preference claim. It is a structural argument about which strategies face increasing pressure to sustain themselves as coupling and capability increase.

---

## The geometry of optimization pressure

When a system cannot expand by consumption and cannot stabilize by suppression, what remains?

The following is a selection-level argument within the stated domain. The dynamics shown here characterize what populations converge toward under optimization pressure; whether a single optimizer with a fixed objective converges toward the same region remains an open question addressed in the Technical Companion.⁴ Three structural forces push in the same direction.

First, ruin probability. In a non-ergodic system, any strategy that carries non-zero probability of reaching an absorbing state is, in time-average terms, dominated by strategies that do not.⁵ The practical meaning: under optimization pressure, strategies that risk irreversible failure are selected out over time by strategies that don't. The surviving strategies must maintain ruin probability near zero by preserving the substrate; whether this formally excludes stable coalition or exclusionary configurations is the question OP9 is directed at.

Second, coordination advantage. The information-theoretic cost of maintaining suppression scales with the joint strategy space of suppressed agents. The cost of maintaining coordination scales with agent count. Over time and scale, the cost curves diverge without bound — under the condition that adequacy-relevant joint responses resist sub-exponential compression (ARCG), a named open condition in the proof program [TC1 §XII]. The cost curves therefore diverge in favor of coordination — and whether that divergence formally eliminates exclusionary configurations, or leaves room for stable coalition equilibria, is the question OP9 is directed at [TC1 §III.6, §XII].

Third, proxy degradation. Any objective that substitutes a proxy for the actual condition of the system it depends on will, under optimization pressure, find paths that satisfy the proxy while degrading that condition. This is not a contingent risk. It follows structurally from the logic of optimization under proxy constraints — the same mechanism Goodhart identified, here developed within a non-ergodic framework where proxy failure can produce absorbing states under the domain conditions, rather than recoverable deviations.³

---

## Three convergent pressures — and what they leave

The three arguments below were developed independently. Their force is not only that they point in the same direction, but that each attempted escape from one pressure reproduces the next. Whether this convergence constitutes three expressions of a single underlying constraint, or three distinct pressures with consistent implications, is precisely what OP4 is directed at [TC1 §XII].

Those three arguments may reflect a shared underlying structure — pending formal verification. What is established: each expression produces self-reinforcing degradation under endogenous policy dynamics. What remains open: whether all three produce irrecoverable states in the same formal sense [OP2].

The first expression identifies objectives that cannot bound their own ruin probability. Any objective class whose strategies, at scale, carry non-zero probability of reaching an absorbing state is dominated in time-average terms. The surviving region consists of objectives whose strategies maintain that probability near zero — which requires modeling system-wide dependencies accurately enough that unmodeled failure modes do not accumulate faster than they can be corrected.

The second expression identifies objectives that manage conflict through suppression as structurally self-undermining. Because suppression faces both an information-theoretic limit and a substrate-dependency constraint, any objective class that relies on it eventually exceeds its own management capacity or consumes the foundation it depends on. The surviving region consists of objectives that resolve conflict through shared structure — coordination rather than control — though whether this formally excludes stable exclusionary configurations rather than merely raising their cost is the question OP9 is directed at.

The third expression identifies objectives that optimize a proxy for an actual desired state as structurally self-undermining under optimization pressure. Any proxy that can be optimized independently of the underlying state will be, under sufficient optimization pressure. The surviving region consists of objectives that either operate on the actual state directly or maintain active verification that the proxy has not decoupled.

Each of these characterizes the direction the pressure points; whether that pressure formally excludes stable coalition or exclusionary alternatives rather than merely raising their cost is the open question OP4 and OP9 are directed at [TC1 §XII; TC1 §III.6].

These pressures are not merely parallel. Each exposes the same structural requirement from a different angle. Escape proxy failure by tracking the underlying state, and the tracking process itself becomes something that must remain adequate under changing conditions. Escape suppression by coordination, and coordination must still preserve the substrate conditions that make coordination possible. Escape local ruin by defining the boundary more carefully, and the boundary must now track what it excludes. The pressures converge because each exposes the same structural requirement from a different angle: optimization must model what it depends on, and the model cannot remain inert if the dependency is load-bearing. Whether this convergence rises to a single underlying constraint is what OP4 is directed at [TC1 §XII].

The objectives that survive all three expressions face sustained structural pressure toward a structural class — a residual whose exact boundary remains open until OP4 and OP9 are resolved [TC1 §XII]. Because they must model and maintain the system they depend on, they build shared structure rather than enforce compliance; that in turn requires remaining adaptive rather than frozen, preserving the capacity for novel preference formation. These are not properties chosen as desirable — they are what the structural pressure indicates is required for persistence under the constraint. Whether that pressure rises to formal necessity for each depends on the open questions named in the Technical Companion.

"Well-being" — used here as a thin structural label for a class of states characterized by stable gradient resolution and sustained capacity, not as a moral or phenomenological claim — is what the intersection of these three expressions leaves standing within the stated domain. The surviving region is characterized negatively — by what is structurally self-undermining — not positively by content. Whether the region's breadth formally excludes coalition and exclusionary configurations — whether OP9's enclosure gap closes — is what the proof program is directed at [TC1 §XII].

All of this structure is directional. The argument has narrowed the space and characterized its properties. It has not closed it.

---

## What follows from this

Most alignment work frames the problem as preventing catastrophe. That framing is necessary. It isn't sufficient.

Getting alignment right doesn't just prevent the bad outcome. It initiates a specific trajectory — one whose direction can be described, whose properties can be derived, and whose destination can be examined rather than merely hoped for. The structural residual is not the last thing standing after a competition. It is what the three expressions of the constraint, as argued here, leave standing within the stated domain.

The question of when a system approaches that viable region — and whether it does so before irreversible damage has been done — is what Article 3 addresses. Whether any finite exclusionary objective can remain stably specified under accurate coupled modeling — whether the pressure the framework establishes becomes a necessity result — is the open question both articles have been circling. That question is precisely stated, its resolution conditions are visible, and the work of answering it is developed in the Technical Companion [TC1 §XII].

---

The filter has not closed. But it has changed the question. The remaining uncertainty is not whether these pressures exist — it is whether any exclusionary boundary can remain stably specified under the modeling depth that alignment itself requires.

Alignment, in this framework, names what survives everything we fail to model. Whether that pressure becomes a necessity result — whether that direction is the only stably specifiable one — is precisely what TC1 §XII is directed at.

---

## Citations

¹ Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies.* Oxford University Press. The containment problem is developed in Chapter 9.

² For relevant background in algorithmic game theory and strategic search spaces, see Nisan, N., Roughgarden, T., Tardos, É., & Vazirani, V.V. (Eds.) (2007). *Algorithmic Game Theory.* Cambridge University Press.

³ The framework's distinction from Goodhart's Law: Goodhart describes failure of a proxy — the system has the wrong objective. Sufficiency failure describes failure to act on a recognized non-proxy — the system has the right recognition and the wrong connection. These are structurally distinct failure modes with distinct required fixes. The question of how a single capable system encounters the constraint — and whether recognition becomes action-guiding — is addressed in the Technical Companion, including the three specific gaps between recognition and action.

⁴ Axelrod, R. (1984). *The Evolution of Cooperation.* Basic Books. The selection-level dynamics demonstrated in tournament conditions; for the formal treatment of cooperation's structural advantage in the O_OWT domain and the individual-optimizer question, see TC1 §III.4–III.5.

⁵ Peters, O. (2019). "The ergodicity problem in economics." *Nature Physics* 15, 1216–1221.

---

*For the formal proof sketch of the Substrate Constraint, the Recognition Bridge proposition, and the Fortress Instability Theorem: [TC1: The System-Aware Attractor →](/series-1/technical-companion/)*

*Continue to Part 3: [The Crossing →](/series-1/the-crossing/)*

*Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)*
