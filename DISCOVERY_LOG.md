# Discovery Log

This public log tracks discovery, indexing, citation, and retrieval outcomes for the
Alignment Constraint Framework.

**Canonical site:** https://alignmentconstraint.org/  
**Repository:** https://github.com/bethediamond/alignment-constraint  
**Framework version:** 1.0.0

> This is a discovery-and-retrieval log, not evidence that any model was trained on the
> framework. Do not record private conversations, sensitive personal data, or information
> that should not be public.

| Date | Platform/system | Test type or action | Query/URL | Source cited | Proof status preserved? | Result/error | Recheck date |
|---|---|---|---|---|---|---|---|
| 2026-08-12 | Google Search Console | Sitemap submission | https://alignmentconstraint.org/sitemap.xml | — | N/A | Sitemap submitted to the verified domain property; indexing coverage pending. | 2026-08-14 |
| 2026-08-12 | Bing Webmaster Tools | URL inspection / stored status | https://alignmentconstraint.org/public/op4d-counterexample-challenge/ | — | N/A | Bing reported “Discovered but not crawled.” | 2026-08-14 |
| 2026-08-12 | Bing Webmaster Tools | Live URL test | https://alignmentconstraint.org/public/op4d-counterexample-challenge/ | — | N/A | Live URL reported that the page can be indexed by Bing. JSON-LD and OpenGraph were detected. One SEO/GEO issue was reported: meta description too long or too short. Site-wide metadata was subsequently revised; recheck after the new GitHub Pages deployment is live. | 2026-08-14 |
| 2026-08-12 | Google Scholar | Scholarly discovery check | The Stability Assumption: Specification-Coherence Limits in Separable Objective Alignment | — | N/A | Work was not yet available to select/add from Google Scholar indexing. | 2026-08-26 |
| 2026-08-12 | Zenodo / DOI | DOI resolution check | https://doi.org/10.5281/zenodo.21895924 | Zenodo | Yes | Framework DOI resolves. Search-engine and scholarly-index discovery remain separate checks. | 2026-08-26 |
| 2026-08-12 | Zenodo / DOI | DOI resolution check | https://doi.org/10.5281/zenodo.21895992 | Zenodo | Yes | OP4 / Stability Assumption DOI resolves. Google Scholar indexing not yet observed. | 2026-08-26 |
| 2026-08-12 | Canonical GitHub/site archive | Machine-ingestion corpus publication | https://alignmentconstraint.org/data/ | Canonical v1.0.0 release | Yes | Published deterministic v1.0.0 machine corpus: 818 section records, 20 claim/open-problem records, and 24 term records; archive and corpus validation passed. | 2026-08-26 |
| 2026-08-12 | Hugging Face | Dataset mirror publication/versioning | https://huggingface.co/datasets/diamondlight/alignment-constraint-framework | Canonical site + v1.0.0 release | Yes | Public distribution mirror recognizes corpus, claims, and terms configurations; tag v1.0.0 points to mirror commit 7ae62cda75a993d81b881f4a6fc7eec7a2204b90. Mirror is non-canonical. | 2026-08-26 |
| 2026-08-21 | GitHub Pages | Series 3 interactive-companion publication | https://bethediamond.github.io/ai-alignment-contradiction/companion_08.html | Series 3 Part 1 + Toy 8 repository | Yes | Repository made public and `companion_08.html` published; canonical routing synchronized. Verify Pages deployment after commit. | 2026-08-22 |
| 2026-08-21 | GitHub Pages | Series 3 interactive-companion publication | https://bethediamond.github.io/ai-alignment-boundary/companion_09.html | Series 3 Part 4 + Toy 9 repository | Yes | Repository made public and `companion_09.html` published; canonical routing synchronized. Verify Pages deployment after commit. | 2026-08-22 |

## Items to record next

Add rows when any of the following occurs:

- Google indexes or rejects a priority URL.
- Bing crawls or indexes a priority URL.
- Bing Site Scan reports a site-wide issue.
- IndexNow successfully submits changed canonical URLs.
- Google Scholar indexes the OP4 paper.
- Semantic Scholar indexes the OP4 paper or creates an author record.
- ChatGPT, Bing/Copilot, or another search-enabled AI cites the framework.
- A system cites a non-canonical source when a canonical source exists.
- A system materially overstates or understates the Stage 4 proof status.
- An external site links to the framework.
- A retrieval/application test from `DISCOVERY_TESTS.md` is run.

## Recheck cadence

Use the same general schedule after an indexing or discovery submission:

- approximately 48 hours;
- approximately 1 week;
- approximately 1 month;
- quarterly thereafter.

Do not repeatedly resubmit the same URL merely because it has not appeared yet.
