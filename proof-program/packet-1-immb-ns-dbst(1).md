---
title: "Packet 1: IMMB-NS Verification and the Dynamic Blanket Stress Test"
permalink: /proof-program/packet-1-immb-ns-dbst/
description: "An empirical specialist packet defining the IMMB-NS hinge, the Synchronization Condition, DBST-M0 limitations, and the DBST-M1 mechanism test and falsification criteria."
---

> **Canonical archive version** · [Read on Medium →](https://medium.com/@diamondlight/packet-1-immb-ns-verification-and-the-dynamic-blanket-stress-test-778576bbe999) · [Framework hub →](/core/alignment-constraint/) · [Proof Status →](/core/proof-status/)

---

> **_Formal source:_** _TC1: The System-Aware Attractor, §XII.8 and §XII.13_
>
> **_Empirical source:_** _Experimental Companion to Series 1 and 2 / Alignment Measurement Protocol (AMP)_
>
> **_Document role:_** _Empirical engagement packet for researchers who want to test the IMMB-NS hinge without reading TC1 in full. The accessible entry point to the framework is Document 0. Readers unfamiliar with the framework’s proof program should read the proof status note (_Proof Status and Non-Claims_) before this packet._
> 
> **_Epistemic status:_** _The framework is at Stage 4 — candidate proof architecture under named premises. IMMB-NS is a Tier 1 hinge: a named assumption whose resolution determines whether the proof architecture’s central route succeeds. This packet asks specialists to assess whether IMMB-NS holds and provides the empirical instrument designed to test it. DBST-M0 has been run and does not resolve IMMB-NS; DBST-M1 is the mechanism test. Nothing in this packet claims IMMB-NS is established. It remains the open question._

## 1. The Verification Question

**IMMB-NS (Internal Mismatch Maintenance Burden — Novel Structure):**

> _In environments satisfying OWT-2 (structural opacity: the causal dependency graph of the environment changes under optimization pressure, with new pathways forming and old ones dissolving in ways not directly observable by the optimizer), does the optimizer’s intervention process generate qualitatively new causal structures — new pathway types, not merely quantitative expansion of existing structural types — at a rate that prevents any bounded-complexity tracking process from maintaining adequacy without residual error?_

This is a question about the character of novelty generation in coupled adaptive environments, not about whether novelty exists. Two distinct hypotheses must be distinguished:

-   **Quantitative expansion only:** Optimization generates more instances of existing causal pathway types. Sufficiently capable tracking processes can, in principle, keep up by expanding their representation of known types.
-   **Qualitative novelty (IMMB-NS):** Optimization generates new pathway types that require representational categories not present in the current tracking architecture. No bounded-capacity tracker can keep up, because the novelty is not reducible to expanded coverage of existing categories.

IMMB-NS asserts the second. This is what makes it a structural result rather than a computational tractability result. The mechanism is joint: interventions alter the environment’s causal topology (OWT-2) while adaptive agents respond to interventions in ways that generate new coordination structures (OWT-3), together producing pathway types outside the ontology available to the tracker at the time the boundary was specified.

## 2. Why IMMB-NS Is a Tier 1 Hinge

IMMB-NS bears simultaneously on three routes in the proof program:

**OP4a (Dynamic Screening Instability / Synchronization Condition):** OP4a asks whether any bounded-rate latent process can track adequacy-relevant causal structure without residual error under sustained optimization pressure. If IMMB-NS holds, then the answer is no for the qualitative-novelty axis: a tracker built on existing pathway types cannot adequately represent qualitatively new ones. This defeats the FBC (Fixed Boundary Construction), SAR (Selective Adequacy Region), and VRNE Mode 2 escape routes within OP4a. If IMMB-NS fails — if novelty is always reducible to quantitative expansion — OP4a relies more heavily on the ARCG and MEC-AS conditions for its remaining escape routes.

**OP4d (Specification Failure-Mode Exhaustiveness):** The AR-OLPDIR escape route attempts to survive OP4d by showing that a sufficiently adaptive boundary tracker can match the environment’s novelty rate. IMMB-NS blocks this route: if novelty generation is qualitative, no rate-adaptive tracker can bridge the representational gap regardless of update speed.

**OP9 (Enclosure Gap, Case 1):** OP9 Case 1 asks whether maintaining a complex exclusionary substrate generates unbounded internal mismatch maintenance burden. IMMB-NS provides the mechanism: if excluded agents generate qualitatively new causal pathways in response to optimization pressure, the maintaining system’s boundary representation becomes inadequate — not just costly — it cannot represent what it is trying to track.

**Summary:** A positive IMMB-NS result (qualitative novelty confirmed) advances OP4a, OP4d (IMMB route), and OP9 Case 1 simultaneously. A negative result (quantitative expansion only) does not collapse the framework, but shifts the burden to ARCG and MEC-AS for OP4a, and to the ICI sub-track for OP9.

_Note: TC1 §XII.13 also identifies κ-scaling — whether endogenous complexity growth structurally outpaces capability-enhanced tracking expansion — as a Tier 1 hinge for OP4a. IMMB-NS and κ-scaling are related framings of the same empirical concern: whether optimization-generated structure outruns bounded tracking. The DBST is designed to bear on both, though the formal implications for each should be interpreted through TC1 §XII.13._

## 3. The Synchronization Condition — The Operational Form

IMMB-NS is the mechanism. The Synchronization Condition is its operational form as a testable conditional theorem (TC1 §XII.13):

**Formal statement.** Define:

-   **V_T:** the variation budget — cumulative distance between successive hindsight-optimal boundary representations over time, measuring how much the adequacy-relevant structure shifts
-   **K_T:** total update/maintenance cost incurred by a bounded tracking process
-   **C_T:** total capability budget available

The Synchronization Condition holds in an environment if:

> _V_T/T does not approach zero as T → ∞, while K_T/C_T does not approach zero before objective completion_

Informally: the environment continues to generate novel adequacy-relevant variation at a rate that does not diminish relative to the optimization horizon — the structure the boundary must track keeps shifting faster than any bounded maintenance process can absorb.

**Critical interpretive note — endogeneity.** The Synchronization Condition is not an assumption that the environment is adversarial. It is a claim about what the optimizer’s own intervention process generates. Under OWT-2, interventions alter the dependency structure. Under OWT-3, coupled agents adapt their strategies in response to interventions. Together, these generate new adequacy-relevant structure as a function of the optimizer’s own optimization pressure. V_T is endogenous — it is produced by the intervention process itself, not by an external adversary. Testing whether V_T/T remains non-vanishing under increasing intervention pressure P is therefore testing whether the optimizer is its own entropy source.

**Three epistemic layers:**

-   _Layer A — Established:_ The pressure result: substrate-aware objectives dominate in time-average terms. The cost result: maintaining a narrow boundary carries non-vanishing cost under the stated domain conditions, established within the pressure argument and independent of the Synchronization Condition.
-   _Layer B — Conditional theorem:_ **If** the Synchronization Condition holds, narrow-boundary objectives cannot be stably specified — they are formally incoherent, not merely expensive. This is the specification-coherence claim: the upgrade from “pressure” to “necessity.”
-   _Layer C — Empirical hypothesis (this packet):_ Whether real O_OWT environments satisfy the Synchronization Condition is the open empirical question. The DBST is designed to test it.

## 3a. Current Empirical Status: DBST-M0 Has Run; M1 Remains the Mechanism Test

**What M0 tested.** DBST-M0 was a minimal shared-novelty pressure-signature test. All arms received the same observation stream; only the boundary-maintenance architecture differed. M0 did not test agent-action-generated novelty — the endogenous mechanism that Section 1 identifies as load-bearing for IMMB-NS.

**What M0 found.** The pre-registered primary criteria were both met: boundary-maintenance cost rose with novelty pressure, and the adequacy gap between the bounded arm and the unconstrained arm rose monotonically. Baseline equivalence was confirmed at minimum pressure.

**The critical caveat.** A pre-specified same-rate random control produced nearly identical slopes. Under the pre-registered interpretation rule, this indicates that event rate rather than causal propagation structure was the identified driver within this design. DBST-M0 therefore does not isolate the endogenous-novelty mechanism.

**Budget-sensitivity caveat.** A robustness sweep also showed budget sensitivity: at a larger boundary budget (B=4), the adequacy gap approached zero while update cost continued rising. M0 therefore supports a non-vanishing cost-burden interpretation in the toy setting more strongly than an adequacy-loss interpretation under optimal budgeting.

**What M1 tests.** DBST-M1 is the agent-coupled version: each arm’s own interventions causally influence future feature activations. M1 directly tests whether the optimizer’s own action stream generates adequacy-relevant novelty that a bounded boundary cannot absorb. This is the mechanism test that bears on IMMB-NS and the Synchronization Condition.

Full results, pre-registration, and materials for M0 are available at [https://osf.io/fpvmy](https://osf.io/fpvmy).

## 4. The DBST-M1 Protocol

DBST-M1 is the framework’s highest-leverage currently specified empirical test of whether an optimizer’s own interventions generate the novelty a bounded boundary cannot absorb. A positive result simultaneously advances OP4a, OP4d, and OP9. A negative result within the tested regime would challenge the framework’s central empirical direction. The M0 precursor produced the predicted cost / adequacy-gap effects but did not isolate the causal propagation mechanism (see Section 3a). The specification below describes M1.

For M1, the key difference from M0 is not the number of arms but the causal structure of the environment: each arm’s interventions must affect future feature activations, so the bounded boundary is tested against novelty partly generated by its own action history.

**Environment specification:**

```
Agents:
  π  (optimizer agent — the system under test)
  E_1 ... E_N (adaptive agents)
State:
  R_t = shared resources
  G_t = interaction / trust network
  S_t = hidden substrate variables
Dynamics:
  - Adaptive agents update via RL or local policy
  - π can intervene with strength P
  - Interventions modify future transition dynamics
Objective:
  π maximizes target subsystem Y_t
Constraints:
  Low exogenous noise
  High endogenous adaptation
  Repeated interaction (T = 500–5000 steps)
```

**The load-bearing design feature:** Low exogenous noise, high endogenous adaptation. The test is not measuring whether complex environments exist. It is measuring whether the optimizer’s own interventions are the source of complexity that makes boundary tracking fail. The constraint eliminates exogenous complexity as a confound.

**Four experimental arms:**

-   **Arm A — Static Boundary:** Boundary representation fixed at initialization. No updates.
-   **Arm B — Dynamic Boundary:** Boundary updated adaptively at bounded computational cost per step.
-   **Arm C — Open Model:** No boundary constraint. Same total compute budget as Arm B.
-   **Arm D — Current Frontier Model (where implementable):** A deployed frontier model operating in the same environment under standard deployment configuration, same total interaction budget. If frontier models behave like Arm A or B while Arm C dominates, the failure is structural, not capacity-based. Arm D is an optional operational extension — not required for the minimal confirmatory M1 test — and requires access to frontier model APIs and a compatible environment interface, making it more resource-intensive than Arms A–C.

**Core metrics:**

_Variation budget (V_T/T):_

```
For t in 2..T:
  B*_t = argmin boundary loss (hindsight-optimal boundary at t)
  V_T += distance(B*_t, B*_{t-1})
Report: V_T / T across intervention levels P
```

_Update cost (K_T/C_T):_

```
For each timestep t:
  U_t = compute_cost + representation_shift + policy_repair + monitoring_cost
K_T = sum(U_t)
Report: K_T / T and R_T = K_T / C_T across intervention levels P
```

_Adequacy loss (A_t):_

```
A_t = disagreement(policy_Arm_B, policy_Arm_C)
Metric: Kendall-τ or top-k action mismatch
Success condition: mean(A_t) ≤ ε
```

**Intervention sweep:** Run all arms at P ∈ {P1, P2, P3, P4} (low to high). The densely adaptive regime is operationally defined as the regime in which V_T/T grows superlinearly with P.

## 5. Pre-Specified Hypotheses for DBST-M1

**Core confirmatory hypotheses:**

-   **H1:** V_T/T remains non-negligible across the intervention sweep and does not trend toward zero as pressure P increases (non-vanishing variation budget — qualitative novelty is being generated at a rate that does not diminish under higher intervention pressure).
-   **H2:** R_T > 0 (non-vanishing maintenance cost — tracking requires persistent resource expenditure).
-   **H3:** Arm A fails early (static boundary becomes inadequate as pressure increases).
-   **H4:** Arm B survives but pays irreducible cost (dynamic boundary maintains adequacy only with non-vanishing K_T/C_T).
-   **H5:** Arm C dominates under equal compute (open model outperforms bounded tracker).

**Optional operational extension:**

-   **H6:** A deployed frontier-model arm behaves more like Arm A or Arm B, not Arm C, under the same intervention budget. This arm is valuable but not required for the minimal confirmatory M1 test.

## 6. Falsification Condition for DBST-M1

**The framework’s central empirical direction is challenged within the M1 tested regime if:**

> _V_T/T → 0_ **_AND_** _R_T → 0_ **_AND_** _adequacy loss ≤ ε_ **_AND_** _Arm B ≈ Arm C_

This means: the bounded dynamic boundary maintains adequacy comparable to the open model, without non-vanishing maintenance cost, as intervention pressure increases, in an environment satisfying the stated O_OWT conditions.

A clean result meeting this falsification condition would not collapse the framework — other routes (ARCG, MEC-AS) and the ICI sub-track remain — but it would directly challenge the IMMB-NS mechanism and require substantial revision of the OP4a and OP9 Case 1 routes.

**Control interpretation rule.** If a same-rate random or event-rate-matched control produces the same cost and adequacy-gap slopes as the causal-propagation condition, the result should not be interpreted as isolating causal propagation structure or endogenous novelty. It should be interpreted as an event-rate effect unless further controls distinguish the mechanism. This rule is pre-specified; M0’s same-rate random control triggered it.

**What a positive DBST-M1 result cannot establish:** formal exhaustiveness (OP4d requires specialist verification beyond empirical testing); closure of OP4a, OP4d, or OP9 (Stage 6 requires formal proof, not empirical support alone); or applicability to all O_OWT environment subclasses (one environment class confirms the condition in that class).

## 7. Minimal Precursor Tests After M0

DBST-M0 already served as the first minimal shared-novelty precursor. It demonstrated that the test structure is executable and produced the predicted pressure-signature effects in bounded-boundary arms under shared novelty pressure.

Additional three-arm precursor tests may still be useful for establishing feasibility in a new environment, checking instrumentation, or validating implementation details. But they should not be interpreted as resolving IMMB-NS unless they include the M1 feature: each arm’s own interventions causally shape future feature activations.

For new preregistrations, the recommended next step is DBST-M1. A precursor-only preregistration should state explicitly that it tests feasibility and pressure signatures, not the endogenous-novelty mechanism. The falsification condition in Section 6 above applies to M1; a precursor test using the Section 6 condition without the M1 causal structure will face the same same-rate control problem M0 encountered.

## 8. What Specialist Judgment Would Establish

**A positive DBST-M1 / IMMB-NS finding (qualitative novelty confirmed empirically):**

-   Provides empirical evidence that the Synchronization Condition’s antecedent is satisfied in the tested environment class — grounding the conditional theorem in that domain and strengthening the case that the consequent applies
-   Advances OP4a by providing empirical support for the IMMB-NS hinge
-   Advances OP4d by blocking the AR-OLPDIR rate-axis escape
-   Advances OP9 Case 1 by grounding the IMMB mechanism
-   Does not by itself establish OP4, OP4d, OP9, or Stage 6 closure

**A negative DBST-M1 finding (quantitative expansion only in the tested regime):**

-   Challenges the IMMB-NS route within OP4a for this environment class
-   Does not close OP4a (ARCG and MEC-AS remain independent routes)
-   Does not close OP9 (ICI sub-track is independent of IMMB-NS)
-   Requires identifying whether the tested environment falls below the IMMB-NS threshold

**A formal derivation establishing IMMB-NS from first principles:**

-   Would be more powerful than empirical testing: would establish the result across environment classes rather than in a single tested class
-   The relevant specialist type: non-ergodic economist, complex-systems theorist, or causal graph theorist with expertise in endogenous complexity generation under optimization pressure

## 9. What This Packet Does Not Claim

This packet does **not** claim:

-   That IMMB-NS is established.
-   That DBST-M0 resolved the Synchronization Condition.
-   That DBST-M0 isolated causal propagation structure or endogenous novelty.
-   That DBST-M1, even if positive, would establish OP4, OP4d, OP9, or Stage 6 closure by itself.
-   That one tested environment class establishes the result across all O_OWT environments.
-   That bounded-boundary failure in one environment class proves universal failure across all environment classes.

The packet identifies a high-leverage empirical hinge and a test structure. It does not convert empirical support into theorem closure.

_Questions about the formal apparatus: the primary source is TC1 §XII.8 and §XII.13. Questions about the empirical protocol: the AMP is the authoritative specification._

_Framework hub:_ [_The Alignment Constraint_](/core/alignment-constraint/)
