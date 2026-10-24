from pathlib import Path
import sys, json, dataclasses, hashlib, io
root = Path(__file__).resolve().parent
out = root / 'output'
sys.path.insert(0, str(root / 'AegisLog/src'))
from aegislog.dashboard import analyze_dashboard
from aegislog.reporting import write_html_report
p = root / 'AegisLog/docs/demo/first-investigation.log'
before = hashlib.sha256(p.read_bytes()).hexdigest()
d = analyze_dashboard(p)
write_html_report(d, out, filename='aegislog-report.html')
summary = dict(lines=d.lines, recognized_records=d.recognized_records, findings=len(d.findings), incidents=len(d.incidents), severities=d.severities, input_sha256=before, source_unchanged=before==hashlib.sha256(p.read_bytes()).hexdigest())
(out/'aegislog-result.json').write_text(json.dumps(summary,indent=2))
sys.path.insert(0,str(root/'AquaVigil'))
from app import create_app
from app.services.analyzer import analyze
p=root/'AquaVigil/data/unexpected_dosing_incident.csv'
payload=p.read_bytes()
result=analyze(payload,p.name)
(out/'aquavigil-result.json').write_text(json.dumps(result,indent=2,default=str))
app=create_app({'TESTING':True,'DATABASE':str(out/'aquavigil.db')})
client=app.test_client()
r=client.post('/upload',data={'evidence':(io.BytesIO(payload),p.name)},content_type='multipart/form-data',follow_redirects=True)
assert r.status_code==200, r.status_code
r=client.get('/report/1/download')
assert r.status_code==200,r.status_code
(out/'aquavigil-report.html').write_bytes(r.data)
print(json.dumps({'aegislog':summary,'aquavigil':{k:result.get(k) for k in ['status','risk_score','record_count','source_type']}}))
