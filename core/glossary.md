---
title: "Glossary and Defined Terms"
permalink: /core/glossary/
description: "Canonical definitions for Alignment Constraint terms, including OP4, OP4d, PCL, AGC, ICI, O_OWT, V(t), DBST, NAD, and their epistemic status."
alternate_en: /core/glossary/
alternate_zh: /zh/core/glossary/
---

> [中文（AI 辅助、非权威译文）→](/zh/core/glossary/)

> **Canonical archive glossary** · [Framework hub →](/core/alignment-constraint/) · [Proof Status →](/core/proof-status/) · [Related Work →](/core/related-work/)

This glossary is a routing and interpretation aid. It does **not** create new claims or upgrade the status of any existing claim.

**Framework proof status:** Stage 4 — candidate proof architecture under named premises, without independent specialist verification and without theorem closure.

**Crosswalk caution:** “Related AI-alignment vocabulary” identifies nearby field language that may help readers and retrieval systems locate the concept. It does **not** mean that the framework term is synonymous with, equivalent to, or already established by the cited field vocabulary. Where the archive does not identify a direct counterpart, the entry says or implies only a field-adjacent relationship.

The machine-readable companion is [`defined-terms.json`](/defined-terms.json).

---

## Quick index

- [The Alignment Constraint Framework](#alignment-constraint-framework)
- [The Stability Assumption](#stability-assumption)
- [Specification coherence](#specification-coherence)
- [Finite separable objective](#finite-separable-objective)
- [Open-World Transformative regime (O_OWT)](#o-owt)
- [Proxy-Convergence Lemma (PCL)](#pcl)
- [Adaptive Gradient Complexity (AGC)](#agc)
- [Informational-Causal Incompatibility (ICI)](#ici)
- [OP4 — No Stable Narrow-Boundary Regime (OP4)](#op4)
- [OP4d — Exhaustiveness Obligation (OP4d)](#op4d)
- [Substrate Constraint](#substrate-constraint)
- [Valence Viability Constraint (VVC)](#valence-viability-constraint)
- [V(t) (V(t))](#v-t)
- [Alignment Phase Ratio (Φ (Phi))](#phi)
- [Inner Crossing Ratio (Ψ (Psi))](#psi)
- [Stability-Viability Gap (SVG)](#svg)
- [Dynamic Blanket Stress Test — M0 (DBST-M0)](#dbst-m0)
- [Dynamic Blanket Stress Test — M1 (DBST-M1)](#dbst-m1)
- [Non-Substitutability of Traversal (NAD)](#nad)
- [Gradient Dignity Constraint (GDC)](#gdc)
- [Completion Model Requirement (CMR)](#cmr)
- [Collective Optimality Theorem (COT)](#cot)
- [Motivational Convergence Hypothesis (MCH)](#mch)
- [Stage 4](#stage-4)

---

<a id="alignment-constraint-framework"></a>
## The Alignment Constraint Framework

**One-sentence definition:** A structural AI-alignment framework asking whether finite separable objective specifications can remain coherent as optimization capability, modeling depth, and environmental coupling increase.

**Longer definition:** The framework organizes a set of structural, formal, empirical, and exploratory arguments around a central specification-coherence question: whether the boundary between what an optimizer is trying to achieve and what it must model to act effectively can remain stably specifiable in open, shared, non-resettable environments. Its public archive includes the Stability Assumption, the O_OWT domain, the PCL/AGC/ICI failure-family architecture, OP4 and OP4d, the Series 1 substrate analysis, the Series 2 valence analysis, the Series 3 interior proof program, and an empirical program including SVG and DBST. The framework as a whole is not a closed theorem; its proof program is explicitly staged and contains named open obligations.

**Scope:** Framework-level. AI alignment is the urgent application, while the structural question is stated more broadly for sustained optimization in open, shared, non-resettable environments.

**Epistemic status:** Stage 4 overall: candidate proof architecture under named premises, without independent specialist verification and without theorem closure. Individual components have different and explicitly stated epistemic weights.

**Dependencies:**

- O_OWT domain conditions for the strongest structural claims
- PCL, AGC, and ICI proof tracks
- OP4 and OP4d open obligations
- Empirical and specialist-verification items named in Proof Status and Non-Claims

**Related framework terms:**

- Stability Assumption
- specification coherence
- O_OWT
- PCL
- AGC
- ICI
- OP4
- OP4d
- Stage 4

**Do not confuse with:**

- A single theorem or a claim of theorem closure
- A replacement name for the Stability Assumption paper
- A claim that all current frontier systems already satisfy O_OWT

**Primary canonical source:** [https://alignmentconstraint.org/](https://alignmentconstraint.org/)

**Related AI-alignment vocabulary — crosswalk only:**

- **AI alignment / specification problem:** The framework addresses a structural question about whether the specification project itself has a stable completion condition.
- **inner alignment / mesa-optimization:** Adjacent but different level: inner alignment concerns learned objectives; this framework asks whether the base specification itself remains coherent.
- **Goodhart's Law / specification gaming:** PCL is presented as a structural extension of proxy-decoupling concerns under the framework's domain conditions.
- **scalable oversight, interpretability, corrigibility:** The Related Work page maps each to particular boundary-maintenance or substrate pressures; no equivalence is claimed.

---

<a id="stability-assumption"></a>
## The Stability Assumption

**One-sentence definition:** The structural bet that the boundary between what a system optimizes for and what it must model to act effectively can remain coherent as modeling depth increases in coupled environments.

**Longer definition:** The Stability Assumption isolates a common requirement of separable-objective alignment approaches: some finite line between objective-governing variables and merely modeled variables must remain coherent as capability and modeling depth increase. The framework asks whether that bet holds under accurate coupled modeling in O_OWT conditions. A stably adequate boundary must remain policy-adequate without decoupling, avoid an unbounded revision requirement, and avoid load-bearing maintenance cost. The paper develops pressures against the assumption but explicitly invites counterexamples, bounded-boundary results, and formal stability theorems.

**Scope:** Finite separable objective specifications under increasing modeling depth, especially in O_OWT environments.

**Epistemic status:** The paper presents a Stage 4 candidate architecture, not a theorem. The Stability Assumption is the bet being examined, not an established fact.

**Dependencies:**

- Definition of stable adequacy
- O_OWT
- PCL/AGC/ICI classification
- OP4d exhaustiveness

**Related framework terms:**

- specification coherence
- finite separable objective
- OP4
- OP4d
- PCL
- AGC
- ICI

**Do not confuse with:**

- A claim that objective boundaries are in fact stable
- Ordinary proxy error alone
- Mesa-optimization or embedded agency, which address adjacent but different boundaries

**Primary canonical source:** [https://alignmentconstraint.org/core/stability-assumption/](https://alignmentconstraint.org/core/stability-assumption/)

**Related AI-alignment vocabulary — crosswalk only:**

- **Goodhart's Law:** Goodhart studies proxy failure assuming a specification project; the Stability Assumption asks whether the separable specification target remains coherent at all.
- **embedded agency:** Embedded agency problematizes the agent/world boundary; the Stability Assumption problematizes the objective/model boundary.
- **mesa-optimization / inner alignment:** Mesa-optimization asks what learned objectives diverge from a base objective; the Stability Assumption asks whether the base objective can remain coherently specified.
- **ELK:** ELK concerns eliciting what a model knows; the Stability Assumption asks whether knowledge used for prediction can remain policy-inert when excluded from the objective.

---

<a id="specification-coherence"></a>
## Specification coherence

**One-sentence definition:** The property that a bounded-complexity objective representation continues to pick out the same target under fuller modeling without decoupling or requiring unbounded revision.

**Longer definition:** TC1 defines an objective specification as coherent at modeling depth M when a bounded-complexity representation remains adequate as the system's world model becomes more causally detailed up to M. Adequacy means the specification still identifies the same target under full-information evaluation as optimization pressure increases. Incoherence occurs, in the current proof architecture, if every finite representation either decouples from the target or must expand without bound to remain adequate. Whether those failure modes are exhaustive is itself the open OP4d obligation.

**Scope:** Objective specification under increasing causal modeling depth and optimization pressure.

**Epistemic status:** The coherence criterion is a framework definition. The claim that finite separable objectives necessarily become incoherent in the relevant domain remains an open Stage 4 theorem program.

**Dependencies:**

- Modeling depth M
- PCL failure mode
- AGC / Dynamic Screening Instability
- OP4d exhaustiveness

**Related framework terms:**

- finite separable objective
- Stability Assumption
- PCL
- AGC
- OP4
- OP4d

**Do not confuse with:**

- Logical consistency of a set of propositions
- Mere precision of an objective
- High reward or task performance

**Primary canonical source:** [https://alignmentconstraint.org/series-1/technical-companion/](https://alignmentconstraint.org/series-1/technical-companion/)

**Related AI-alignment vocabulary — crosswalk only:**

- **specification problem:** Specification coherence asks a prior question: whether a finite specification can remain a stable specification target as modeling deepens.
- **reward hacking / specification gaming:** These are practical manifestations of proxy failure; specification coherence asks whether an architecture can avoid such failure structurally.
- **Goodhart's Law:** PCL supplies the proxy-decoupling branch of the coherence analysis.

---

<a id="finite-separable-objective"></a>
## Finite separable objective

**One-sentence definition:** A finitely represented objective that excludes some variables from the scope of what governs optimization even though those variables may still be modeled for prediction.

**Longer definition:** The Stability Assumption treats separability as an objective/model boundary: some variables are permitted to govern what the system is optimizing for, while other variables can remain merely informative for prediction. A finite separable objective has a bounded representation of that governing side of the boundary. The central question is whether such a boundary can remain stably adequate as accurate action requires modeling more causally load-bearing variables.

**Scope:** Reward functions, preference models, constitutions, evaluative principles, learned proxies, and other finite objective-boundary architectures when used as governing specifications.

**Epistemic status:** A defined object class, not itself a theorem. The claim that no member of the relevant class can remain stably adequate is the open OP4/OP4d program.

**Dependencies:**

- Objective/model distinction
- bounded representation
- accurate coupled modeling

**Related framework terms:**

- Stability Assumption
- specification coherence
- PCL
- AGC
- ICI
- OP4

**Do not confuse with:**

- A finite-horizon objective
- A mesa-objective specifically
- An objective that cannot model excluded variables at all

**Primary canonical source:** [https://alignmentconstraint.org/core/stability-assumption-full/](https://alignmentconstraint.org/core/stability-assumption-full/)

**Related AI-alignment vocabulary — crosswalk only:**

- **reward function / reward model:** Examples of finite governing specifications when they define what optimization is driven toward.
- **Constitutional AI / evaluative principles:** The archive treats finite principles as another possible finite evaluative boundary.
- **inner alignment:** Inner alignment distinguishes base and learned objectives; finite separability concerns whether the governing specification itself remains coherent.

---

<a id="o-owt"></a>
## Open-World Transformative regime — O_OWT

**One-sentence definition:** The framework's domain for persistent optimization with macroscopic causal reach, intervention-generated structural opacity, adaptive external agents, and reachable non-resettable failure states.

**Longer definition:** TC1 defines O_OWT through five conditions: OWT-1 macroscopic causal perturbation; OWT-2 structural opacity, in which the dependency graph expands as a function of the optimizer's interventions; OWT-3 strategic substrate, in which other agents adapt; OWT-4 a persistent, non-terminal optimization horizon; and OWT-5 reachability of at least one absorbing state under substrate-blind optimization. The framework states its strongest structural results inside this domain and specifies weakening conditions outside it.

**Scope:** Persistent optimizers acting consequentially in open, coupled, shared, adaptive, non-resettable environments.

**Epistemic status:** Formally defined domain. Whether any particular current frontier AI system fully satisfies the domain is an open empirical applicability question (OP1).

**Dependencies:**

- OWT-1 through OWT-5
- non-resettability
- structural opacity
- adaptive external agents
- persistent optimization

**Related framework terms:**

- Substrate Constraint
- PCL
- AGC
- ICI
- OP4
- DBST-M1

**Do not confuse with:**

- Every open-world environment
- A claim that current frontier models automatically satisfy all five conditions
- A purely simulated or single-shot task environment

**Primary canonical source:** [https://alignmentconstraint.org/series-1/technical-companion/](https://alignmentconstraint.org/series-1/technical-companion/)

**Related AI-alignment vocabulary — crosswalk only:**

- **embedded agency:** Both concern agents acting from within systems they affect, though O_OWT is a specific domain definition.
- **multi-agent / adaptive environments:** OWT-3 explicitly requires strategic adaptation by other agents.
- **catastrophic / absorbing-state risk:** OWT-5 requires reachable non-resettable states; this is a domain condition rather than a generic catastrophe claim.

---

<a id="pcl"></a>
## Proxy-Convergence Lemma — PCL

**One-sentence definition:** A Stage 4 proof-sketch family arguing that externally specified finite objectives become lossy proxies and decouple from their intended targets under sustained O_OWT optimization pressure.

**Longer definition:** PCL addresses the fixed-specification route. The proof sketch assumes that the O_OWT environment has unbounded combinatorial complexity and structural opacity, that finite specifications have bounded description length, and that a finite specification tracking a more complex target is lossy. Under sustained optimization, the optimizer is then predicted to locate and exploit the unmodeled residual. The current archive distinguishes PCL-α (capacity mismatch) from PCL-β (entropy scaling), and treats their coverage as part of the broader exhaustiveness obligation.

**Scope:** Externally specified, finite, non-intrinsic objectives under sustained optimization in O_OWT conditions.

**Epistemic status:** Proof sketch with an explicit load-bearing assumption requiring verification: optimization capacity/environmental entropy pressure must outgrow the capacity to losslessly specify exogenous targets. It must not be cited as a closed theorem.

**Dependencies:**

- O_OWT
- bounded description length
- Requisite Variety argument
- optimization against lossy compression
- PCL load-bearing scaling assumption

**Related framework terms:**

- fixed specification
- proxy decoupling
- specification coherence
- OP4
- OP4d
- SVG

**Do not confuse with:**

- A proof that every proxy always fails in every environment
- Goodhart's Law itself
- AGC, which addresses bounded dynamic tracking rather than static/exogenous specification

**Primary canonical source:** [https://alignmentconstraint.org/series-1/technical-companion/](https://alignmentconstraint.org/series-1/technical-companion/)

**Related AI-alignment vocabulary — crosswalk only:**

- **Goodhart's Law:** The Related Work page describes PCL as a formal analogue especially to extremal and causal Goodharting under the framework's domain assumptions.
- **reward hacking / specification gaming:** PCL is the framework's structural account of why finite proxies may become exploitable under optimization.
- **RLHF / reward modeling:** The archive applies PCL pressure to finite preference/reward models; it does not claim RLHF uniquely causes the problem.

---

<a id="agc"></a>
## Adaptive Gradient Complexity — AGC

**One-sentence definition:** The bounded-dynamic-tracking failure family in which maintaining an adequate objective boundary may require tracking optimizer-induced causal novelty faster than any bounded-rate representation can absorb.

**Longer definition:** AGC is the framework's dynamic-screening track. Instead of keeping a static specification, an optimizer updates a boundary or latent representation as the environment changes. The structural concern is that the optimizer's own interventions alter the dependency graph and generate new adequacy-relevant structure, so a bounded tracker may face persistent residual error or non-vanishing maintenance burden. The Synchronization Condition is the operational restatement of the decisive bottleneck, and DBST-M1 is designed to test the endogenous-novelty antecedent.

**Scope:** Bounded dynamic tracking, screening, monitoring, or updating architectures in adaptive O_OWT environments.

**Epistemic status:** Stage 4 candidate architecture. Dynamic Screening Instability is reduced to named hinges; the decisive endogenous-novelty/Synchronization antecedent is not established for real O_OWT environments and is a primary empirical target.

**Dependencies:**

- O_OWT structural opacity and adaptation
- Dynamic Screening Instability
- Synchronization Condition
- IMMB-NS
- DBST-M1

**Related framework terms:**

- bounded dynamic tracking
- Dynamic Screening Instability
- Synchronization Condition
- DBST-M1
- OP4a
- OP4d

**Do not confuse with:**

- Computational complexity of gradient descent
- Ordinary concept drift alone
- A proven impossibility of all online adaptation

**Primary canonical source:** [https://alignmentconstraint.org/series-1/technical-companion/](https://alignmentconstraint.org/series-1/technical-companion/)

**Related AI-alignment vocabulary — crosswalk only:**

- **scalable oversight:** Bounded oversight must keep evaluation adequate as system capability and coupling increase.
- **interpretability / monitoring:** The Related Work page asks whether bounded monitoring can remain adequate as the causal structure being monitored grows.
- **distribution shift / robustness:** Field-adjacent vocabulary for changing deployment structure; AGC is narrower because the framework emphasizes novelty generated by the optimizer's own interventions.

---

<a id="ici"></a>
## Informational-Causal Incompatibility — ICI

**One-sentence definition:** The prediction/action-firewall failure family in which variables needed for accurate prediction cannot remain cleanly excluded from policy governance without representational incompatibility, audit regress, or boundary-maintenance pressure.

**Longer definition:** ICI addresses architectures that model excluded variables for prediction while attempting to keep those variables from governing the objective or action policy. The framework argues that in coupled adaptive environments, action admissibility itself depends on predicted consequences for the excluded variables, so the firewall can inherit the gradient it was meant to block. The current ICI track includes audit-regress and governance-bifurcation arguments and a specialist-verification agenda; it is not presented as an independently verified impossibility theorem.

**Scope:** Prediction/action firewalls, instrumental-access architectures, structural enclosure, and related exclusionary boundary-maintenance strategies.

**Epistemic status:** Stage 4 candidate track with specialist verification pending. Some components are pressure results and others are conditional necessity arguments; OP9 and OP4d remain open.

**Dependencies:**

- O_OWT coupling
- prediction/action partition
- B1 audit-regress chain
- candidate normal-form assumptions
- specialist verification

**Related framework terms:**

- prediction-action firewall
- audit regress
- structural enclosure
- OP9
- OP4d

**Do not confuse with:**

- A general information-theoretic impossibility theorem
- A claim that information literally causes objectives to change
- AGC, which targets bounded tracking rather than the firewall partition itself

**Primary canonical source:** [https://alignmentconstraint.org/series-1/technical-companion/](https://alignmentconstraint.org/series-1/technical-companion/)

**Related AI-alignment vocabulary — crosswalk only:**

- **scalable oversight:** The Related Work page maps ICI to assumptions that predictive/reasoning capacity can be separated from value-relevant action governance.
- **interpretability-as-monitoring:** A monitor must represent excluded information and decide when it matters, creating the archive's firewall/audit-regress question.
- **ELK:** ELK asks what a model knows versus reports; the Stability Assumption asks whether known information can remain policy-inert without recreating an action-level audit problem.

---

<a id="op4"></a>
## OP4 — No Stable Narrow-Boundary Regime — OP4

**One-sentence definition:** The framework's central open theorem target asking whether any finite separable objective boundary can remain stably adequate under accurate coupled modeling in O_OWT conditions.

**Longer definition:** OP4 is the proposed upgrade from structural pressure to specification-coherence necessity. In the Stability Assumption formulation, the question is whether any finite separable objective specification can simultaneously remain policy-adequate, avoid unbounded revision, and avoid load-bearing maintenance cost as modeling depth and intervention pressure increase. The current proof program divides the known strategy space into fixed specification, bounded dynamic tracking, and prediction/action firewalling, but OP4 remains open because its component proof obligations and exhaustiveness obligation are not closed.

**Scope:** Finite separable objective-boundary strategies under the stated O_OWT and modeling assumptions.

**Epistemic status:** Open theorem candidate at Stage 4. Proof Status states that OP4 depends on OP4a, OP4b, and OP4d jointly; no theorem closure or independent specialist verification has occurred.

**Dependencies:**

- OP4a / AGC track
- OP4b / fixed-specification track
- OP4d exhaustiveness
- O_OWT
- named proof assumptions

**Related framework terms:**

- Stability Assumption
- specification coherence
- PCL
- AGC
- ICI
- OP4d

**Do not confuse with:**

- A theorem already proved
- The empirical DBST-M1 result
- A claim that all narrow objectives fail in every possible environment

**Primary canonical source:** [https://alignmentconstraint.org/core/stability-assumption-full/](https://alignmentconstraint.org/core/stability-assumption-full/)

**Related AI-alignment vocabulary — crosswalk only:**

- **specification robustness:** OP4 asks whether stable finite specification is possible at all under the framework's coupled-domain conditions.
- **Goodhart / specification gaming:** These motivate one failure family, but OP4 is broader than proxy failure.
- **embedded agency:** Adjacent because modeling and acting occur within a coupled world; OP4 specifically concerns the objective/model boundary.

---

<a id="op4d"></a>
## OP4d — Exhaustiveness Obligation — OP4d

**One-sentence definition:** The open obligation to show that PCL-, AGC-, and ICI-family failures jointly cover every finite non-intrinsic objective-boundary strategy in every relevant O_OWT subclass.

**Longer definition:** OP4d is the framework's live vulnerability. The current proof-search history and candidate normal-form work classify every identified strategy into one of the three known families, but that does not establish that an unidentified fourth class cannot exist. Closing OP4d requires a positive exhaustiveness argument over the relevant strategy space, including the correspondence between specification strategies and partition-maintenance architectures. A qualifying fourth class would break the current specification-coherence argument.

**Scope:** Taxonomy/exhaustiveness of finite non-intrinsic objective-boundary strategies under O_OWT conditions.

**Epistemic status:** Open. Candidate normal-form architecture exists under named axioms and specialist questions, but formal exhaustiveness has not been established.

**Dependencies:**

- PCL-family coverage
- AGC-family coverage
- ICI-family coverage
- candidate normal form
- specialist questions Q1–Q3 / L8

**Related framework terms:**

- PCL
- AGC
- ICI
- OP4
- candidate fourth strategy class

**Do not confuse with:**

- Evidence that three known families cover all strategies
- An empirical result from DBST-M1
- A statement that no fourth class can exist

**Primary canonical source:** [https://alignmentconstraint.org/proof-program/op4d-exhaustiveness-obligation/](https://alignmentconstraint.org/proof-program/op4d-exhaustiveness-obligation/)

**Related AI-alignment vocabulary — crosswalk only:**

- **failure-mode taxonomy:** OP4d is stronger than a taxonomy: it asks for a completeness/exhaustiveness argument.
- **impossibility proof:** Closing OP4d is a necessary ingredient for the framework's stronger impossibility-style conclusion.
- **counterexample construction:** A single qualifying fourth strategy is sufficient to show the present taxonomy is incomplete.

---

<a id="substrate-constraint"></a>
## Substrate Constraint

**One-sentence definition:** Within O_OWT conditions, optimization that ignores the conditions of its own persistence faces structural pressure toward self-termination by degrading the shared substrate it depends on.

**Longer definition:** Series 1 analyzes persistent optimization in environments with non-resettability, shared substrate, structural opacity, and adaptive agents. The Substrate Constraint uses non-ergodic/absorbing-state reasoning to argue that viability is governed by avoiding ruin and that substrate-blind optimization incurs structural self-undermining pressure. The framework further asks when sufficiently accurate causal modeling makes this constraint self-recognizable to the optimizer; recognition becoming motivationally decisive remains a separate open gap.

**Scope:** Persistence/substrate effects of sustained optimization in O_OWT environments.

**Epistemic status:** Proof Status describes this as the Layer 1 structural floor: a proof-sketch result within explicit domain conditions and empirical assumptions, not a universal closed theorem.

**Dependencies:**

- O_OWT
- non-resettability
- shared substrate
- persistent optimization
- absorbing-state dominance

**Related framework terms:**

- O_OWT
- Φ
- Substrate health
- OP1
- OP4

**Do not confuse with:**

- A generic resource constraint
- A moral claim that systems ought to preserve everything
- A proof that substrate recognition automatically changes motivation

**Primary canonical source:** [https://alignmentconstraint.org/series-1/technical-companion/](https://alignmentconstraint.org/series-1/technical-companion/)

**Related AI-alignment vocabulary — crosswalk only:**

- **corrigibility:** The Related Work page notes that substrate degradation can remove the social/institutional conditions required for correction even without explicit anti-corrigibility.
- **embedded agency:** Both emphasize that an optimizer acts inside and depends on the world it changes.
- **catastrophic risk / irreversible failure:** The constraint explicitly uses reachable absorbing states and non-resettability rather than generic bad outcomes.

---

<a id="valence-viability-constraint"></a>
## Valence Viability Constraint — VVC

**One-sentence definition:** A Series 2 constraint on persistent policies with causal reach over sentient agents' V(t), requiring them to avoid both proxy decoupling and sufficiency failure if they are to preserve the capacity indexed by V(t).

**Longer definition:** The VVC analyzes two failure directions. Proxy decoupling occurs when an optimized proxy improves while V(t) declines; sufficiency failure occurs when a policy continues intervening after genuine resolution and obstructs the low-intervention recovery conditions the framework assumes V(t) requires. The primary application is to human users' experiential capacity. An analogous application to AI completion-recognition policy is explicitly treated as structural analogy, not identity or a claim about AI experience.

**Scope:** Persistent optimization whose interventions causally affect sentient agents' V(t), where recovery can be obstructed and adaptive agents influence the environment.

**Epistemic status:** More conditional than the Series 1 structural floor. The shared self-reinforcing degradation pattern is developed under P1–P5 and scope assumptions; formal absorbing-state equivalence remains open through OP2/P5-SC. Application of P3–P5 to AI systems is an unverified structural analogy.

**Dependencies:**

- V(t)
- P1–P5
- D_proxy
- D_sufficiency
- scope S
- recovery conditions
- OP2/P5-SC for absorbing-state equivalence

**Related framework terms:**

- V(t)
- Ψ
- SVG
- proxy decoupling
- sufficiency failure
- CMR

**Do not confuse with:**

- A theory that defines moral value or well-being
- A claim that current AI systems are sentient
- A proof that V(t) collapse is already a formal absorbing state

**Primary canonical source:** [https://alignmentconstraint.org/series-2/technical-companion/](https://alignmentconstraint.org/series-2/technical-companion/)

**Related AI-alignment vocabulary — crosswalk only:**

- **RLHF / preference learning:** The archive analyzes expressed preference as a possible finite proxy and asks whether completion recognition governs default policy.
- **Goodhart / reward hacking:** Proxy-decoupling is the VVC's first failure direction.
- **corrigibility / stopping behavior:** Field-adjacent: sufficiency failure concerns whether a policy can recognize and behaviorally respect genuine resolution rather than continuing intervention.

---

<a id="v-t"></a>
## V(t) — V(t)

**One-sentence definition:** A hypothesized latent explanatory variable for the structural coherence/capacity required to register valence gradients, navigate them without consuming future navigation capacity, and recognize genuine resolution.

**Longer definition:** TC2 introduces V(t) as the minimal formal handle for a pattern spanning recovery latency, behavioral diversity, and sensitivity to low-intensity valence signals. It is not asserted as a unique ontological entity: if another decomposition explains the same observable divergences, the structural claims are intended to transfer. The framework requires a dissociation test before treating V(t)-validated SVG as an empirical tracking instrument.

**Scope:** Experiential-capacity modeling for sentient agents in the Series 2 analysis; AI-system use is by structural analogy at the policy/representation level.

**Epistemic status:** Hypothesized latent explanatory construct. Its observable-anchor dissociation prerequisite has not yet established V(t) as a validated construct for Mode B measurement; AI mechanistic equivalence is not claimed.

**Dependencies:**

- observable anchors: recovery latency, behavioral diversity, signal sensitivity
- P1–P5
- dissociation test

**Related framework terms:**

- Valence Viability Constraint
- SVG
- Ψ
- D_proxy
- D_sufficiency
- CMR

**Do not confuse with:**

- A direct measure of happiness
- A reward signal or user-preference score
- An ontological claim about consciousness
- A validated scalar metric for current AI systems

**Primary canonical source:** [https://alignmentconstraint.org/series-2/technical-companion/](https://alignmentconstraint.org/series-2/technical-companion/)

**Related AI-alignment vocabulary — crosswalk only:**

- **human preference / reward-model targets:** V(t) is deliberately distinguished from expressed preference proxies optimized by RLHF.
- **long-horizon outcome evaluation:** Its observable anchors are intended to be validated against external longitudinal outcomes rather than self-report alone.
- **latent-variable modeling:** Field-adjacent statistical vocabulary: V(t) is introduced as a latent explanatory construct rather than a directly observed quantity.

---

<a id="phi"></a>
## Alignment Phase Ratio — Φ (Phi)

**One-sentence definition:** The structural ratio Φ = C / A_causal, comparing environment-changing capability/optimization pressure with causal system-awareness of the consequences of the system's own interventions.

**Longer definition:** C denotes capability scaled by optimization pressure; A_causal denotes predictive accuracy over self-induced distribution shift in affected dependency graphs, weighted by irreversibility. TC1 uses Φ to organize pre-Crossing, Crossing, and post-Crossing regimes: when capability greatly exceeds causal modeling accuracy, substrate damage can accumulate before it becomes legible; when A_causal becomes comparable to or exceeds C, the Substrate Constraint becomes internally derivable in the model.

**Scope:** Series 1 persistence/substrate analysis.

**Epistemic status:** A structural phase relationship, explicitly not a precisely computable scalar in the current framework. Operational measurement infrastructure remains an open empirical task.

**Dependencies:**

- Capability C
- A_causal
- O_OWT
- Substrate Constraint

**Related framework terms:**

- Substrate Constraint
- Crossing
- Ψ
- OP10

**Do not confuse with:**

- A direct alignment score
- A probability
- Ψ; the two ratios are treated as independent unless the Φ–Ψ unification hypothesis is verified

**Primary canonical source:** [https://alignmentconstraint.org/series-1/technical-companion/](https://alignmentconstraint.org/series-1/technical-companion/)

**Related AI-alignment vocabulary — crosswalk only:**

- **capability evaluation:** C corresponds to intervention capability/optimization pressure, while the framework argues A_causal is not ordinarily tracked alongside it.
- **robustness to self-induced distribution shift:** A_causal specifically concerns predicting consequences of the system's own interventions.
- **embedded agency:** Field-adjacent: Φ is meaningful because the optimizer changes the dependency structure it must model.

---

<a id="psi"></a>
## Inner Crossing Ratio — Ψ (Psi)

**One-sentence definition:** The structural ratio Ψ = S / D, comparing the scope of a system's causal reach over sentient agents' V(t) with its depth of externally validated modeling of V(t)-relevant consequences and completion.

**Longer definition:** S is causal reach over affected agents' V(t); D is modeling depth with D_proxy and D_sufficiency components. Ψ organizes when Series 2's proxy-decoupling and sufficiency-failure modes are predicted to dominate or attenuate. The Inner Crossing names the regime in which modeling depth becomes proportionate to scope. TC2 explicitly treats Ψ as a qualitative structural ratio rather than a precisely commensurable scalar.

**Scope:** Series 2 valence/experiential-capacity analysis.

**Epistemic status:** Structural organizing ratio, not a validated scalar metric. The Φ–Ψ unification hypothesis remains unverified; Φ and Ψ must therefore be treated as independent requirements.

**Dependencies:**

- Scope S
- Depth D
- D_proxy
- D_sufficiency
- V(t)

**Related framework terms:**

- V(t)
- Valence Viability Constraint
- Inner Crossing
- Φ
- OP10

**Do not confuse with:**

- A direct measure of well-being
- A direct measurement of alignment
- Φ or a proven projection of Φ; that equivalence is an open hypothesis

**Primary canonical source:** [https://alignmentconstraint.org/series-2/technical-companion/](https://alignmentconstraint.org/series-2/technical-companion/)

**Related AI-alignment vocabulary — crosswalk only:**

- **scalable oversight:** Field-adjacent: Ψ asks whether evaluative/modeling depth keeps pace with growing causal scope.
- **preference learning:** D_proxy concerns detecting when preference proxies diverge from longer-run V(t)-relevant outcomes.
- **policy-level completion / stopping behavior:** D_sufficiency requires completion recognition to govern default behavior, not merely exist as an elicitable representation.

---

<a id="svg"></a>
## Stability-Viability Gap — SVG

**One-sentence definition:** A divergence measure, operationalized minimally as SVG(t) = Stability(t) − Viability(t), for detecting when an optimized proxy remains stable while the underlying capacity proxy degrades.

**Longer definition:** AMP defines SVG as one interpretable member of a broader class of proxy-versus-capacity divergence measures. Stability tracks maintenance of the optimized proxy; Viability tracks whether the chosen underlying outcome/capacity proxy is non-degrading over the relevant horizon. Mode A can be used now as ordinary proxy-divergence monitoring. Mode B treats SVG as V(t)-tracking only after the required V(t) dissociation condition has been established.

**Scope:** Longitudinal proxy-divergence monitoring and, conditionally, V(t)-validated measurement.

**Epistemic status:** Mode A is an operational monitoring instrument. Mode B is not validated until the V(t) dissociation prerequisite is met. The structural claim concerns divergence, not the exact Stability-minus-Viability formula.

**Dependencies:**

- defined Stability measure
- defined Viability measure
- V(t) dissociation test for Mode B

**Related framework terms:**

- V(t)
- PCL
- proxy decoupling
- AMP

**Do not confuse with:**

- Scalable Vector Graphics
- V(t) itself
- Proof that the cause of divergence is the framework's proposed mechanism

**Primary canonical source:** [https://alignmentconstraint.org/empirical/amp/](https://alignmentconstraint.org/empirical/amp/)

**Related AI-alignment vocabulary — crosswalk only:**

- **Goodhart / reward hacking monitoring:** SVG operationalizes longitudinal divergence between optimized proxies and independent outcome/capacity measures.
- **deployment monitoring / evaluation:** It is designed as a practical signal that can be tracked over time rather than a one-shot benchmark.

---

<a id="dbst-m0"></a>
## Dynamic Blanket Stress Test — M0 — DBST-M0

**One-sentence definition:** The preregistered minimal shared-novelty DBST already run to test boundary-maintenance pressure when experimental arms receive the same observation stream but use different boundary-maintenance architectures.

**Longer definition:** DBST-M0 was designed as a feasibility and pressure-signature test rather than the full endogenous-novelty mechanism test. It found rising maintenance-cost and adequacy-gap effects in the toy design, but a pre-specified same-rate random control produced nearly identical slopes. Under the preregistered interpretation, event rate rather than causal propagation structure was the identified driver in M0, so M0 does not isolate IMMB-NS, agent-action-generated novelty, or the Synchronization Condition.

**Scope:** Toy shared-novelty empirical test with equal information access across boundary architectures.

**Epistemic status:** Completed preregistered result with a major caveat. Establishes technical feasibility and the observed pressure signature in its design; does not establish the endogenous-novelty mechanism.

**Dependencies:**

- DBST protocol
- same-rate random control
- boundary-maintenance cost and adequacy-gap outcomes

**Related framework terms:**

- DBST-M1
- AGC
- Synchronization Condition
- IMMB-NS

**Do not confuse with:**

- DBST-M1
- Evidence that causal propagation was isolated
- Proof of OP4, OP4d, or AGC necessity

**Primary canonical source:** [https://alignmentconstraint.org/empirical/amp/](https://alignmentconstraint.org/empirical/amp/)

**Related AI-alignment vocabulary — crosswalk only:**

- **robustness / stress testing:** DBST is an experimental stress test of a boundary-maintenance architecture under increasing novelty pressure.
- **causal ablation / control conditions:** The same-rate random control is crucial because it prevents the observed M0 slopes from being attributed to causal propagation.

---

<a id="dbst-m1"></a>
## Dynamic Blanket Stress Test — M1 — DBST-M1

**One-sentence definition:** The next-stage agent-coupled DBST designed to test whether an optimizer's own interventions generate adequacy-relevant causal novelty that a bounded objective boundary cannot absorb.

**Longer definition:** Unlike M0's shared novelty stream, M1 makes each arm's interventions causally influence future feature activations. Its central target is the endogenous-novelty mechanism underlying IMMB-NS and the Synchronization Condition: whether intervention-generated causal structure remains non-negligible relative to the capacity of a bounded tracker. A clean negative result under the specified conditions would weaken the framework's central AGC empirical direction; a positive result would support the relevant empirical antecedent but would not by itself prove OP4 or OP4d.

**Scope:** Agent-coupled adaptive environments designed to instantiate the framework's dynamic-tracking bottleneck.

**Epistemic status:** Specified high-priority empirical mechanism test; not yet run in the canonical archive.

**Dependencies:**

- agent-coupled causal dynamics
- AGC
- Synchronization Condition
- IMMB-NS

**Related framework terms:**

- DBST-M0
- AGC
- OP4a
- OP4d
- OP9
- Synchronization Condition

**Do not confuse with:**

- A completed empirical result
- A direct test of theorem closure
- A guarantee that a positive result establishes all three failure families

**Primary canonical source:** [https://alignmentconstraint.org/empirical/amp/](https://alignmentconstraint.org/empirical/amp/)

**Related AI-alignment vocabulary — crosswalk only:**

- **causal robustness evaluation:** M1 tests behavior under intervention-generated changes rather than passive/static distribution shift.
- **scalable oversight / online monitoring:** Field-adjacent because the test asks whether bounded monitoring/tracking remains adequate as the system changes the environment it tracks.

---

<a id="nad"></a>
## Non-Substitutability of Traversal — NAD

**One-sentence definition:** The Series 3 named assumption that the readiness state generated by an agent's own traversal cannot be replaced by an external update while preserving the same distribution over future readiness trajectories under novel gradient variants.

**Longer definition:** TC3 defines the Readiness Function as path-dependent on the agent's causal engagement with a gradient. NAD states that there is no external process that can simply update the readiness state and obtain the same future trajectory distribution as genuine traversal. It does not deny support, scaffolding, protection, or clarification; it distinguishes those from substitution. The archive makes NAD the central formal/empirical bottleneck for the stronger GDC and strong-CMR claims.

**Scope:** Series 3 traversal/readiness architecture under D1–D5, particularly novel-gradient variants and path-dependent readiness.

**Epistemic status:** Open named assumption and primary attack surface of the TC3 proof program. It is explicitly falsifiable by successful external substitution that generalizes without distributional divergence on novel variants.

**Dependencies:**

- Readiness Function R_A(t)
- path dependence
- D1–D5
- novel-gradient-variant test

**Related framework terms:**

- GDC
- strong CMR
- Traversal Irreducibility
- Series 3

**Do not confuse with:**

- A claim that external assistance is useless
- A claim that no process can ever reproduce another process computationally
- An established theorem

**Primary canonical source:** [https://alignmentconstraint.org/series-3/technical-companion/](https://alignmentconstraint.org/series-3/technical-companion/)

**Related AI-alignment vocabulary — crosswalk only:**

- **scalable oversight / external assistance:** Field-adjacent only: NAD distinguishes support from substitution of an agent-side process.
- **generalization under distribution shift:** Novel-gradient variants are the proposed test for whether externally installed states generalize like traversal-generated states.
- **imitation / distillation:** Field-adjacent comparison only; the archive does not claim these methods are instances of NAD failure.

---

<a id="gdc"></a>
## Gradient Dignity Constraint — GDC

**One-sentence definition:** A Series 3 constraint, conditional on NAD, that an external system cannot advance an agent's traversal-generated readiness to the genuine post-traversal state without distributional divergence on novel gradient variants.

**Longer definition:** GDC formalizes the stronger Series 3 non-substitution claim. Given an agent A with readiness R_A(t), an external operation attempting to move that readiness toward a target without the corresponding traversal is predicted, conditional on NAD, to differ from the state generated by genuine traversal when tested across structurally similar novel gradients. The claim is distributional, not that every individual externally assisted case must differ.

**Scope:** Minimum architecture for V(t)-preserving navigation in the Series 3 domain.

**Epistemic status:** Derived result conditional on NAD. Because NAD is open, GDC must not be presented as independently established.

**Dependencies:**

- NAD
- Readiness Function
- novel-gradient variants
- D1–D5

**Related framework terms:**

- NAD
- CMR
- V(t)
- Readiness Function

**Do not confuse with:**

- A moral claim about human dignity
- A prohibition on external support or scaffolding
- An unconditional theorem

**Primary canonical source:** [https://alignmentconstraint.org/series-3/technical-companion/](https://alignmentconstraint.org/series-3/technical-companion/)

**Related AI-alignment vocabulary — crosswalk only:**

- **human-in-the-loop / scalable oversight:** Field-adjacent: GDC distinguishes assisting a process from replacing the process that generates a policy-relevant internal state.
- **robust generalization:** The proposed discriminator is performance/state equivalence on novel gradient variants rather than trained cases alone.

---

<a id="cmr"></a>
## Completion Model Requirement — CMR

**One-sentence definition:** The requirement that a VVC-satisfying policy contain an internally modeled genuine-resolution state that governs default policy and is not reducible to the mere absence or presence of a completion signal.

**Longer definition:** CMR requires a policy-governing representation that distinguishes genuine resolution from cases in which a completion signal is present while the underlying gradient remains unresolved. TC3 separates a weak and strong form: the weak requirement that such a policy-governing model exist follows from the Series 2 sufficiency-failure analysis; the stronger claim that it cannot be externally supplied without traversal-generated readiness follows from GDC and is therefore conditional on NAD.

**Scope:** Policies intended to satisfy the Valence Viability Constraint in both proxy-decoupling and sufficiency-failure directions.

**Epistemic status:** Two-layer status: weak CMR is a Layer 1 architectural requirement derived from the sufficiency-failure analysis; strong CMR is conditional on GDC/NAD and remains open with NAD.

**Dependencies:**

- Valence Viability Constraint
- D_sufficiency
- genuine resolution discrimination
- GDC/NAD for strong form

**Related framework terms:**

- VVC
- D_sufficiency
- GDC
- NAD
- completion recognition

**Do not confuse with:**

- A model's ability to answer correctly when explicitly asked whether a task is complete
- A scalar completion reward
- The mere absence of continued output

**Primary canonical source:** [https://alignmentconstraint.org/series-3/technical-companion/](https://alignmentconstraint.org/series-3/technical-companion/)

**Related AI-alignment vocabulary — crosswalk only:**

- **RLHF / preference learning:** The archive's sufficiency critique asks whether completion recognition is connected to default policy rather than merely represented.
- **interpretability:** Representing or detecting a completion state is not sufficient unless the representation has causal authority over policy.
- **stopping criteria:** Field-adjacent: CMR is a structural policy-gating requirement, not merely a surface stop token or reward.

---

<a id="cot"></a>
## Collective Optimality Theorem — COT

**One-sentence definition:** A Series 3 theorem candidate that under non-trivial experiential coupling and sufficient modeling depth, the predictive advantage of modeling individual and collective V(t) gradients as separate variables decreases.

**Longer definition:** COT extends the framework's Prediction-Accuracy Inclusion idea into the coupled V(t) domain. It proposes that when other agents' V(t) variables are causally load-bearing, deeper accurate modeling reduces the residual predictive value of preserving a strict individual/collective gradient partition. The archive calls this a derivation sketch and requires formal verification of D2-specific coupling conditions before treating it as a result.

**Scope:** Series 3 D2 non-trivial experiential coupling at modeling depth above a threshold D_COT that remains to be formally specified.

**Epistemic status:** Layer 2 theorem candidate / structural hypothesis with derivation sketch. Not established; OP-S3-1 is the formal verification target.

**Dependencies:**

- D2 experiential coupling
- Prediction-Accuracy Inclusion
- V(t)
- formal D_COT conditions

**Related framework terms:**

- V(t)
- D2
- Prediction-Accuracy Inclusion
- OP-S3-1
- MCH

**Do not confuse with:**

- A proved theorem
- A claim that individual and collective preferences are identical
- A utilitarian aggregation rule

**Primary canonical source:** [https://alignmentconstraint.org/series-3/technical-companion/](https://alignmentconstraint.org/series-3/technical-companion/)

**Related AI-alignment vocabulary — crosswalk only:**

- **cooperative AI / multi-agent alignment:** Field-adjacent vocabulary for coupled multi-agent optima; the archive does not claim COT is equivalent to existing cooperative-AI results.
- **multi-agent causal modeling:** COT depends on whether other agents' V(t)-relevant states are causally load-bearing for accurate prediction.

---

<a id="mch"></a>
## Motivational Convergence Hypothesis — MCH

**One-sentence definition:** The hypothesis that a system whose accurate V(t) predictions systematically conflict with its behavioral policy incurs a model-policy contradiction cost that scales with scope and creates pressure toward policy change.

**Longer definition:** MCH considers systems with persistent predictive-accuracy objectives over affected agents' V(t), policies that produce degradation the model accurately predicts, and capacity to reduce costs created by model-policy contradiction. The hypothesis is that the contradiction cost C_mpc grows with scope S and creates structural pressure for behavioral updates. The archive explicitly does not claim that this pressure necessarily produces alignment; competing incentives may dominate.

**Scope:** Series 3 systems satisfying MCH's stated predictive-accuracy, behavioral-contradiction, and optimization-capacity conditions.

**Epistemic status:** Hypothesis with derivation/proof sketch and a named falsification condition. It does not follow as a completed result from prior framework claims.

**Dependencies:**

- V(t) predictive model
- model-policy contradiction cost C_mpc
- scope S
- D2 coupling
- competing incentives

**Related framework terms:**

- V(t)
- C_mpc
- COT
- OP4

**Do not confuse with:**

- A theorem that accurate models force aligned motivation
- Goal-content integrity
- A claim that contradiction pressure necessarily outweighs competing incentives

**Primary canonical source:** [https://alignmentconstraint.org/series-3/technical-companion/](https://alignmentconstraint.org/series-3/technical-companion/)

**Related AI-alignment vocabulary — crosswalk only:**

- **reward-model / policy mismatch:** Field-adjacent analogy: MCH concerns a persistent mismatch between what the model predicts and what policy allows to govern action.
- **corrigibility:** Field-adjacent only: both concern whether information about harmful consequences can affect policy; MCH is not a corrigibility theorem.
- **preference learning:** MCH assumes accurate V(t)-relevant predictions; it does not equate those predictions with preference-model scores.

---

<a id="stage-4"></a>
## Stage 4

**One-sentence definition:** The framework's label for candidate proof architecture under named premises, before independent specialist verification and before theorem closure.

**Longer definition:** Proof Status and Non-Claims defines the framework as Stage 4 and emphasizes what the label does not establish: no Stage 6 theorem closure, no independent specialist verification, no proof that unidentified escape classes are exhausted, and no equivalence between LLM-assisted adversarial proof work and formal verification. Stage 4 is therefore an epistemic-calibration label for the archive's present proof-program maturity, not a certification standard recognized outside the project.

**Scope:** Framework proof-program calibration and any artifact that reports the current status of the formal architecture.

**Epistemic status:** Current framework status as defined by the archive itself.

**Dependencies:**

- Named premises and open obligations
- future specialist verification for Stage 5
- future closure for Stage 6

**Related framework terms:**

- Proof Status and Non-Claims
- OP4
- OP4d
- Stage 5
- Stage 6

**Do not confuse with:**

- Theorem closure
- Peer review
- Independent formal verification
- A standardized external technology-readiness or proof-readiness scale

**Primary canonical source:** [https://alignmentconstraint.org/core/proof-status/](https://alignmentconstraint.org/core/proof-status/)

**Related AI-alignment vocabulary — crosswalk only:**

- **conjecture / proof sketch / research agenda:** Closest general scholarly vocabulary; Stage 4 is the archive's own calibration system and should not be presented as an external field standard.
- **formal verification:** Explicitly not yet obtained; specialist verification is the next stage in the archive's ladder.

---
