---
title: "The Stability Assumption"
permalink: /core/stability-assumption/
description: "A field-facing entry essay on whether separable objective specification has a stable completion condition under accurate coupled modeling."
---

> **Canonical archive version** · [Read on Medium →](https://medium.com/@diamondlight/the-stability-assumption-b5dbdcfa6a2c) · [Framework hub →](/core/alignment-constraint/) · [Full OP4 paper →](/core/stability-assumption-full/)

---

Does separable objective specification have a stable completion condition? Or does the boundary between what a system optimizes for and what it must model break down as modeling depth increases — not as a practical difficulty, but as a structural feature of accurate action in coupled environments?

Every alignment approach — including this one — is making a structural bet about the answer.

The bet is not about whether current systems are dangerous or whether alignment is hard. It is a structural claim about a specific property of objective specification: that the boundary between what a system optimizes for and what it must model remains stable as the two converge — that this boundary can remain coherent as the system becomes more capable and the environment it acts in becomes more coupled. The claim here is not just that objectives Goodhart, or that capable systems pursue the wrong goals. It is that, as modeling depth increases, the boundary between objective and model may stop being a coherent object of specification. If that is right, the problem is not harder specification. It is a different kind of problem.

RLHF, Constitutional AI, debate, scalable oversight, and interpretability-as-monitoring differ in important ways. But each depends, somewhere, on a finite line between what the system optimizes for and what it merely models remaining coherent as capability and modeling depth increase. The mechanisms differ; the underlying stability assumption is shared.

AI alignment is the urgent test case, not the boundary of the claim. The question applies wherever sustained optimization operates in open, shared, non-resettable environments; AI is where the assumption is becoming practically unavoidable.

This is related to embedded agency, but the question is different. Embedded agency asks how agents model and act from within the world. This asks whether separable objective specification remains a coherent project once the model is accurate enough to include the conditions the objective depends on. Embedded agency asks how self-reference is handled. This asks whether the project of specifying a separable objective has a stable completion condition at all — a different question with a different answer structure. Embedded agency makes the agent/world boundary problematic; the stability assumption makes the objective/model boundary problematic. A system could handle many embedded-agency difficulties correctly and still face stability-assumption failure, because the latter concerns the objective/model boundary rather than only the agent/world boundary.

This is also distinct from ordinary Goodhart failure and mesa-optimization. Those assume a specification target whose adequacy can in principle be evaluated, then ask how proxies or learned objectives diverge from it. The stability assumption asks whether the separable specification target itself remains coherent under the modeling depth consequential action requires — a prior question, not a harder version of the same one.

The observation is this: as a system becomes capable enough to act consequentially in an open, coupled environment, it must model more of the structure of that environment — other agents’ strategies, long-range causal chains, the conditions under which its own interventions remain viable. At some point, the variables it needs to represent in order to act effectively are no longer cleanly separable from the variables its objective treats as outside the scope of what matters.

When that happens, the system is using a single model to do two things simultaneously: determine what actions lead to good outcomes, and enforce a boundary between what is allowed to influence the objective and what is merely informative. Those two roles are in structural tension. The model’s increasing accuracy in the first role creates pressure on the second.

Consider a writing assistant trained to help users produce better work. To act well, it may need to model something like the user’s creative autonomy: when to scaffold, when to push, when to stop, when intervention would make the work worse. But suppose autonomy is explicitly excluded from what the system optimizes; it is treated as useful for prediction, not as part of success.

At first, this distinction can look stable. The assistant uses autonomy-readings instrumentally while optimizing the proxy it was given. But as its interventions shape the user’s future behavior, the proxy-maximizing action and the autonomy-preserving action can come apart. The system now needs a rule for when autonomy is merely informative and when it should constrain action. That rule depends on the very model it was introduced to limit. The boundary has become part of the object being modeled.

There are several natural strategies for managing this tension. Keep the objective fixed and accept that it becomes an increasingly imperfect proxy for what you actually care about. Update it continuously, tracking the environment as it changes. Maintain an explicit firewall between what the model knows and what the objective covers. Extract value through structural position rather than direct specification. Each of these is a way of trying to preserve the separation.

The question the field has not made explicit enough is whether any of them work.

More precisely: can a finitely specified objective remain stably adequate — not perfect, but coherent as a specification — when the system must model and act within a coupled environment whose relevant variables are not contained within that specification? Or does the modeling required for effective action eventually make the specification itself unstable — not merely imprecise, but not well-defined as a stable boundary at sufficient modeling depth?

This is a question about the structure of objective specification, not about any particular objective’s content. It applies regardless of whether the objective is a reward function, a preference model, a set of principles, or a learned proxy. It applies to corrigible systems and non-corrigible systems alike. It does not depend on the system being deceptive or the designers being careless. It depends only on what accurate modeling in coupled environments requires.

The field has asked whether we can specify better objectives. It has not made central the question of whether the project of specifying separable objectives has a stable completion condition at all — whether there exists a class of finite objective specifications that can remain coherent at the modeling depths required for the systems we are building.

If the answer is yes, alignment is a specification problem and the field’s current direction is broadly correct. If the answer is no, the problem is misframed at its foundation. Not harder. Different.

The concern, at its sharpest, is referential. The worry is not only that a finite objective boundary becomes costly or unstable. It is that, at sufficient modeling depth, the target the boundary is trying to name may no longer have a stable referent — because the variables it excludes are part of what makes that target identifiable.

> The challenge, made direct: show a finite objective-boundary strategy that survives accurate coupled modeling without collapsing into fixed specification, bounded dynamic tracking, or prediction-action firewalling. If such a strategy exists, it is the counterexample. The formal counterexample conditions are in [the full OP4 paper: The Stability Assumption](/core/stability-assumption-full/).

The framework developed in [_The Alignment Constraint_](/core/alignment-constraint/) tests the opposite bet: that objective-boundary stability may fail under the conditions where it matters most. That may be wrong. But if an alignment approach depends on the bet going the other way, the question is no longer whether better specifications are achievable in principle. It is why the boundary between what the system optimizes for and what it must model remains stable as the two converge — and what evidence would settle that.

The full framework develops this question across physical, coordination, and experiential substrates. This post isolates the structural bet — and the smallest test I know for beginning to check it.

A minimal pre-registered version of that test, DBST-M0, has now been run — with an important caveat. A pre-specified same-rate random control produced nearly identical slopes to the bounded-boundary arm, indicating that event rate rather than causal propagation structure is the identified driver within this design. What M0 established is technical feasibility and rising cost / adequacy-gap effects in the simplest shared-novelty regime; it did not isolate causal propagation from event-rate effects, and it does not test agent-action-generated novelty. DBST-M1 — in which each arm’s own interventions causally influence future feature activations — is the mechanism test.

The predicted failure is not lower reward. It is rising boundary-maintenance cost or adequacy loss in the bounded-boundary arms relative to the open model, as pressure increases. If the bounded dynamic boundary maintains adequacy comparable to the open model without non-vanishing maintenance cost, the empirical direction of this framework is challenged. DBST-M0 established the design’s feasibility but not the mechanism. DBST-M1 is the next step.

The formal version of this question — including the three strategy families, the current Stage 4 proof architecture, and the counterexample challenge — is developed in [the OP4 paper: The Stability Assumption](/core/stability-assumption-full/).

The full framework is mapped in [The Alignment Constraint](/core/alignment-constraint/).

In concrete terms: show a system that can maintain a finite objective boundary without drifting from its target, expanding to track what it excluded, or generating mounting boundary-maintenance overhead — under conditions where the system’s own actions reshape the environment the boundary was specified over. If there is a finite-boundary strategy outside fixed specification, bounded dynamic tracking, and prediction-action firewalling that remains adequate under accurate coupled modeling in O_OWT environments, that is the thing to show. It would change the framework directly.
