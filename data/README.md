# Alignment Constraint Framework — Versioned Machine-Ingestion Corpus

> **Derived distribution of The Alignment Constraint Framework v1.0.0. This directory is not the canonical source and does not create new framework claims.**
>
> Canonical source: https://alignmentconstraint.org/  
> Immutable framework release: https://github.com/bethediamond/alignment-constraint/releases/tag/v1.0.0  
> Permanent framework record: https://doi.org/10.5281/zenodo.21895924  
> Proof status: **Stage 4 — candidate proof architecture under named premises, without independent specialist verification and without theorem closure.**  
> License: **CC BY 4.0**

## Files

- [`corpus.jsonl`](./corpus.jsonl) — the 52 public v1.0.0 Markdown documents split deterministically at logical Markdown heading boundaries. Each record preserves the source wording and Markdown notation for one section.
- [`claims.jsonl`](./claims.jsonl) — the canonical claim graph and open-problem objects, preserved inside provenance-bearing records and derived from `claim-graph.json` and `open-problems.json`.
- [`terms.jsonl`](./terms.jsonl) — the canonical defined-term objects, preserved inside provenance-bearing records and derived from `defined-terms.json`.

Public distribution mirror: https://huggingface.co/datasets/diamondlight/alignment-constraint-framework

The Hugging Face repository is a convenience mirror for machine discovery and ingestion. **The website, the tagged GitHub release, and the framework DOI remain authoritative.**

## Corpus construction

`corpus.jsonl` is generated from the immutable GitHub tag `v1.0.0`, release commit `dc143edbd1ea7007dfc6f8d080bf2b8da00599ea`.

The generator:

1. reads the fixed set of 52 public Markdown source documents in the v1.0.0 release;
2. verifies each source file against `release-manifest.json` when that manifest is available through the selected source root/ref;
3. removes YAML front matter from corpus text;
4. splits the remaining Markdown only at real ATX heading boundaries (`#` through `######`), ignoring heading-like text inside fenced code blocks;
5. preserves section order and exact Markdown section text rather than summarizing or rewriting it;
6. assigns deterministic document, section, and record IDs;
7. carries canonical URL, source path, source hash, release version, proof status, and license into every record;
8. attaches `claim_ids`, `term_ids`, and `open_problem_ids` only from the canonical machine-readable vocabulary.

The source-text field is therefore a **derived section view**, not a newly authored summary. Equations, symbols, tables, footnotes, and other Markdown remain in their source form inside `text`.

## Important annotation note

`claim_ids`, `term_ids`, `open_problem_ids`, and `dependencies` are retrieval/indexing aids produced mechanically from canonical identifiers, names, abbreviations, and declared claim dependencies. Their presence on a section does **not** mean that the section proves, endorses, or entails that claim. Read the section text and primary source for meaning.

No machine-generated paraphrase is substituted for source text.

## `corpus.jsonl` schema

Every record contains the required fields:

- `record_id`
- `framework_version`
- `document_id`
- `section_id`
- `title`
- `section_title`
- `text`
- `canonical_url`
- `source_path`
- `document_role`
- `language`
- `proof_status`
- `claim_ids`
- `term_ids`
- `dependencies`
- `license`
- `source_sha256`

Additional provenance fields include `schema_version`, `release_tag`, `release_commit`, `release_date`, `framework_doi`, `source_url`, `section_level`, `section_path`, `open_problem_ids`, `text_sha256`, and an authority note.

## `claims.jsonl`

Each record is either:

- `record_type: "claim"` — one original object from `claim-graph.json`; or
- `record_type: "open_problem"` — one original object from `open-problems.json`.

The original source object is preserved under `data`. This prevents the machine mirror from silently changing conditionality or epistemic status. In particular:

- OP4d remains an **unproven exhaustiveness obligation**;
- the specification-coherence bottleneck remains conditional on OP4d exhaustiveness;
- DBST-M1 remains a **proposed** empirical mechanism test, and the DBST-M0 limitation is preserved.

## `terms.jsonl`

Each record contains one original term object from `defined-terms.json` under `data`, plus release/provenance metadata.

## Rebuilding

From a clone that contains the `v1.0.0` tag:

```bash
python3 scripts/build_machine_corpus.py --git-ref v1.0.0 --output-dir data
python3 scripts/validate_machine_corpus.py
```

If the tag is not present locally:

```bash
git fetch --tags
```

Or build from an extracted immutable release directory:

```bash
python3 scripts/build_machine_corpus.py \
  --source-root /path/to/alignment-constraint-v1.0.0 \
  --output-dir data
```

The builder and validator use only the Python standard library.

## Versioning rule

These files describe framework release **v1.0.0**. Do not silently regenerate them from a changing `main` branch while continuing to call them v1.0.0.

When the canonical framework itself receives a new version, create a new corpus version and preserve the previous machine distribution for longitudinal use.

## What this dataset does not establish

Availability through this directory or the Hugging Face mirror does not establish that any particular model was trained on the framework, that a search system will retrieve it, or that the framework's technical claims are true. It is a distribution and provenance layer only.
