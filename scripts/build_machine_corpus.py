#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, tempfile
from pathlib import Path
from urllib.parse import urlparse

FRAMEWORK='The Alignment Constraint Framework'
FRAMEWORK_VERSION='1.0.0'
RELEASE_TAG='v1.0.0'
RELEASE_COMMIT='dc143edbd1ea7007dfc6f8d080bf2b8da00599ea'
RELEASE_DATE='2026-08-12'
FRAMEWORK_DOI='10.5281/zenodo.21895924'
CANONICAL_BASE='https://alignmentconstraint.org'
REPOSITORY='https://github.com/bethediamond/alignment-constraint'
LICENSE='CC BY 4.0'
PROOF_STATUS='Stage 4 — candidate proof architecture under named premises, without independent specialist verification and without theorem closure.'
SCHEMA_VERSION='1.0'

PUBLIC_SOURCE_PATHS = [
'index.md','open-problems/index.md','apply/index.md','core/for-researchers.md','core/related-work.md','core/glossary.md','empirical/index.md','toys/index.md','cite/index.md','specialist-handoff/index.md','public/redefining-rationality.md','public/ai-race-is-not-rational.md','public/winning-the-wrong-race.md','public/op4d-counterexample-challenge.md','core/alignment-constraint.md','core/stability-assumption.md','core/stability-assumption-full.md','core/field-facing-bridge.md','core/proof-status.md','core/tightening-sequence.md','proof-program/op4d-exhaustiveness-obligation.md','proof-program/op4d-candidate-normal-form.md','proof-program/packet-1-immb-ns-dbst.md','series-1/introduction.md','series-1/alignment-of-intelligence.md','series-1/aligned-intelligence-converges-toward.md','series-1/the-crossing.md','series-1/technical-companion.md','series-2/introduction.md','series-2/invariant-drive.md','series-2/depth-constraint.md','series-2/inner-crossing.md','series-2/shape-of-what-does-not-end.md','series-2/technical-companion.md','series-3/introduction.md','series-3/participating-structure.md','series-3/navigation.md','series-3/resolution.md','series-3/asymptote.md','series-3/convergence-map.md','series-3/epistemic-status-map.md','series-3/apophatic-discipline-framework.md','series-3/technical-companion.md','empirical/amp.md','empirical/drg-frame-manipulation-preregistration.md','empirical/vt-dissociation-study.md','specialist-handoff/b1-audit-regress-handoff.md','specialist-handoff/b2-governance-bifurcation-handoff.md','specialist-handoff/passive-extraction-handoff.md','specialist-handoff/proof-artifacts-locked-results.md','specialist-handoff/five-problems-stage-4-handoff.md','specialist-handoff/phases-1-7-formal-proof-handoff.md']

CLAIM_ALIASES = {
'stability_assumption':['Stability Assumption'],
'owt_conditions':['O_OWT','Open-World Transformative'],
'substrate_constraint':['Substrate Constraint'],
'valence_viability_constraint':['Valence Viability Constraint','VVC'],
'pcl':['PCL','Proxy-Convergence Lemma','Proxy-Convergence'],
'agc':['AGC','Adaptive Gradient Complexity','dynamic screening instability'],
'ici':['ICI','Informational-Causal Incompatibility'],
'op4d':['OP4d'],
'specification_coherence_argument':['specification coherence','specification-coherence'],
'dbst_m1':['DBST-M1','Dynamic Blanket Stress Test M1','Dynamic Blanket Stress Test — M1'],
'cot':['Collective Optimality Theorem','COT'],
'nad':['Non-Substitutability of Traversal','NAD'],
}


def sha256_bytes(data: bytes) -> str: return hashlib.sha256(data).hexdigest()
def sha256_text(text: str) -> str: return sha256_bytes(text.encode('utf-8'))

def git_show(repo: Path, ref: str, path: str) -> bytes:
    return subprocess.check_output(['git','-C',str(repo),'show',f'{ref}:{path}'])

class Source:
    def __init__(self, source_root: Path|None, git_repo: Path|None, git_ref: str):
        self.root=source_root; self.repo=git_repo; self.ref=git_ref
    def bytes(self,path:str)->bytes:
        if self.root is not None: return (self.root/path).read_bytes()
        return git_show(self.repo,self.ref,path)
    def text(self,path:str)->str: return self.bytes(path).decode('utf-8-sig')

def parse_frontmatter(text: str):
    if not text.startswith('---\n'):
        return {}, text
    lines=text.splitlines(keepends=True)
    end=None
    for i in range(1,len(lines)):
        if lines[i].strip()=='---': end=i; break
    if end is None: raise ValueError('front matter not closed')
    front=''.join(lines[1:end]); body=''.join(lines[end+1:])
    meta={}
    for raw in front.splitlines():
        if not raw or raw[0].isspace() or raw.lstrip().startswith('#'): continue
        m=re.match(r'^([A-Za-z0-9_-]+)\s*:\s*(.*)$',raw)
        if not m: continue
        k,v=m.groups(); v=v.strip()
        if len(v)>=2 and ((v[0]==v[-1]=='"') or (v[0]==v[-1]=="'")): v=v[1:-1]
        meta[k]=v
    return meta, body

def canonical_url(path:str, meta:dict)->str:
    if path=='index.md': route='/'
    elif meta.get('permalink'): route=meta['permalink']
    elif path.endswith('/index.md'): route='/' + path[:-len('index.md')]
    else: route='/' + re.sub(r'\.md$','/',path)
    if not route.startswith('/'): route='/'+route
    if route!='/' and '.' not in route.rsplit('/',1)[-1] and not route.endswith('/'): route+='/'
    return CANONICAL_BASE + route

def document_id(path:str)->str:
    if path=='index.md': return 'home'
    x=re.sub(r'/index\.md$','',path)
    x=re.sub(r'\.md$','',x)
    return x.replace('/','--')

def document_role(path:str)->str:
    if path=='index.md': return 'framework hub'
    first=path.split('/')[0]
    if first=='core':
        if path.endswith('related-work.md'): return 'field bridge / related work'
        if path.endswith('glossary.md'): return 'canonical terminology'
        if path.endswith('proof-status.md'): return 'epistemic calibration'
        return 'core framework / technical argument'
    return {
      'proof-program':'proof program / open verification obligation',
      'empirical':'empirical protocol / results context',
      'series-1':'Series 1 framework exposition',
      'series-2':'Series 2 framework exposition',
      'series-3':'Series 3 exploratory / formal-extension exposition',
      'specialist-handoff':'specialist verification handoff',
      'public':'public-facing exposition / challenge',
      'open-problems':'research agenda',
      'apply':'application guide',
      'cite':'citation guidance',
      'toys':'interactive simulation documentation',
    }.get(first,'framework document')

def split_sections(body:str):
    # Preserve exact source text. Heading detection is disabled inside fenced code blocks.
    lines=body.splitlines(keepends=True)
    starts=[]; in_fence=False; fence_char=None; fence_len=0
    for i,line in enumerate(lines):
        fm=re.match(r'^\s*(`{3,}|~{3,})',line)
        if fm:
            token=fm.group(1); c=token[0]
            if not in_fence:
                in_fence=True; fence_char=c; fence_len=len(token)
            elif c==fence_char and len(token)>=fence_len:
                in_fence=False; fence_char=None; fence_len=0
            continue
        if in_fence: continue
        hm=re.match(r'^(#{1,6})[ \t]+(.+?)(?:[ \t]+#+)?[ \t]*(?:\r?\n)?$',line)
        if hm:
            title=hm.group(2).strip()
            starts.append((i,len(hm.group(1)),title))
    sections=[]
    if not starts:
        if body.strip(): sections.append((0,'Preamble',[],body))
        return sections
    if any(''.join(lines[:starts[0][0]]).strip() for _ in [0]):
        pre=''.join(lines[:starts[0][0]])
        sections.append((0,'Preamble',[],pre))
    stack=[]
    for j,(start,level,title) in enumerate(starts):
        end=starts[j+1][0] if j+1<len(starts) else len(lines)
        chunk=''.join(lines[start:end])
        while stack and stack[-1][0]>=level: stack.pop()
        stack.append((level,title))
        sections.append((level,title,[x[1] for x in stack],chunk))
    return sections

def alias_present(text:str, alias:str)->bool:
    # Unicode-aware enough for these canonical tokens; symbols use substring matching.
    if any(ch in alias for ch in 'ΦΨ') or '(' in alias:
        return alias.casefold() in text.casefold()
    # Short all-uppercase abbreviations require token-ish boundaries.
    if len(alias)<=5 and alias.upper()==alias and any(c.isalpha() for c in alias):
        return re.search(r'(?<![A-Za-z0-9_])'+re.escape(alias)+r'(?![A-Za-z0-9_])',text,re.I) is not None
    return alias.casefold() in text.casefold()

def match_claims(text:str, claims_by_id:dict)->list[str]:
    out=[]
    for cid,aliases in CLAIM_ALIASES.items():
        if cid in claims_by_id and any(alias_present(text,a) for a in aliases): out.append(cid)
    return sorted(out)

def term_aliases(term:dict)->list[str]:
    aliases=[]
    if term.get('canonical_name'): aliases.append(term['canonical_name'])
    if term.get('abbreviation'): aliases.append(term['abbreviation'])
    # Add exact framework-style ID only when it is itself a distinctive token.
    if term['id'] in {'op4','op4d','pcl','agc','ici','nad','gdc','cmr','cot','mch','svg','dbst-m0','dbst-m1','o-owt'}:
        aliases.append(term['id'].replace('-','_') if term['id']=='o-owt' else term['id'])
    return list(dict.fromkeys(aliases))

def match_terms(text:str,terms:list[dict])->list[str]:
    out=[]
    for term in terms:
        if any(alias_present(text,a) for a in term_aliases(term)): out.append(term['id'])
    return sorted(out)

def match_open_problems(text:str,ops:list[dict])->list[str]:
    out=[]
    for op in ops:
        aliases=[op['id'],op.get('name','')]
        if any(a and alias_present(text,a) for a in aliases): out.append(op['id'])
    return sorted(out)

def release_hashes(manifest:dict)->dict[str,str]:
    return {x['path']:x['sha256'] for x in manifest['files']}

def dump_jsonl(path:Path, records:list[dict]):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',encoding='utf-8',newline='\n') as f:
        for obj in records:
            f.write(json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n')

def build(source:Source,out:Path):
    claim_graph=json.loads(source.text('claim-graph.json'))
    open_probs=json.loads(source.text('open-problems.json'))
    defined_terms=json.loads(source.text('defined-terms.json'))
    manifest=json.loads(source.text('release-manifest.json'))
    hashes=release_hashes(manifest)
    claims=claim_graph['claims']; claims_by_id={c['id']:c for c in claims}
    ops=open_probs['open_problems']; terms=defined_terms['terms']
    corpus=[]
    for spath in PUBLIC_SOURCE_PATHS:
        raw=source.bytes(spath)
        actual=sha256_bytes(raw)
        expected=hashes.get(spath)
        if expected and actual!=expected: raise RuntimeError(f'{spath}: SHA-256 does not match v1.0.0 release manifest')
        text=raw.decode('utf-8-sig'); meta,body=parse_frontmatter(text)
        title=meta.get('title') or spath
        url=canonical_url(spath,meta); did=document_id(spath)
        sections=split_sections(body)
        for idx,(level,stitle,spath_titles,chunk) in enumerate(sections):
            cids=match_claims(chunk,claims_by_id)
            tids=match_terms(chunk,terms)
            opids=match_open_problems(chunk,ops)
            deps=sorted({d for cid in cids for d in claims_by_id[cid].get('depends_on',[])})
            sid=f'sec-{idx:03d}'
            rec={
              'schema_version':SCHEMA_VERSION,
              'record_id':f'ac-v{FRAMEWORK_VERSION}::{did}::{sid}',
              'framework':FRAMEWORK,
              'framework_version':FRAMEWORK_VERSION,
              'release_tag':RELEASE_TAG,
              'release_commit':RELEASE_COMMIT,
              'release_date':RELEASE_DATE,
              'framework_doi':FRAMEWORK_DOI,
              'document_id':did,
              'section_id':sid,
              'title':title,
              'section_title':stitle,
              'section_level':level,
              'section_path':spath_titles,
              'text':chunk,
              'canonical_url':url,
              'source_path':spath,
              'source_url':f'{REPOSITORY}/blob/{RELEASE_TAG}/{spath}',
              'document_role':document_role(spath),
              'language':'en',
              'proof_status':PROOF_STATUS,
              'claim_ids':cids,
              'term_ids':tids,
              'open_problem_ids':opids,
              'dependencies':deps,
              'license':LICENSE,
              'source_sha256':actual,
              'text_sha256':sha256_text(chunk),
              'authority_note':'Derived machine-ingestion record. Canonical authority remains the cited alignmentconstraint.org page and the versioned framework DOI.'
            }
            corpus.append(rec)
    common={
      'schema_version':SCHEMA_VERSION,'framework':FRAMEWORK,'framework_version':FRAMEWORK_VERSION,
      'release_tag':RELEASE_TAG,'release_commit':RELEASE_COMMIT,'release_date':RELEASE_DATE,
      'framework_doi':FRAMEWORK_DOI,'proof_status':PROOF_STATUS,'license':LICENSE,
      'authority_note':'Derived machine-ingestion record. Canonical authority remains alignmentconstraint.org and the versioned framework DOI.'
    }
    claim_records=[]
    for c in claims:
        claim_records.append({**common,'record_type':'claim','record_id':'claim:'+c['id'],'source_file':'claim-graph.json','source_sha256':hashes['claim-graph.json'],'data':c})
    for op in ops:
        claim_records.append({**common,'record_type':'open_problem','record_id':'open_problem:'+op['id'],'source_file':'open-problems.json','source_sha256':hashes['open-problems.json'],'data':op})
    term_records=[]
    for t in terms:
        term_records.append({**common,'record_type':'term','record_id':'term:'+t['id'],'source_file':'defined-terms.json','source_sha256':hashes['defined-terms.json'],'data':t})
    dump_jsonl(out/'corpus.jsonl',corpus)
    dump_jsonl(out/'claims.jsonl',claim_records)
    dump_jsonl(out/'terms.jsonl',term_records)
    return len(corpus),len(claim_records),len(term_records)

def main():
    ap=argparse.ArgumentParser(description='Build deterministic v1.0.0 Alignment Constraint machine-ingestion files.')
    ap.add_argument('--source-root',type=Path,help='Path to an extracted v1.0.0 release root.')
    ap.add_argument('--git-repo',type=Path,default=Path('.'),help='Git repository used with --git-ref when --source-root is omitted.')
    ap.add_argument('--git-ref',default=RELEASE_TAG,help='Immutable source ref (default: v1.0.0).')
    ap.add_argument('--output-dir',type=Path,default=Path('data'))
    a=ap.parse_args()
    if a.source_root:
        src=Source(a.source_root.resolve(),None,a.git_ref)
    else:
        src=Source(None,a.git_repo.resolve(),a.git_ref)
    counts=build(src,a.output_dir.resolve())
    print(f'Built corpus={counts[0]} records, claims/open-problems={counts[1]}, terms={counts[2]} into {a.output_dir}')
if __name__=='__main__': main()
