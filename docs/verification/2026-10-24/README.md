# Reproducible project verification

[Profile](../../../README.md) · [Demo gallery](../../demo-gallery.md)

Executed 24 October 2026 (Asia/Dubai) in an isolated Linux x86_64 environment, Python 3.12.14. These are source runs on bundled synthetic fixtures, not customer or industrial deployments.

| Project | Exact source commit | Result |
| :--- | :--- | :--- |
| [AegisLog](https://github.com/HR-Presents/AegisLog/tree/b70abd16e7673b75eabd4cc07fb7ca3a6ccc7a81) v2.1.17 | `b70abd16e7673b75eabd4cc07fb7ca3a6ccc7a81` | **689 tests passed** in 5.07 seconds |
| [AquaVigil](https://github.com/HaziqBinAfzal/AquaVigil/tree/82832c7436b79be93ec441bcb597f9664bc61536) | `82832c7436b79be93ec441bcb597f9664bc61536` | **14 tests passed**, 361 warnings, in 1.74 seconds |

## Actual sample outputs

- **AegisLog:** `first-investigation.log` produced 9 recognized records, 2 findings (HIGH 1, MEDIUM 1) and 1 incident. The input SHA-256 remained unchanged. [Result JSON](aegislog-result.json) · [Generated summary HTML](aegislog-report.html) · [Full evidence HTML](aegislog-report-appendix.html).
- **AquaVigil:** `unexpected_dosing_incident.csv` produced 6 records, status **Critical**, risk score **100** on this synthetic sample. This score is the application's output, not measured detection accuracy. [Result JSON](aquavigil-result.json) · [Exported HTML report](aquavigil-report.html).

Download the HTML files and open them locally. Keep the AegisLog summary and appendix together. GitHub displays their source rather than hosting an interactive app.

## Streaming benchmark

The repository's unmodified benchmark processed **100,000 synthetic records per run across 3 repeats**, with a median **15,348.56 records/second** in this environment. Each run retained 100 findings and omitted 900 under the configured retention limit; all 100,000 records were processed, with no truncated lines and an unchanged input.

[Complete benchmark JSON](aegislog-benchmark.json)

This measures the streaming engine with tracemalloc overhead. It excludes HTML rendering, native collection and live polling; Python allocations are not whole-process RSS. These environment-specific timings are not a production throughput, scalability or detection-accuracy guarantee.

## Reproduce

Use a clean working directory with sibling `AegisLog`, `AquaVigil`, `venv` and `output` directories. Save [reproduce.py](reproduce.py) into that directory.

```bash
git clone https://github.com/HR-Presents/AegisLog.git
git -C AegisLog checkout b70abd16e7673b75eabd4cc07fb7ca3a6ccc7a81
git clone https://github.com/HaziqBinAfzal/AquaVigil.git
git -C AquaVigil checkout 82832c7436b79be93ec441bcb597f9664bc61536
python3 -m venv venv
venv/bin/pip install -r requirements-lock.txt
mkdir -p output
(cd AegisLog && ../venv/bin/python -m pytest -q --junitxml=../output/aegislog-tests.xml)
(cd AquaVigil && ../venv/bin/python -m pytest -q --junitxml=../output/aquavigil-tests.xml)
(cd AegisLog && PYTHONPATH=src ../venv/bin/python tools/benchmark_streaming.py --records 100000 --repeats 3 > ../output/aegislog-benchmark.json)
venv/bin/python reproduce.py
```

Download [requirements-lock.txt](requirements-lock.txt) into the working directory first. It records the installed versions; this is a reproducibility snapshot, not a dependency security audit. Start with a fresh output directory/database when rerunning the report driver.

[Test log: AegisLog](aegislog-tests.txt) · [JUnit: AegisLog](aegislog-tests.xml) · [Test log: AquaVigil](aquavigil-tests.txt) · [JUnit: AquaVigil](aquavigil-tests.xml)

## Scope and remaining checks

No tracked application source was edited. AegisLog tests generated an untracked local report directory. Existing authorship, contributor credits and repository history are preserved.

The runtime had no Docker or Windows environment. Docker Compose, Grafana/Prometheus stack acceptance and the packaged Windows executable were not tested. The Cloud Browser denied local-file navigation, so no new application screenshot or video is represented as captured or visually verified. The generated HTML reports are authentic outputs, with visual review still pending.

**Credits:** Original HR-Presents and repository contributors retain their existing credits, including Haziq Afzal and Ruveeha Ashfaq. This verification records a specific source snapshot and environment; it does not certify production readiness.
