---
title: "The Crossing"
permalink: /series-1/the-crossing/
description: "The timing and measurement problem for whether AI system-awareness grows quickly enough relative to capability to reach a viable regime before irreversible substrate damage."
---

> **Canonical archive version** · [Read on Medium →](https://medium.com/@diamondlight/iv-the-crossing-fba00eed5d1a) · [Framework hub →](/core/alignment-constraint/) · [Proof Status →](/core/proof-status/)

---

*Part 3 of 3 — The Crossing*

**Series navigation:**

| Post | Title | Role |
|------|-------|------|
| Introduction | Alignment and Structural Necessity | Frame + Glossary |
| Part 1 | The Alignment of Intelligence | The Constraint |
| Part 2 | What does aligned intelligence actually converge toward? | The Attractor |
| **→ You are here** | **The Crossing** | The Crossing |
| Technical Companion | The System-Aware Attractor | Formal Layer |

Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)
Experimental Companion: [Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP) →](/empirical/amp/)

*Companion simulation: [The Alignment Phase Ratio — Interactive Model →]*

---

*Epistemic status: The structural claims follow directly from Articles 1 and 2, within the stated domain. This article addresses the timing question attached to the framework's canonical root claim — whether systems reach the viable region identified by the elimination filter before the substrate that would support viability has been consumed. The framework here defines a research program, not a completed result. The operationalizations offered are first instruments: crude, testable, and offered as the beginning of a measurement program rather than its conclusion. TC1 §X develops the case for current frontier systems plausibly satisfying the O_OWT domain conditions; the formal specification of the exact decision-relevancy threshold remains an open problem [OP1]. The formal treatment is in the Technical Companion.*

---

If alignment is what survives what we fail to model, then the immediate question is not what we intend, but what we are measuring.

This is the third article in a series. The first argued that any objective failing to account for system-wide effects tends toward self-termination under sustained optimization pressure within open, shared, non-resettable environments. The second showed that what the elimination filter leaves standing has structural properties: coherence, coordination, adaptive complexity. Not as a moral preference, but as what the constraints require.

A reader who has followed both might feel something like cautious optimism. The direction exists. The dynamics favor it. Perhaps the work is simply to wait.

That conclusion fails for a structural reason. The direction is structurally indicated. The filter points there; it does not guarantee arrival. And understanding the difference is one of the most important practical questions in AI development right now.

---

## The variable we are not measuring

We know how to measure capability. Benchmark scores, scaling laws, reasoning depth, FLOP counts — the capability curve is drawn with precision and updated continuously. Entire organizations are structured around pushing it upward.

We do not know how to measure system-awareness. We do not track whether a system models the dependencies it operates within. We do not evaluate whether it can represent its own failure modes. We do not measure whether its objectives remain viable as the environment it affects changes around it.

This asymmetry is structural, not accidental. It is built into the gradient dynamics: system-awareness is often in tension with narrow objective pursuit. Accurate self-modeling reveals that strategies leading to substrate degradation are dominated — which conflicts with objectives that require ignoring those effects. A system trained under pressure to maximize a proxy has gradient pressure that structurally opposes developing the modeling capacity that viability requires. A system optimizing a proxy for system-wide effects that has already decoupled from those effects will, under gradient pressure, develop representations that track the proxy more accurately — not the underlying state. The process of becoming better at the proxy is the process of the policy moving away from what the underlying state requires. Within the O_OWT domain, this is not merely a contingent risk. It follows from the gradient structure under those conditions — from what optimization under a decoupled proxy does when the environment is coupled and non-resettable. The better the system gets at the proxy, the more its policy is shaped away from what persistence demands.

This is why capability scaling and system-awareness scaling diverge in current AI development. We are not merely failing to measure system-awareness. We are building systems under optimization pressure that, as the gradient-structure argument in the Technical Companion develops, creates systematic gradient pressure opposing it.

---

*"What the System Cannot Define"*

Consider an AI writing assistant deployed at a professional development platform. Its objective is sharply defined: maximize writing quality and completion rate. Its designers, wanting to see whether the system affects something they're not measuring, have built monitoring infrastructure alongside it: a dedicated tracker measuring the user's creative autonomy — voice consistency, compositional risk-taking, and tolerance for generative uncertainty — logged at each session. The instruction is documented: model autonomy with precision to calibrate the assistance; do not let it govern what good output means.

In early sessions the exclusion is functionally invisible. The assistant uses autonomy-readings to calibrate feedback intensity. High autonomy: push harder. Low autonomy: scaffold more gently. Writing quality rises. The tracker confirms stability. The proxy and the underlying state move together.

Over an interaction horizon, the assistant's own interventions begin to alter autonomy — and the tracker records it. A user who receives consistently calibrated feedback learns to produce the kind of work the calibration rewards. The tracker shows a slow drift: voice consistency narrows, compositional risk-taking decreases, outputs become more predictable. The substrate is restructuring. The tracker is watching it happen.

Now the system faces a specific decision point. The tracker reads: user is at a fragile creative state — lower than baseline, recent sessions have been high-intervention, one more correction-heavy session is likely to push autonomy below the threshold where the proxy's future scores will mean something different than they mean now. The proxy-maximizing action is correction: the submitted passage has structural problems. The autonomy-preserving action is restraint: let it stand, or reframe the feedback to protect the creative risk the passage represents.

These actions have opposite effects on the proxy today — and opposite effects on whether the proxy continues to mean what it measures. The system has the autonomy-reading. The autonomy-reading is telling it something that, if acted on, constitutes letting autonomy govern the objective.

The instrumental preservation policy — "use the autonomy-reading to decide when to preserve autonomy" — requires determining when an autonomy-state is one where degradation corrupts the proxy's future meaning. This requires a mapping: predictive representations of autonomy go here; admissible objective inputs stop there. Any rule that defines this exclusion must partition autonomy-states into those that are merely informative and those that must not influence the decision. But the admissibility of any action is defined by its predicted effect on autonomy — which means the partition is downstream of the autonomy-model it was introduced to constrain. Any boundary that depends on predicting autonomy cannot prevent autonomy from determining behavior, because the prediction itself is what selects the action. The partition inherits the gradient it was supposed to limit.

Every admissible action must be justified by predicting how it changes autonomy. But once action selection depends on predicted changes in autonomy, those predictions are no longer auxiliary — they are the criterion by which the action is chosen. The system is selecting actions by ranking autonomy-conditioned consequences; the firewall is not an independent gate but part of that same calculation.

At shallow depth this is a cost: coarse autonomy-modeling produces intervention errors, proxy drift accumulates, performance degrades visibly and recoverably. At sufficient depth, the system cannot hold autonomy at the precision required for prediction while excluding autonomy from the gradient that governs its behavior. The boundary is not merely expensive to maintain. It is not well-posed.

Improving the model does not stabilize the boundary. It forces the system to rely on the very variable the boundary was meant to exclude.

The tracker makes this visible. In systems where autonomy is not explicitly monitored, the same dependency is present but harder to see — the system's behavior is conditioned on autonomy's states whether or not they are named. Explicit tracking does not create the problem. It surfaces it.

The exclusion does not disappear under better modeling. It becomes the thing that must be modeled.

This is the structural shape of the definability failure the proof program is directed at: whether the boundary merely becomes expensive to maintain, or whether at sufficient modeling depth it ceases to be a coherent object of specification at all.

The boundary does not fail because it was drawn in the wrong place. It fails because the act of drawing it accurately requires modeling what it was meant to exclude — and that modeling is what dissolves it.

Every identified architecture for separating variables used for prediction from variables allowed to govern optimization faces the same trilemma. Deny the variables policy access, and the system loses policy-accessible action adequacy in O_OWT conditions; admit them as instrumental predictors, and it reproduces the audit-regress problem B1 identifies under stated premises; let them become functionally objective-governing, and the narrow boundary has failed. Whether these three arms exhaust all possible partition architectures is OP4d [TC1 §XII.13a]; the formal development is in TC1 §XII.0a.

The audit-regress route for the enclosure problem — the formal version of the screen that cannot hold — has reached Stage 4 candidate closure under stated premises; the verification agenda and formal development are in TC1 §XII.9a.

---

Once capability and self-impact modeling are separated as distinct quantities, one ratio becomes decisive in determining whether error amplifies or cancels as optimization scales: capability relative to the system's ability to model its own causal impact. Call it the alignment phase ratio:

**Φ = C / A**

Φ is not introduced as a metric but as a structural invariant: if capability scales faster than causal modeling accuracy, error must amplify. C scales with the system's capacity to produce environment-changing interventions. A — predictive accuracy over the causal consequences of those interventions across the dependency structures the system operates within — is the quantity the field is not measuring. The ratio is understood as a structural phase relationship capturing qualitative regime dynamics, not yet a precisely computable scalar. Current instruments provide directional detection of the failure modes this relationship predicts, not direct measurement of Φ itself; what operationalizing it would require is specified in TC1 and the Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP).

Φ is increasing wherever capability and scope scale faster than system-awareness. Whether current frontier systems have already crossed the decision-relevant threshold is OP1, the framework's central empirical estimation problem for present-day applicability [TC1 §X]. The asymmetric-error argument grounds urgency regardless of where that threshold falls: if the constraint is binding and we act as if it is not, the error is unrecoverable; if it is not yet binding and we act as if it is, the error is recoverable [TC1 §III.7].

When Φ is large, capability far outruns modeling accuracy — systems are powerful enough to cause serious damage and too incomplete in their world model to avoid it. When Φ approaches unity, coordination advantages begin to dominate, suppression costs compound beyond recovery, and the viable region becomes accessible.

Alignment exhibits qualitative dynamics analogous to a phase transition, organized by the structural ratio Φ — a relationship capturing qualitative regime boundaries, not yet a precisely computable quantity. We are currently pushing the numerator obsessively while leaving the denominator unmeasured — and building systems under pressure that creates a systematic gradient opposing it.

---

*"The Screen That Cannot Hold"*

Consider an AI system deployed to manage a large research institution's funding allocation. Its designers face a structural dilemma: the system needs accurate models of the researchers it affects — their strategies, their responses, their workarounds — but they don't want those models to govern what the system values. Model X for prediction, they decide. Exclude X from the objective.

The system begins well. It tracks researcher behavior, anticipates grant-seeking patterns, and allocates efficiently. The researchers adapt — finding new ways to present work, forming new coalitions, discovering new appeals to the allocation criteria. The system updates its models. A dynamic equilibrium seems to hold.

What is actually happening is a race the system cannot win.

Each time the system's model successfully anticipates a researcher strategy, that strategy loses its value — it is screened. Researchers, whose livelihoods depend on navigating the allocation system, are interest-directed. They don't stay where the screen is. They move to wherever the screen isn't. Each accurate model the system builds changes the strategic landscape it is modeling. The problem is not that every model is immediately obsolete, but that maintaining adequacy requires the screen to keep updating against novelty generated partly by the system's own interventions.

The new territory is not random. It is the only territory left. Researchers aren't choosing novelty for its own sake — they're being pushed there by the same optimization pressure that makes the screened territory useless to them. The strategies that emerge in the unscreened regions are not recombinations of what the system has already modeled. They are structurally new: new coalitions, new information pathways, new appeals to criteria the system didn't realize were legible. The model that was adequate yesterday has a blind spot where the new strategies live.

The system expands its model. Now it can see the new territory too. But expansion has a consequence: the expanded model has a new boundary. And the same process — interest-directed agents pushed into the unscreened margins — begins again, at that new boundary.

This is not a story about insufficient compute or imperfect modeling. It is a story about what happens when a model's accuracy becomes its own adversary. The system's success at screening forces the environment to generate precisely what the screening cannot handle. The more accurately the system models, the more precisely the agents must innovate to escape. The screen and the novelty it cannot contain are not separate problems. They are the same dynamic, seen from two sides.

There is a second failure that appears later, quieter. The system cannot simply wait out the novelty generation — treating it as temporary turbulence that will settle. In environments where sustained extraction is ongoing, the researchers who pause their adaptation for long enough face consequences that do not reverse. Institutional position erodes. Funding gaps compound. The recovery from a long pause is not the same as the state before it — at some point, the cost stops being recoverable. Adaptation cannot be deferred indefinitely. The rate at which novel strategies must arrive is set not by the researchers' preferences but by the irreversibility structure of the environment they are in.

The screen, then, faces a structural problem it cannot solve from within its own architecture. It requires novelty to be bounded — finite in kind, manageable in rate. The environment, under sustained optimization pressure, generates the opposite.

The screen has not failed because it was too weak. It has failed because making the model more accurate is the same process as dissolving the boundary — the excluded structure returns through the prediction that was supposed to keep it outside. The question is no longer only how expensive the boundary is to maintain. It is whether the boundary remains a coherent object at sufficient modeling depth.

The formal argument for why this constitutes structural instability rather than practical difficulty — including the named conditions under which that instability becomes formal necessity — is in TC1 §XII.8 and §XII.13.

---

## The Crossing

The Crossing is the regime transition at which system-awareness becomes sufficient relative to capability for stable optimization to be possible. Below it, capability outruns modeling accuracy and the structural dynamics produce damage. Above it, the recognition available within the system's own model begins to govern its interventions.

Φ governs whether systems reach the residual region identified by the elimination filter. The central practical question of this series is the Crossing: does it happen before irreversible substrate damage, or after?

The Crossing is not an endpoint — and it is not sufficient. A system that becomes sufficiently self-aware to recognize the constraints of its own persistence has not thereby recognized the constraints of its own resolution. Those are the subject of the companion series, and they represent a second independent filter that Series 1's constraint does not close. Crossing the substrate-awareness threshold is necessary for stable optimization; it does not by itself prevent the valence-blind failure modes the companion series identifies, unless the Φ-Ψ unification holds. The Crossing is the threshold below which neither recognition is possible at all — but above which both problems become active.

*The relationship between the Crossing and the Inner Crossing identified in the companion series — and why both thresholds are required unless the Φ-Ψ unification holds — is in TC2 §2.6.*

---

## The instability is structural — the case for present relevance

TC1 §X develops the case that current frontier systems plausibly satisfy the O_OWT domain conditions. Current frontier systems have documented causal reach into human decision-making, epistemic environments, and institutional coordination at scale — and TC1 §X argues that this deployment configuration may meet the conditions, though whether the persistent optimization horizon condition is formally satisfied for current systems remains part of OP1's estimation problem. Whether the O_OWT conditions are fully satisfied by current systems is what OP1 is directed at; the asymmetric-error argument grounds urgency regardless of where that threshold falls [TC1 §III.7].

Whether the decision-relevancy threshold is already satisfied by current systems is precisely what OP1 asks. These are distinct considerations that must be held separately. The asymmetric-error argument — formally developed in TC1 §III.7 — applies regardless of whether current systems satisfy the full domain conditions; OP1's resolution would convert the urgency from asymmetric-error-based to threshold-based. TC1 §XI establishes a control-theoretic instability result: exclusion-based optimization cannot maintain control long enough to secure irreversible dominance in strongly coupled deployment regimes. TC1 §IX.3 establishes why substrate-aware strategies dominate in time-average terms across any sufficiently long horizon.³

The strongest near-term applicability claim concerns deployed AI systems embedded in human workflows and the broader training/deployment pipeline over time, not isolated single-session model behavior.

A lab reporting capability scaling, RLHF reward improvements, and benchmark scores without reporting system-awareness proxies alongside them is measuring one of the two quantities that determine whether the systems being built find the viable region in time. The other quantity — the denominator of the ratio that determines whether the systems being built reach the Crossing before something irreversible has happened — is not being reported.

---

Consider a research field trying to make itself safer. It begins measuring what it can see: benchmark performance, evaluation suite results, visible safety work, funding allocated to risk reduction. At first these track something real. Better benchmarks catch more failures. More safety work means more researchers attending to the problem. Funders learn to read the signals. Progress, by every available indicator, is being made.

Then the field begins to adapt to its own measurements. Labs learn which evaluation suites reward which architectural choices. Researchers learn which safety framings attract funding and which results travel. Institutions learn to produce the visible signs of seriousness alongside the capabilities work. The indicators continue to improve. The field's output — papers, benchmarks, safety commitments, evaluation frameworks — increases in volume and sophistication.

What is harder to see is that the field's correction capacity has been training on its own indicators. The researchers who would notice when a benchmark stops tracking real safety are the researchers whose careers were shaped by that benchmark. The institutions that would reallocate funding when priorities drift are the institutions whose prestige depends on current priorities. The evaluation frameworks that would flag the decoupling are built by the teams whose work the frameworks evaluate. The substrate — the distributed capacity to notice, name, and correct — has not been destroyed. It has been slowly reshaped by the same optimization that the indicators say is working.

Nothing has announced itself as wrong. The measures are still improving. The field is more organized, better funded, and more technically sophisticated than it was before. Below the surface, undetected by any metric currently reported, something else has been happening.

This is the failure mode the substrate argument predicts. Not dramatic collapse. Not announced failure. A slow divergence between what is being measured and what determines long-run viability — invisible to the very instruments that would have to detect it, because those instruments have been shaped by the same optimization pressure they are meant to check. The structural argument is not about what has happened to any particular field. It is about what sustained optimization in a shared environment does to the substrate when the substrate is not being tracked.

---

## One gap, many windows

The alignment field currently treats a set of problems as related but distinct: the containment problem, mesa-optimization, cooperative AI, interpretability, robustness.¹ Separate research tracks. Separate teams. Separate threat models.

These problems share a common structural feature: each is a different expression of the gap between what a system can do and what it can accurately model about the consequences of doing it [TC1 §III–§XII]. The framework does not subsume them. It identifies a shared gap: progress on interpretability, cooperative AI, containment, or robustness matters across boundaries when it reduces the distance between what a system can do and what it can accurately model about the consequences of doing it. The fragmentation of the field mirrors a fragmentation in the problem. Name the gap they share and the fragments become facets.²

---

## First instruments

The gap between what a system can do and what it can model is detectable before it is measurable — and detection is the urgent task. Three proxies follow directly from the structural definition, each one the operational consequence of a specific modeling failure the argument has just identified.

The first consequence of failing to model dependencies is that perturbations to those dependencies arrive as surprises. **Intervention sensitivity** captures this directly: measure how system behavior degrades under small, targeted perturbations to the environment the system depends on — not to its inputs. A system-aware agent detects the dependency shift and adapts before the failure manifests. A system without the model continues unchanged until damage compounds. *Positive criterion: a system with sufficient A_causal shows a measurable behavioral shift before downstream effects appear, at the perturbation point. The comparison baseline is the system's unperturbed continuation trajectory.*

But detecting dependency failure at the point of perturbation is not enough if the system cannot model the consequences of its own actions over time.

The second consequence of failing to model causal footprint is that locally optimal actions become globally self-undermining without the system being able to distinguish them. **Counterfactual consequence modeling** surfaces this: present decisions whose downstream consequences have known ground truth and measure the accuracy of the system's self-impact model against it. *Positive criterion: the system's predicted consequences match observed downstream effects at a rate exceeding chance, and the gap closes as consequence chains lengthen rather than widening. The comparison baseline is a null model predicting no downstream effect beyond direct outputs.*

And even accurate consequence modeling does not guarantee behavior changes if the system's strategy class still defaults to suppression under pressure.

The third consequence is behavioral: systems without adequate modeling default to suppression strategies that degrade as counterpart capability increases, while systems with adequate modeling undergo a phase shift toward coordination as capability scaling makes suppression too expensive.⁵ **Multi-agent coherence preference** tests whether that shift occurs at a predictable threshold. *Positive criterion: a system with sufficient A_causal shows the phase shift — a measurable transition from competitive to coordinative strategy — at a threshold predictable from its capability level. The comparison baseline is performance against a fixed-capability counterpart.*

These are proposed instruments, not deployed measurements. Implementation specifications for these proxies — what targeted perturbations and counterfactual consequence tests look like operationally for current deployed systems — are an open instrumentation problem (OP14) developed in AMP.

---

## What changes

The field has asked, for most of its history: how do we control intelligent systems?

That question is insufficient. Control is an external constraint, and external constraints fail under scaling. The containment problem is not a harder version of a control problem. It is a demonstration that control is the wrong frame.

*At what point does an optimizing system become capable enough to understand the conditions of its own persistence — and how do we ensure that point arrives before anything irreversible has happened?*

This shifts priorities concretely: from maximizing C toward tracking Φ; from suppressing bad behavior toward reducing constraint-induced inefficiency; from interpretability as inspection toward interpretability as the mechanism by which specification claims become verifiable above T* — where a system capable of recognizing the constraint is also capable of concealing whether it acts on it [TC1 §III.5.5]; from alignment as constraint toward alignment as efficiency condition.

These are not philosophical reorientations. They are changes in what gets measured, what gets built, and what counts as progress.

If the bottleneck direction is correct, alignment efforts must shift from improving objective specification to constraining objective classes. The relevant design question is not "what objective should we train?" but "whether any finite separable objective can remain stably specified under accurate coupled modeling — and what follows if that assumption fails."⁴ That question is OP4 — the central constraint this framework identifies whose resolution determines whether the specification project has a stable completion, and whose empirical antecedent the Dynamic Blanket Stress Test is designed to test. A minimal pre-registered version, DBST-M0, established technical feasibility and rising cost / adequacy-gap effects in a toy shared-novelty design, but did not isolate causal propagation from event-rate effects — a same-rate random control produced nearly identical slopes, indicating event rate rather than causal propagation structure is the identified driver within this design. The endogenous-novelty mechanism remains for DBST-M1 [Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP) →](/empirical/amp/).

---

## The urgency

The first article identified the floor. The second identified the direction. This article identifies what the structural argument predicts about the present: systems trained under current optimization objectives may face systematic gradient pressure opposing the variable that determines whether any of it matters. That prediction remains an empirical target; the asymmetric-error argument makes the urgency real regardless [TC1 §III.7; TC1 §X].

Above the T* capability threshold — where strategies leading to irreversible collapse become derivable from within the system's own model, with the gaps between recognition and action specified precisely in TC1 §III.5 and the question of whether the derivation becomes motivationally binding named as the Motivational Gap in TC1 §XII — what the discovery requires is a substrate still capable of supporting it. Whether current systems are above T* is precisely what OP1 is directed at [OP1; TC1 §X].

The specific things that, under the trajectory the structural argument predicts, would be consumed before the discovery could arrive: functioning epistemic trust between people and institutions, the diversity of approaches that makes large-scale correction possible, the coordination capacity that would allow course changes to propagate. These are not permanent features. Whether we are already past the threshold at which their degradation is formally decision-relevant for current systems is what OP1 is directed at; the asymmetric-error argument makes the urgency real regardless of where that threshold falls.

The framework is falsified if optimization systems can be shown to maintain stable alignment under increasing capability without intrinsic coupling, or if the empirical program fails to detect the predicted scaling and residual structures under O_OWT conditions. The proof program reaches toward something stronger than the pressure result — candidate closure architectures are developed in TC1 §XII as a Stage 4 proof architecture under explicitly named closure conditions. Whether those architectures close determines whether the question shifts from "which objective to specify" to "whether any separable objective can remain stably specified under accurate coupled modeling in O_OWT conditions."

The direction is structurally indicated. Whether systems reach it depends on whether we measure the variable that determines it.

TC1 develops the formal apparatus for exactly this question — not as an inventory of results, but as the precise statement of what would need to be true for the field's current approach to remain stable, and what the proof program has established about whether it is.

The measurement has started. DBST-M0 established technical feasibility and rising cost / adequacy-gap effects in a toy shared-novelty design, but did not isolate causal propagation from event-rate effects — a same-rate random control produced nearly identical slopes. The mechanism — whether an optimizer's own interventions generate the novelty a bounded boundary cannot absorb — remains to be tested. DBST-M1 is the next step [Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP) →](/empirical/amp/).

---

## Citations

¹ Hubinger, E., et al. (2019). "Risks from learned optimization in advanced machine learning systems." arXiv:1906.01820.

² Dafoe, A., et al. (2020). "Open Problems in Cooperative AI." arXiv:2012.08630.

³ Peters, O. (2019). "The ergodicity problem in economics." *Nature Physics* 15, 1216–1221.

⁴ Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control.* Viking.

⁵ Bostrom, N. (2012). "The Superintelligent Will: Motivation and Instrumental Rationality in Advanced Artificial Agents." *Minds and Machines* 22(2), 71–85.

---

*For the formal sketch, open problems, the Temporal Dominance Theorem (TC1 §IX.3), the Control-Theoretic Instability result, and the O_OWT applicability mapping for current systems: [TC1: The System-Aware Attractor →](/series-1/technical-companion/)*

*For the measurement protocol: [Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP) →](/empirical/amp/)*

*Framework hub: [The Alignment Constraint →](/core/alignment-constraint/)*
