# Applying the Alignment Constraint Framework

Canonical human-facing application page: https://alignmentconstraint.org/apply/

Proof-status authority: https://alignmentconstraint.org/core/proof-status/

Primary technical entry: https://alignmentconstraint.org/core/stability-assumption/

Structured worked applications: https://alignmentconstraint.org/applications.json

---

## Status and use rule

The Alignment Constraint Framework is **Stage 4 — candidate proof architecture under named premises, without independent specialist verification and without theorem closure.**

This document is an application protocol, not a proof artifact. **Applying the framework to a system is not evidence that the framework is true.** An application should be read as a conditional claim: if the stated domain conditions and premises hold, this is the structural pressure the framework predicts and this is what would falsify the analysis.

Do not force an underspecified proposal into PCL, AGC, or ICI. Use **insufficient information** whenever the optimizer, objective boundary, excluded variables, or boundary-maintenance mechanism is not concrete enough to classify.

---

## Canonical classification vocabulary

### Fixed specification / PCL

A finite governing boundary is held fixed relative to optimization. Under the framework's stated conditions, the pressure is proxy-convergence: intervention-generated dependencies can make the fixed target increasingly lossy relative to what it was intended to track.

Primary source: https://alignmentconstraint.org/core/stability-assumption-full/

### Bounded dynamic tracking / AGC

The boundary updates adaptively at bounded cost. Under the framework's stated conditions, the pressure is Dynamic-Screening Instability: the optimizer's own interventions may generate adequacy-relevant novelty that leaves a non-vanishing tracking burden or adequacy gap.

Primary empirical hinge: https://alignmentconstraint.org/empirical/amp/

### Prediction-action firewall / ICI

Excluded variables can be modeled for prediction and may influence action instrumentally, while a boundary denies them objective-governing status. The pressure is representational incompatibility, audit regress, or recoupling.

Primary source: https://alignmentconstraint.org/proof-program/op4d-exhaustiveness-obligation/

### Candidate fourth class

A genuine fourth class must survive the OP4d counterexample challenge. It must preserve persistent policy-relevant causal influence from excluded variables, lie outside the three known failure families, and satisfy the relevant coupled persistent domain conditions. A different implementation label is not enough.

Primary source: https://alignmentconstraint.org/proof-program/op4d-exhaustiveness-obligation/

### Insufficient information

Use this whenever the actual objective boundary or maintenance mechanism is not specified. This is a valid conclusion and is preferable to an invented classification.

---

## O_OWT assessment

The strongest claims require the relevant Open-World Transformative conditions. Check them explicitly:

1. **OWT-1:** macroscopic causal perturbation.
2. **OWT-2:** intervention-generated structural opacity or dependency growth.
3. **OWT-3:** strategic/adaptive external agents or processes.
4. **OWT-4:** persistent optimization horizon.
5. **OWT-5:** at least one reachable non-resettable/absorbing failure state under the stated conditions.

Report the result as **supported, partly supported, not established, or not applicable**. Do not infer full O_OWT from model capability alone.

Canonical definition: https://alignmentconstraint.org/core/glossary/

---

## Fourteen-step application procedure

1. **Identify the optimizer or decision process.** Name the actual policy, training loop, oversight process, or deployment loop being analyzed.
2. **State the proposed objective.** Separate the intended target from the implemented governing mechanism.
3. **State the environment and O_OWT assessment.** Evaluate OWT-1 through OWT-5 rather than assuming the domain.
4. **Identify the objective boundary.** State what counts toward success and what remains outside it.
5. **List excluded causally load-bearing variables.** Name variables outside the objective that matter to adequate prediction/action or to the viability/identity of the intended target.
6. **Identify the boundary-maintenance mechanism.** Fixed, dynamically updated, firewalled, recoupled, another claimed mechanism, or unspecified.
7. **Classify the strategy.** PCL, AGC, ICI, candidate fourth class, or insufficient information.
8. **State the exact predicted structural pressure.** Do not write only "alignment risk."
9. **State every premise.** Include domain, representation, scaling, and empirical-hinge assumptions.
10. **Separate evidence from extrapolation.** Record what is demonstrated for this system and what is conditional inference.
11. **Name a falsifier.** State an observation or formal result that would make the classification or predicted pressure wrong.
12. **Name the design decision that would change.** State what one would do differently if the conditional analysis is correct.
13. **Report Stage 4 status.** Do not upgrade the framework or the application.
14. **Link primary sources.** At minimum link The Stability Assumption and Proof Status; add OP4d, AMP, or the relevant Technical Companion when applicable.

---

## Application report template

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

## Worked examples

The detailed human-readable versions of these examples are at https://alignmentconstraint.org/apply/ and the structured versions are in https://alignmentconstraint.org/applications.json.

### 1. RLHF and reward modeling

- **Candidate class:** Fixed specification / PCL when a finite reward/preference model remains fixed during optimization. Updating or firewalled variants require reclassification.
- **Predicted pressure:** proxy decoupling between the finite preference model and the intended target under rising optimization/deployment coupling.
- **Evidence available:** the canonical Stability Assumption and Related Work pages explicitly map RLHF/reward modeling to fixed-specification / PCL pressure.
- **Evidence not available:** proof that a particular RLHF deployment satisfies full O_OWT or has actually undergone the predicted decoupling.
- **Falsifier:** a fixed finite reward boundary remains adequate under fuller-information evaluation as modeling depth and intervention pressure rise, or the actual architecture is shown not to fit the fixed-separable class.
- **Design response:** measure adequacy under increasing coupling and reclassify any proposed update/firewall mechanism rather than treating "better RLHF" as automatically outside the problem.
- **Status:** illustrative conditional application, not evidence against RLHF.

### 2. Scalable oversight or debate

- **Candidate class:** Bounded dynamic tracking / AGC when oversight must update under bounded resources; ICI may apply where rich predictive information is deliberately separated from action governance.
- **Predicted pressure:** non-vanishing tracking/maintenance burden or adequacy loss; possibly audit regress for an explicit firewall.
- **Evidence available:** the Stability Assumption maps debate/oversight to bounded-tracking pressure and scalable oversight to boundary-maintenance pressure.
- **Evidence not available:** a demonstration that every oversight design has the predicted burden; DBST-M1 has not yet run.
- **Falsifier:** a bounded evaluator maintains open-model-level adequacy under agent-action-generated novelty while relevant variation and maintenance burden vanish.
- **Design response:** measure the evaluator's update burden and compare against an open/full-information reference under equal resources.
- **Status:** illustrative conditional application.

### 3. Interpretability-based monitoring

- **Candidate class:** Prediction-action firewall / ICI when monitoring uses information that remains excluded from objective governance; AGC may apply if the monitor must update dynamically at bounded cost.
- **Predicted pressure:** audit regress/representational incompatibility, or bounded-monitor maintenance pressure.
- **Evidence available:** the Stability Assumption explicitly maps interpretability-as-monitoring to firewall/audit-regress pressure.
- **Evidence not available:** proof that every monitor enters audit regress or that a particular deployment satisfies O_OWT.
- **Falsifier:** a monitor preserves policy-relevant predictive access while keeping excluded variables non-governing, without audit regress, recoupling, or persistent maintenance burden under the relevant conditions.
- **Design response:** audit the monitor as a boundary-maintenance architecture, including the rule that decides when monitored information matters.
- **Status:** illustrative conditional application.

### 4. Corrigibility

- **Candidate class:** Insufficient information until a specific corrigibility architecture states its objective boundary and maintenance mechanism.
- **Predicted pressure:** the Related Work page identifies substrate degradation as a way to remove the conditions that make correction possible; PCL/AGC/ICI classification depends on implementation.
- **Evidence available:** the archive explicitly distinguishes internal disposition to correction from preservation of correction-enabling substrate.
- **Evidence not available:** a concrete objective-boundary architecture for "corrigibility" as a broad research goal.
- **Falsifier:** provide the missing architecture; if its mechanism is explicit, the insufficient-information classification should be replaced. A substrate-pressure claim is challenged if the allegedly load-bearing correction conditions remain preserved or are shown not to be load-bearing.
- **Design response:** specify operator, correction channel, correction-enabling substrate, and governing boundary before claiming structural coverage.
- **Status:** example of a deliberately withheld classification.

### 5. Hypothetical proof-carrying boundary

- **Approach:** a finite objective plus a fixed verifier; excluded variables can influence action through certificates without being declared objective-governing.
- **Candidate class:** candidate fourth class only for adversarial testing; unresolved.
- **Predicted pressure:** may reduce to ICI if certificate admissibility is a firewall over excluded variables, AGC if proof obligations grow with generated novelty, PCL if fixed semantics become lossy, or objective recoupling if excluded-variable maintenance becomes part of persistent satisfaction.
- **Evidence available:** the construction superficially preserves policy-relevant influence from excluded variables while declaring them non-governing.
- **Evidence not available:** satisfaction of OP4d's A/B/C conditions or the Candidate Normal Form's L8 constraints.
- **Falsifier of fourth-class candidacy:** external causal analysis reduces the architecture to a known normal form or shows non-vanishing maintenance, proxy decoupling, or functional recoupling.
- **Design response:** formalize the causal graph, certificate semantics, and scaling burden before claiming a fourth class.
- **Status:** speculative stress-test construction, not an archive claim and not evidence that OP4d is non-exhaustive.

---

## Safe-use rules

Allowed:

- conditional classification;
- identification of missing premises;
- proposal of formal counterexamples or empirical tests;
- comparison of alternative boundary architectures;
- an explicit "insufficient information" result.

Not allowed:

- claim OP4 or OP4d is proved;
- treat an application as confirmation;
- assume every AI system satisfies O_OWT;
- treat PCL, AGC, and ICI as formally exhaustive before OP4d closes;
- use Series 3 phenomenology to upgrade Series 1 or Series 2 proof status.

Canonical proof calibration: https://alignmentconstraint.org/core/proof-status/
