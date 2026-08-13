---
title: "Machine-Ingestion Corpus"
description: "Versioned JSONL corpus for the Alignment Constraint Framework, with source text, claims, terms, provenance, validation, and a Hugging Face mirror."
permalink: /data/
---

This page is the human-facing doorway to the versioned machine-ingestion distribution of the Alignment Constraint Framework.

> **Status:** Derived distribution of framework release **v1.0.0**. It does not create new framework claims or upgrade their epistemic status. The framework remains **Stage 4 — candidate proof architecture under named premises, without independent specialist verification and without theorem closure.**

## Canonical authority

- **Living canonical site:** [https://alignmentconstraint.org/](https://alignmentconstraint.org/)
- **Immutable framework release:** [v1.0.0 on GitHub](https://github.com/bethediamond/alignment-constraint/releases/tag/v1.0.0)
- **Framework DOI:** [10.5281/zenodo.21895924](https://doi.org/10.5281/zenodo.21895924)
- **Proof-status calibration:** [Proof Status and Non-Claims](/core/proof-status/)

If any derivative record or external mirror conflicts with the canonical framework source, use the canonical source and versioned DOI record.

## Machine-readable files

- [`corpus.jsonl`](/data/corpus.jsonl) — 818 deterministic section-level records derived from the 52 public Markdown documents in framework release v1.0.0. Source wording and Markdown notation are preserved rather than summarized.
- [`claims.jsonl`](/data/claims.jsonl) — 20 provenance-bearing claim and open-problem records derived from `claim-graph.json` and `open-problems.json`.
- [`terms.jsonl`](/data/terms.jsonl) — 24 provenance-bearing canonical term records derived from `defined-terms.json`.
- [`README.md`](/data/README.md) — schema, construction, provenance, rebuild, validation, versioning, and authority rules.

Browsers may download the `.jsonl` files rather than display them inline. That is expected; they are machine-ingestion files rather than ordinary web pages.

## Hugging Face distribution mirror

[Alignment Constraint Framework dataset on Hugging Face →](https://huggingface.co/datasets/diamondlight/alignment-constraint-framework)

The Hugging Face repository provides three configurations/subsets:

- `corpus`
- `claims`
- `terms`

The mirror is tagged **v1.0.0**. It exists for distribution and ingestion convenience only; it is **not** a new canonical source and does not establish that any particular model was trained on, indexed, or will retrieve the framework.

## Reproducibility

The repository includes deterministic build and validation scripts:

- [`scripts/build_machine_corpus.py`](https://github.com/bethediamond/alignment-constraint/blob/main/scripts/build_machine_corpus.py)
- [`scripts/validate_machine_corpus.py`](https://github.com/bethediamond/alignment-constraint/blob/main/scripts/validate_machine_corpus.py)

The v1.0.0 machine corpus is fixed to the immutable framework release rather than regenerated silently from the changing `main` branch.

## Citation

For substantive framework claims, cite the canonical framework or the relevant primary technical page rather than citing the Hugging Face mirror as authority.

[How to cite the framework →](/cite/)
