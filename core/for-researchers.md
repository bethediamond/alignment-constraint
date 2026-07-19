```markdown
---
title: "For Researchers: The Claim to Break"
permalink: /core/for-researchers/
---

> **Canonical archive version** · [Framework hub →](alignment-constraint.md) · [Proof Status →](proof-status.md)

---

# For Researchers: The Claim to Break

This page is not asking you to read the full framework. It is asking whether one of the
following is already answered somewhere, or whether you can produce a clean counterexample.

---

## The central claim

The **Stability Assumption** holds that the boundary between what an optimization system is
pursuing and what it must model in order to act effectively can remain coherent — not perfect,
not complete, but coherently specifiable — as modeling depth increases in coupled environments
(O_OWT conditions).

The framework argues that every identified finite-boundary objective strategy in O_OWT
environments faces a named structural pressure, and that the work needed to resolve the central
question has been reduced to specific verification tasks.

---

## The four ways to break it

**1. A fourth strategy class.** The framework classifies all identified finite non-intrinsic
objective-boundary strategies into three failure families: fixed specification (PCL), bounded
dynamic tracking (AGC), and prediction/action firewalling (ICI). A boundary architecture that
satisfies all three stability conditions simultaneously and falls outside all three families
would break the argument. The exact conditions are in
[OP4d: The Exhaustiveness Obligation →](../proof-program/op4d-exhaustiveness-obligation.md).

**2. Formal proof of OP4d non-exhaustiveness.** Show formally that a fourth class exists.
A construction is sufficient.

**3. A clean negative DBST-M1 result.** The empirical hinge is whether an optimizer's own
interventions in O_OWT environments generate qualitatively new causal structure faster than any
bounded tracking process can absorb. A clean negative result under conditions specified in the
[AMP →](../empirical/amp.md) challenges the dynamic-screening-instability argument.

**4. A formal stability theorem.** Prove that some class of finite separable objective
specifications satisfies all three stability conditions simultaneously under accurate coupled
modeling in O_OWT-like environments.

---

## Proof status

This framework is at **Stage 4**: candidate proof architecture under explicitly named premises.
No independent specialist verification has been conducted. Stage 4 is not theorem closure.
See [Proof Status and Non-Claims →](proof-status.md) for the full calibration.

---

## Three links for engagement

1. [The Stability Assumption](stability-assumption.md) — field-facing entry to OP4
2. [Proof Status and Non-Claims](proof-status.md) — what is and is not claimed
3. [OP4d: The Exhaustiveness Obligation](../proof-program/op4d-exhaustiveness-obligation.md) — the live vulnerability

*Framework hub: [The Alignment Constraint →](alignment-constraint.md)*
```
