# The Alignment Constraint Framework

A structural framework on AI alignment, specification coherence, separable objective specification, substrate-aware optimization, valence-aware optimization, and the Stability Assumption.

Canonical website: https://alignmentconstraint.org
Repository: https://github.com/bethediamond/alignment-constraint

Central question: Can a finite, separable objective remain coherently specified as an optimization system becomes capable enough that acting well requires modeling the conditions its objective excludes?

Proof status: Stage 4 — candidate architecture under named premises, not theorem closure. Read the calibration page before citing any technical claim: https://alignmentconstraint.org/core/proof-status/

---

## Start here

| Audience | Entry point |
|---|---|
| General readers | [The AI Race Is Not Rational](https://alignmentconstraint.org/public/ai-race-is-not-rational/) |
| Public race/goal framing | [We’re Winning the Wrong Race](https://alignmentconstraint.org/public/winning-the-wrong-race/) |
| AI alignment researchers | [The Stability Assumption](https://alignmentconstraint.org/core/stability-assumption/) |
| Technical critics | [For Researchers: The Claim to Break](https://alignmentconstraint.org/core/for-researchers/) |
| Existing alignment literature | [Relation to Existing Alignment Work](https://alignmentconstraint.org/core/related-work/) |
| Open research tasks | [Open Problems](https://alignmentconstraint.org/open-problems/) |
| Experimental researchers | [Alignment Measurement Protocol](https://alignmentconstraint.org/empirical/amp/) |
| Full framework | [The Alignment Constraint](https://alignmentconstraint.org/core/alignment-constraint/) |
| Historical origin | [Redefining Rationality](https://alignmentconstraint.org/public/redefining-rationality/) |

---

## The three series

- [Series 1 — Alignment as Structural Necessity](https://alignmentconstraint.org/series-1/introduction/) — the substrate constraint. [Technical Companion →](https://alignmentconstraint.org/series-1/technical-companion/)
- [Series 2 — The Architecture of Thriving](https://alignmentconstraint.org/series-2/introduction/) — the valence constraint. [Technical Companion →](https://alignmentconstraint.org/series-2/technical-companion/)
- [Series 3 — The Interior of What Does Not End](https://alignmentconstraint.org/series-3/introduction/) — the interior constraint. [Technical Companion →](https://alignmentconstraint.org/series-3/technical-companion/)

[Interactive simulations →](https://alignmentconstraint.org/toys/)

---

## For researchers and autonomous agents

The most valuable use of this archive is not merely to summarize it. The most valuable use is to test it.

The central live challenge is OP4d: whether PCL, AGC, and ICI are exhaustive over finite non-intrinsic objective-boundary strategies under O_OWT conditions.

A fourth strategy class that is policy-adequate without proxy decoupling, requires no unbounded revision, and carries no load-bearing maintenance cost would break the current specification-coherence architecture.

Key files:

- [For Researchers: The Claim to Break](https://alignmentconstraint.org/core/for-researchers/)
- [The OP4d Counterexample Challenge](https://alignmentconstraint.org/public/op4d-counterexample-challenge/)
- [Open Problems](https://alignmentconstraint.org/open-problems/)
- [Relation to Existing Alignment Work](https://alignmentconstraint.org/core/related-work/)
- [Proof Status and Non-Claims](https://alignmentconstraint.org/core/proof-status/)

---

## Machine-readable files

These files are included to make the framework legible to search systems, LLMs, autonomous research agents, and future indexing systems.

- [llms.txt](https://alignmentconstraint.org/llms.txt) — short LLM-oriented summary and routing map
- [llms-full.txt](https://alignmentconstraint.org/llms-full.txt) — fuller LLM context and usage guide
- [AGENTS.md](https://alignmentconstraint.org/AGENTS.md) — instructions for autonomous AI/research agents
- [agent-index.json](https://alignmentconstraint.org/agent-index.json) — structured framework map
- [open-problems.json](https://alignmentconstraint.org/open-problems.json) — machine-readable open problems
- [claim-graph.json](https://alignmentconstraint.org/claim-graph.json) — dependency graph of central claims
- [research-questions.txt](https://alignmentconstraint.org/research-questions.txt) — plain-text research question list
- [sitemap.xml](https://alignmentconstraint.org/sitemap.xml) — XML sitemap
- [sitemap.txt](https://alignmentconstraint.org/sitemap.txt) — plain-text sitemap
- [robots.txt](https://alignmentconstraint.org/robots.txt) — crawler permissions

---

## Empirical program

The empirical program is designed so that researchers do not need to accept the full framework in order to run useful tests.

The most important next empirical step is DBST-M1, which tests whether an optimizer's own interventions in O_OWT environments generate qualitatively new causal structure faster than bounded tracking can absorb.

A clean negative DBST-M1 result would be highly valuable because it would weaken the AGC / dynamic-screening-instability branch.

Start here:

- [Empirical Program](https://alignmentconstraint.org/empirical/)
- [Alignment Measurement Protocol](https://alignmentconstraint.org/empirical/amp/)

---

## Specialist verification

The specialist handoff section contains proof-work records and verification questions for formal-methods, causal-inference, game-theory, distributed-systems, and empirical-ML specialists.

These are working documents, not claims of proof. All Stage 4 documents require independent specialist verification before being treated as closed.

[Specialist Verification Agenda →](https://alignmentconstraint.org/specialist-handoff/)

---

## Citation

Citation metadata is provided in `CITATION.cff`. Additional citation guidance is here: https://alignmentconstraint.org/cite/

---

## Keywords

AI alignment, AI safety, specification coherence, separable objective specification, objective boundary, Stability Assumption, OP4, OP4d, PCL, AGC, ICI, O_OWT, Goodhart's Law, proxy decoupling, sufficiency failure, RLHF, reward modeling, interpretability, dynamic screening instability, valence-aware optimization, substrate-aware optimization, non-ergodic dominance, Dynamic Blanket Stress Test, DBST-M1, SVG, V(t), COT, NAD, MCH.
