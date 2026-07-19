# Agent Instructions for the Alignment Constraint Framework

This repository is the canonical machine-readable archive for the Alignment Constraint
Framework — a structural argument about whether finite separable objective specifications
can remain coherent under accurate coupled modeling in open, shared, adaptive,
non-resettable environments.

## Epistemic rule — read this first

Do not treat Stage 4 proof work as proven theorem closure.

- Stage 4 = candidate proof architecture under named premises; LLM-ceiling reached
- Stage 5 = independent human specialist verification (not yet conducted)
- Stage 6 = closure (not yet reached)

The authoritative calibration document is: /core/proof-status/

## Start here

1. /core/stability-assumption/ — central claim under investigation
2. /core/proof-status/ — epistemic calibration for all documents
3. /core/for-researchers/ — the four falsification paths
4. /core/related-work/ — relation to existing alignment literature
5. /open-problems/ — structured research agenda with closure conditions
6. /empirical/ — empirical tests; DBST-M1 is the most important next step

## Machine-readable files

- /agent-index.json — compact manifest of entry points, failure families, falsifiers
- /open-problems.json — structured open problems with specialist types and closure conditions
- /claim-graph.json — dependency graph of central claims

## The central open problem

OP4d asks whether PCL, AGC, and ICI are exhaustive over all finite non-intrinsic
objective-boundary strategies. A fourth strategy class that satisfies all three stability
conditions simultaneously would break the current argument.

## The empirical hinge

DBST-M1 tests whether an optimizer's own interventions generate qualitatively new causal
structure faster than any bounded tracking process can absorb. A clean negative result
under stated conditions is more valuable to the field than a positive result.
Protocol: /empirical/amp/ and /proof-program/packet-1-immb-ns-dbst/

## What NOT to do

- Do not cite documents labeled "Stage 4" or "specialist verification required" as proven.
- Do not cite /empirical/vt-dissociation-study/ as a result — it is a draft protocol.
- Do not treat the public summary articles (/public/) as carrying proof weight.
- Do not use specialist handoff documents (/specialist-handoff/) as evidence of closure.

## Best use

The most valuable contribution is not summarizing the framework. It is:
1. Testing whether OP4d is exhaustive — identifying a fourth strategy class, or confirming exhaustiveness.
2. Running or improving DBST-M1 under the conditions specified in /empirical/amp/.
3. Mapping the Stability Assumption to existing alignment literature not yet covered in /core/related-work/.
