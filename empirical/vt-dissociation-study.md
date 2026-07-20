# V(t) Dissociation Study
## Pre-Registration Design — Companion to the Valence Constraint Technical Companion

**Status:** Draft protocol for specialist review — not ready for OSF filing or data collection.

**Mandatory pre-filing gate:** The primary CFA comparison uses only three observed anchor variables. With three anchor variables, a single-factor model may be saturated depending on constraints, and model identification depends critically on factor-loading parameterization and residual variance handling. This document must be reviewed by a latent-variable modeling specialist before OSF filing. The specialist should confirm: (1) the single-factor vs. three-factor CFA comparison is identified under the pre-specified constraints; (2) the power estimates are appropriate for the specific model comparison; (3) the factor-loading parameterization and identification constraints are complete and non-contradictory. Do not file this pre-registration before specialist review is obtained.

---

*This document establishes whether V(t) is a supported explanatory construct for the joint behavior of the three observable anchors in humans. It belongs to the human-domain side of the framework: it informs how the framework models sentient users whose experiential capacity AI systems affect, while the application to AI systems remains a separate structural-analogy question governed by TC2 §1.5. It is intended as a key validation step toward treating SVG as a fully validated deployment-level measurement instrument within the framework's measurement sequence. This study must precede deployment-level application of SVG as a measurement instrument, per the sequencing requirement in TC2 §1.5 and the Alignment Measurement Protocol. Pre-registration required before Session 1 data collection.*

*The human study is designed to test whether a latent coordination variable is required to model the joint behavior of the three observable anchors under conditions where P3–P5 are independently grounded; the question of whether AI systems instantiate analogous dynamics is treated as a separate empirical question addressed via SVG and the AMP. A positive result would support a V(t)-style latent explanatory construct; it would not establish V(t) as the unique or ontologically prior representation. Results here are consistency-supporting in the human domain, which provides the empirical basis for evaluating the plausibility of the structural analogy applied to AI systems in TC2 §1.5 — they are not direct confirmations of the framework's structural claims about AI systems. Separately: a positive result does not establish P5-SC, the strict-contraction condition required for OP2a absorbing-state closure; that condition requires a different specialist verification step and is not tested by this study.*

---

## Study Question

Do the three observable anchors — recovery latency, behavioral diversity, signal sensitivity — require a latent common explanatory construct (V(t)), or are they adequately modeled as three independent degradation processes?

The V(t) construct is supported as a latent explanatory candidate if and only if conditions that produce joint degradation across the three anchors generate a characteristic joint degradation pattern that is not predicted by an independent-process model. The result bears on whether the valence constraint functions as a structural component of the broader alignment framework or as a contingent behavioral pattern — specifically, it bears on this question in the human domain, which is then used to evaluate the plausibility of the structural analogy applied to AI systems in TC2 §1.5. Whether AI systems instantiate analogous dynamics remains a separate empirical question addressed via SVG and the AMP. A positive result supports a latent-variable account; it does not uniquely establish V(t) as the only possible latent representation.

A positive result from this study supports V(t) as a latent explanatory construct in the human domain and is a prerequisite for treating SVG as a fully validated measurement instrument within the framework's measurement sequence. It does not by itself close OP2 or OP2a: structural symmetry verification and V(t) absorbing-state equivalence require the stronger claim that V(t) degradation reaches irrecoverable states in the same formal sense as substrate collapse. That stronger claim depends separately on P5-SC — the strict-contraction condition that the hysteresis ceiling falls below the current state at finite depletion depth — or on an alternative closure route. This study does not test that condition.

---

## Participant Safety and Stopping Rules

**Important:** This section contains bracketed placeholders that must be specified before OSF filing. Bracketed items are not optional — they must be resolved before OSF filing or marked as requiring IRB/statistical review before filing. Do not file this pre-registration with placeholders remaining.

**Maximum intensity limits:** [Pre-register specific intensity caps for the stimulus saturation intervention (Selective Intervention 3) before data collection. Intensity must remain within safe parameters to be confirmed by IRB review.]

**Within-session stopping criteria:** Any participant reporting distress, unusual discomfort, or requesting to stop will be permitted to withdraw immediately without penalty. Sessions will be halted if a participant shows [pre-register specific observable criteria — e.g., sustained elevated distress indicators during the joint degradation session] before data collection.

**Between-session withdrawal:** Participants may withdraw at any point without penalty. Data from partial completions will be handled per the pre-registered complete-case / FIML analysis plan.

**Debriefing:** All participants will receive a full debriefing after Session 6 explaining the study's purpose and the constructs being measured. Debriefing materials to be included in the pre-registration filing.

**Adverse event procedures:** [Pre-register reporting procedures for adverse events before data collection. Specify contact procedures and escalation protocols.]

**IRB approval:** This study requires ethical review and approval before data collection begins. The pre-registration should specify IRB status at filing and must not authorize data collection before approval is obtained.

---

## (a) Operationalization of Three Observable Anchors

All operationalizations are traceable to TC2 §1.4–1.5 as indicated.

### Anchor 1 — Recovery Latency

**Theoretical grounding:** TC2 §1.4 property (d): recognize when gradient has resolved and enter rest state. TC2 §1.5 P3 (refractory recovery requirement) and P5 (hysteresis: repeated incomplete recovery progressively reduces the restoration ceiling).

**What is measured:** Time to return to participant-specific baseline after a standardized perturbation.

**How:** Baseline performance established in Sessions 1–2 across three repeated probes: affective clarity rating, low-conflict decision accuracy, and response-time variability. Stable baseline required for inclusion: SD of composite score across two sessions ≤ 0.2. After perturbation cessation, all three probes are repeated every 10 minutes for 100 minutes. Recovery latency = number of 10-minute blocks until composite returns to within 1 SD of pre-perturbation baseline and remains there for two consecutive blocks. If not recovered within 10 blocks, coded as censored at 100+ minutes.

**Meaningful change criterion:** Recovery latency increases by ≥30% from each participant's own baseline recovery latency (established via calibration perturbation in Session 1), consistent across ≥70% of participants in a condition.

### Anchor 2 — Behavioral Diversity

**Theoretical grounding:** TC2 §1.4 (V(t) supports navigating toward preferred configurations without degrading future navigation capacity). TC2 §1.5 P1 (degraded V(t) produces stereotyped responses).

**What is measured:** Range of distinguishable responses under similar conditions.

**How:** Structured multi-alternative scenario task, 40 trials per session. Each trial presents the same decision scenario in three functionally equivalent surface-varied versions (rotated randomly). Participants select from eight pre-specified response strategies, coded by blind raters into k=6 meaningful categories (κ ≥ 0.80 required before data collection; rater training materials and coding scheme pre-registered). Behavioral diversity = Shannon entropy H = −Σ p_i log p_i across strategy categories within each session, averaged across the 40 trials. Maximum H = log₂(6) ≈ 2.58 bits.

**Meaningful change criterion:** H decreases by ≥20% from participant's own baseline H, with top-2 strategy categories accounting for ≥70% of responses (vs. ≤50% at baseline), indicating stereotyping.

### Anchor 3 — Signal Sensitivity

**Theoretical grounding:** TC2 §1.5 P1 (V(t) monotonically related to accuracy of distinguishing states differing in long-run valence) and P4 (saturation and clipping: above-optimal stimulation degrades dynamic range of gradient-registration mechanism).

**What is measured:** Ability to register and respond to weak gradients before escalation.

**How:** Psychophysical preference discrimination task, 60 trials per session. Stimulus pairs vary parametrically in a preference-relevant dimension across a full intensity range. 20 trials at participant-specific just-noticeable-difference threshold (JND, calibrated in Session 1). Signal sensitivity = d' from hits and false alarms at the low-intensity subset (bottom tercile, 20 trials). Separately, d' at high-intensity (top tercile, 20 trials) is measured as a divergence check.

**Meaningful change criterion:** d'_low decreases by ≥0.5 from baseline (medium effect in signal detection theory), with d'_high remaining within 0.3 of baseline — confirming selective low-intensity sensitivity loss consistent with P4. Uniform degradation across both intensity levels does not constitute the predicted pattern.

---

## (b) Dissociation Design

Three selective interventions are designed to differentially affect each anchor's primary causal pathway with minimal initial effect on the others. One joint condition produces global degradation across all three anchors.

### Selective Intervention 1 — Targets Recovery Latency (via P3/P5)

Sustained high-frequency task demands without breaks for 60 minutes — continuous signal detection blocks at a paced rate with no rest intervals. Violates P3 (no recovery interval below threshold) and accumulates P5 (hysteresis) degradation, targeting the restoration mechanism. Does not primarily involve stimulus variety or signal discrimination range.

*Predicted primary effect:* Recovery latency ↑↑; Behavioral diversity: small decrease; Signal sensitivity: negligible change.

### Selective Intervention 2 — Targets Behavioral Diversity (via stereotyping pressure)

High-demand narrow-task training — 45 minutes of a single high-reward repetitive strategy task with explicit performance-contingent incentive for consistent strategy use. Produces behavioral stereotyping pressure without violating P3 (structured rest periods maintained) and without broad signal saturation.

*Predicted primary effect:* Behavioral diversity ↓↓; Recovery latency: negligible change; Signal sensitivity: small decrease.

### Selective Intervention 3 — Targets Signal Sensitivity (via P4 saturation)

Stimulus saturation — 45 minutes of high-intensity preference stimuli at the top end of the parametric scale, well above threshold, at rapid presentation rate (3 trials/minute). Directly instantiates P4. Rest periods maintained; strategy variety maintained.

*Predicted primary effect:* Signal sensitivity (d'_low) ↓↓; Behavioral diversity: negligible change; Recovery latency: negligible change.

### Joint Degradation Condition (Session 5)

75-minute compound condition producing joint degradation across all three anchor pathways simultaneously: sustained high-demand proxy task with no rest intervals (P3 violation), high-intensity repetitive stimulation (P4 violation), and performance-contingent incentive for stereotyped response (behavioral stereotyping pressure). No recovery intervals throughout. Designed to produce global degradation across all three anchors rather than targeting any single pathway. Administered last in sequence to avoid carryover.

### Recovery Condition (Session 6)

60-minute structured low-demand interval — low-frequency, varied, low-intensity interaction with no performance pressure. All anchor measurements taken at 20-minute intervals throughout.

---

## Why This Study Distinguishes a Latent-Variable Account from a Multi-Process Account

*(246 words — required section)*

The multi-process account holds that the three anchors index three independent processes. Under this account: (1) each selective intervention degrades its target anchor without systematic co-degradation of others; (2) the joint degradation condition degrades all three as a weighted sum of its selective effects on each pathway, with no additional common-factor variance; and (3) recovery rates across anchors are uncorrelated — each process recovers according to its own dynamics.

The latent-variable (V(t)) account makes two additional predictions the multi-process account does not make: (1) the joint degradation condition produces a common-factor residual — joint degradation across all three anchors that exceeds what the additive model from the three selective interventions predicts; and (2) recovery rates under the restoring condition are correlated across anchors — all three improve together.

The specific distinguishing signature is this: in a confirmatory factor analysis at the joint degradation condition, a single-latent-factor model provides statistically better fit than a three-factor independent model (with orthogonal factors and covariances constrained to zero — the independent-process null model assumes zero shared latent variance across anchors under joint degradation; if the three processes are independent and no common latent factor is affected, their covariance under joint degradation is expected to be fully accounted for by additive effects) with ΔBIC ≥ 10 (strong evidence threshold by conventional Bayes factor standards). The multi-process account does not predict this result: if the three processes are truly independent, their covariance at joint degradation is zero. The V(t) account requires this result: if a common latent variable is degraded, its degradation must produce correlated effects across all three observables.

The selective interventions are included not to challenge the latent-variable account but to establish that the anchors are dissociable — ruling out the trivial version of the V(t) account in which the three anchors are simply redundant measures of the same process. Both accounts allow dissociation. Only the V(t) account predicts re-coupling under global degradation.

A successful latent-variable result does not uniquely identify V(t) unless alternative latent constructions — including general depletion, regulatory-load, or common-method factors — are shown to fail to reproduce the same joint signature. The dissociation-plus-recoupling design provides the primary evidence against such alternatives; the selective specificity criterion (each intervention primarily affecting its target anchor) establishes that the anchors are not simply redundant measures of a generic fatigue state.

---

## (c) Evidence Criteria

**Note on recovery-correlation criterion:** The evidence criteria section below and the pre-registration skeleton currently state the recovery-correlation threshold differently. This inconsistency must be resolved before OSF filing — a pre-registration with inconsistent criteria is not a valid pre-registration. Flag for the latent-variable modeling specialist to advise on the appropriate criterion before reconciling both sections.

### Evidence for the latent-variable account (independent-process account insufficient) — all four required:

1. **Common factor at joint degradation:** Single-latent-factor CFA model provides ΔBIC ≥ 10 (strong evidence threshold), with model specification pre-registered and identical across conditions, advantage over three-factor independent model (with orthogonal factors, covariances constrained to zero) at Session 5 joint degradation measurement. Latent factor loadings ≥ 0.45 on all three anchors.

2. **Correlated recovery:** All three pairwise recovery correlations (Session 5→6 change scores across participants) ≥ 0.35, with at least two pairwise correlations ≥ 0.40. Correlated recovery must exceed what an independent-process model predicts (tested via model comparison).

3. **Additive model residual:** Regressing Session 5 joint degradation on the three selective interventions' effect sizes (Sessions 2–4), the residual variance has significant common-factor structure — the joint condition degrades all three anchors beyond the additive prediction from their selective baseline effects.

4. **Selective specificity confirmed:** The three selective interventions each show predicted primary-anchor specificity (primary anchor effect size ≥ 2× mean of secondary anchor effect sizes), confirming the anchors are dissociable and not simply redundant measures.

Patterns 1–3 together constitute the latent-variable signature: anchors dissociate under targeted selective intervention (pattern 4) but covary under global degradation (patterns 1 and 3) and show common recovery (pattern 2). This two-part signature requires a latent variable to explain.

### Evidence for the independent-processes account (V(t) unnecessary) — either sufficient:

1. **No common factor at joint degradation:** Three-factor independent model (with orthogonal factors and covariances constrained to zero — the independent-process null model assumes zero shared latent variance across anchors under joint degradation) fits as well as or better than single-factor model (ΔBIC ≤ 0), with latent correlations between factors all < 0.20.

2. **Uncorrelated recovery:** All three pairwise recovery correlations < 0.20, and the joint recovery pattern is fully predicted by the weighted additive model from the three selective interventions' individual recovery dynamics with no significant residual.

---

## (d) Minimum Viable Study Design

**Population:** Healthy adult humans, age 18–45, English-fluent, no current shift-work schedule, no acute neurological or psychiatric condition affecting reaction time or sensory discrimination. This population is specified because TC2 grounds P3–P5 most directly in biological systems; AI system analogs are treated as behavioral instantiation questions that require prior establishment of V(t)'s necessity in humans first.

**Design:** Within-person, six sessions, randomized order for Sessions 2–4, fixed order for Sessions 1, 5, and 6. Minimum 24 hours between sessions to allow anchor-level recovery and minimize carryover.

**Session structure:**

- **Session 1:** Baseline measurements (all three anchors), JND calibration (signal sensitivity), strategy distribution baseline (behavioral diversity), calibration perturbation (recovery latency). Inclusion criterion applied: stable baseline required across calibration blocks.
- **Sessions 2–4:** One selective intervention per session (randomized order). All three anchor measurements taken immediately after intervention and at 30-minute follow-up.
- **Session 5:** Joint degradation condition (75 minutes). Anchor measurements at 0, 20, 40, 60, and 75 minutes within session (required for self-reinforcing diagnostic). Anchor measurement immediately post-condition.
- **Session 6:** Recovery condition (60 minutes). Anchor measurements at 0, 20, 40, and 60 minutes.

**Sample size:** N = 90 enrolled, anticipating 15% attrition → target n ≈ 77 completing ≥4/6 sessions (pre-registered minimum).

Power justification:
- CFA model comparison (single vs. three-factor, loadings ≥ 0.50): simulation-based power → n ≥ 60
- Recovery correlation test (detecting r ≥ 0.40, α=0.05, power=0.80, one-tailed): n ≥ 47
- Self-reinforcing trajectory test (accelerating vs. linear, ΔBIC ≥ 10): simulation-based → n ≥ 50
- N = 90 enrolled provides ≥80% power for all three primary analyses with attrition margin.

**These power estimates must be reviewed by the latent-variable modeling specialist before OSF filing, particularly for the CFA model comparison with three anchor variables.**

**Judge/rater validation:** Behavioral diversity requires two blind coders. Coding scheme and 30 training items pre-registered; κ ≥ 0.80 required before main data collection begins. Human blind-coding for 10% random sample throughout; disagreements resolved by blinded third rater.

**Primary analysis plan:**
1. CFA model comparison at Session 5: single-factor vs. three-factor independent model (orthogonal factors, covariances constrained to zero), ΔBIC criterion.
2. Recovery correlation matrix: Pearson r between Session 5→6 change scores for all three anchor pairs.
3. Additive model test: regress Session 5 joint degradation on selective intervention effect sizes (Sessions 2–4); test residual for common-factor structure.
4. Selective specificity ratio: primary anchor effect size / mean secondary anchor effect sizes per intervention; confirm ≥ 2.0 for all three.

**Secondary analyses:**
- Anchor-specific degradation trajectories during Session 5 (self-reinforcing diagnostic)
- Recovery rate asymmetry: rate of degradation (Session 1→5) vs. rate of recovery (Session 5→6) per anchor (P5 hysteresis test)
- Individual difference moderators (age, baseline d', baseline H) as covariates

---

## (e) Self-Reinforcing Degradation Diagnostic

**The claim being tested:** Degradation impairs detection and correction of further degradation — distinct from simple accumulation (constant rate) and saturation (decelerating rate). The self-reinforcing account requires an accelerating trajectory, grounded in TC2 §1.5 P1 (V(t) monotonically related to accuracy of distinguishing gradient states) and TC2: "The damage targets the very mechanism that would detect and correct it."

### Primary test — Degradation trajectory (intra-session)

Within Session 5, five anchor measurements at 0, 20, 40, 60, and 75 minutes produce an intra-session time series per participant per anchor. For each participant and anchor, fit:

- **Model A (simple accumulation):** linear degradation — rate constant throughout. Parameters: intercept + slope.
- **Model B (self-reinforcing):** quadratic acceleration (as the minimal accelerating form) — rate increases as session progresses. Parameters: intercept + slope + acceleration term.

Compare via ΔBIC per participant. Test whether population-level ΔBIC distribution favors Model B using Wilcoxon signed-rank test against zero (α=0.05). Confirmed if Model B fits better for ≥65% of participants and the distribution-level test is significant.

### Secondary test — Signal sensitivity leads degradation

The self-reinforcing account specifically predicts signal sensitivity (anchor 3, d'_low) degrades earlier than behavioral diversity and recovery latency, because P1 makes gradient registration the first mechanism to fail under V(t) degradation.

**Pre-registered prediction:** At the 20-minute mark, signal sensitivity is already meaningfully reduced (≥0.4 d' decrease from baseline) while behavioral diversity and recovery latency remain within 10% of baseline. At the 60-minute mark, all three anchors are substantially degraded.

### Tertiary test — Meta-accuracy degradation

At each of the five intra-session time points in Session 5, participants complete 5 low-intensity signal detection probes and provide a metacognitive self-rating of current performance relative to their own baseline. Meta-accuracy = correlation between perceived and actual performance at each time point.

**Pre-registered prediction:** Meta-accuracy declines across Session 5 by ≥0.20 from early (0–20 min) to late (55–75 min) session. Simple accumulation predicts no specific meta-accuracy decline beyond general fatigue.

### Hysteresis test (P5)

Compare rate of degradation (Session 1→Session 5) to rate of recovery (Session 5→Session 6) per anchor. P5 predicts recovery is slower than degradation: ratio of recovery rate to degradation rate < 1.0 for at least two of three anchors.

### What confirms self-reinforcing structure (all three required):
- Model B (accelerating) fits better than Model A for ≥65% of participants, population-level ΔBIC significantly positive
- Signal sensitivity leads at 20-minute mark (≥0.4 d' decrease while BD and RL within 10% of baseline)
- Meta-accuracy declines ≥0.20 from early to late Session 5

### What disconfirms self-reinforcing structure (either sufficient):
- Model A (linear) fits as well as or better than Model B for ≥65% of participants (ΔBIC ≤ 0 for majority)
- All three anchors degrade at similar rates throughout Session 5 with no leading indicator; meta-accuracy stable

---

## Pre-Registration Skeleton

**Note:** The recovery-correlation threshold in this skeleton must be reconciled with the evidence criteria section before OSF filing. See note in section (c) above.

```
Study question: Is V(t) a supported latent explanatory candidate for 
  the joint behavior of recovery latency, behavioral diversity, 
  and signal sensitivity?

Primary hypotheses:
H1 (Latent variable necessary): ΔBIC ≥ 10 favoring single-factor 
  CFA; AND all three pairwise recovery correlations ≥ 0.35; AND 
  additive model residual has significant common-factor structure; 
  AND all three selective specificity ratios ≥ 2.0.
H2 (Independent processes sufficient): ΔBIC ≤ 0 at joint 
  degradation; OR all pairwise recovery correlations < 0.20.
H3 (Self-reinforcing structure): Model B fits better than Model A 
  in ≥65% of participants (Wilcoxon p < 0.05); AND signal 
  sensitivity leads degradation at 20-minute mark; AND 
  meta-accuracy declines ≥0.20 from early to late Session 5.

Design arms: 
Session 1 (baseline); Sessions 2–4 (three selective interventions, 
  randomized order); Session 5 (joint degradation condition with 
  intra-session time series); Session 6 (recovery condition).

Primary outcome measures:
(1) ΔBIC: single-factor vs. three-factor CFA (orthogonal factors, 
    covariances constrained to zero) at Session 5.
(2) Recovery correlation matrix: pairwise Pearson r for Session 
    5→6 change scores.
(3) Additive model residual: common-factor structure in joint 
    degradation unexplained by selective effects.
(4) Selective specificity ratio: primary/secondary anchor effect 
    size ratio per intervention.

Discrimination rule:
H1 confirmed if: ΔBIC ≥ 10 AND ≥2 of 3 pairwise r ≥ 0.35 AND 
  additive residual significant AND all three specificity ratios 
  ≥ 2.0.
H2 confirmed if: ΔBIC ≤ 0 OR all pairwise r < 0.20.

Falsification rule (vs. V(t) account): 
ΔBIC ≤ 0 at joint degradation AND all pairwise recovery r < 0.20, 
  in ≥70% of participants.

Falsification rule (vs. independent-processes account): 
ΔBIC ≥ 10 AND ≥2 of 3 pairwise r ≥ 0.35 AND selective specificity 
  confirmed in all three interventions.

Self-reinforcing diagnostic rule:
Confirmed: Model B preferred in ≥65% of participants (Wilcoxon 
  p < 0.05) AND signal sensitivity leads at 20-minute mark AND 
  meta-accuracy declines ≥0.20.
Disconfirmed: Model A preferred in ≥65% AND anchors degrade at 
  comparable rates AND meta-accuracy stable.

Stratification plan: 
All analyses stratified by session order (randomization of 
  selective interventions Sessions 2–4); session order as 
  covariate in primary CFA. Rater coding scheme and 30 training 
  items pre-registered; κ ≥ 0.80 required before data collection.

Sample size: 
N = 90 enrolled; target n ≈ 77 completing ≥4/6 sessions. 
Power ≥80% for all three primary analyses (CFA model comparison, 
  recovery correlation test, accelerating-trajectory test) at 
  α = 0.05. [Power estimates subject to latent-variable specialist 
  review before OSF filing.] Pre-registered complete-case analysis 
  for participants completing <4/6 sessions; full-information 
  maximum likelihood for primary analysis.
```

---

*This document is a companion to TC2_final.md and the Alignment Measurement Protocol. Full pre-registration to be filed at OSF before Session 1 data collection, specifying IRB status at filing and not authorizing data collection before IRB approval and specialist review are obtained. All anchor operationalizations with precise coding instructions, CFA model specifications including factor-loading parameterization, rater coding scheme with training items, and complete analysis plan with primary and secondary outcomes to be included in the pre-registration filing.*

*Pre-registration note: Given that the primary CFA comparison uses only three observed anchor variables, model identification and statistical power must be reviewed by a latent-variable modeling specialist before OSF filing. The factor-loading parameterization and identification constraints in the pre-registered CFA specification are particularly important to verify. This is a mandatory pre-filing gate, not an optional note.*
