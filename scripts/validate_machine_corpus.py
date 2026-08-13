#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, sys, tempfile
from pathlib import Path
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'
VERSION='1.0.0'; TAG='v1.0.0'; LICENSE='CC BY 4.0'
PROOF='Stage 4 — candidate proof architecture under named premises, without independent specialist verification and without theorem closure.'
HOST='alignmentconstraint.org'
EXPECTED_CLAIMS={'stability_assumption','owt_conditions','substrate_constraint','valence_viability_constraint','pcl','agc','ici','op4d','specification_coherence_argument','dbst_m1','cot','nad'}
EXPECTED_OPEN={'OP4d','DBST-M1','B1','OP2','Vt_dissociation','DRG_mechanism','OP-S3-1','OP-S3-3'}
EXPECTED_TERMS={'alignment-constraint-framework','stability-assumption','specification-coherence','finite-separable-objective','o-owt','pcl','agc','ici','op4','op4d','substrate-constraint','valence-viability-constraint','v-t','phi','psi','svg','dbst-m0','dbst-m1','nad','gdc','cmr','cot','mch','stage-4'}
EXPECTED_SOURCES = set('''index.md
open-problems/index.md
apply/index.md
core/for-researchers.md
core/related-work.md
core/glossary.md
empirical/index.md
toys/index.md
cite/index.md
specialist-handoff/index.md
public/redefining-rationality.md
public/ai-race-is-not-rational.md
public/winning-the-wrong-race.md
public/op4d-counterexample-challenge.md
core/alignment-constraint.md
core/stability-assumption.md
core/stability-assumption-full.md
core/field-facing-bridge.md
core/proof-status.md
core/tightening-sequence.md
proof-program/op4d-exhaustiveness-obligation.md
proof-program/op4d-candidate-normal-form.md
proof-program/packet-1-immb-ns-dbst.md
series-1/introduction.md
series-1/alignment-of-intelligence.md
series-1/aligned-intelligence-converges-toward.md
series-1/the-crossing.md
series-1/technical-companion.md
series-2/introduction.md
series-2/invariant-drive.md
series-2/depth-constraint.md
series-2/inner-crossing.md
series-2/shape-of-what-does-not-end.md
series-2/technical-companion.md
series-3/introduction.md
series-3/participating-structure.md
series-3/navigation.md
series-3/resolution.md
series-3/asymptote.md
series-3/convergence-map.md
series-3/epistemic-status-map.md
series-3/apophatic-discipline-framework.md
series-3/technical-companion.md
empirical/amp.md
empirical/drg-frame-manipulation-preregistration.md
empirical/vt-dissociation-study.md
specialist-handoff/b1-audit-regress-handoff.md
specialist-handoff/b2-governance-bifurcation-handoff.md
specialist-handoff/passive-extraction-handoff.md
specialist-handoff/proof-artifacts-locked-results.md
specialist-handoff/five-problems-stage-4-handoff.md
specialist-handoff/phases-1-7-formal-proof-handoff.md'''.splitlines())
CORPUS_REQUIRED={'record_id','framework_version','document_id','section_id','title','section_title','text','canonical_url','source_path','document_role','language','proof_status','claim_ids','term_ids','dependencies','license','source_sha256','text_sha256','release_tag'}
DERIVED_REQUIRED={'record_id','framework_version','record_type','proof_status','license','release_tag','source_file','source_sha256','data'}
BAD_PATH_PARTS={'draft','drafts','private','staging','preview','unreviewed-translation'}

def sha(text:str): return hashlib.sha256(text.encode('utf-8')).hexdigest()
def load_jsonl(path:Path):
    errors=[]; recs=[]
    if not path.exists(): return [],[f'missing file: {path.relative_to(ROOT)}']
    try: text=path.read_text(encoding='utf-8-sig')
    except Exception as e: return [],[f'{path}: not valid UTF-8: {e}']
    for n,line in enumerate(text.splitlines(),1):
        if not line.strip():
            errors.append(f'{path.relative_to(ROOT)}:{n}: blank JSONL line')
            continue
        try: obj=json.loads(line)
        except Exception as e:
            errors.append(f'{path.relative_to(ROOT)}:{n}: invalid JSON: {e}'); continue
        if not isinstance(obj,dict): errors.append(f'{path.relative_to(ROOT)}:{n}: record must be object'); continue
        recs.append(obj)
    return recs,errors

def validate_common(rec,required,label,errors):
    miss=sorted(required-set(rec))
    if miss: errors.append(f'{label}: missing fields: {", ".join(miss)}')
    if rec.get('framework_version')!=VERSION: errors.append(f'{label}: framework_version must be {VERSION}')
    if rec.get('release_tag')!=TAG: errors.append(f'{label}: release_tag must be {TAG}')
    if rec.get('license')!=LICENSE: errors.append(f'{label}: license must be {LICENSE}')
    if rec.get('proof_status')!=PROOF: errors.append(f'{label}: exact Stage 4 proof status missing or changed')

def main():
    errors=[]; warnings=[]
    corpus,e=load_jsonl(DATA/'corpus.jsonl'); errors+=e
    claims,e=load_jsonl(DATA/'claims.jsonl'); errors+=e
    terms,e=load_jsonl(DATA/'terms.jsonl'); errors+=e
    ids=set()
    sources=set()
    for i,r in enumerate(corpus,1):
        label=f'corpus record {i} ({r.get("record_id","?")})'; validate_common(r,CORPUS_REQUIRED,label,errors)
        rid=r.get('record_id')
        if rid in ids: errors.append(f'{label}: duplicate record_id')
        ids.add(rid)
        if not isinstance(r.get('text'),str) or not r.get('text','').strip(): errors.append(f'{label}: text must be non-empty')
        elif r.get('text_sha256')!=sha(r['text']): errors.append(f'{label}: text_sha256 mismatch')
        u=urlparse(str(r.get('canonical_url','')))
        if u.scheme!='https' or u.netloc!=HOST: errors.append(f'{label}: invalid canonical_url {r.get("canonical_url")!r}')
        sp=str(r.get('source_path','')); sources.add(sp)
        if sp not in EXPECTED_SOURCES: errors.append(f'{label}: unexpected/non-public source_path {sp!r}')
        if any(part.casefold() in BAD_PATH_PARTS for part in Path(sp).parts): errors.append(f'{label}: draft/private path forbidden: {sp}')
        for fld in ('claim_ids','term_ids','dependencies'):
            if not isinstance(r.get(fld),list): errors.append(f'{label}: {fld} must be a list')
        if isinstance(r.get('claim_ids'),list):
            bad=set(r['claim_ids'])-EXPECTED_CLAIMS
            if bad: errors.append(f'{label}: invented/unknown claim_ids {sorted(bad)}')
        if isinstance(r.get('term_ids'),list):
            bad=set(r['term_ids'])-EXPECTED_TERMS
            if bad: errors.append(f'{label}: invented/unknown term_ids {sorted(bad)}')
        src=ROOT/sp
        if not src.exists(): warnings.append(f'{label}: current-main path missing locally: {sp} (release provenance still points to v1.0.0)')
    if sources!=EXPECTED_SOURCES:
        missing=sorted(EXPECTED_SOURCES-sources); extra=sorted(sources-EXPECTED_SOURCES)
        if missing: errors.append('corpus missing public v1.0.0 sources: '+', '.join(missing))
        if extra: errors.append('corpus has extra sources: '+', '.join(extra))
    if len(corpus)<len(EXPECTED_SOURCES): errors.append('corpus has fewer records than public source documents')

    claim_ids=set(); open_ids=set(); derived_ids=set()
    for i,r in enumerate(claims,1):
        label=f'claims record {i} ({r.get("record_id","?")})'; validate_common(r,DERIVED_REQUIRED,label,errors)
        rid=r.get('record_id')
        if rid in derived_ids: errors.append(f'{label}: duplicate record_id')
        derived_ids.add(rid)
        data=r.get('data') if isinstance(r.get('data'),dict) else {}
        typ=r.get('record_type')
        if typ=='claim': claim_ids.add(data.get('id'))
        elif typ=='open_problem': open_ids.add(data.get('id'))
        else: errors.append(f'{label}: record_type must be claim or open_problem')
    if claim_ids!=EXPECTED_CLAIMS: errors.append(f'claim set mismatch: expected {sorted(EXPECTED_CLAIMS)}, got {sorted(x for x in claim_ids if x)}')
    if open_ids!=EXPECTED_OPEN: errors.append(f'open-problem set mismatch: expected {sorted(EXPECTED_OPEN)}, got {sorted(x for x in open_ids if x)}')
    by_claim={r.get('data',{}).get('id'):r.get('data',{}) for r in claims if r.get('record_type')=='claim'}
    if 'exhaustiveness unproven' not in by_claim.get('op4d',{}).get('status','').casefold(): errors.append('OP4d status no longer says exhaustiveness unproven')
    sc=by_claim.get('specification_coherence_argument',{})
    if 'op4d' not in [str(x).casefold() for x in sc.get('depends_on',[])]: errors.append('specification-coherence claim lost OP4d dependency')
    if 'if' not in sc.get('status','').casefold() or 'exhaustive' not in sc.get('status','').casefold(): errors.append('specification-coherence claim lost conditional OP4d status')
    db=by_claim.get('dbst_m1',{})
    if 'proposed' not in db.get('status','').casefold() or 'did not isolate' not in db.get('status','').casefold(): errors.append('DBST-M1 record lost proposed status or DBST-M0 limitation')

    term_ids=set(); tids=set()
    for i,r in enumerate(terms,1):
        label=f'terms record {i} ({r.get("record_id","?")})'; validate_common(r,DERIVED_REQUIRED,label,errors)
        rid=r.get('record_id')
        if rid in tids: errors.append(f'{label}: duplicate record_id')
        tids.add(rid)
        if r.get('record_type')!='term': errors.append(f'{label}: record_type must be term')
        data=r.get('data') if isinstance(r.get('data'),dict) else {}
        term_ids.add(data.get('id'))
    if term_ids!=EXPECTED_TERMS: errors.append(f'term set mismatch: expected {sorted(EXPECTED_TERMS)}, got {sorted(x for x in term_ids if x)}')

    # Optional deterministic byte-for-byte rebuild if immutable tag is available locally.
    try:
        ok=subprocess.run(['git','-C',str(ROOT),'cat-file','-e',f'{TAG}^{{commit}}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0
    except Exception: ok=False
    if ok:
        builder=ROOT/'scripts'/'build_machine_corpus.py'
        if builder.exists():
            with tempfile.TemporaryDirectory() as td:
                p=subprocess.run([sys.executable,str(builder),'--git-repo',str(ROOT),'--git-ref',TAG,'--output-dir',td],capture_output=True,text=True)
                if p.returncode!=0: errors.append('deterministic rebuild failed: '+(p.stderr.strip() or p.stdout.strip()))
                else:
                    for name in ('corpus.jsonl','claims.jsonl','terms.jsonl'):
                        rebuilt=Path(td)/name; committed=DATA/name
                        if rebuilt.read_bytes()!=committed.read_bytes(): errors.append(f'deterministic rebuild mismatch for data/{name}')
        else: errors.append('scripts/build_machine_corpus.py missing; cannot perform available deterministic rebuild')
    else:
        warnings.append(f'local checkout does not contain tag {TAG}; skipped optional byte-for-byte rebuild check (no network request made)')

    if warnings:
        print('Machine-corpus validator warnings:')
        for w in warnings: print('  - '+w)
    if errors:
        print('Machine-corpus validation: FAIL')
        for e in errors: print('  ERROR: '+e)
        return 1
    print(f'Machine-corpus validation: PASS — {len(corpus)} corpus records, {len(claims)} claim/open-problem records, {len(terms)} term records, {len(sources)} public source documents.')
    return 0
if __name__=='__main__': raise SystemExit(main())
