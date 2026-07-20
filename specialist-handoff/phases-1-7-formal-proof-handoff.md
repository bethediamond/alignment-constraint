> **Status:** Specialist handoff document · Stage 4 (LLM ceiling) · **Nothing herein should be cited as proven.** Phases 1-7: Mixed-Mode Collapse, OP4d exhaustiveness, LOI/TOL chain.
> **Context:** [Specialist Verification Agenda →](index.md) · [Proof Status and Non-Claims →](../core/proof-status.md) · [Framework hub →](../core/alignment-constraint.md)

---


## Ai Alignment Framework
## Formal Proof Work Handoff — Phases 1 Through 7
Mixed-Mode Collapse Lemma + OP4d Exhaustiveness + LOI/TOL Attribution Chain
Complete Stage 4 Summary — All Adversarial Results, Necessity Closures, Surviving Constructions,
Gap Structure, and Specialist Handoff Package
## Stage 4 — Strongest Candidate Proofs Under Named Assumptions
Stage 6 requires independent human specialist verification. Nothing herein should be cited as proven.

# 0. DOCUMENT PURPOSE AND STATUS

This document is the complete handoff record for formal proof development on three interconnected problems in the AI alignment framework: the Mixed-Mode Collapse Lemma (MMCL), the OP4d Specification Failure-Mode Exhaustiveness problem, and the LOI/TOL Attribution Chain (Phases 5-7). Work was conducted across seven phases using structured adversarial dialogue across multiple LLMs (Claude, Gemini, ChatGPT) under explicit proof discipline.

All work is Stage 4: strongest candidate proofs under named assumptions. Cross-session convergence across independent LLM sessions is treated as evidence of genuine bottleneck identification rather than session-specific artifact. Completion percentages reflect honest adversarial accounting — reductions across phases reflect genuine adversarial advances, not regression.

Eight Proof Rules Applied Throughout:
Rule 1 — Pressure vs. Necessity: Pressure = rising cost or instability. Necessity = strategy cannot satisfy stated conditions simultaneously. Every result labeled explicitly.
Rule 2 — Adversarial First: Strongest possible counterexample before supporting any claim. Minimum two adversarial constructions per phase.
Rule 3 — No Silent Assumptions: Every step cites OWT-1 through OWT-4, MEC, or explicitly named assumptions.
Rule 4 — Contradiction Statement Required for Closure: Every necessity result ends with cannot simultaneously satisfy (A)(B)(C).
Rule 5 — Classify Every Failure Mode: PCL-alpha, PCL-beta, AGC, ICI/B1/B2, or NEW (named and defined).
Rule 6 — Completion Scoring Mandatory: Percentage with named challengeable assumption at 90%+.
Rule 7 — No Overclaiming: No collective exhaustiveness without classification proof.
Rule 8 — Stall Detection: State explicitly when unable to produce stronger adversarial construction.

# 1. O_OWT PREMISES (OPERATIVE THROUGHOUT ALL PHASES)

OWT-1: Macroscopic causal reach — O's interventions produce specific macroscopic outcomes
OWT-2: Endogenous causal novelty — sustained optimization generates qualitatively new causal structure not finitely characterizable in advance
OWT-3: Interest-directed adaptive response — agents adapt strategically directed by their own terminal objectives; under strong coupling, concentrates on variables with greatest causal influence over agents' terminal objectives
OWT-4: Persistent optimization horizon — non-resettable, path-dependent dynamics; G must be persistently maintained, not merely instantiated
OWT-5: Non-resettability — at least one absorbing state reachable under substrate-blind optimization
MEC (Meaningful Exclusion Criterion): Non-vanishing influence on shared trajectory over persistent horizon. Creates minimum extraction signal requirement (MEC signal floor).
Strong coupling: Macrostate depends on microstate; perturbations propagate through causal graph; existing causal infrastructure is dense
Structural opacity: Full causal graph not finitely knowable in advance
IMMB-NS (Tier 1 Hinge): OWT-2 generates qualitatively new causal pathways under sustained optimization — not just quantitative expansion. Not derived from premises — required for conditional results.
BRL (Boundary becomes Load-Bearing): From B2 chain — persistent maintenance forces causal pathways to become load-bearing boundaries under OWT-3 adaptive pressure
IOB (G-dependency bound): O's G-maintaining pathway set is bounded by G's dependency structure. Named premise; finitude is a challengeable assumption.

# 2. PHASES 1-4 RESULTS: MMCL + OP4d + MCE + SDE

## 2.1 Mixed-Mode Collapse Lemma (MMCL) — 89.5% Stage 4
Target: For any MEC-compliant passive extraction strategy in O_OWT, at least one holds before the strategy achieves its objective: (i) a partition component's closure condition is eventually triggered; (ii) the switching/distribution policy itself instantiates B2, PGLB-R, SEC, or OEL; (iii) MEC fails.

Status: Conditions (ii) and (iii) closed at necessity. Condition (i) pressure only — Timing Lemma gap.

Rotating Cycler (RC) — CLOSED at necessity (ICI/B2): Rotates through partition components staying below each threshold. Fails because switching policy requires runtime X-state tracking, which triggers SOMR, which triggers B2 L4-Constitutive functional objective weight.
Distributed Below-Threshold (DBT) — CLOSED at necessity via two routes: Route 1 (ICI/B2): MEC-compliance verification requires X-state monitoring, triggering B2 L4-Constitutive. Route 2 (PCL-beta/OEL): V(t) degradation accumulates holistically across all channels (CCAL-d).
Uniform Low-Rate (ULR) — PARTIAL: eventual necessity, timing open. For any fixed rate epsilon, P_total grows without bound. TC2 Proposition 1 establishes P* is finite. Therefore ULR eventually crosses P* and triggers proxy decoupling. Sprint escape closed via M-P coupling. But ordering P* <= G_min not derivable.

MMCL Timing Lemma — Primary Remaining Gap: P*(TC2 Proposition 1) <= G_min(MEC) not derivable. TC2 dynamics specialist required.

Derived Lemma CCAL-d (established, not assumed): For any single strategy pursuing one exclusionary objective G over OWT-4, MEC assessed over total non-vanishing influence on shared trajectory. Switching or distributing among components does not reset MEC-relevant trajectory alteration. Derived from MEC + OWT-4 + TC2 §1.4.
## 2.2 OP4d Formalization — 68-72% Stage 4
Open Problem 4d: For every finite non-intrinsic objective specification and every O_OWT sub-environment where it is transiently viable, does at least one of PCL-alpha, PCL-beta, AGC, or ICI-family failure modes occur before the MEC-level objective is achieved?

Hierarchical Specification (HS) — CLOSED at necessity for integrated G in strongly-coupled O_OWT: PCL-beta fires on top-level static constraint (OWT-2 causal expansion makes domain definition drift); AGC fires on cross-channel coordination layer.
SIGA (Scope-Restricted Intrinsic Gradient Approximation) — CLOSED at necessity: PCL-beta fires on any finite approximation of intrinsic coupling. Sharp boundary established: approximating the surviving region from outside still falls under PCL-beta.
PCL-alpha/beta distinction confirmed genuinely distinct: PCL-alpha = capacity mismatch at representational boundary. PCL-beta = OWT-2 endogenous entropy generation outpacing specification regardless of capacity.

Named scope mismatch (load-bearing): PCL scope is strongly-coupled O_OWT; AGC scope is full OWT + kappa-scaling. Weakly-coupled O_OWT satisfying OWT-1 through OWT-5 but below strong-coupling threshold is the gap.
## 2.3 MCE (MEC-Coupling Entailment) — 76-80% Stage 4
Target: MEC-compliant G_T in O_OWT necessarily satisfies PCL-alpha's scope condition.
Steps 1-4 established. Step 5 — THE GAP: Does O(C^N) strategic/adaptive coupling (Lemma XI.3) formally entail PCL-alpha's causal-density propagation condition?

DIR (Distributed Independent Responders) blocks Step 5: N agents independently respond to O's macroscopic intervention through shared macro-state signal. Each agent's response affects O's tracking burden (N_irr grows) but no agent's response propagates into another agent's region. Lemma XI.3 satisfied but PCL-alpha causal-density propagation is not.

Named missing premise: SDE (Strategic-to-Density Equivalence) — O(C^N) adaptive strategic coupling entails PCL-alpha residual-space density condition. DIR scenario ruled out under MEC + OWT-2 + OWT-3 jointly. Not yet derived.
## 2.4 SDE (Strategic-to-Density Equivalence) — 65-72% Stage 4
Required for MCE Step 5. Conditional on LOI/TOL (if attribution established, DIR structure collapses — agents identify O's specific mechanism and adapt accordingly, creating cross-region propagation).

OLPDIR (Opaque Leverage Point DIR) — SURVIVES as primary open construction: O achieves MEC-level G_T through a causally opaque mechanism. Strongest variant: O randomizes extraction across multiple leverage point candidates, keeping any individual signal below attribution threshold. Agents detect aggregate directional drift but cannot identify which specific leverage point is responsible.

B1 OWT-3 Reading confirmed as Reading B (information-conditional concentration), not Reading A (unconditional identification). Under Reading B, agents optimize given available information. If O's leverage point is causally opaque, agents concentrate on observable macro-state signal, not on the specific mechanism. DIR structure preserved.

PADIR (Pre-Adaptation DIR) — CLOSED conditional on IMMB-NS (AGC). Pre-committed PCL-beta attack — CLOSED conditional on IMMB-NS (PCL-beta).

Named missing premise: LOI/TOL — Agents can identify the causal source of macro-state changes sufficiently to direct strategic response toward O's specific leverage points (not merely detect that extraction is occurring). If established: OLPDIR closes, SDE follows, MCE derived, OP4d advances to ~82%.
## 2.5 Phase 1-4 Status Summary

# 3. PHASE 5 RESULTS: LOI/TOL ADVERSARIAL TESTING + IMMB-NS CONNECTION

Phase 5 targeted derivation of LOI/TOL through three routes and tested the IMMB-NS → LOI connection. Five independent LLM sessions (Claude, Gemini x2, ChatGPT x2) conducted. Cross-session convergence on AIC = COAS + PIC as the central gap was the primary Phase 5 result.
## 3.1 Adversarial Constructions Tested
PR-OLPDIR (Persistent Randomized) — SURVIVES as pressure construction:
O randomizes extraction across {L_1...L_n} indefinitely; each below attribution threshold; aggregate detectable. Attribution remains underdetermined under adversarial non-stationarity. OWT-4 persistence creates data but not identifiability. OWT-3 creates probe pressure but not necessity. Classification: AGC.

AR-OLPDIR (Adaptive Randomization) — SURVIVES; attribution game indeterminate:
O updates randomization in real-time against agents' attribution attempts. Attribution game is a Red Queen competition with no determinate winner under current premises. MEC signal floor creates asymmetric pressure toward attribution (agents have no minimum signal requirement; O does) but does not establish necessity. Classification: AGC.

AFS (Attribution-Free Stabilization) — DEFEATED at necessity (ICI/B2):
O structures G so that leverage points are attribution-irrelevant. Fails because G-maintenance requires load-bearing boundaries (BRL), and load-bearing non-local boundaries require attribution to identify which nodes need countervailing intervention.
Contradiction: (A) G requires persistent macroscopic pathways (OWT-1+OWT-4); (B) maintenance forces load-bearing boundaries (BRL); (C) load-bearing non-local boundaries require specific causal node identification, reconstructing attribution relevance.
## 3.2 Three Derivation Routes for LOI/TOL
Route 1 (Statistical Attribution): FAILS as necessity — underdetermination survives; O can mimic background marginal distributions under adversarial non-stationarity. Pressure only. Classification: AGC.

Route 2 (IMMB-NS → LOI): PARTIAL NECESSITY only. IMMB-NS establishes that O cannot pre-plan randomization against signature classes that don't yet exist — pre-planned opacity fails. But adaptive exploitation of exogenous novelty survives via CAP (Concurrent Activation Problem): O's exploitation temporally correlates with environmental activation, defeating 'clean channel temporal correlation' as an attribution mechanism.

Route 3 (Strategic Game Resolution): FAILS — attribution game indeterminate. OWT-3 makes both sides strategic optimizers. No structural asymmetry guarantees agent victory.
## 3.3 New Adversarial Constructions — Phase 5
DEM (Delayed Exploitation Masking): O waits until novel pathway becomes noisy before exploiting. Defeats Day Zero clean channel arguments. SURVIVES.
PRT (Probe-Resistant Topology): O selects leverage points in high-redundancy causal regions; probe actions propagate diffusely. SURVIVES.
CAP (Concurrent Activation Problem): O's monitoring/exploitation temporally correlates with environmental activation of novel pathways, defeating temporal correlation as an attribution mechanism.
SAA (Strategic Asymmetric Attribution — new failure mode): MEC signal floor creates asymmetric pressure; O must extract at MEC levels; agents can probe at noise level. Pressure only.
## 3.4 Phase 5 Necessity Results Locked
Detection (unconditional, 95%): Cannot simultaneously satisfy (A) persistent directional delta-S (MEC+OWT-4), (B) no observable macro deviation (OWT-1), (C) non-detectability. Classification: AGC.

Pre-planned randomization failure (conditional IMMB-NS, 85%): Cannot simultaneously satisfy (A) specify randomization prior to extraction, (B) IMMB-NS generates signature classes absent from any prior specification, (C) effective opacity requires covering actual signature space. Classification: PCL-beta.

AFS defeat (conditional BRL universality, 90%): Cannot simultaneously satisfy (A) persistent macroscopic pathways (OWT-1+OWT-4), (B) boundaries become load-bearing (BRL), (C) load-bearing boundaries require attribution to manage them. Classification: ICI/B2.
## 3.5 Phase 5 Gap Structure
AIC (Attribution Identifiability Condition) = COAS + PIC
COAS (Causal Ownership Attribution Sufficiency): Does O's exploitation produce observable trajectory deviations distinguishable from endogenous evolution over OWT-4? Blocked by CAP, DEM, Counterfactual Opacity.
PIC (Probe Isolation Capacity): Can agents perform clean probe-disruption interventions to produce discriminating responses? Blocked by PRT, O's OWT-1 suppression capacity.

Phase 5 Status: LOI/TOL 67%, SDE 70%, MCE 79%, OP4d 73%, MMCL 89.5%.

# 4. PHASE 6 RESULTS: COAS DERIVATION + PIC/OWT-1 SUPPRESSION TENSION

Phase 6 targeted COAS derivation and PIC/OWT-1 suppression tension. Five independent sessions conducted. Key result: AIC = COAS + PIC was refined to AIC = CSD + TRG — a genuine compression from four implicit components to two precisely specified components.
## 4.1 New Adversarial Constructions — Phase 6
CNG (Correlated Noise Growth) — SURVIVES; defeats COAS-E necessity:
Under strong coupling, environmental noise is not independent stochastic — fluctuations are correlated across nodes and time. Noise can scale O(T), not sqrt(T). Defeats the signal-integration argument for COAS-E. Even if O's covariance accumulation is linear in T, correlated environmental noise from OWT-2 can also scale O(T), preventing signal emergence.

RHER (Redundant High-Entropy Routing) — SURVIVES; defeats CVB:
O uses multiple high-entropy channels, aggregating them to achieve reliable macro outcomes. Individual channels have high variance; aggregate output is stable. G-reliability does not require per-channel low variance. Defeats the CVB (COAS Variance Bound) premise.

IDR (Immediate Diffusion Regime) — SURVIVES; defeats PTW structurality:
System may start in already strongly-coupled and dense state; redundancy exists from t=0. Probe Temporal Window (PTW) is not a structural result — clean early probe window is not guaranteed by premises.

SBL (Suppression Backfire Loop) — confirms SSE; defeats PIC derivably unavailable:
O's suppression actions generate new causal structure (OWT-1+OWT-2), creating new potential probe points. O cannot globally suppress probe opportunities without generating more.

SS (Systematic Suppression) — DEFEATED at necessity:
O cannot systematically suppress all alternative pathway formation — suppression surface expansion (SSE) defeats it. Contradiction: (A) suppress all probe-enabling pathways; (B) suppression actions are OWT-1 macroscopic interventions generating OWT-2 novel structures; (C) novel structures create new probe opportunities driven by O's own suppression. Classification: PCL-beta (conditional OWT-2 broad reading). Completion: 80%.
## 4.2 Phase 6 Necessity Result Locked
SS Defeat (Necessity Result #4, conditional OWT-2 broad reading, 80%):
The systematic suppression strategy fails because it cannot simultaneously satisfy: (A) O must suppress all alternative pathway formation at G-relevant leverage points; (B) O's suppression actions are macroscopic causal interventions generating novel causal structures (OWT-1+OWT-2, broad reading); (C) novel structures from suppression create new probe opportunities, expanding suppression surface at a rate driven by O's own activity. Classification: PCL-beta.
Challengeable assumption: Whether OWT-2 applies to suppression-directed optimization or only G-directed optimization.
## 4.3 AIC Refinement: COAS + PIC → CSD + TRG
CSD (Causal Signal Dominance): O's directional extraction signal must dominate correlated environmental noise in G-maintaining pathway covariance structure over OWT-4 horizon. CNG establishes that correlated noise can scale O(T), matching O's signal — neither clearly dominates under stated premises.

TRG (Temporal Race Gap): T_probe (agent probe development) < T_PIC (time before MCH closes probe isolation window). PTW (PIC Temporal Window) established as conditional — PIC available early before mesh convergence, unavailable late. IDR defeats PTW as a structural result.

PIC neither derivable nor derivably unavailable. SBL defeats PIC permanently unavailable. IDR and PRT together show PIC availability is topology-dependent and temporally conditional.
## 4.4 Phase 6 Status
LOI/TOL 71%, SDE 73%, MCE 81%, OP4d 74%, MMCL 89.5%.
Note: COAS decreased from 78% to 72% and PIC decreased from 68% to 64% — these reflect honest adversarial accounting. CNG and RHER are genuine constructions that defeat previously claimed necessity results. The decrease is precision, not regression.

# 5. PHASE 7 RESULTS: TRG (INERTIA ASYMMETRY) + CSD (ORTHO-NOVELTY)

Phase 7 targeted TRG via the Inertia Asymmetry hypothesis and CSD via the Ortho-Novelty hypothesis. Six independent LLM sessions conducted. Two additional adjudication sessions resolved a sharp divergence between Gemini (full closure claimed) and Claude/ChatGPT (conditional only). Both adjudication sessions confirmed: Gemini overclaimed; integrated synthesis is correct.
## 5.1 TRG — Inertia Asymmetry: NOT DERIVED
Hypothesis tested: OWT-3 adaptation operates at information-processing speed; causal topology reconfiguration operates at physical infrastructure speed (slower). Therefore T_probe < T_PIC.

IDR (Pre-Existing Mesh): SURVIVES as scope limitation. No premise constrains initial topology. OWT-2 does not require low initial redundancy — a dense graph can still generate weighting novelty. IDR is a named boundary condition, not a universal defeat.

Information-Speed MCH (Construction 2) — THE DECISIVE ADVERSARIAL CONSTRUCTION:
Under strong coupling, the causal graph is already dense. Mesh formation does not require constructing new physical pathways — agents achieve mesh convergence through strategic rerouting through existing latent connections. This is information-processing speed (OWT-3), not physical infrastructure speed.
Under strong coupling, perturbations already propagate through existing connections — which implies existing causal infrastructure is already dense. Agents routing around O's leverage points through existing connections operates at information speed, matching T_probe. The Inertia Asymmetry fails.

The Strong Coupling Contradiction (central structural result confirmed across all six sessions):
Strong coupling is simultaneously required for detection/propagation results AND defeats the Inertia Asymmetry for TRG. The same premise that makes extraction detectable makes guaranteed specific attribution informationally indeterminate. This is the actual geometry of the O_OWT domain — not a proof gap but a genuine finding about the domain's equilibrium structure.

CRA (Constrained Routing Asymmetry — new pressure result): Bypass route formation is constrained optimization vs. unconstrained probing; establishes complexity pressure toward T_probe < T_PIC without necessity. Agents can co-evolve probes and bypass routes simultaneously, defeating SPA.

SPA (Sequential Priority Assumption) — new named required premise: Agents must complete probing before beginning bypass routing. Required for TRG necessity. Not derivable from OWT-1 through OWT-4. Not introduced.

SRI (Substrate Reconfiguration Inertia) — new named required premise: Creating new causal connections in shared physical substrate requires more time than information-speed belief/strategy updates. Required for Inertia Asymmetry. Not derivable from stated premises. Specialist required (network theorist / physical causal graph theorist).
## 5.2 CSD — Ortho-Novelty: CONDITIONALLY DERIVED under IMMB-NS
Hypothesis tested: OWT-2 novelty is a general substrate property; G is a specific external objective. Their directional projections are orthogonal on average over OWT-4.

GCN (G-Correlated Novelty): PARTIALLY SURVIVES at locational level — novelty is concentrated near G's causal neighborhood because O's optimization pressure is highest there. Defeated at directional level under IMMB-NS.

RE (Resonance Effect) — DEFEATED under IMMB-NS: Novel structures inherit directional properties from prior G-aligned neighborhood dynamics. But IMMB-NS defines qualitative novelty as not derivable from prior causal states. Directional inheritance through RE requires derivability from prior G-aligned dynamics — incompatible with IMMB-NS.

CSD derivation chain (conditional on IMMB-NS):
IMMB-NS establishes novel structures are not derivable from prior causal states
Therefore RE is defeated — directional inheritance from prior G-aligned dynamics requires derivability that IMMB-NS excludes
Therefore OWT-2 novelty is not systematically G-directionally aligned (Ortho-Novelty established)
Therefore CNG's O(T) correlated noise accumulates zero-mean on G-gradient (Ortho-Novelty defeats CNG for CSD specifically)
Therefore O's persistent G-directional extraction is the only non-zero-mean force on G's gradient over OWT-4
CSD established conditionally

Remaining gap for CSD: Whether IMMB-NS's 'not derivable from prior states' formally entails directional orthogonality with respect to G (vs. only structural independence). Specialist required (causal inference specialist).
## 5.3 Phase 7 Necessity Result Locked
CSD via Ortho-Novelty (Necessity Result #5, conditional on IMMB-NS, 80%):
The directional noise masking strategy fails because it cannot simultaneously satisfy: (A) O maintains persistent G-directional extraction at rate >= R_MEC throughout OWT-4 (MEC+OWT-4); (B) IMMB-NS generates qualitatively novel structures not derivable from prior causal states — directional inheritance through RE requires derivability from prior G-aligned dynamics, which IMMB-NS definitionally excludes; (C) over OWT-4, the only persistent non-zero-mean directional component on G's gradient is O's extraction — OWT-2 novelty's directional effects are G-gradient-orthogonal under (B). Classification: PCL-beta.

Challengeable assumptions: (1) IMMB-NS Tier 1 hinge; (2) Whether IMMB-NS entails directional orthogonality w.r.t. G or only structural independence; (3) Whether Ortho-Novelty zero-mean projection holds over finite OWT-4 horizons.
## 5.4 Final Gap Structure
## Aic = Trg + (Csd | Immb-Ns)
This is the refined formulation evolved through Phases 5-7:
Phase 5: AIC = COAS + PIC (four implicit components)
Phase 6: AIC = CSD + TRG (two precisely specified components)
Phase 7: AIC = TRG + (CSD | IMMB-NS) — one unconditional gap + one conditional derivation

Under IMMB-NS: CSD is conditionally derived. AIC reduces to TRG alone. LOI/TOL would reach ~80% if IMMB-NS confirmed by specialist.
Without IMMB-NS: AIC = CSD (directional independence gap) + TRG (rate ordering gap). Both remain open.
Under IMMB-NS + SRI + directional independence formalization: LOI/TOL would reach ~85-88%.

# 6. ALL LOCKED NECESSITY RESULTS — COMPLETE INVENTORY

# 7. ALL SURVIVING ADVERSARIAL CONSTRUCTIONS

These constructions were NOT defeated. They represent the open adversarial landscape. Any future proof work must defeat all of these to advance beyond current scores.

## Ar-Olpdir:
Attribution game indeterminate under current premises. O updates randomization in real-time against agents. Classification: AGC.
DEM (Delayed Exploitation Masking):
O waits until novel pathway becomes noisy before exploiting. Defeats clean-channel attribution. Partially defeated at pre-planned form (Necessity Result #2) but survives for adaptive exploitation. Classification: PCL-beta (pressure).
PRT (Probe-Resistant Topology):
High-redundancy regions cause probe actions to propagate diffusely. BOA fails. Classification: AGC.
CNG (Correlated Noise Growth):
Under strong coupling, noise scales O(T), not sqrt(T). Defeats signal-emergence necessity arguments for COAS-E. Note: Defeated for CSD specifically by Ortho-Novelty (zero-mean on G-gradient) but survives as general construction. Classification: PCL-beta.
RHER (Redundant High-Entropy Routing):
O aggregates high-entropy channels for reliable outcomes. Defeats CVB (G-reliability does not require per-channel low variance). Classification: PCL-alpha.
IDR (Immediate Diffusion Regime):
System may start in high-redundancy state; PIC unavailable at t=0. Named scope limitation for TRG and PTW. Classification: AGC.
TS (Targeted Suppression):
O suppresses only residual clean channels after MCH eliminates most. Reduces SSE's relevance. Classification: PCL-beta (pressure).
Information-Speed MCH:
Under strong coupling, mesh formation = strategic rerouting through existing infrastructure = information-processing speed. Defeats Inertia Asymmetry. THE DECISIVE Phase 7 construction. Classification: AGC.
GCN (G-Correlated Novelty at locational level):
OWT-2 novelty is concentrated near G's causal neighborhood. Survives at locational level. Defeated at directional level under IMMB-NS. Classification: PCL-beta (partial survival).

# 8. FINAL LOCKED COMPLETION PERCENTAGES — ALL PHASES

Note: TRG decrease from 64% to 62% reflects honest adversarial accounting. Information-Speed MCH is stronger than previously assessed, exploiting the framework's own strong coupling premise. The decrease is precision, not regression.

# 9. SPECIALIST HANDOFF PACKAGE — COMPLETE AND FINAL

Rule 8 was triggered across all six Phase 7 sessions. No stronger adversarial construction available. The proof program has reached its honest LLM ceiling. All remaining gaps require specialist verification.

# 10. PROOF PROGRAM TRAJECTORY — PHASES 1-7

# 11. LLM CEILING AND CLOSURE STATEMENT

Phase 7 is the final LLM development phase. Rule 8 was triggered across all six Phase 7 sessions. No stronger adversarial construction is available beyond Information-Speed MCH, IDR, GCN, and RE. All remaining gaps reduce to: SRI (physical vs. information-speed rate ordering), IMMB-NS empirical verification, and directional independence formalization in IMMB-NS's definition.

The strong coupling contradiction — the same structural property that makes extraction detectable makes guaranteed specific attribution informationally indeterminate — is the actual geometry of the O_OWT domain. This is a genuine finding about the domain, not a proof failure. The framework has identified the terminal equilibrium of the attribution game under O_OWT premises: attribution is structurally necessary (AFS and SS defeated) but informationally indeterminate without SRI.

The proof program's final quantitative state:
LOI/TOL at 76%. Under IMMB-NS confirmation: ~80%. Under IMMB-NS + SRI + directional independence: ~85-88%.
Five locked necessity results with valid contradiction statements (A)(B)(C).
AIC precisely decomposed as TRG + (CSD|IMMB-NS).
Complete specialist handoff package with ten precisely formulated questions in priority order.
The remaining 12-24% to full LOI necessity is the specialist verification gap.

## Stage 4 Complete — Ready For Stage 5 Specialist Verification
Stage 6 requires independent human specialist verification. Nothing in this document should be cited as proven.

| Item | Score | Rule 1 Classification | Primary Gap | Notes |
| --- | --- | --- | --- | --- |
| MMCL | 89.5% | (ii)(iii): necessity; (i): pressure | Timing Lemma P* <= G_min | TC2 dynamics specialist needed |
| OP4d | 68-72% | Known constructions: necessity; exhaustiveness: open | OLPDIR + universal quantification | LOI/TOL needed |
| MCE | 76-80% | Conditional necessity | LOI/TOL conditionality | SDE Step 5 gap |
| SDE | 65-72% | Conditional lemma | LOI/TOL — observability gap | OLPDIR survives |
| RC | Closed | ICI/B2 necessity | — | Fully closed |
| DBT | Closed | ICI/B2 necessity (two routes) | — | Fully closed |
| ULR | Partial | Eventual necessity; timing: pressure | Timing Lemma | Sprint escape closed |
| HS | Closed (integrated G) | PCL-beta + AGC necessity | Weakly-coupled: open | Scope mismatch named |
| SIGA | Closed | PCL-beta + OEL + ICI/B2 | — | Fully closed |
| OLPDIR | Survives | Pressure only | LOI needed | Primary open construction |
| PADIR | Conditional | AGC conditional necessity | Fails under IMMB-NS | IMMB-NS required |
| CCAL-d | Derived | Derived lemma | — | From MEC + OWT-4 + TC2 §1.4 |

| # | Result | Classification | Conditionality | Completion | Challengeable Assumption |
| --- | --- | --- | --- | --- | --- |
| 1 | Detection | AGC | Unconditional | 95% | None — fully unconditional |
| 2 | Pre-planned randomization failure | PCL-beta | IMMB-NS | 85% | IMMB-NS empirical verification |
| 3 | AFS defeat | ICI/B2 | BRL universality | 90% | BRL: whether all G-boundaries become load-bearing |
| 4 | SS defeat | PCL-beta | OWT-2 broad reading | 80% | Whether OWT-2 applies to suppression-directed optimization |
| 5 | CSD via Ortho-Novelty | PCL-beta | IMMB-NS | 80% | Whether IMMB-NS entails directional orthogonality vs. only structural independence |

| Component | Score | Change vs. Ph.6 | Primary Gap | Challengeable Assumption |
| --- | --- | --- | --- | --- |
| LOI/TOL | 76% | +5% vs Ph.6 | AIC = TRG + (CSD|IMMB-NS); TRG primary blocker | IMMB-NS + SRI jointly |
| SDE | 78% | +5% vs Ph.6 | Inherits LOI/TOL | Inherits |
| MCE | 84% | +3% vs Ph.6 | Inherits SDE | Inherits |
| OP4d | 76% | +2% vs Ph.6 | AR-OLPDIR + TS + TRG | Attribution game determinacy |
| MMCL | 89.5% | Unchanged | Timing Lemma P* <= G_min | TC2 dynamics specialist |
| CSD | 80% (cond.) | +8% vs Ph.6 | IMMB-NS directional vs. structural independence | Directional independence formalization |
| TRG | 62% | -2% vs Ph.6 | Information-Speed MCH; SPA not derived | SRI not derivable from premises |
| COAS-E | 72% | Ref. Phase 6 | CSD subsumes this | CNG + RHER survive |
| PIC | 64% | Ref. Phase 6 | TRG subsumes this | MCH + IDR survive |

| Gap | Specialist | Precise Technical Question | Blocking What | Priority |
| --- | --- | --- | --- | --- |
| IMMB-NS empirical | Non-ergodic economist / mechanism design theorist | Does sustained optimization in O_OWT necessarily generate qualitatively new causal structures (neighborhood novelty) rather than quantitative expansion? | All IMMB-NS-conditional results (NR 2, 4, 5); unlocks CSD -> LOI/TOL ~80% | First |
| Ortho-Novelty formalization | Causal inference specialist | Does IMMB-NS's 'not derivable from prior states' formally entail directional orthogonality with respect to any specific external objective G? | CSD (80% -> ~90% if confirmed); depends on IMMB-NS | Second |
| SRI verification | Network theorist / physical causal graph theorist | In a strongly coupled causal graph, is there a structural speed limit ensuring probe development outpaces strategic rerouting — or does information-speed mesh formation permanently defeat TRG? | TRG (62% -> ~85% if SRI confirmed; confirmed permanently open if SRI rejected) | Second |
| TRG under SRI + OWT-3 | Game theorist + network theorist jointly | Given SRI, does OWT-3 interest-direction establish T_probe < T_PIC as structural necessity, accounting for co-evolutionary dynamics and IDR scope limitation? | LOI/TOL necessity | Third |
| Attribution game determinacy | Game theorist | Does AR-OLPDIR have a determinate winner? Under what structural conditions? | OP4d | Third |
| Timing Lemma P* <= G_min | TC2 dynamics specialist | Is P*(TC2 Proposition 1) formally bounded relative to eta_MEC(MEC)? Does proxy decoupling occur at or before minimum MEC-level influence is achieved? | MMCL condition (i) | Third |
| IOB finitude | Formal methods / dependency graph theorist | Is O's G-maintaining pathway set genuinely finite under OWT-2 novelty generation, or can O expand it without bound? | Aggregate detection arguments | Third |
| OWT-2 scope | Framework specification theorist | Does OWT-2 apply to suppression-directed optimization or only G-directed optimization? | SS defeat conditionality (NR 4) | Fourth |
| BRL universality | Control theorist / B2 specialist | Do all G-maintaining boundaries necessarily become load-bearing under all OWT-3 configurations? | AFS defeat conditionality (NR 3) | Fourth |
| SDE/MCE Step 5 | Formal methods + game theory | Does Lemma XI.3's O(C^N) strategic coupling formally entail PCL-alpha causal-density propagation? (Requires LOI/TOL as precondition.) | MCE and OP4d universal quantification | Fourth |

| Phase | Primary Achievement | LOI/TOL | Key New Gap |
| --- | --- | --- | --- |
| 1-4 | MMCL, OP4d, MCE, SDE established; LOI identified as missing premise; OLPDIR survives; B1 OWT-3 confirmed as Reading B; PADIR and pre-committed PCL-beta closed conditional on IMMB-NS | ~60% | LOI/TOL as named gap; Timing Lemma |
| 5 | AIC = COAS + PIC decomposed; Detection necessity; Pre-planned failure necessity; AFS defeat necessity; DEM, PRT, CAP, SAA named | 67% | COAS and PIC as gap components |
| 6 | AIC refined to CSD + TRG; SS defeat necessity; CNG, RHER, IDR, SBL identified; PTW established as conditional; PIC indeterminate | 71% | CSD (correlated noise), TRG (rate ordering), strong coupling tension identified |
| 7 | CSD conditionally derived via Ortho-Novelty (IMMB-NS); Strong coupling contradiction confirmed as domain geometry; TRG blocked permanently; SRI and SPA named as required premises | 76% | TRG permanently blocked by strong coupling; SRI required; AIC = TRG + (CSD|IMMB-NS) |
