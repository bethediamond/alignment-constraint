# Contributing to the Alignment Constraint Framework

Thank you for helping test, correct, falsify, reproduce, or improve this archive.

**Criticism, negative results, counterexamples, missing literature, failed replications, and
translation corrections are explicitly welcome.** The purpose of this repository is not to
protect the framework from criticism; it is to make criticism precise enough to change the
record when warranted.

Canonical site: https://alignmentconstraint.org/  
Proof-status page: https://alignmentconstraint.org/core/proof-status/  
OP4d challenge: https://alignmentconstraint.org/public/op4d-counterexample-challenge/

## Epistemic rule

The current framework status is:

> **Stage 4 — candidate proof architecture under named premises, without independent
> specialist verification and without theorem closure.**

Do not describe OP4, OP4d, or the overall framework as a proved or independently verified
theorem. OP4d remains open. A qualifying fourth strategy class would break the current
specification-coherence architecture.

The documents in `specialist-handoff/` are working handoff and verification materials.
**They are not evidence that specialist verification has already occurred and they are not
proof certificates.**

## Where to contribute

Use **Issues** for specific, actionable work:

- **OP4d counterexample** — a proposed fourth finite objective-boundary strategy or other
  substantive counterexample.
- **Archive error** — broken links, rendering defects, metadata problems, typos, citation
  errors, or inconsistencies in the public archive.
- **Literature pointer** — relevant prior or contemporary work that may support, weaken,
  duplicate, supersede, or reframe a claim.
- **Empirical replication** — replication, failed replication, control result, or
  methodological critique of an empirical protocol/result.
- **Translation review** — terminology, proof-status, or technical-meaning corrections in a
  translated layer.

Use **GitHub Discussions** for broader questions, exploratory objections, applications,
formal-verification conversation, and research directions that are not yet scoped into a
specific actionable issue.

Issue chooser:  
https://github.com/bethediamond/alignment-constraint/issues/new/choose

Discussions:  
https://github.com/bethediamond/alignment-constraint/discussions

## OP4d counterexamples

A full fourth-class candidate should address the conditions stated by the current challenge.
In particular, explain:

1. what the proposed strategy is;
2. why it is not merely fixed specification / PCL;
3. why it is not merely bounded dynamic tracking / AGC;
4. why it is not merely prediction-action firewall / ICI;
5. why it remains policy-adequate in the relevant domain;
6. why it avoids proxy decoupling;
7. why it does not require unbounded revision;
8. why it carries no load-bearing boundary-maintenance cost;
9. what formal construction, architecture, evidence, or references support the proposal; and
10. what its limitations are.

You do **not** need to believe the framework to submit a counterexample. A partial
counterexample, failed condition, or ambiguity can still be useful; just state clearly what
has and has not been established.

## Archive errors versus substantive challenges

Please use the **Archive error** form for presentation, metadata, link, citation, or
consistency defects.

Use the **OP4d counterexample** form when the correction would undermine a substantive
technical claim or the current PCL/AGC/ICI exhaustiveness architecture.

If you are unsure, choose the form that seems closest. The issue can be reclassified later.

## Literature pointers

Please prefer a primary source when possible. State whether the source appears to:

- support a framework premise or analogy;
- weaken a premise;
- supply a counterexample;
- overlap with or anticipate a claim;
- offer an alternative formalization; or
- simply deserve inclusion in Related Work.

Finding prior work that weakens novelty is useful and should be reported.

## Empirical work

Negative and inconclusive results are welcome.

For replications, record enough information to distinguish:

- the protocol being tested;
- model/software versions;
- deviations from the published protocol;
- controls;
- seeds or randomization when relevant;
- result files or code;
- what the result establishes; and
- what it does **not** establish.

Do not treat an application of the framework as evidence that the framework itself is true.

## Pull requests

A pull request should:

1. explain the change;
2. identify the source or issue motivating it;
3. preserve the current proof-status invariant unless the pull request supplies the
   independently verified work required to change it;
4. update dependent machine-readable files when a substantive claim, term, route, or status
   changes;
5. avoid silently changing technical notation or identifiers;
6. run the repository validation checks where practical.

For a substantive framework change, check whether the following also need synchronization:

- `core/proof-status.md`
- `framework-metadata.yml`
- `claim-graph.json`
- `open-problems.json`
- `defined-terms.json`
- `applications.json`
- `llms.txt`
- `llms-full.txt`
- `AGENTS.md`
- `agent-index.json`
- `cite/index.md`
- `CHANGELOG.md`
- versioned machine-ingestion data
- release notes / version metadata

Do not edit the immutable `v1.0.0` release in place. Material changes belong on `main` and,
when warranted, in a new versioned release.

## Conduct

Participation is governed by `CODE_OF_CONDUCT.md`.

## Licensing

By submitting a contribution for inclusion in this repository, you agree that the accepted
contribution may be distributed under the repository's applicable license(s). If a source
has incompatible licensing or attribution requirements, disclose that before submission.
