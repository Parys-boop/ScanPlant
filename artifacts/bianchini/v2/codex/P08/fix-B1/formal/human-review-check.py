from pathlib import Path
import json,hashlib,sys
base=Path('/home/administradorarthur/datasets/scanplant/p08-recovery-20261005')
events=[json.loads(l) for l in (base/'journal.jsonl').read_text().splitlines()]
records=json.loads((base/'records.json').read_text())
if isinstance(records,dict): records=list(records.values())
template=json.loads((base/'decisions.template.json').read_text())['decisions']
receipt=json.loads(Path('artifacts/bianchini/v2/codex/P08/human-acceptance.json').read_text())
real=[]
for item in records:
 d=item.get('decision') or {}
 if d.get('authority')=='human' and d.get('reviewer') and d.get('reviewed_at') and d.get('rationale'): real.append(item)
result={'required_candidate_opinions':1088,'records':len(records),'human_candidate_opinions':len(real),'blank_template_entries':sum(not x.get('reviewer') for x in template),'historical_U803':receipt['U-803'],'technical_zero_transfer_accepted':receipt['zero_transfer_result_accepted'],'candidate_approval':receipt['candidate_approval'],'result':'passed' if len(real)==1088 else 'blocked_missing_human_candidate_opinions'}
print(json.dumps(result,sort_keys=True),flush=True)
sys.exit(0 if len(real)==1088 else 1)
