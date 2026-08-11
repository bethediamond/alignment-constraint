# Archive QC — beginner instructions

This folder package adds an automatic safety check to the Alignment Constraint Framework repository.

It **does not change your website or files**. It only reads the repository and reports problems.

## Files in this package

Upload these three files to the same paths shown inside the ZIP:

```text
scripts/validate_archive.py
.github/workflows/archive-qc.yml
ARCHIVE_QC_README.md
```

The first two are the functional files. This README is only for your reference.

---

## What happens after you upload them

Every time you:

- commit a change to GitHub; or
- open or update a pull request,

GitHub automatically runs **Archive QC**.

The validator does not visit the internet. It checks the files that GitHub has just checked out.

It uses only Python that is already available on the GitHub-hosted Ubuntu runner, so there is no separate package-install step.

---

## What a green check means

A **green check** means the automatic validator did not find any of the problems it is designed to detect.

It checks:

- public Markdown pages have well-formed front matter in the simple format this archive uses;
- public page permalinks are unique;
- JSON files parse correctly;
- `sitemap.xml` parses as XML;
- `sitemap.xml` and `sitemap.txt` point to local canonical pages and contain the same URL set;
- internal Markdown links point to a page or file that exists in the repository;
- known forbidden build placeholders are gone;
- common Medium-export artifacts are gone;
- front matter has not collapsed onto one line;
- a page does not repeat the same title as both its front-matter title and first body H1;
- Markdown and HTML images have non-empty alt text;
- known obsolete archive paths are not used;
- the major routing/calibration files contain Stage 4 status plus non-closure/candidate language.

A green check is **not** a mathematical or scientific verification of the framework. It only means the repository passed these mechanical archive-quality checks.

A green check also does not prove that every external website link works, because this push-time validator deliberately makes no internet requests.

---

## What a red X means

A **red X** means the validator found one or more concrete repository problems.

Nothing is automatically changed.

### How to see the problem

1. Open your GitHub repository.
2. Click **Actions** near the top.
3. Click the most recent **Archive QC** run.
4. Click **Check archive quality**.
5. Open **Run archive validator**.
6. Scroll to the red error messages.

The errors are written in plain English and normally show the filename and line number.

Example of the kind of message you may see:

```text
ERROR [duplicate title/H1] core/example.md:12 — first body H1 duplicates the front-matter title and may render twice
```

### What to do next

Copy the complete red error message into ChatGPT and say:

> The Alignment Constraint Archive QC workflow failed with this exact error. Please tell me what it means and create only the corrected replacement file. Do not change substantive framework claims.

Upload the corrected file to the same GitHub path.

GitHub will automatically run Archive QC again.

---

## Authorized DOI placeholders

The repository is still in Session 4, so pending DOI fields may legitimately exist until the real scholarly records are created.

The validator therefore does **not** treat the planned OSF/Zenodo DOI fields as forbidden build placeholders.

Once the real DOI records are created, those fields should be replaced as part of the citation session.

---

## About YAML/front-matter checking

The archive currently uses simple Jekyll front matter: root-level fields such as `title`, `permalink`, and `description`.

To keep this quality check fully offline and dependency-free, the validator checks that conservative front-matter format itself. The normal GitHub Pages/Jekyll build remains the final parser for YAML and site generation.

If you later introduce complex nested YAML into front matter, update the validator at that time rather than weakening the current check.

---

## What this validator deliberately does NOT do

It does not:

- edit files;
- rewrite prose;
- change claims;
- decide whether an argument is correct;
- make external web requests;
- check whether Medium, OSF, Zenodo, or other external links are currently online;
- determine whether Google, Bing, ChatGPT, or another system has indexed the site.

Those are separate live-site and discovery checks.

---

## Running it yourself is optional

You do not need to run Python on your own computer.

GitHub will run the check for you automatically.

If you ever do want to run it locally from the repository root, use:

```text
python3 scripts/validate_archive.py
```

A successful local run ends with:

```text
RESULT: PASS
```

A failed local run ends with:

```text
RESULT: FAIL
```

---

## The simple rule

**Green check:** continue.

**Red X:** open the error, fix only what it identifies, and let GitHub run the check again.
