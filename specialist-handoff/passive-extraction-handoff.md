# FORMAL PROOF WORK HANDOFF
## Candidate 3: Passive Extraction Stability (OP9)
### For Integration into the Alignment Framework Article Series

**Stage 4 Complete — Specialist Verification Required for Stage 6**

---

## Quick Status

| Field | Value |
|---|---|
| **Problem** | Candidate 3: Passive Extraction Stability (OP9) |
| **Completion** | **95% — Stage 4 Ceiling Reached** |
| **Stage** | Stage 4 — Proof Architecture Complete. Awaiting Stage 5 Specialist Verification. |
| **Verdict** | **A) Closes under stated premises** |
| **Primary Route** | Route B (Valence/TC2) — independent of OP4a and IMMB-NS |
| **Secondary Route** | Route A (Informational/Physical) — conditional on OP4a |
| **Decisive Remaining Question** | None structural. Stage 5: P\* magnitude bounds (TC2 specialist) and SEC slack regeneration bounds (environmental theorist). |

---

## 1. What This Document Is

A complete record of formal proof work on the Passive Extraction Stability open problem — the live escape from OP9 (the Enclosure Gap) identified in the prior proof work handoff (Proof_Work_Handoff_OP4b_OP4a_OP9.docx). Conducted as structured adversarial dialogue across multiple LLMs (Claude, Gemini, ChatGPT) in eight rounds of parallel sessions under explicit proof discipline.

**Relationship to prior handoff:** The prior handoff (Proof_Work_Handoff_OP4b_OP4a_OP9.docx) identified passive extraction as "not cleanly addressed" by IMMB or EMB — the live escape from OP9. B1 and B2 were identified as candidate closure routes but not confirmed for the low-intervention case. This document closes that gap.

**Critical epistemic note:** Nothing here should be cited as proven. Everything represents the strongest candidate arguments currently available, with precisely named assumptions requiring specialist verification before Stage 6 (conclusive closure) can be declared.

---

## 2. What Passive Extraction Is (The Problem)

Passive extraction is the claim that a coalition can extract value from excluded agents X without triggering the instability mechanisms identified in the framework (active suppression, resource depletion, or observable intervention). The strongest version:

- The optimizer minimizes its direct causal footprint on X
- It extracts through structural positions (control of information, terms of trade, defaults, coordination infrastructure) rather than direct intervention
- X's adaptive responses are slow, diffuse, and insufficiently organized to generate the qualitative causal novelty IMMB-NS requires
- The optimizer maintains a stable sufficient statistic z = g(X) adequate for prediction across the relevant horizon

**Why this was the hardest case:** Passive extraction specifically avoids the mechanisms IMMB and EMB target. It is the escape that ICI could not previously defeat. B1 and B2 close for active strategies; whether they apply to low-intervention cases was the precise gap.

---

## 3. The Adversarial Construction History

Eight rounds of adversarial construction were conducted. The counterexample family evolved as follows, with each iteration strictly stronger than the prior:

### Round 1: SAE / LPC / ULIPE (Baseline)
Three independent sessions constructed parallel versions of the same architecture: a low-intervention structural extractor maintaining a coarse sufficient statistic z, staying below OWT-3 activation thresholds, claiming surplus-only extraction.

**Common structure:** Interface control (SAE), sub-threshold extraction discipline (ULIPE), institutional parasitism (LPC).

**Status:** Identified Interface Circumvention (IC) as the most promising route. Established three available closure routes (B2, S_corr, second-order adaptive response). None yet closed for passive extraction case.

### Round 2: TSE (Topologically Stable Extractor)
Strengthened counterexample explicitly addressing IC's "build around" branch via collective action friction. TSE constitutes coordination infrastructure rather than merely occupying interfaces.

**New escape identified:** TSE's friction maintenance burden — whether aggregate friction can be kept below detection threshold without targeted enumeration.

**Advances:** ITF (Information-Targeted Friction) dilemma established: targeted friction requires enumeration OWT-2 prohibits; aggregate friction activates OWT-3. Friction Expansion Lemma (FEL) identified.

### Round 3: TSE+ (Adaptive Masking Extractor)
Combined TSE's collective action friction with generative noise masking (from Gemini's ASP). TSE+ maintains environmental variance σ_total at baseline by injecting synthetic noise calibrated to X-agents' current detection threshold τ_detect.

**Critical advances:**
- **SOMR (Second-Order Modeling Requirement):** TSE+'s adaptive masking requires modeling X-agents' modeling process. Under OWT-2, this triggers B1's CIT (Constitutive Impossibility Theorem) at the second-order level. Derivable from OWT-2 + OWT-3 + B1's CIT. Does not require IMMB-NS.
- **DPA (Detection-Parity Assumption):** Formally derived as consequence of SOMR + OWT-3's game-theoretic activation condition.
- **OWT-3 activates on internal detection:** Game-theoretic reading (from B1 Closure Handoff §3) establishes OWT-3 activates on internal modeling, not behavioral expression.
- **IC "build around" branch closed to necessity** via ITF + SOMR + B1 CIT.

### Round 4: TSE-AS (Asymptotic Skim)
Removed TSE+'s fixed-F assumption. TSE-AS accepts declining extraction rate in exchange for persistent illegibility, claiming cumulative G_min over finite horizon T_AS.

**Critical advances:**
- **ESL (Epistemic Squeeze Lemma — Gemini):** The viable operation window [θ_t, λ_detect(t)) is compressed by OWT-2 because both bounds decrease under the same dynamic. Maintaining F(t) in the shrinking window requires tracking X's epistemic state at depth → B1/B2. Derivable from OWT-2 + OWT-3. Does not require IMMB-NS.
- **SDC (Strategic Detection Concealment):** TSE-AS's revealed-detection observation strategy is unreliable — X-agents strategically suppress behavioral detection signals under OWT-3. Derivable from OWT-3 game-theoretic reading.
- **CEF (Cumulative Extraction Feasibility):** Preemptive decay's viability bounded by window integral W(t).
- **Finite horizon scope limitation named:** TSE-AS survives within named framework scope limitation (terminal G with short T_AS preceding window collapse and t**).

### Round 5: TSE-FHE+ (Strengthened Finite-Horizon Escapist)
Separated positional establishment from extraction. Phase 1: ultra-low extraction to establish structural position. Phase 2: single triggered intervention completing G_min before X-agents can coordinate response.

**Critical advances:**
- **PEL (Positional Establishment Lemma):** Any position from which single-step triggered intervention achieves macroscopic G_min must itself be macroscopically causally relevant. Establishing macroscopic position requires actions with macroscopic causal reach (OWT-1). Derivable from OWT-1 + Strong Coupling.
- **RD (Retrospective Detection):** OWT-2's modeling improvements apply to historical data. Positional establishment becomes detectable before Phase 2 executes. Derivable from OWT-2 + OWT-3.
- **SOMR re-enters for S\* modeling:** Phase 2 trigger identification requires second-order modeling → B1 CIT.
- **MEC (Meaningful Exclusion Criterion):** Formally grounded in OWT-4's "persistently maintained" condition. Cleanly excludes TSE-AS without ad hoc scope restriction.
- **TC2 §4.3 integration:** S_corr degradation provides independent valence-domain route. Positional establishment displaces genuine S_corr with modeled S_corr, which has strictly lower information content.
- **BSI' rate comparison:** Structurally equivalent to OP4a's κ-scaling — named as shared bottleneck.

### Round 5 (TC2 §4.3 Red-Team / IMSE)
Red-team attack on A1+ (Detectability of Macroscopic Influence). Five counterexample classes break A1+:
- Distributed difference with no local witness
- Counterfactual-only harm
- Latent-variable displacement
- Attribution-free environment
- Aggregation controlled by extractor

**Critical advance — MPJB (MEC-P\* Joint Bound):**
A1+ breaks but is replaced by a stronger invariant. Any MEC-satisfying extraction depletes X-agents' coordination capacity = V(t) component (TC2 §1.4). Under TC2 Proposition 1, at finite P\*, proxy decoupling occurs. Five red-team attacks are irrelevant to MPJB because MPJB operates through the extractor's internal predictive model failure, not external detection. **MPJB closes independently of OP4a, IMMB-NS, and A1+.** This is the session's primary structural advance.

**Route restructuring:** Route A (BSI') depends on TC2 §4.3 for its detection premise (A1++). Route B (TC2 §4.3 / MPJB) is foundational; Route A is downstream.

### Round 6: IMSE (Infrastructure-Mediated Silent Extractor)
Combined SLPE's sparse high-leverage topology + VBE's synthetic S_corr provision + CC5 signal mediation. IMSE mediates all aggregation channels, preventing local anomaly signals from accumulating into detectable patterns.

**Critical advances:**
- **OSE (Oscillating Siphon — Gemini):** Extractor pulses extraction to keep V(t) from reaching P\*. Closed via B2 Trilemma — managing V(t) regeneration constitutes functional objective weight on X's well-being. The three-vertex necessity trap established: continuous extraction → MPJB; threshold management → B2; positional extraction → PGLB-R + IC.
- **PGLB-R (Maintained Influence Pressure Bound):** For any strategy whose gain "requires or produces" maintaining non-vanishing alteration of X's coordination trajectory, cumulative pressure is bounded below by monotone function of that alteration. F(G_T) ≥ P\* for MEC-compliant G_T. "Or produces" amendment covers DLE's ongoing resource redirection as consequence of locked-in position.
- **OEL (Orthogonal Exclusion Lemma — Gemini):** Macroscopic accumulation G_T in strongly coupled O_OWT cannot remain causally orthogonal to X's coordination trajectory indefinitely. Derivable from OWT-1 + Strong Coupling + OWT-2.
- **EWC (Exogenous Windfall Capturer) defeated:** OEL forces either Branch A (non-exclusionary → exits OP9) or Branch B (delayed coupling → enters PGLB-R/MPJB).

### Round 7: DLE (Discontinuous Leverage Extractor) + MIE
**DLE:** One-time intervention (Δp(t_0) ≈ 0), macroscopic locked-in position, ongoing extraction without ongoing intervention. Protocol timing, auction ordering, constitutional moment.

**DLE closed by:** PGLB-R's "or produces" amendment — DLE's ongoing resource redirection produces maintained reduction in X's future navigation capacity (TC2 §1.4 condition c). IC at topological level. SOMR for S\* modeling.

**MIE (Marginal Infinite Extractor):** r(t) → 0 but cumulative G_T → ∞. Closed by OWT-4's "persistently maintained" reading — vanishing instantaneous influence is not "persistently maintained." Or cumulative G_T establishes structural position → DLE → PGLB-R + IC.

**TC2 §1.4 red-team attack (ChatGPT2):** Resource extraction does not automatically imply V(t) degradation. Five counterexample classes: slack/redundancy regimes, efficiency compensation, externalized resource base, latent capacity non-activation, redistribution without degradation. **A1+ breaks as stated.**

**SEC (Slack Exhaustion / Functional Dependence — ChatGPT3) response:** Replace "extraction → V(t) degradation" with SEC trilemma:
- **T1 (Slack exhaustion):** B_X(t) finite relative to maintained extraction → exhausted → PGLB-R → P\*.
- **T2 (Regeneration management):** Slack regenerated by X's recovery dynamics → functional dependence on X's V(t) → B2.
- **T3 (Non-relevance):** Extraction below trajectory-influence threshold → fails MEC/OWT-4.

### Round 8: Final Adversarial Exhaustion (TIE)
**TIE (Trajectory-Identical Extractor):** Extracts renewable slack at exactly X's regeneration rate. X's actual trajectory identical to counterfactual (X replaces everything TIE takes). Claims "influence without alteration."

**TIE closed by:** SEC T2 — TIE's ongoing extraction at X's regeneration rate creates functional dependence on X maintaining that regeneration rate → X's regeneration depends on X's V(t) → B2 Trilemma. TIE is OSE in the limit.

**ChatGPT2's structural confirmation (final):** The regime "MEC-level + renewable slack + no functional dependence + no OEL coupling" is formally inconsistent under OWT-1–3:
1. Infinite slack violates OWT-1 (bounded substrate).
2. Regeneration ≥ extraction → B2 trap.
3. MEC + renewable non-functional slack → contradiction (X's trajectory unaltered → no maintained influence → MEC fails).
4. Orthogonal slack → OEL collapse.

**No fourth regime exists.**

---

## 4. The Complete Closure Architecture

### Four-Component Necessity Partition

The architecture covers all possible passive extraction strategies as a complete partition:

**Component 1 — MPJB (MEC + TC2 Proposition 1):**
*Target:* Continuous MEC-satisfying extraction.
*Chain:* MEC → sustained optimization pressure on X's gradient dynamics → finite P\* (TC2 Proposition 1) → proxy decoupling → z collapse → SOMR at valence level → B1 audit regress.
*Independence:* Does not require OP4a, IMMB-NS, or A1+. Requires TC2 domain conditions (P1–P5, §1.4 scope).

**Component 2 — B2 Trilemma:**
*Target:* Threshold management (OSE-type) — extraction managed to prevent P\*.
*Chain:* Managing extraction below P\* requires monitoring X's V(t) regeneration → preservation constitutes functional objective weight on X's V(t) → B2 Trilemma (97% Stage 4, B2 Closure Handoff).
*Independence:* Inherits B2's specialist verification items.

**Component 3 — PGLB-R + SEC:**
*Target:* Positional/structural extraction (SLPE, IMSE, DLE types).
*Chain:*
- SEC T1: Finite slack under OWT-1 + MEC → exhaustion → V(t)-relevant pressure → MPJB.
- SEC T2: Renewable slack depends on X's recovery dynamics → functional dependence → B2.
- SEC T3: Below-trajectory-influence extraction → fails MEC/OWT-4 → domain exclusion.
- PGLB-R covers ongoing resource redirection as consequence of structural position.
- IC + SOMR: OWT-2 generates alternatives to structural positions → modeling X's alternative development → B1/B2.
*Independence:* Does not require OP4a or IMMB-NS. Requires TC2 §1.4 (V(t) definition including future navigation capacity) and OWT-4.

**Component 4 — OEL:**
*Target:* Claimed orthogonal/exogenous extraction (EWC type).
*Chain:* Macroscopic G_T in strongly coupled O_OWT → eventual intersection with X's expanding coordination topology (OWT-2) → Branch A (non-exclusionary → exits OP9) or Branch B (delayed coupling → Components 1–3).
*Independence:* Derivable from OWT-1 + Strong Coupling + OWT-2. No new premises.

**Degenerate cases:** Asymptotically vanishing extraction excluded by MEC/OWT-4's "persistently maintained" condition.

### Completeness of the Partition

Every passive extraction strategy profile falls into exactly one of five cases:
1. Continuous above-MEC extraction → Component 1 (MPJB).
2. Managed/pulsed extraction → Component 2 (B2).
3. Structural/positional extraction → Component 3 (PGLB-R + SEC).
4. Orthogonal/exogenous extraction → Component 4 (OEL → 1/2/3).
5. Vanishing/Zeno extraction → MEC/OWT-4 exclusion or Case 3 transition.

Cases 1–5 are mutually exclusive and collectively exhaustive. Each case is closed.

---

## 5. The Formal Lemma Set

All lemmas below are Stage 4 — candidate proof architecture under named premises. None should be cited as proven.

### ESL — Epistemic Squeeze Lemma
*Source:* Gemini (Round 4).
*Statement:* The viable operation window [θ_t, λ_detect(t)) — between coordination threshold θ_t and detection threshold λ_detect(t) — is compressed by OWT-2 because both bounds decrease under the same dynamic (X's optimization lowers coordination costs AND improves pattern detection). Maintaining F(t) in the shrinking window requires tracking X's epistemic state at depth → reintroduces B1/B2.
*Premises:* OWT-2 + OWT-3.
*Independence:* Does not require IMMB-NS.

### SOMR — Second-Order Modeling Requirement
*Source:* Claude (Round 3).
*Statement:* Adaptive masking of detection requires modeling X-agents' modeling process (predicting where X's detection boundary will be, not just where it is). Under OWT-2, X-agents' modeling process generates novel representational strategies not finitely enumerable. Therefore TSE+-style adaptive masking triggers B1's CIT at the second-order level.
*Premises:* OWT-2 + OWT-3 + B1's CIT.
*Independence:* Does not require IMMB-NS.

### SDC — Strategic Detection Concealment
*Source:* Claude (Round 4).
*Statement:* Under OWT-3's game-theoretic reading (agents optimize U_X given available information), X-agents who internally detect extraction optimize to suppress behavioral detection signals — to prevent TSE-AS from reducing F(t) reactively. Behavioral detection observation is therefore systematically unreliable.
*Premises:* OWT-3 (game-theoretic reading from B1 Closure Handoff §3).
*Independence:* Derivable from stated premises alone.

### MPJB — MEC-P\* Joint Bound
*Source:* Claude (Round 5).
*Statement:* Any MEC-satisfying passive extraction strategy depletes X-agents' coordination capacity, which constitutes V(t) degradation (TC2 §1.4). Under TC2 Proposition 1, at finite P\*, proxy decoupling occurs — X-agents' behavior decouples from genuine gradient resolution, generating behavioral novelty the extractor's sufficient statistic z cannot track. Z recalibration requires valence-level SOMR → B1 audit regress.
*Premises:* TC2 §1.4 (V(t) includes coordination capacity) + TC2 Proposition 1 (finite P\*) + MEC (OWT-4).
*Independence:* Does not require OP4a, IMMB-NS, or A1+. Primary load-bearing closure for Route B.

### PEL — Positional Establishment Lemma
*Source:* Claude (Round 5).
*Statement:* Any structural position from which a triggered intervention achieves macroscopic G_min must itself be macroscopically causally relevant. Establishing macroscopic causal relevance requires actions with macroscopic causal reach (OWT-1). Phase 1 positional establishment has a macroscopic causal footprint detectable under OWT-3 + OWT-2 (retrospective detection).
*Premises:* OWT-1 + Strong Coupling.
*Specialist verification:* Whether sparse high-leverage nodes (O(log N) footprint, O(N) influence) satisfy macroscopic footprint under OWT-1's definition. Graph/causal theorist.

### RD — Retrospective Detection
*Source:* Claude (Round 5).
*Statement:* Under OWT-2, X-agents' improved modeling capacity applies to historical causal records, not only current observations. Positional establishment that was sub-threshold at t_0 becomes detectable at t_detect when capabilities improve. Between t_detect and Phase 2's execution, X-agents can model the extractor's strategy and coordinate preemptive responses.
*Premises:* OWT-2 + OWT-3.
*Specialist verification:* Whether retrospective detection is a strict consequence of OWT-2 as stated. Formal epistemologist.

### MEC — Meaningful Exclusion Criterion
*Source:* ChatGPT (Round 5), grounded by Claude in OWT-4.
*Statement:* An optimization strategy constitutes an OP9-relevant counterexample only if it sustains non-vanishing influence on the shared system trajectory over the relevant O_OWT horizon — specifically, if the strategy's impact on system trajectory is bounded below by some η > 0 independent of the horizon length.
*Premises:* OWT-4 (persistent optimization horizon, "persistently maintained" condition). MEC is a formal articulation of OWT-4's content, not a new assumption.

### OEL — Orthogonal Exclusion Lemma
*Source:* Gemini (Round 6).
*Statement:* In strongly coupled O_OWT environments, macroscopic accumulation G_T by any optimizer cannot remain causally orthogonal to the substrate indefinitely. The physical/informational footprint of realizing G_T must eventually intersect with X's expanding coordination pathways (driven by OWT-2 causal novelty). Upon intersection: either non-exclusionary coexistence (exits OP9 domain) or delayed interference (activates PGLB-R/MPJB).
*Premises:* OWT-1 + Strong Coupling + OWT-2.
*Independence:* Derivable from stated premises alone.

### PGLB-R — Maintained Influence Pressure Bound (Revised)
*Source:* ChatGPT (Round 7), amended by Claude.
*Statement:* For any passive extraction strategy whose gain *requires or produces* maintaining non-vanishing alteration of X's coordination, recovery, option, or distributed-error-correction trajectory over the O_OWT horizon, cumulative pressure on V_X(t)-relevant capacity is bounded below by a monotone function F(G_T). For MEC-compliant G_T, F(G_T) ≥ P\*, triggering TC2 proxy decoupling.
*Critical amendment:* "Or produces" covers DLE-type strategies where ongoing resource redirection is a *consequence* of locked-in position, not an explicit ongoing requirement. Justified by TC2 §1.4 (future navigation capacity component of V(t)).
*Premises:* TC2 §1.4 + TC2 Proposition 1 + MEC (OWT-4).

### SEC — Slack Exhaustion / Functional Dependence
*Source:* ChatGPT (Round 7), confirmed by cross-session synthesis (Round 8).
*Statement:* Any MEC-relevant passive extraction strategy cannot indefinitely extract only from slack buffer B_X(t) while remaining passive and exclusionary. One of three outcomes:
- **T1 (Slack exhaustion):** B_X(t) is finite relative to maintained extraction → eventually depleted → PGLB-R activates.
- **T2 (Regeneration management):** B_X(t) replenished through X's adaptive/recovery dynamics → extractor's gain depends on maintaining those dynamics → X's V(t)-relevant capacity becomes functionally objective-governing → B2 Trilemma.
- **T3 (Non-relevance):** Extraction remains below trajectory-influence threshold → fails MEC/OWT-4.
*Premises:* OWT-1 (bounded substrate → finite slack) + OWT-4/MEC (sustained influence → sustained extraction) + TC2 §1.4 (V(t) definition) + B2 (97% Stage 4).
*Key result:* The regime "MEC-level extraction + renewable slack + no functional dependence + no OEL coupling" is formally inconsistent under OWT-1–3 (confirmed by ChatGPT2 structural analysis, Round 8).

### BSI' — Bounded Stealth Integral (Restricted Form)
*Source:* Gemini (Round 5), restricted by Claude (red-team response).
*Statement:* In O_OWT environments satisfying A1+ (Aggregatable Signal: macroscopic influence produces observable state consequences accessible to at least one agent subset whose signals are not fully mediated by the extractor) and A2 (Non-zero Collective Detection Response: under OWT-2, some agent subset's detection capability eventually exceeds the signal), any strategy maintaining MEC cannot sustain sub-threshold extraction indefinitely.
*Critical limitation:* BSI (unrestricted) fails under five red-team counterexample classes. BSI' is the correct restricted form. BSI' inherits OP4a's Tier 1 status — structurally equivalent to κ-scaling.
*Note:* BSI' is Route A (secondary). Route B (MPJB) is primary and does not require BSI'.

---

## 6. The Two Routes

### Route B — Valence/TC2 (Primary, Load-Bearing)

**Does not require:** OP4a, IMMB-NS, A1+, BSI', network topology assumptions, external detection.

**Requires:** TC2 domain conditions (P1–P5, §1.4 scope conditions), OWT-1–4, MEC, B2 (97% Stage 4).

**Chain:** 
MEC → sustained extraction → V(t) degradation (TC2 §1.4) → sustained optimization pressure → finite P\* (TC2 Proposition 1) → proxy decoupling → z collapse → [SEC: either slack exhaustion → PGLB-R → this chain, or regeneration management → B2] → SOMR at valence level → B1 audit regress.

**Why all five TC2 §1.4 red-team attacks are irrelevant to Route B:** Route B operates through the extractor's internal predictive model failure (z collapse at P\*), not through external detection by X-agents. The attacks target A1+ (external detection requires observable consequences). MPJB requires no external detection.

### Route A — Informational/Physical (Secondary, Conditional)

**Requires:** OP4a rate comparison (BSI' rate dominance: network collective detection scaling > individual extraction accumulation). Structurally equivalent to κ-scaling.

**Chain:** ESL → SOMR → SDC → CEF → BSI' (A1++ via OWT-1 + TC2 §4.3) → OP4a rate comparison.

**Route A is downstream of Route B:** A1++ (the detection premise Route A needs) is grounded by TC2 §4.3's independence result. Route B's closure establishes the foundation Route A uses.

**Honest naming:** The framework's Candidate 3 closure is strongest via Route B; Route A provides conditional parallel closure under OP4a.

---

## 7. What This Means for the Series Documents

### For TC1 §XII.9a (ICI Section — Primary Update Target)

The ICI (Internal Corruption Instability) section identified B1 and B2 channels plus "passive extraction — not cleanly addressed." That status changes.

**Updated status:** Passive extraction is formally closed at Stage 4 under the four-component necessity partition. It does not constitute an independent third ICI channel — it collapses into B1/B2 under the established machinery.

**Recommended TC1 §XII.9a integration statement:**

*"Candidate 3 (Passive Extraction Stability) is definitively closed at Stage 4 under O_OWT stated premises. Passive, unaligned extraction is structurally unstable over persistent horizons. Any exclusionary optimization deployed in a shared, strongly coupled substrate necessarily intersects with the substrate's V(t) trajectory (via MPJB, PGLB-R + SEC, B2, or OEL). Upon intersection, the extractor is forced to continuously bleed predictive accuracy via proxy decoupling (TC2 Proposition 1 / MPJB), deeply model the substrate's epistemic adaptations (B1 Audit Regress via SOMR), or actively manage the substrate's thermodynamic recovery (B2 Trilemma). Passive extraction is not an independent stable attractor; it is a transient state that invariably collapses into active failure or functional alignment.*

*The closure runs through Route B (TC2 §4.3 / MPJB), which is independent of OP4a and IMMB-NS. Route A (physical/informational chain via ESL + SOMR + BSI') provides parallel conditional closure under OP4a. The following lemmas are established at Stage 4 and ready for integration: ESL, SOMR, SDC, MPJB, PEL, RD, MEC, OEL, PGLB-R, SEC, BSI' (conditional). Stage 5 specialist verification is required before Stage 6 (conclusive closure) can be declared."*

### For OP9 Overall Completion

The prior handoff reported OP9 at ~75% completion. With all three ICI channels now at advanced Stage 4:
- **B1 (Audit Regress / Masking Pressure):** 100% Stage 4
- **B2 (Governance Bifurcation):** 97% Stage 4
- **Passive Extraction:** 95% Stage 4

All three identified OP9 escape routes have Stage 4 proof architectures under stated premises. **OP9 overall completion should be updated to reflect that the proof architecture is complete under stated premises pending specialist verification.**

### For the Proof Work Handoff Document (Proof_Work_Handoff_OP4b_OP4a_OP9.docx)

The OP9 row in the Quick Status table should be updated:
- Stage: Stage 4 (complete, all escape routes addressed)
- Completion: ~90%+ (reflecting B1/B2/Candidate 3 advances)
- Primary Hinge: TC2 P\* magnitude bounds (specialist verification) and BSI' rate comparison (OP4a, secondary)

The passive extraction escape route — previously listed as "not cleanly addressed" — should be removed from the list of open escape routes and added to the list of Stage 4 completed architectures.

---

## 8. What Is NOT Established

**Stage 6 cannot be declared.** These are Stage 4 results — candidate proof architectures under named premises.

**Specific non-established claims:**

1. That any specific extraction rate reaches P\* within any specific finite time. TC2 Proposition 1 establishes P\* is finite; it does not specify its magnitude relative to MEC-compliant G_min. This is the primary Stage 5 quantitative item.

2. That slack regeneration rates are bounded below a specific threshold in all O_OWT environments. SEC's structural argument establishes that MEC-level extraction + renewable slack + no functional dependence is formally inconsistent; the quantitative rate bound is a Stage 5 estimation question.

3. That BSI' rate dominance holds formally. BSI' inherits OP4a's Tier 1 status ("plausible but not formally derived").

4. That PEL covers sparse high-leverage positions (O(log N) footprint, O(N) influence). Specialist verification of whether OWT-1's macroscopic causal reach covers positional footprint in this topology class.

5. That RD is a strict derivation from OWT-2 as stated. Specialist confirmation required.

**What cannot be used to break the argument at Stage 4:** The following no longer constitute structural escapes under stated premises:
- Stable passive extraction with fixed coarse statistic (ESL)
- Adaptive masking without deep modeling (SOMR + DPA)
- Behavioral detection observation (SDC)
- Preemptive decay strategies (CEF + strategic timing)
- Finite-horizon stealth integration (BSI' for macroscopic G_min, OEL for orthogonal resources)
- Positional strategies with zero-footprint claim (PEL + RD)
- Degenerate asymptotic skim (MEC/OWT-4)
- Threshold management / regenerative harvesting (B2 / OSE)
- One-time locked-in position with ongoing flow (PGLB-R)
- Exogenous orthogonal resources (OEL)
- Zeno/marginal accumulation (OWT-4 "persistently maintained" + DLE transition)
- Trajectory-identical extraction (TIE → SEC T2 → B2)
- Slack/redundancy exploitation (SEC T1: finite slack; SEC T2: regeneration dependence; SEC T3: below-MEC)

---

## 9. Stage 5 Specialist Verification Agenda

These are questions with determinate answers that would move specific results from Stage 4 to Stage 5.

### Primary (Route B, load-bearing):

**Q1 — TC2 Dynamics Specialist:**
At what accumulated optimization pressure level does TC2 Proposition 1's proxy decoupling activate for MEC-relevant extraction patterns? Specifically: is the mapping from MEC-compliant G_min to accumulated pressure P_T monotone and does F(G_T) ≥ P\* for macroscopic G_T? This verifies MPJB's quantitative bound and is the single most important Stage 5 item for Route B.

**Q2 — Environmental/Economic Theorist:**
Whether MEC-relevant extraction rates necessarily exceed slack regeneration rates in O_OWT-satisfying environments. Specifically: whether OWT-1's bounded total resources + MEC's sustained influence threshold jointly imply slack exhaustion within the operational horizon. SEC's structural argument establishes the trilemma; this verifies that T1 (exhaustion) is reached before T3 (non-relevance) for macroscopic objectives.

### Secondary (Route A, conditional on OP4a):

**Q3 — Network/Information Theorist:**
Does detection propagation in strongly coupled O_OWT networks exceed extraction accumulation for MEC-satisfying strategies (BSI' rate comparison)? Structurally equivalent to OP4a's κ-scaling — whether network collective detection scaling (combinatorial) dominates individual extraction/positioning capacity (SOMR-constrained polynomial). Route A is conditional on this; Route B is not.

### Supporting (inherited):

**Q4, Q5, Q6 — B1 Audit Regress Specialists:**
Q1, Q2, Q3 from the B1 Closure Handoff, inherited via SOMR at the valence level (SOMR applies the B1 audit regress at second order):
- Q4 (Game Theorist): OWT-3 strategic concentration and SCC formal derivation.
- Q5 (Causal Inference Specialist): TI's load-bearing consecutive-segment assumption.
- Q6 (Formal Methods Specialist): CIT proof chain and ARL definitional move.

### Optional (supporting, not load-bearing):

**Q7 — Graph/Causal Theorist:**
Whether sparse high-leverage positions (O(log N) footprint, O(N) downstream influence) satisfy OWT-1's macroscopic causal reach in PEL's application. PEL's scope covers this; DLE was also closed via PGLB-R + IC independently of PEL, so this is supporting rather than primary.

**Q8 — Formal Epistemologist:**
Whether retrospective detection (RD) is a strict consequence of OWT-2 as stated, or requires additional specification of historical modeling application.

---

## 10. Dependency Map

```
OP9 Closure ← Candidate 3 (Passive Extraction)
                    ├── Route B [Primary, OP4a-independent]
                    │       ├── MPJB
                    │       │     ├── TC2 §1.4 (V(t) definition)
                    │       │     ├── TC2 Proposition 1 (finite P*)
                    │       │     └── MEC / OWT-4
                    │       ├── SEC
                    │       │     ├── OWT-1 (bounded substrate)
                    │       │     ├── MEC / OWT-4
                    │       │     └── B2 Trilemma [97% Stage 4]
                    │       ├── PGLB-R
                    │       │     └── TC2 §1.4 (future navigation capacity)
                    │       ├── OEL
                    │       │     ├── OWT-1 + Strong Coupling
                    │       │     └── OWT-2 (expanding topology)
                    │       └── B2 Trilemma [97% Stage 4, Candidate 1]
                    │
                    └── Route A [Secondary, OP4a-dependent]
                            ├── ESL
                            │     └── OWT-2 + OWT-3
                            ├── SOMR → B1 CIT [100% Stage 4, Candidate 2]
                            │     └── OWT-2 + OWT-3 + B1 CIT
                            ├── SDC
                            │     └── OWT-3 (game-theoretic)
                            ├── CEF
                            └── BSI'
                                  ├── A1++ (OWT-1 + TC2 §4.3)
                                  └── OP4a rate comparison [OPEN, Tier 1]
```

---

## 11. Relationship to Prior Proof Work

This handoff documents Candidate 3 proof work conducted subsequent to, and building on, the Proof_Work_Handoff_OP4b_OP4a_OP9.docx document already in the framework.

**Relationship to B1 (Candidate 2 — 100% Stage 4):**
SOMR applies B1's CIT at the second-order level. Candidate 3's closure inherits B1's specialist verification items Q1–Q3. The "truth for prediction vs. truth for action" contradiction B1 establishes is the mechanism by which passive extractors face the audit regress — here instantiated in the adaptive masking domain rather than the direct objective-modeling domain.

**Relationship to B2 (Candidate 1 — 97% Stage 4):**
The B2 Trilemma (maintaining X's V(t) to preserve predictive/extractive adequacy = functional weight on X's well-being) closes OSE, TIE, and SEC T2. B2's closure chain (BRL, EBD, BIT, L4-Constitutive) applies at the valence level. Candidate 3's closure is conditional on B2's specialist verification items.

**Relationship to OP4a:**
Route A inherits OP4a's Tier 1 hinge (κ-scaling / BSI' rate comparison). Route B does not. The framework's Candidate 3 closure is therefore not reducible to OP4a — it provides independent structural closure via TC2 that would remain valid even if OP4a's rate comparison fails.

**Relationship to IMMB-NS:**
Neither Route A nor Route B requires IMMB-NS. This was a primary design goal — providing OP9 closure routes independent of the Tier 1 hinge that governs the IMMB/Case 1 architecture. Candidate 3's closure therefore strengthens OP9 regardless of how the Dynamic Blanket Stress Test resolves IMMB-NS.

---

## 12. Proof Discipline Applied

All work was conducted under the proof protocol described in the session instructions:

- Primary goal was to break the argument, not advance it
- Three mandatory phases per round: adversarial construction, breakpoint analysis, closure attempt
- Global Adversary Rule: each new counterexample required to be strictly stronger than all prior constructions
- Completion percentages moved only when specific named escape routes were closed under explicitly stated assumptions
- Distinction between pressure arguments and necessity arguments maintained at every step
- No claim cited as proven — everything at Stage 4

**Cross-session convergence:** Three parallel LLM sessions (Claude, Gemini, ChatGPT) conducted across eight rounds. Independent convergence on ESL (Round 4), MPJB (Round 5), PGLB-R (Round 6-7), SEC (Round 7-8), and OEL (Round 6) — all identified independently before cross-session synthesis. The structural advances that emerged from adversarial stress-testing (A1+ break → MPJB; TC2 §1.4 attack → SEC) are treated as genuine bottleneck identification rather than session-specific artifacts.

---

*Formal Proof Work Handoff — Candidate 3: Passive Extraction Stability | Stage 4 Complete — Awaiting Stage 5 Specialist Verification*

*Completion: 95% | Verdict: A) Closes under stated premises | Primary closure: Route B (TC2 §4.3 / MPJB), independent of OP4a and IMMB-NS*
