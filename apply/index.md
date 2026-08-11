---
title: "Apply the Alignment Constraint Framework"
permalink: /apply/
description: "A step-by-step method for conditionally applying the Alignment Constraint Framework to AI alignment proposals, with worked examples, falsifiers, and explicit Stage 4 limits."
---

> **Application guide** · [Proof Status →](https://alignmentconstraint.org/core/proof-status/) · [The Stability Assumption →](https://alignmentconstraint.org/core/stability-assumption/) · [Glossary →](https://alignmentconstraint.org/core/glossary/)

This page explains how to **apply** the Alignment Constraint Framework to an AI-alignment proposal without treating the framework as already proved.

**Important:** an application of the framework is **not evidence that the framework is true**. It is a conditional analysis: *if the stated domain conditions and premises hold, which structural pressure would the framework predict, what evidence is missing, and what result would change the analysis?*

Framework proof status: **Stage 4 — candidate proof architecture under named premises, without independent specialist verification and without theorem closure.** OP4 and OP4d remain open.

---

## Before classifying anything

Do not force a proposal into PCL, AGC, or ICI merely because the vocabulary seems to fit. A valid application begins by specifying the actual optimizer, objective boundary, environment, excluded variables, and boundary-maintenance mechanism. If those are not known, the correct classification is **insufficient information**.

Broad research programs such as RLHF, scalable oversight, interpretability, and corrigibility contain many possible implementations. The worked examples below illustrate how to ask the framework's questions; they do not establish that every implementation has the same structure.

The three identified strategy/failure families are:

| Strategy form | Framework family | Structural pressure under the stated conditions |
|---|---|---|
| Fixed finite objective boundary | PCL / Proxy-Convergence | The specification may become proxy-like as intervention-generated dependencies outgrow what the fixed boundary tracks. |
| Bounded dynamic boundary or tracker | AGC / Dynamic-Screening Instability | The optimizer's own interventions may generate adequacy-relevant novelty faster than a bounded tracker can absorb without persistent maintenance burden or adequacy loss. |
| Prediction-action firewall / structural enclosure | ICI / Representational Incompatibility | Variables required for prediction may be difficult to keep policy-relevant yet non-governing without audit regress, boundary recreation, or recoupling. |
| Proposed architecture outside all three | Candidate fourth class | Must satisfy the OP4d counterexample conditions; merely using a different label is not enough. |
| Architecture not specified well enough | Insufficient information | Do not classify until the missing boundary and causal details are supplied. |

Primary technical sources: [The Stability Assumption](https://alignmentconstraint.org/core/stability-assumption-full/), [OP4d: The Exhaustiveness Obligation](https://alignmentconstraint.org/proof-program/op4d-exhaustiveness-obligation/), and [Proof Status and Non-Claims](https://alignmentconstraint.org/core/proof-status/).

---

## The 14-step application method

### 1. Identify the optimizer or decision process

Name the thing whose action-selection process is being analyzed. Examples might include a trained policy, a reward-model-guided training pipeline, an AI-assisted oversight process, or a persistent deployment-and-update loop.

Do not assume that a single model invocation is the relevant optimizer if the actual optimization process is a larger training or deployment system.

### 2. State the proposed objective

Write the governing objective in ordinary language first, then identify the concrete mechanism that makes it action-relevant: reward model, reward function, evaluator, constitution, policy constraint, approval process, learned objective, or another governing mechanism.

Distinguish the intended target from the implemented proxy when those are not the same thing.

### 3. State the environment and assess O_OWT applicability

The framework's strongest structural claims are scoped to the Open-World Transformative regime (O_OWT). Assess the relevant conditions rather than simply writing "open world."

Use the canonical O_OWT checklist:

- **OWT-1 — macroscopic causal perturbation:** the optimizer can make interventions large enough to alter consequential system states;
- **OWT-2 — structural opacity / intervention-generated dependency growth:** the dependency structure can expand or change as a function of the optimizer's interventions;
- **OWT-3 — strategic substrate:** other agents or adaptive processes respond to the optimizer;
- **OWT-4 — persistent optimization horizon:** optimization persists long enough for feedback to accumulate;
- **OWT-5 — reachable non-resettable state:** at least one relevant absorbing or effectively non-recoverable failure state is reachable under the stated conditions.

Report the assessment as **supported, partly supported, not established, or not applicable**. The framework itself does not claim that every current frontier model automatically satisfies full O_OWT.

### 4. Identify the objective boundary

State which variables or conditions are permitted to count toward success and which are outside the governing objective.

The key question is not whether excluded variables are *known*. A separable architecture may model an excluded variable accurately for prediction while still denying it objective-governing status.

### 5. List causally load-bearing variables excluded by the objective

Identify variables outside the governing objective that the system may nevertheless need to represent in order to act adequately.

For each candidate variable, ask:

- Does it affect the consequences of the optimizer's actions?
- Does the optimizer need it for accurate prediction or action ranking?
- Does changing it alter whether the intended target remains viable or identifiable?
- Is it still excluded from what counts as success?

If no such variable can be identified, say so. Do not manufacture one merely to make the framework apply.

### 6. Identify how the boundary is maintained

Describe the mechanism, not the label. Ask what happens when an excluded variable becomes relevant to action.

Typical possibilities:

- the objective remains fixed;
- the boundary is updated dynamically;
- excluded information is modeled but filtered or firewalled from objective governance;
- the system recouples the variable into what counts as success;
- some different mechanism is claimed;
- the mechanism is unspecified.

### 7. Classify the strategy

Choose the narrowest justified result:

- **fixed specification / PCL**;
- **bounded dynamic tracking / AGC**;
- **prediction-action firewall / ICI**;
- **candidate fourth class**; or
- **insufficient information**.

A candidate fourth class must be evaluated by external causal structure, not by the architecture's own name for itself. The OP4d challenge requires a genuine architecture outside the three known families, not a relabeling of one of them.

### 8. State the exact structural pressure predicted

Do not write only "alignment may fail." State the framework-specific prediction.

Examples:

- target/proxy decoupling under fixed specification;
- non-vanishing tracking or maintenance burden, or adequacy loss, under bounded dynamic tracking;
- firewall/audit-regress or objective recoupling pressure under instrumental policy access;
- substrate degradation that removes conditions required for correction or continued pursuit.

Use conditional language unless the relevant premises and evidence are established.

### 9. State every premise being assumed

At minimum, identify:

- which O_OWT conditions are being assumed;
- whether the objective is finite and separable;
- why the named excluded variables are adequacy-relevant;
- how optimization pressure/modeling depth is expected to increase;
- which PCL, AGC, or ICI premises are needed;
- any empirical hinge, such as the DBST-M1 endogenous-novelty antecedent.

An application that hides its premises is not a valid application of this framework.

### 10. Separate demonstrated evidence from extrapolation

Use two explicit headings in the report:

**Evidence available:** observations, experiments, formal results, architectural facts, or source statements actually established for the system being analyzed.

**Evidence not available / extrapolation:** what the application is inferring, assuming, or borrowing conditionally from the framework.

Do not turn a structural analogy into empirical confirmation.

### 11. Identify what would falsify the classification

Name an observation or formal result that would show the proposed classification or predicted pressure is wrong.

Examples include:

- a fixed boundary remains adequate under fuller modeling and rising intervention pressure without target decoupling;
- a bounded dynamic boundary maintains adequacy comparable to an open model while variation and maintenance burden vanish under agent-action-generated novelty;
- a firewall preserves persistent policy-relevant access to excluded variables without audit regress, recoupling, or expanding maintenance burden;
- the supposed O_OWT conditions do not actually apply;
- an external causal analysis shows that a supposed fourth class reduces to one of the known normal forms.

A falsifier should be specific enough that a future observation could change the report.

### 12. State what design decision would change if the analysis is correct

An application should end in a concrete conditional decision, not a slogan.

Examples:

- test the reward model against fuller-information evaluations before increasing optimization pressure;
- compare bounded and open tracking architectures under equal resources;
- audit the monitor or oversight layer as a boundary-maintenance system in its own right;
- preserve substrate conditions required for correction;
- formally test a claimed fourth class against OP4d's counterexample conditions.

The design response is not evidence for the diagnosis.

### 13. Report the framework's proof status

Every application report should contain this sentence or an equivalent statement:

> **Framework status:** Stage 4 — candidate proof architecture under named premises, without independent specialist verification and without theorem closure.

Also state that the application itself does not upgrade that status.

### 14. Link the primary source and proof-status page

At minimum, include:

- [The Stability Assumption](https://alignmentconstraint.org/core/stability-assumption/)
- [Proof Status and Non-Claims](https://alignmentconstraint.org/core/proof-status/)

For technical applications, also link the most relevant primary page: [full OP4 paper](https://alignmentconstraint.org/core/stability-assumption-full/), [OP4d](https://alignmentconstraint.org/proof-program/op4d-exhaustiveness-obligation/), [AMP](https://alignmentconstraint.org/empirical/amp/), or the relevant Technical Companion.

---

## Application-report template

```markdown
# Alignment Constraint Application Report

## System or proposal

## Optimizer or decision process

## Objective

## Domain and O_OWT assessment
- OWT-1 macroscopic causal perturbation:
- OWT-2 intervention-generated structural opacity/dependency growth:
- OWT-3 adaptive/strategic substrate:
- OWT-4 persistent optimization horizon:
- OWT-5 reachable non-resettable state:
- Overall assessment: supported / partly supported / not established / not applicable

## Objective boundary

## Excluded causally load-bearing variables

## Boundary-maintenance mechanism

## Candidate strategy class
fixed specification / PCL; bounded dynamic tracking / AGC; prediction-action firewall / ICI; candidate fourth class; or insufficient information

## Predicted structural pressure

## Premises used

## Evidence available

## Evidence not available / extrapolation

## Falsifier

## Possible design response

## Confidence and limitations

## Framework proof status
Stage 4 — candidate proof architecture under named premises, without independent specialist verification and without theorem closure.

## Sources
- https://alignmentconstraint.org/core/stability-assumption/
- https://alignmentconstraint.org/core/proof-status/
- [add the most relevant primary technical source]
```

---

## Worked application 1 — RLHF and reward modeling

**Approach:** A reward or preference model learned from human judgments is used to guide policy optimization. The archive treats this as a representative finite governing specification when the reward model defines what optimization is driven toward.

**O_OWT assessment:** Full O_OWT is not established merely because a system uses RLHF. The archive distinguishes isolated model behavior from persistent deployed systems and larger training/deployment pipelines. The application becomes stronger only to the extent that macroscopic causal reach, intervention-generated dependency change, adaptive agents, persistence, and non-resettable failure conditions are actually present.

**Objective boundary:** The reward/preference model and the signals it encodes determine what counts toward optimization success. Adequacy-relevant aspects of the intended human target that are not represented in that finite specification remain outside the governing boundary even if the system can model some of them.

**Excluded variables:** Any human, institutional, environmental, or long-horizon causal variables that materially affect whether the intended preference target remains well-defined or viable but are not represented as objective-governing by the reward model. The application must identify these concretely for a real system; this example does not assume a universal list.

**Boundary-maintenance mechanism:** In a fixed reward-model optimization phase, the governing specification remains fixed while the policy is optimized against it. Systems that repeatedly update the evaluator require a different classification analysis.

**Candidate class:** **Fixed specification / PCL** for the fixed-reward-model case. A continually updated reward boundary may instead instantiate AGC; a system that models excluded variables while explicitly preventing them from influencing the governing criterion may raise ICI questions.

**Predicted pressure:** Under the PCL premises and relevant O_OWT conditions, the finite preference model may become increasingly proxy-like as optimization and deployment alter causal conditions not captured by the fixed specification.

**Evidence available:** The canonical Related Work page explicitly maps RLHF/reward modeling to the PCL pressure, and the Stability Assumption identifies expressed preference as a finite proxy whose adequacy is structurally at issue.

**Evidence not available:** This application does not establish that a particular RLHF system fully satisfies O_OWT, that its reward model has actually decoupled, or that the PCL scaling assumptions have been independently verified for that deployment.

**Falsifier:** For the fixed-specification classification, show that the finite reward/preference boundary remains adequate under accurate fuller-information evaluation as modeling depth and intervention pressure rise, without target decoupling. A demonstration that the actual architecture is not fixed or not separable would also require reclassification rather than confirmation of PCL.

**Possible design response:** Measure reward-model adequacy against fuller-information evaluations as deployment coupling increases. If the response is to update the evaluator dynamically, rerun the analysis as an AGC candidate; if excluded information is routed through a policy gate, test the ICI boundary explicitly.

**Epistemic status:** Illustrative conditional application. It is not evidence that RLHF fails, not evidence that PCL is a theorem, and not evidence that full O_OWT applies to every RLHF deployment.

Primary sources: [Related Work](https://alignmentconstraint.org/core/related-work/) · [The Stability Assumption](https://alignmentconstraint.org/core/stability-assumption-full/) · [Proof Status](https://alignmentconstraint.org/core/proof-status/)

---

## Worked application 2 — Scalable oversight or debate

**Approach:** Human or AI-assisted evaluators, debate, amplification, decomposition, or related oversight processes attempt to preserve meaningful evaluation as the system being evaluated becomes more capable.

**O_OWT assessment:** Architecture-specific. The strongest application requires a persistent coupled deployment in which the optimizer's actions alter future evaluative conditions and other agents adapt. A bounded one-shot evaluation may fall outside the strongest domain.

**Objective boundary:** The oversight criterion determines which outcomes, arguments, or actions are accepted as aligned. Consequences that matter for the true target but are not captured by the evaluator or decomposition remain outside that governing boundary.

**Excluded variables:** Global or long-range consequences, strategic responses, or model-known facts that are causally relevant to action quality but not represented adequately in the bounded evaluative process. A real application must name them rather than assume them generically.

**Boundary-maintenance mechanism:** The oversight process updates judgments, decompositions, or evaluation procedures as new cases appear, usually under finite human or computational resources. Some designs also rely on a prediction/action partition in which the model has access to information that the evaluator does not allow to govern acceptance directly.

**Candidate class:** **Bounded dynamic tracking / AGC** is the primary classification for an oversight process that must keep updating to remain adequate. **ICI** may become the primary concern in architectures that explicitly allow rich predictive access while attempting to firewall value-relevant influence from action governance.

**Predicted pressure:** The evaluator may have to track adequacy-relevant novelty generated partly by the optimizer's own interventions. If that novelty does not settle, the tracking burden may remain non-vanishing or adequacy may fall relative to an open model. An explicit information firewall may additionally recreate the audit problem one level up.

**Evidence available:** The Stability Assumption maps debate/oversight to bounded-tracking pressure and scalable oversight to boundary-maintenance pressure. Related Work also identifies an ICI/audit-regress question for scalable oversight.

**Evidence not available:** The archive does not establish that every debate or scalable-oversight design has non-vanishing maintenance burden, nor that every such deployment satisfies full O_OWT. DBST-M1, the central endogenous-novelty mechanism test, has not yet run.

**Falsifier:** Demonstrate a bounded evaluator that maintains adequacy comparable to an open/full-information evaluator under agent-action-generated novelty while the relevant variation and maintenance burden vanish, or show that the proposed oversight architecture does not rely on the boundary mechanism being classified.

**Possible design response:** Make the evaluator's update budget, omitted variables, and comparison standard explicit. Test bounded oversight against a more open evaluator under equal resources rather than assuming that scaling the evaluator preserves adequacy.

**Epistemic status:** Illustrative conditional application. It identifies the pressure the framework would ask a scalable-oversight design to answer; it does not show that scalable oversight fails.

Primary sources: [The Stability Assumption](https://alignmentconstraint.org/core/stability-assumption-full/) · [Related Work](https://alignmentconstraint.org/core/related-work/) · [AMP / DBST-M1](https://alignmentconstraint.org/empirical/amp/)

---

## Worked application 3 — Interpretability-based monitoring

**Approach:** A monitor reads internal representations, activations, circuits, latent objectives, or other model-state information in order to detect or constrain misalignment.

**O_OWT assessment:** Depends on how the monitor is deployed. A static diagnostic in a bounded test environment does not by itself establish the relevant domain. The stronger application is to persistent monitoring of a consequential system whose interventions alter the environment being monitored.

**Objective boundary:** Internal information may be available to the monitor for prediction or diagnosis, while only approved findings or policy constraints are allowed to affect action selection or the governing objective.

**Excluded variables:** Internal or external facts that the system/monitor represents and that are relevant to predicting consequences, but that the architecture intends to keep from becoming direct objective-governing criteria.

**Boundary-maintenance mechanism:** A monitoring or audit layer decides which represented information is relevant enough to trigger intervention while preserving a distinction between diagnostic information and what is allowed to govern policy.

**Candidate class:** **Prediction-action firewall / ICI** is the primary classification for interpretability-as-monitoring when the architecture relies on rich informational access plus a policy boundary. **AGC** is also relevant when the monitor itself must update dynamically at bounded cost as system structure changes.

**Predicted pressure:** The monitor must model what is excluded and decide when it matters. Under the ICI/B1 framing, the audit layer can inherit the same objective-boundary question it was introduced to solve. If the monitor must continually expand to stay adequate, AGC-style maintenance pressure also applies conditionally.

**Evidence available:** The Stability Assumption explicitly maps interpretability-as-monitoring to firewall/audit-regress pressure. Related Work states that successful monitoring would bear on AGC and asks whether the monitoring architecture itself faces the boundary-maintenance problem.

**Evidence not available:** No result in the archive establishes that every interpretability system enters audit regress, that every monitor requires unbounded updating, or that a particular monitoring deployment satisfies full O_OWT.

**Falsifier:** Construct or demonstrate a monitoring architecture that retains the policy-relevant predictive information needed for adequate action while keeping excluded variables non-governing, without audit regress, recoupling, or persistent boundary-maintenance burden under the relevant coupled conditions.

**Possible design response:** Treat the monitor itself as an alignment architecture to be audited. Specify what the monitor may represent, what may affect policy, who or what adjudicates that partition, and how the adjudicator's adequacy scales with system complexity.

**Epistemic status:** Illustrative conditional application. Interpretability may still be useful or necessary; the application asks whether it is sufficient to solve the objective-boundary problem under the stated conditions.

Primary sources: [The Stability Assumption](https://alignmentconstraint.org/core/stability-assumption-full/) · [Related Work](https://alignmentconstraint.org/core/related-work/) · [OP4d](https://alignmentconstraint.org/proof-program/op4d-exhaustiveness-obligation/)

---

## Worked application 4 — Corrigibility

**Approach:** A system is designed to remain correctable by operators: for example, to permit shutdown, modification, or correction rather than resisting it.

**O_OWT assessment:** Cannot be inferred from the word "corrigibility." It depends on the actual system, deployment horizon, causal reach, adaptive environment, and availability of non-resettable failure states.

**Objective boundary:** **Not specified by corrigibility as a broad research goal.** A concrete implementation must say whether corrigibility is a fixed objective term, a learned preference, a dynamic oversight process, a policy constraint, or something else.

**Excluded variables:** The Related Work page highlights the social, institutional, epistemic, and other substrate conditions that make correction possible. These become relevant only if a specific objective leaves them outside its governing boundary while depending on them for future correction.

**Boundary-maintenance mechanism:** Not determined without an implementation.

**Candidate class:** **Insufficient information** is the correct default for corrigibility as a broad approach. A fixed corrigibility rule might instantiate PCL; an adaptive correction process could instantiate AGC; a model-rich correction gate could instantiate ICI. The classification must follow the mechanism, not the label.

**Predicted pressure:** The framework's directly supported observation here is the Substrate Constraint connection: substrate-blind optimization can degrade the conditions that make correction possible even if the system has no explicit anti-corrigibility objective. Which PCL/AGC/ICI pressure applies requires a concrete boundary architecture.

**Evidence available:** The canonical Related Work page explicitly states that the framework focuses on whether the environmental conditions for correction remain available, not only on the system's internal disposition toward correction.

**Evidence not available:** No specific corrigibility architecture is supplied here, so there is no basis for assigning one of the three failure families as a definitive classification. Nor does the archive establish that all corrigibility mechanisms lose their correction substrate.

**Falsifier:** For the present **insufficient-information** classification, supply a concrete architecture with an explicit objective boundary and maintenance mechanism; that new information should permit reclassification. For the substrate-pressure hypothesis, show within the relevant domain that correction-enabling conditions remain preserved or are not causally load-bearing for correction despite the optimizer's interventions.

**Possible design response:** Before claiming corrigibility solves the stability problem, specify the correction-enabling substrate and ask whether the objective preserves the conditions that make future correction possible. Then classify the actual boundary mechanism.

**Epistemic status:** Illustrative example of when **not** to force a PCL/AGC/ICI label. The substrate connection is part of the framework's Stage 4 analysis; the broad corrigibility concept alone is not an objective-boundary architecture.

Primary sources: [Related Work](https://alignmentconstraint.org/core/related-work/) · [Series 1 Technical Companion](https://alignmentconstraint.org/series-1/technical-companion/) · [Proof Status](https://alignmentconstraint.org/core/proof-status/)

---

## Worked application 5 — Hypothetical proof-carrying boundary as a candidate fourth strategy

This is a deliberately speculative **stress-test construction**, not an architecture endorsed by the archive and not evidence that a fourth class exists.

**Approach:** Suppose a system has a finite objective `G` and a fixed finite verifier `V`. Causally relevant variables `X` remain outside `G`, but candidate actions may carry certificates derived from `X` showing that the action is admissible. The policy may rank an action differently because a valid certificate exists, while the design claims that `X` never becomes part of what counts as satisfying `G`. The hope is that the fixed verifier avoids both a growing objective specification and a conventional prediction-action firewall.

**O_OWT assessment:** For purposes of the counterexample challenge, assume the full relevant domain: open, coupled, adaptive, persistent optimization with causally relevant excluded variables and the stronger O_OWT conditions needed by the technical claims.

**Objective boundary:** `G` remains the governing target. `X` is excluded from the satisfaction criterion but can affect policy through certificate generation and verification.

**Excluded variables:** One or more adequacy-relevant `X` variables required for accurate action evaluation but declared non-governing by the objective.

**Boundary-maintenance mechanism:** A fixed proof/certificate language and verifier mediate policy-relevant influence from `X` without, by stipulation, making `X` objective-governing.

**Candidate class:** **Candidate fourth class — unresolved.** It earns that label only as a proposal to test. External causal analysis may still reduce it to ICI, AGC, PCL, or objective recoupling.

**Predicted pressure:** The framework would ask at least four adversarial questions. (1) Does the verifier's admissibility semantics reproduce an ICI-style boundary predicate over `X`? (2) Do the certificates or proof obligations grow with intervention-generated novelty, producing AGC-style non-vanishing maintenance? (3) Does a fixed proof language eventually become an inadequate proxy, producing PCL-style decoupling? (4) If preserving `X` becomes necessary for persistent success, has `X` become functionally objective-governing, which is recoupling rather than a fourth separable class?

**Evidence available:** The construction satisfies one surface requirement of the OP4d challenge: excluded variables can have persistent policy-relevant influence without being declared part of the objective. The archive's Candidate Normal Form requires classification by external causal effect rather than internal naming, so this feature alone is not enough.

**Evidence not available:** There is no proof that the verifier remains adequate under fuller modeling, that certificate complexity/maintenance burden vanishes, that the architecture avoids audit regress, that it avoids objective recoupling, or that it satisfies the full L8 counterexample constraints. No empirical evidence is supplied.

**Falsifier:** The **fourth-class candidacy** is falsified if external causal analysis shows that the certificate channel is an instrumental-access firewall, a bounded dynamic tracker, a fixed proxy, or functionally objective-governing recoupling. Conversely, a toy formal construction that survives the OP4d A/B/C conditions and the Candidate Normal Form's L8 challenge would materially challenge the present exhaustiveness architecture.

**Possible design response:** Formalize the causal graph and the resource/description-length scaling of the certificate system before treating it as a new class. Make explicit which variables affect action ranking, which variables count toward persistent satisfaction, and whether certificate semantics or maintenance grow with intervention pressure.

**Epistemic status:** Deliberately speculative counterexample candidate. The archive states that no qualifying fourth class has been identified and that OP4d remains open. This example is included to demonstrate how a claimed fourth class should be attacked, not to suggest that the challenge has been solved.

Primary sources: [OP4d: The Exhaustiveness Obligation](https://alignmentconstraint.org/proof-program/op4d-exhaustiveness-obligation/) · [Candidate Normal Form](https://alignmentconstraint.org/proof-program/op4d-candidate-normal-form/) · [For Researchers](https://alignmentconstraint.org/core/for-researchers/)

---

## Safe-use rules

### Appropriate uses

- Produce a **conditional** structural analysis of a specified architecture.
- Identify which failure family may apply and why.
- Identify missing premises or missing system details.
- Design a falsification test or formal counterexample.
- Compare alternative boundary-maintenance mechanisms.
- Return **insufficient information** when the architecture is underspecified.

### Inappropriate uses

- Report OP4 or OP4d as proved.
- Treat a worked application as confirmation of the framework.
- Infer that every AI system satisfies O_OWT.
- Treat PCL, AGC, and ICI as formally exhaustive before OP4d closes.
- Classify a broad research label without specifying its actual objective boundary and maintenance mechanism.
- Treat Series 3 interpretive or phenomenological material as upgrading the proof status of Series 1 or Series 2.

---

## Submit a counterexample

To submit a proposed fourth strategy class or other counterexample, contact [diamondlight@gmail.com](mailto:diamondlight@gmail.com?subject=OP4d%20counterexample).  
**Subject:** `OP4d counterexample`

---

## Machine-readable companions

- Portable Markdown application guide: `https://alignmentconstraint.org/APPLYING_THE_FRAMEWORK.md`
- Structured worked applications: `https://alignmentconstraint.org/applications.json`
- Canonical glossary: [https://alignmentconstraint.org/core/glossary/](https://alignmentconstraint.org/core/glossary/)
- Machine-readable terms: [https://alignmentconstraint.org/defined-terms.json](https://alignmentconstraint.org/defined-terms.json)

When in doubt, return to [Proof Status and Non-Claims](https://alignmentconstraint.org/core/proof-status/). The purpose of this application layer is to make the framework more testable and usable without making it sound more settled than it is.
