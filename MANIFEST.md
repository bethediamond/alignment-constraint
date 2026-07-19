# Alignment Constraint Framework — Master Manifest

This is the control document for the archive build. Every artifact in the framework is listed
with its authoritative source, its destination path in the GitHub archive, its publication
status, its intended audience, and which object is canonical for citation.

**Source-of-truth hierarchy** (agreed):
1. Published Medium text — final authority for wording and navigation on published articles
2. Local REVISED Markdown files — clean base for the machine-readable archive (tables already in Markdown, not images)
3. Medium pages — used only to detect final edits, not as extraction source
4. GitHub simulations (`bethediamond.github.io`) — canonical for toys; do not migrate
5. OSF pages — canonical for public experiment records
6. Uploaded `.docx`/`.md` handoffs — source of truth for unpublished specialist material

**Legend — Status:** `published` (live on Medium) · `forthcoming` (written, not yet on Medium) · `draft-gated` (not ready to file/cite; behind gateway) · `external-live` (already public at its own URL)
**Legend — Tier:** `T1 public` · `T2 core/field-facing` · `T3 series` · `T4 empirical` · `T5 specialist-handoff`

---

## Tier 1 — Public summaries (top of funnel)

| Title | Source file | Medium URL | GitHub path | Status | Audience |
|---|---|---|---|---|---|
| Redefining Rationality | *export from Medium* | /redefining-rationality-cab469cc5b6c | `public/redefining-rationality.md` | published | general / origin |
| The AI Race Is Not Rational | *export from Medium* | /the-ai-race-is-not-rational-9a83d6d0940c | `public/ai-race-is-not-rational.md` | published | general (summarizes S1–3) |
| We're Winning the Wrong Race | *export from Medium* | /were-winning-the-wrong-race-9ef38b061cfa | `public/winning-the-wrong-race.md` | published | general (summarizes S1–2) |
| The OP4d Counterexample Challenge | *export from Medium* | /the-op4d-counterexample-challenge-bc8d9cc5d8e7 | `public/op4d-counterexample-challenge.md` | published | technical critics |

*These four have no local Markdown. Export from Medium during build. They are the primary doorways — place in `/public/`, not buried in `/core/`.*

---

## Tier 2 — Core / field-facing

| Title | Source file | Medium URL | GitHub path | Status | Audience |
|---|---|---|---|---|---|
| The Alignment Constraint (Doc 0 / hub) | `document0_REVISED_v2_n_.md` | /the-alignment-constraint-ebed3f6c4eae | `core/alignment-constraint.md` | published | all / framework map |
| The Stability Assumption (LW entry) | `lesswrong_post_REVISED_v2_n_.md` | /the-stability-assumption-b5dbdcfa6a2c | `core/stability-assumption.md` | published | alignment researchers |
| OP4 paper (full) | `OP4_paper_REVISED_v2_n_.md` | /op4-the-stability-assumption-e19955599adb | `core/stability-assumption-full.md` | published | researchers / OSF+arXiv base |
| Field-Facing Bridge | `field_facing_bridge_REVISED_v2_n_.md` | /when-better-objectives-are-not-enough-...-ae83b1322b01 | `core/field-facing-bridge.md` | published | researchers |
| Proof Status and Non-Claims | `proof_status_REVISED_v2_n_.md` | /what-this-framework-claims-and-what-it-does-not-fecca0c7901a | `core/proof-status.md` | published | all / calibration |
| The Tightening Sequence | `tightening_sequence_REVISED_v2_n_.md` | /the-tightening-sequence-e8e96de8fef5 | `core/tightening-sequence.md` | published | researchers |
| For Researchers: The Claim to Break | *drafted in build* | — | `core/for-researchers.md` | forthcoming | researchers / outreach |

---

## Proof program (bridges T2 and T5 — field-facing but technical)

| Title | Source file | Medium URL | GitHub path | Status | Audience |
|---|---|---|---|---|---|
| OP4d: The Exhaustiveness Obligation | `OP4d_technical_note_REVISED_v2_n_.md` | /op4d-the-exhaustiveness-obligation-e5710071f066 | `proof-program/op4d-exhaustiveness-obligation.md` | published | technical critics |
| OP4d: Candidate Normal Form | `OP4d_normalform_REVISED_v2_n_.md` | /op4d-candidate-normal-form-specialist-verification-bd29a48283d4 | `proof-program/op4d-candidate-normal-form.md` | published | specialists |
| Packet 1: IMMB-NS + DBST | `Packet1_REVISED_v2_n_.md` | /packet-1-immb-ns-verification-...-778576bbe999 | `proof-program/packet-1-immb-ns-dbst.md` | published | specialists / empirical |

---

## Tier 3 — Series 1: Alignment as Structural Necessity

| Title | Source file | Medium URL | GitHub path | Status |
|---|---|---|---|---|
| Introduction | `S1_introduction_REVISED_v2_n_.md` | /i-alignment-as-structural-necessity-07e38568754f | `series-1/introduction.md` | published |
| The Alignment of Intelligence | `S1_article01_REVISED_v4_n_.md` | /ii-the-alignment-of-intelligence-187b09d2f902 | `series-1/alignment-of-intelligence.md` | published |
| What Aligned Intelligence Converges Toward | `S1_article02_REVISED_v2_n_.md` | /iii-what-does-aligned-intelligence-...-2fd726374363 | `series-1/system-aware-attractor.md` | published |
| The Crossing | `S1_article03_REVISED_v3_n_.md` | /iv-the-crossing-fba00eed5d1a | `series-1/the-crossing.md` | published |
| TC1: The System-Aware Attractor | `TC1_REVISED_v2_n_.md` | /v-the-system-aware-attractor-c749f984b842 | `series-1/technical-companion.md` | published |

## Tier 3 — Series 2: The Architecture of Thriving

| Title | Source file | Medium URL | GitHub path | Status |
|---|---|---|---|---|
| Introduction | `S2_introduction_REVISED_v2_n_.md` | /i-the-architecture-of-thriving-b3617a28ba0e | `series-2/introduction.md` | published |
| The Invariant Drive | `S2_article01_REVISED.md` | /the-invariant-drive-cec5a3eaa22a | `series-2/invariant-drive.md` | published |
| The Depth Constraint | `S2_article02_REVISED_v2_n_.md` | /the-depth-constraint-04c5b71aad5b | `series-2/depth-constraint.md` | published |
| The Inner Crossing | `S2_article03_REVISED_v2_n_.md` | /the-inner-crossing-abafa53fe508 | `series-2/inner-crossing.md` | published |
| The Shape of What Does Not End | `S2_article04_REVISED_v2_n_.md` | /the-shape-of-what-does-not-end-aee2dda478cc | `series-2/shape-of-what-does-not-end.md` | published |
| TC2: The Valence Constraint | `TC2_REVISED_v2_n_.md` | /the-valence-constraint-4b7b4656f433 | `series-2/technical-companion.md` | published |

## Tier 3 — Series 3: The Interior of What Does Not End

| Title | Source file | Medium URL | GitHub path | Status |
|---|---|---|---|---|
| Introduction | `S3_Introduction_REVISED.md` | /the-interior-of-what-does-not-end-b9d84c83da67 | `series-3/introduction.md` | published |
| Part 1: The Participating Structure | `S3_Part1_REVISED.md` | /the-interior-of-what-does-not-end-5a4f93d553b2 | `series-3/participating-structure.md` | published |
| Part 2: The Navigation | `S3_Part2_REVISED.md` | /the-interior-of-what-does-not-end-2269a4bf8dae | `series-3/navigation.md` | published |
| Part 3: The Resolution | `S3_Part3_REVISED.md` | /the-interior-of-what-does-not-end-3b549a30aabd | `series-3/resolution.md` | published |
| Part 4: The Asymptote | `S3_Part4_REVISED__n2_.md` | /the-interior-of-what-does-not-end-db845147a946 | `series-3/asymptote.md` | published |
| The Convergence Map | `S3_Convergence_Map_REVISED.md` | /the-convergence-map-e2e482e9fbfa | `series-3/convergence-map.md` | published |
| Epistemic Status Map | `S3_Epistemic_Status_Map_REVISED.md` | /epistemic-status-map-...-fb182c665eed | `series-3/epistemic-status-map.md` | published |
| Apophatic Discipline Framework | `Apophatic_Framework_REVISED.md` | /apophatic-discipline-framework-72fde3440158 | `series-3/apophatic-discipline-framework.md` | published |
| TC3: The Interior Constraint | `TC3_REVISED.md` | /the-interior-constraint-a-formal-sketch-2f29933db062 | `series-3/technical-companion.md` | published |

---

## Tier 4 — Empirical

| Title | Source | URL | GitHub path | Status |
|---|---|---|---|---|
| AMP (Experimental Companion) | `AMP_REVISED_v2_n_.md` | Medium /experimental-companion-...-1afb2dd0f1de | `empirical/amp.md` | published |
| Completion Recognition (OSF) | OSF record | osf.io/xpsf2 | linked from `empirical/index.md` | external-live |
| DBST-M0 (OSF) | OSF record | osf.io/fpvmy | linked from `empirical/index.md` | external-live |
| Scaled Matched-Signal Replication (OSF) | OSF record | osf.io/8tr92 | linked from `empirical/index.md` | external-live |
| DRG Frame-Manipulation Preregistration | `DRG_replication_preregistration_REVISED.md` (uploaded) | — | `empirical/drg-frame-manipulation-preregistration.md` | draft-gated (prospective; label clearly) |
| V(t) Dissociation Study | `Vt_dissociation_REVISED.md` (uploaded) | — | `empirical/vt-dissociation-study.md` | draft-gated (NOT ready to file) |
| Experiments to Run (index) | *compile in build* | — | `empirical/experiments-to-run.md` | forthcoming |

**Note:** The DRG document reports a preregistered criterion that was *not met* (CI excluded zero in only 1 of 3 models). This honestly-reported null is a credibility asset — label it "prospective design; prior null reported," not "result."

---

## Tier 5 — Specialist handoff (behind gateway; crawlable, not promoted)

| Title | Source (uploaded) | GitHub path | Status |
|---|---|---|---|
| Gateway / Verification Agenda | *drafted in build* | `specialist-handoff/index.md` | forthcoming |
| Phases 1–7 Formal Proof Handoff | `AI_Alignment_Framework_Formal_Proof_Handoff_Phases_1-7_Stage4_Complete.docx` | `specialist-handoff/phases-1-7-formal-proof-handoff.md` | draft-gated |
| Proof Artifacts — Locked Results v2 | `_S2_ProofArtifacts_LockedResults_v2.docx` | `specialist-handoff/proof-artifacts-locked-results.md` | draft-gated |
| Five-Problems Stage-4 Handoff | `Proof_Handoff_5-problems__Stage_4_q2_.docx` | `specialist-handoff/five-problems-stage-4-handoff.md` | draft-gated |
| B1 Audit Regress Handoff | `B1_Closure_Handoff.docx` | `specialist-handoff/b1-audit-regress-handoff.md` | draft-gated |
| B2 Closure Handoff Summary | `B2_Closure_Handoff_Summary.md` (uploaded) | `specialist-handoff/b2-governance-bifurcation-handoff.md` | draft-gated |
| Candidate 3: Passive Extraction | `Candidate3_Passive_Extraction_Handoff.md` (uploaded) | `specialist-handoff/passive-extraction-handoff.md` | draft-gated |

**All Tier 5 documents self-label "Stage 4 / LLM ceiling / nothing herein should be cited as proven."** The gateway page must frame this as epistemic discipline *before* a reader reaches any raw handoff.

---

## Toys (external-live; link, do not migrate)

| Toy | URL | Status |
|---|---|---|
| Toy 1 (S1) | bethediamond.github.io/ai-alignment-simulation/toy_01.html | external-live |
| Toy 2 (S1) | bethediamond.github.io/ai-alignment-attractor/toy_02.html | external-live |
| Toy 3 (S1) | bethediamond.github.io/ai-alignment-crossing/toy_03.html | external-live |
| Toy 4 (S2) | bethediamond.github.io/ai-alignment-tracer/toy_04.html | external-live |
| Toy 5 (S2) | bethediamond.github.io/ai-alignment-proxy/toy_05.html | external-live |
| Toy 6 (S2) | bethediamond.github.io/ai-alignment-phase/toy_06.html | external-live |
| Toy 7 (S2) | bethediamond.github.io/ai-alignment-landscape/toy_07.html | external-live |
| Toy 8 (S3) | bethediamond.github.io/ai-alignment-contradiction/toy_08.html | forthcoming (confirm public) |
| Toy 9 (S3) | bethediamond.github.io/ai-alignment-boundary/toy_09.html | forthcoming (confirm public) |

---

## Citation objects (created during build)

| Object | Covers | DOI source |
|---|---|---|
| OSF preprint | OP4 / Stability Assumption paper | OSF (Phase 3) |
| Zenodo release v1.0 | Full framework archive | Zenodo/GitHub (Phase 3) |
| arXiv note | Narrow technical version of OP4 | arXiv (Phase 4) |

---

## Build sequence (unchanged from agreed plan)
1. This manifest ← **done**
2. Convert 4 `.docx` handoffs → Markdown
3. Draft framing pages (homepage, gateway, llms.txt, for-researchers)
4. Reconcile local Markdown against Medium (edit pass), add archive headers + relative nav
5. Assemble repo, enable Pages, custom domain, robots.txt, sitemaps, CITATION.cff, /cite/
6. OSF preprint (cites the 3 live OSF records) → Zenodo DOI
7. arXiv narrow note (endorser if needed)
8. Outreach: 3-link packet
