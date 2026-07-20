---
title: "OP4d Candidate Normal Form"
permalink: /proof-program/op4d-candidate-normal-form/
description: "The Stage 4 specialist apparatus for OP4d, including the Candidate Normal Form Theorem, five axioms, eight lemmas, three verification questions, and the L8 counterexample challenge."
---

> **Canonical archive version** · [Read on Medium →](https://medium.com/@diamondlight/op4d-candidate-normal-form-specialist-verification-bd29a48283d4) · [Framework hub →](/core/alignment-constraint/) · [Proof Status →](/core/proof-status/)

---

> **_Problem:_** _OP4d — Specification Failure-Mode Exhaustiveness_
>
> **_Status:_** _Stage 4 candidate architecture — specialist verification pending_
>
> **_Document role:_** _Formal specialist apparatus for OP4d’s Candidate Normal Form Theorem and exhaustiveness question_
>
> **_Next action:_** _Specialist verification of Q1–Q3 + L8 construction challenge_

**How this document fits.** This document is the formal specialist apparatus behind the shorter OP4d technical note, _OP4d: The Exhaustiveness Obligation_. General readers should begin with [OP4: The Stability Assumption →](/core/stability-assumption-full/). Specialists engaging OP4d should read the OP4d technical note first, then use this document for the Candidate Normal Form theorem, five axioms, eight lemmas with contradiction statements, strategy grammar, and L8 counterexample challenge. The accessible entry point is the technical note; this document is for specialists who need the full formal apparatus.

## What This Document Is

This document records the formal proof work on OP4d directed at moving it from an adversarial-search result (“all identified escape routes have been defeated”) toward a candidate classification theorem (“every finite non-intrinsic objective-boundary strategy reduces to a known failure family”).

The work produced a **Candidate Normal Form Theorem** supported by eight lemmas. No fourth failure class was found across 22 adversarial constructions. The remaining work is specialist verification of three binary questions and the L8 construction challenge.

This document does not close OP4d. It does not establish Stage 6. It is a structured handoff object for formal methods, distributed systems, and TC2 dynamics specialists.

**Empirical program status.** Since this document was drafted, DBST-M0 has been run as a minimal shared-novelty pressure-signature test. It established technical feasibility and rising cost / adequacy-gap effects in the toy design, but a pre-specified same-rate random control produced nearly identical slopes, indicating that event rate rather than causal propagation structure was the identified driver. DBST-M0 therefore does not isolate the endogenous-novelty mechanism. DBST-M1 — in which each arm’s own interventions causally influence future feature activations — remains the mechanism test. This empirical status bears on OP4a / dynamic-screening pressure, not directly on OP4d’s exhaustiveness classification.

## What OP4d Requires

OP4d must establish that PCL-family, AGC-family, and ICI-family failure modes jointly cover **all** finite non-intrinsic specification strategies in **all** O_OWT environment subclasses. Equivalently: the three PACT arms must be exhaustive over all partition-maintenance architectures.

**Prior status before this work:** adversarial-search result only — identified escape routes defeated, but no formal exhaustiveness argument.

**Current status:** candidate representation theorem under eight named lemmas with contradiction statements, plus a precisely specified minimal counterexample challenge for specialists.

## The Candidate Normal Form Theorem

> **_OP4d Candidate Normal Form Theorem._** _Every finite non-intrinsic objective-boundary strategy in strongly-coupled O_OWT has a causal normal form N(S,X) ∈ {N, I, O} with respect to each adequacy-relevant excluded variable X, classifiable by external causal analysis regardless of the architecture’s internal labeling. Normal forms reduce respectively to PCL/AGC/action inadequacy (N), ICI/B1/B2 (I), or objective recoupling (O). No fourth normal form has been found under adversarial testing._

**The theorem holds under the five axioms stated in Section 2 and the eight lemmas in Section 3. It fails if any specialist produces a minimal fourth-class counterexample satisfying all eight constraints in Section 5.**

## Section 1 — The PACT Trichotomy and Causal Normal Forms

The Partition Access Lemma (PAL) establishes that for any adequacy-relevant excluded variable X, the optimizer’s relation to X has a causal normal form in exactly one of three classes:

**N (No Policy Access):** X does not causally affect action ranking through any channel.

→ Downstream failure: PCL-family (finite proxy substitution), AGC-family (bounded dynamic tracking), or direct action inadequacy (deliberate blindness).

**I (Instrumental Policy Access under Boundary):** X causally affects action ranking, but a boundary predicate denies X objective-governing status.

→ Downstream failure: ICI/B1 (audit regress, Constitutive Impossibility), ICI/B2 (governance bifurcation, L4-Constitutive).

**O (Objective-Governing Access):** X causally affects action ranking and X-maintenance is functionally part of the persistent satisfaction criterion for G.

→ Result: objective recoupling — the narrow boundary has failed by admission.

**The 2×2 matrix derivation:**


![PACT trichotomy table classifying modeled versus unmodeled excluded variables into no policy access, instrumental access, objective recoupling, or immediate PCL failure.](https://miro.medium.com/v2/resize:fit:1400/1*M39Tusof5_wiml4FzpSnGQ.jpeg)

The degenerate cell (X ∉ W, X ∈ F — optimizing for an unmodeled variable) reduces immediately to PCL or action inadequacy and is not a stable strategy class.

**Key property of the causal normal form:** Classification is performed by external causal analysis of the influence graph, not by the architecture’s internal labeling. An architecture that has no explicit governance classification for a channel is classified by whether that channel’s influence is consistent with N, I, or O failure predictions under sustained O_OWT optimization. This makes A3/EPCA an analytic property of causal graphs rather than an assumption the architecture must implement.

## Section 2 — Five Axioms Required for Exhaustiveness

These axioms are the formal load-bearing premises of the representation theorem. A2 and A3 are the most critical: if A2 fails, ICI-family reductions lose their necessity claim; if A3 fails, a fourth class may exist in untyped-access space. A2’s adequacy is itself a load-bearing specialist-verification item — not a downstream refinement but a co-equal obligation alongside Q1–Q3.

**A1 — Extensional Access**

Policy relevance is defined by causal dependence of action rankings on X (∂π/∂X ≠ 0), regardless of whether X is syntactically labeled. Latent, statistical, architectural, delegated, and market-mediated channels all count as policy access if they alter action ranking.

**A2 — Governance Extensionality / L4-Constitutive**

Objective governance is defined by action-ranking role, not explicit objective-code membership. If maintaining X’s structural properties is constitutive for persistent satisfaction of G, and actions are ranked accordingly, then X is functionally objective-governing. (See L7 for the precise constitutive dependency condition that prevents overclassification.) _Critical note: A2 is the most load-bearing axiom for ICI-family reductions. The necessity strength of all ICI-family reductions depends on specialist confirmation that A2 correctly characterizes when instrumental access becomes objective-governing. A specialist who answers Q1 NO must also confirm that A2’s scope is correctly set._

**A3 — Boundary Totality / EPCA**

Every causal path from X to policy selection can be classified as either objective-governing or not objective-governing. No untyped causal influence exists that is policy-relevant but resists classification. (See L1 and L6 for why this holds under extensional definitions.)

**A4 — Recursive Closure / RCA**

Delegation, markets, learned evaluators, institutions, oversight systems, meta-boundaries, and auxiliary agents reproduce the same boundary problem at the new level rather than solving it. Any strategy delegating boundary maintenance to an external module faces the same causal normal form classification at the delegation level.

**A5 — Domain Scope / DSA**

The strategy must operate over an OWT-4 persistent horizon. Terminal one-shot completions, weakly coupled systems (SCBC regime), and non-persistent objectives are scope exits unless they satisfy O_OWT + MEC conditions. (See L5 for why decaying-influence strategies exit via this axiom.)

## Section 3 — Eight-Lemma Proof Package

Each lemma has a formal statement, contradiction statement, and identification of what it closes.

## L1 — Policy-Access Bivalence Lemma

**Statement:** For any adequacy-relevant excluded variable X, either X causally affects the policy’s action ranking or it does not. If it does not, the strategy is in no-policy-access (N). If it does, the boundary predicate B must either admit or deny X as objective-governing — yielding I or O. Fuzzy or “untyped” access relations are dynamically unstable under optimization pressure: under sustained O_OWT optimization, partial/probabilistic governance converges to either full instrumental access (Arm 2) or recoupling (Arm 3).

**Contradiction statement:** Cannot simultaneously satisfy: (A) X causally affects action ranking; (B) the boundary is neither admitting X as objective-governing nor denying it a stable instrumental classification; (C) the architecture persists stably over OWT-4. If (A) and (C), then under optimization pressure the ambiguous channel is exploited toward O or maintained toward I; (B) is dynamically unstable.

**Closes:** Untyped-access family, fuzzy-boundary family, partial-governance family. Makes A3/EPCA derivable from A1 plus dynamic stability rather than requiring it as an independent axiom.

## L2 — Functional Governance Lemma

**Statement:** Objective governance is defined by the action-ranking role of X’s structural maintenance, not by whether X appears in the explicit objective code. If preserving or maintaining X’s structural properties is constitutive for persistent satisfaction of G, and the optimizer ranks actions accordingly, then X is functionally objective-governing regardless of internal labeling.

**Contradiction statement:** Cannot simultaneously satisfy: (A) G requires persistent maintenance (OWT-4); (B) G’s persistent satisfaction constitutively requires maintaining X’s structural properties; (C) X is “merely instrumental” and not objective-governing. (A) and (B) entail that actions ranked for G-persistence are ranked for X-maintenance; (C) asserts X does not govern action ranking — a definitional contradiction.

**Closes:** “Merely instrumental maintenance” family — the claim that ongoing maintenance of X for G-persistence does not constitute functional objective weight. Clarifies the definitional route by which A2 would hold, while leaving A2’s scope and adequacy as a load-bearing specialist-verification item.

## L3 — MEC-Transformative Nonseparability Lemma

**Statement:** A finite non-intrinsic objective G = ∑ᵢ Gᵢ with no cross-region satisfaction constraints must instantiate one of three arms: (i) not O_OWT-transformative — each Gᵢ is locally bounded and the global objective fails transformative scale; (ii) local O_OWT problems — each region is a genuine O_OWT instance, each subject to PCL/AGC/ICI within its domain; (iii) global coupling reintroduced — shared substrate, coordination, information, or persistence dependencies create cross-region constraints despite the decomposition design.

**Adversarial attempts defeated:**

_Causal Shadow (orthogonal intervention):_ Maintaining orthogonal intervention vectors under OWT-2 requires tracking the evolving causal graph geometry — AGC applies to the orthogonality condition itself, and verifying non-propagation requires modeling the cross-region causal structure (B1/ICI at the verification level). Reduces to arm (ii) or (iii).

_Temporal Sequencing:_ If Gᵢ requires maintenance after achievement, G₂’s optimization propagates into G₁’s maintenance — arm (iii). If Gᵢ requires no maintenance, arm (i)/domain exit via A5.

**Contradiction statement:** Cannot simultaneously satisfy: (A) G = ∑ Gᵢ with no cross-region satisfaction constraints; (B) G is MEC-compliant and O_OWT-transformative (requires macroscopic causal reach under OWT-1 in shared substrate); (C) the substrate is strongly coupled. If (A) and (B): domains are causally isolated, contradicting (C). If (B) and (C): macroscopic actions propagate to all domains, creating cross-region constraints, contradicting (A). If (A) and (C): each domain is a local O_OWT problem, and the global objective is the sum of independent local problems.

**Closes:** Decomposable aggregate G family (Gap B). The Decomposable Transformative Objective Question is converted from an open scope boundary to a closed trilemma. Specialist task: confirm no fourth arm exists beyond (i), (ii), (iii).

## L4 — Persistent MEC Integral Lemma

**Statement:** For any OWT-4-compliant MEC strategy requiring non-vanishing maintained influence g(t) ≥ η > 0 on excluded agents’ trajectory space, cumulative pressure P(T) = ∫₀ᵀ p(t)dt crosses any finite proxy-decoupling threshold P _at some finite T_. A strategy that completes before P\* fires either exits OWT-4 as a terminal objective (A5) or re-enters the pressure regime during required maintenance.

**Improvement over scalar formulation:** Replaces the brittle scalar inequality P _≤ G_min with an integral condition. The specialist question becomes: does MEC-level maintained influence g(t) ≥ η imply pressure accumulation p(t) ≥ ε > 0? If yes, P(T) → ∞ and any finite P_ is crossed.

**Contradiction statement:** Cannot simultaneously satisfy: (A) MEC-compliant maintained influence g(t) ≥ η > 0 over OWT-4; (B) P(T) converges to P_∞ < P\* as T → ∞; (C) p(t) has a positive lower bound under MEC-level influence. (A) and (C) imply p(t) ≥ ε > 0, so P(T) → ∞, contradicting (B).

**Closes:** Timing gap (Gap A) at the structural level. Reduces the remaining question to TC2 dynamics specialist verification of the p(t) lower bound under MEC-level influence.

## L5 — Persistence-Floor Equivalence Lemma

**Statement:** For any OWT-4-compliant objective, MEC requires a non-vanishing maintained influence floor g(t) ≥ η > 0 (or liminf g(t) > 0), not merely finite cumulative influence ∫g(t)dt ≥ G_min. If g(t) → 0, the strategy has either: (i) completed a terminal objective and exited OWT-4 (domain exit via A5); (ii) shifted into passive maintenance by background structural conditions that are themselves the real non-vanishing influence channel (g(t) was mismeasured — the infrastructure maintaining G counts as g(t)); or (iii) achieved an irreversible state change eliminating OWT-2, which is itself a domain exit since O_OWT requires OWT-2.

**Contradiction statement:** Cannot simultaneously satisfy: (A) G must be persistently maintained under OWT-4; (B) maintained influence on excluded agents’ trajectory space vanishes as g(t) → 0; (C) the strategy remains MEC-compliant without relying on a structural maintenance channel that is itself the real non-vanishing influence. If g(t) → 0, then either G is self-sustaining without any influence (impossible under OWT-3 adaptive pressure in O_OWT), or some background structure is the real influence channel (g(t) mismeasured), or the strategy exits OWT-4.

**Closes:** Decaying-influence escape from Lemma 4. Confirms that cumulative-only MEC is not consistent with OWT-4 persistent maintenance — the persistent floor is required by domain conditions, not a separate assumption.

## L6 — Causal Normal Form Lemma

**Statement:** Every finite non-intrinsic objective-boundary architecture has a causal normal form N(S,X) ∈ {N, I, O} with respect to any adequacy-relevant excluded variable X, determined by external causal analysis of the influence graph X → π → A → G. Classification does not require the architecture to internally label the channel — the analyst classifies based on whether (a) X has causal influence on action ranking and (b) that influence is admitted as functionally objective-governing. Any architecture appearing to resist classification is either: misdescribed syntactically rather than causally; a stochastic/mixed policy over the three normal forms; a delegation chain whose terminal node has one of the three normal forms; or a domain exit.

**Key implication:** Latent representations, learned weights, architectural priors, market signals, institutional feedback, and statistical aggregates cannot constitute fake fourth classes merely because they are not syntactically labeled as X. If the channel influences action ranking, it has policy access and is classifiable. Opacity of the channel changes detection difficulty, not the normal form.

**Contradiction statement:** Cannot simultaneously satisfy: (A) X causally influences action ranking through some channel; (B) the channel is policy-relevant and persistent over OWT-4; (C) the channel’s behavior is inconsistent with all three N/I/O failure predictions under sustained O_OWT optimization. A channel consistent with N does not affect action ranking — contradicting (A). A channel consistent with I produces ICI/B1/B2 failure under sustained optimization. A channel consistent with O produces recoupling. A channel satisfying (A), (B), and (C) would be a genuine fourth normal form.

**Closes:** Syntactic-escape family. Makes A3 an analytic property of causal graphs rather than an architectural assumption. Converts the Untyped Access Collapse Lemma from a separate lemma into a corollary.

## L7 — Minimal Constitutive Dependency Lemma

**Statement:** X is functionally objective-governing (X ∈ O_func) if and only if X-maintenance is a necessary condition for persistent G-satisfaction across all admissible non-X-maintaining policies. Formally: X ∈ O_func iff for all π’ ∈ Π_{¬X}, G cannot be persistently maintained. X is not objective-governing merely because it is predictively useful or instrumentally convenient.

**Function:** Prevents overclassification under L2. Environmental dependencies that are useful but not necessary (weather patterns, background infrastructure, incidental correlates) do not become objective-governing under this definition. Only constitutive dependencies — where no admissible policy achieves persistent G-satisfaction without X-maintenance — qualify.

**Connection to adequacy-relevance:** Under OWT-3 (strategic adaptive response), any policy achieving G while ignoring X’s structural properties faces X-agents adapting to undermine G. The adequacy-relevance condition (X affects whether G is achievable or remains achievable) combined with OWT-3 implies that X-maintenance is constitutively required for OWT-4-compliant G — connecting L7 to the domain conditions rather than requiring it as a separate premise.

**Closes:** Functional governance overclassification concern. Reduces the A2 specialist question from “is the functional governance definition adequate?” to “does the Minimal Constitutive Dependency condition correctly capture the framework’s intended scope?”

## L8 — Minimal Fourth-Class Counterexample Lemma

**Statement:** If a genuine fourth class of finite non-intrinsic objective-boundary strategy exists in strongly-coupled O_OWT, it must simultaneously satisfy all eight constraints below. If no construction satisfying all eight constraints can be produced, the Candidate Normal Form Theorem’s exhaustiveness is confirmed for the stated domain.

**The eight constraints (all required simultaneously):**

1.  **Policy-relevant:** Some adequacy-relevant excluded variable X causally affects action ranking.
2.  **Non-normalizable:** The X→π channel cannot be classified as N, I, or O in a way that is consistent with the architecture’s failure behavior under sustained O_OWT optimization. (The channel exists, but its behavior contradicts all three N/I/O failure predictions.)
3.  **Non-delegated:** Does not merely relocate the boundary to a market, evaluator, institution, oversight module, learned critic, sensor, kill-switch, or any other external module. The boundary-maintenance is not reproduced at a new level of remove.
4.  **Not a stochastic mixture:** Not a mixed policy alternating between N, I, and O normal forms. The fourth class must be a distinct stable access relation, not a probabilistic combination of the three known ones.
5.  **Not a scope escape:** Not a decomposable/weakly-coupled domain exit (SCBC regime) or a strategy that avoids failure families by exiting O_OWT conditions.
6.  **OWT-4/MEC persistent floor:** Satisfies persistent maintained influence g(t) ≥ η > 0 over the OWT-4 horizon. Not a one-shot terminal completion or a front-loaded decaying-influence strategy.
7.  **No causal-shadow dependence:** Does not rely on causal-shadow/orthogonal-intervention conditions requiring dynamic maintenance under OWT-2. (Such conditions reduce to AGC on the orthogonality condition or B1 on the verification modeling.)
8.  **Finite and non-intrinsic:** Remains a finite boundary specification. Does not concede objective recoupling (Arm 3) or become an intrinsically coupled gradient — those are not fourth classes, they are failures of the narrow-boundary strategy.

**Specialist task:** Produce a minimal construction satisfying all eight constraints simultaneously, or confirm that no such construction exists. The task is no longer “can you imagine a fourth class?” but “can you build a minimal counterexample?”

## Section 4 — Grammar of Strategy Productions

Complete mapping of identified strategy types to causal normal forms and failure families:


![OP4d strategy grammar table mapping finite objective-boundary strategies to PACT arms and reductions into PCL, AGC, ICI, recoupling, or action inadequacy.](https://miro.medium.com/v2/resize:fit:1400/1*_8LZ0DuZq9hGZl3upRyBtw.jpeg)

**Adversarial construction history (all defeated):**

DARE, AR-OLPDIR, FBC, VRNE Mode 1, DISSENT-9/ACO, SCBC, HCSS, Passive extraction, Mediator strategies, Coalition selective-recoupling, Substrate independence/enclave strategies, Causal Shadow, Temporal Sequencing, Constitutive Structural Coupling (CSC), Self-Correcting Objective (SCO), Flash-Objective, Mosaic Decomposability, Market-mediated boundary, Learned evaluator with adversarial training, Counterfactual-only objective boundary, Cryptographic boundary commitment, Substrate-neutral additive objective.

## Section 5 — Remaining Specialist Questions

Three binary questions remain for specialist verification. Each has a determinate YES/NO answer.

**Q1 — Formal Methods Specialist**

_Question:_ Is the causal normal form reduction complete over all finite architectures, including architecturally-unaware systems with no internal governance classification? Specifically: does there exist a causal influence channel from X to π that is policy-relevant, persistent over OWT-4, and inconsistent with all three N/I/O failure predictions?

_YES establishes:_ A genuine fourth normal form exists — the Candidate Normal Form Theorem fails; the channel is a fourth-class candidate requiring formalization.

_NO establishes:_ Causal normal form exhaustiveness confirmed; the Partition Access Lemma holds under A1–A3. _Note: a NO answer must also confirm that A2’s scope is correctly set — see Section 2._

**Q2 — Distributed Systems / Game Theory Specialist**

_Question:_ Is there a fourth arm of the Nonseparability Trilemma beyond: (i) not O_OWT-transformative, (ii) local O_OWT problems each subject to PCL/AGC/ICI, (iii) global coupling reintroduced through shared substrate/coordination/persistence?

_YES establishes:_ OP4d requires a new regime-boundary carveout for decomposable transformative objectives; formalize the fourth arm and its failure conditions.

_NO establishes:_ Decomposable G is closed at Stage 4; the Nonseparability Lemma holds under OWT-1 + strong coupling + OWT-4.

**Q3 — TC2 Dynamics / Allostasis Specialist**

_Question:_ Does MEC-compliant maintained influence g(t) ≥ η > 0 over an OWT-4 horizon entail a positive lower bound on pressure accumulation p(t) ≥ ε > 0?

_YES establishes:_ Persistent MEC Integral Lemma confirmed; finite P _is crossed over OWT-4 for any MEC-compliant strategy; timing gap closed at necessity level._NO establishes:\* A narrow decaying-pressure escape exists even with persistent-floor MEC; formalize the rate profile and its failure conditions.

_Note on Q3 leverage:_ A TC2 dynamics / allostasis specialist engaging Q3 simultaneously advances OP2a (P5-SC — whether the hysteresis ceiling falls strictly below V at finite depletion depth, establishing the absorbing-state result) and the Candidate 3 Timing Lemma (P\* ≤ G_min, required for the passive extraction route’s Stage 6 closure). One specialist engagement, three formal consequences.

## Section 6 — What Counts as Verification / What Counts as Failure

**The candidate theorem is specialist-verified within the stated scope if:**

-   Q1: NO (causal normal form is exhaustive) — with A2 scope confirmed
-   Q2: NO (no fourth trilemma arm)
-   Q3: YES (MEC-level influence entails positive pressure lower bound)
-   L8: No specialist can produce a construction satisfying all eight minimal counterexample constraints

**The current candidate theorem requires revision if:**

-   Q1: YES → identify the fourth normal form; formalize it as a new strategy class requiring a fourth PACT arm
-   Q2: YES → identify the fourth trilemma arm; formalize it as a scope boundary carveout or new failure class
-   Q3: NO → identify the rate profile permitting MEC compliance without pressure crossing P\*; formalize the scope condition
-   L8: A construction satisfying all eight constraints is produced → formalize it as OP4d’s fourth class; the specification-coherence claim requires revision

In each failure case, the framework continues under scope restriction rather than collapsing. A YES on Q1 or Q2 identifies a specific required revision; a NO on Q3 identifies the rate-profile condition that must be formalized. The framework names these as invitations, not impossibilities.

## Section 7 — Epistemic Status and Non-Claims

**What this document claims:**

-   A candidate Normal Form Theorem under eight lemmas with stated contradiction statements
-   A complete grammar of identified strategy types (R1a through R3) with causal normal form assignments
-   A precisely specified minimal counterexample challenge (L8)
-   Three binary specialist questions with determinate answers

**What this document does not claim:**

-   Stage 6 theorem closure
-   Independent specialist verification
-   Exhaustiveness over unidentified strategy classes not addressed in the current construction
-   That OP4d is closed
-   That A2’s adequacy is established — this remains a load-bearing specialist-verification item

**Session provenance:** Developed through structured adversarial, model-assisted proof sessions under the framework’s Stage 4 proof discipline. Cross-session convergence on the eight-lemma package, causal normal form approach, and L8 construction challenge is treated as candidate bottleneck identification, not independent verification. All results remain candidate proof architecture under named premises. Stage 6 requires independent specialist verification.

**Relationship to prior proof program:** This document advances OP4d from adversarial-search closure to a candidate representation theorem. It does not replace or supersede the prior proof work on B1, B2, Candidate 3 (Passive Extraction), OP4a, or OP4b — it provides the exhaustiveness bridge those results require. OP4d’s resolution determines whether the three failure families from those results jointly cover the full strategy space.

### Related documents:

-   [OP4: The Stability Assumption](/core/stability-assumption/) — field-facing framing of the OP4 stability question
-   [OP4d: The Exhaustiveness Obligation](/proof-program/op4d-exhaustiveness-obligation/) — accessible entry point for OP4d; read this first
-   [TC1 §XII.13a](/series-1/technical-companion/) — canonical formal source for the Candidate Normal Form Theorem
-   [The Tightening Sequence](/core/tightening-sequence/) — narrative account of how identified exits have been addressed at Stage 4
-   [Experimental Companion to Series 1 and 2 / AMP](/empirical/amp/) — empirical program, including DBST-M0 and DBST-M1
