# AquaVigil — Connecting process observations with cyber evidence

[Profile](../../README.md) · [Demo gallery](../demo-gallery.md) · [Repository](https://github.com/HaziqBinAfzal/AquaVigil)

**Focus:** Python · Flask · Docker Compose · evidence provenance · Prometheus · Grafana  
**Credits:** Haziq Afzal — project author; Ruveeha Ashfaq — contributor. Development is collaborative.

[![AquaVigil CI on main](https://github.com/HaziqBinAfzal/AquaVigil/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/HaziqBinAfzal/AquaVigil/actions/workflows/ci.yml)

<sub>Live CI status for the main branch. Release publishing and deployment checks are separate workflows.</sub>

## Quick start — investigate unexpected dosing

**My role:** project author working collaboratively with Ruveeha, a credited contributor. The repository's contributor section remains the source for attribution.

**Requirements:** Windows 10/11, Git and Docker Desktop with Compose v2. Start Docker Desktop and wait for the engine to be ready.

```powershell
git clone https://github.com/HaziqBinAfzal/AquaVigil.git
cd AquaVigil
.\start-aquavigil.ps1
```

Alternatively, open `START-AQUAVIGIL.cmd` from the cloned folder for visible startup diagnostics. The launcher starts the stack and opens the application; use its displayed URL if ports were reassigned.

1. Open **Analyze Evidence** and upload `data/unexpected_dosing_incident.csv`.
2. Inspect classification and SHA256 provenance, then review the unauthorized dosing records alongside the process readings.
3. Open the generated report and audit export. Inspect Prometheus and Grafana after the analysis.

**Recorded result:** the [24 October Linux source run](../verification/2026-10-24/README.md) processed the six-record fixture as **Critical**, risk score **100**. This is a synthetic scenario result, not a detection-accuracy percentage. Docker and monitoring-stack acceptance were not tested in that run.

**If startup fails:** stay in the cloned repository folder and inspect the launcher output. [Recovery guide](https://github.com/HaziqBinAfzal/AquaVigil/blob/main/docs/FAILURE_RECOVERY.md) · [Demonstration guide](https://github.com/HaziqBinAfzal/AquaVigil/blob/main/docs/DEMONSTRATION_GUIDE.md).


## The problem

A water-quality observation and a suspicious network or dosing record can be difficult to interpret in isolation. An educational investigation needs to retain the original evidence, explain the context and distinguish demonstrated analysis from proposed industrial architecture.

## Approach and contribution

I developed AquaVigil collaboratively with Ruveeha as a read-only educational prototype. The repository identifies me as project author and Ruveeha as a contributor.

The application accepts supported CSV/JSON/JSONL evidence, validates and classifies it, calculates SHA256 provenance, correlates supported observations, and produces findings and reports. SQLite retains analysis history. Prometheus and Grafana provide observability.

```mermaid
flowchart TD
    U["Uploaded evidence"] --> V["Validation and SHA256"]
    V --> A["Process and cyber analysis"]
    A --> R["Findings and reports"]
    A --> M["Application metrics"]
    M --> G["Prometheus and Grafana"]
    R --> H["Human review"]
```

This summarizes the application workflow. Industrial DMZ and SCADA diagrams in the source describe a design model, not infrastructure provisioned at a real utility.

## A concrete scenario

The bundled [unexpected dosing fixture](https://github.com/HaziqBinAfzal/AquaVigil/blob/main/data/unexpected_dosing_incident.csv) contains six synthetic records.

| UTC time | Dosing record | Authorized | Source zone | Chlorine value |
| :--- | :--- | :--- | :--- | ---: |
| 09:00 | hold | true | OT | 1.1 |
| 09:05 | hold | true | OT | 1.2 |
| 09:10 | increase_chlorine | false | enterprise | 2.8 |
| 09:15 | increase_chlorine | false | enterprise | 4.8 |
| 09:20 | hold | true | OT | 5.3 |
| 09:25 | hold | true | OT | 3.6 |

All rows are dated **19 September 2026**. Values above are copied from the fixture; they are not calibrated plant measurements. The linked verification record separately documents a dated source run.

The useful investigation question is whether authorization context, source zone and subsequent process readings deserve review together. Temporal association alone does not prove the command caused the process change.

## Walkthrough

1. Start the default Docker Compose stack using the repository launcher or setup instructions.
2. Upload `unexpected_dosing_incident.csv`.
3. Review input classification, provenance, observations and supported findings.
4. Inspect Water Quality and OT/SCADA views, then the report and audit export.
5. Open Prometheus/Grafana after an analysis and explain which metrics they display.

The fixture has six records. Do not promise a next-record flow projection: the documented projection requires at least twelve ordered flow readings.

## Implementation evidence

| Evidence | What it establishes |
| :--- | :--- |
| [Compose file](https://github.com/HaziqBinAfzal/AquaVigil/blob/main/docker-compose.yml) | Default application, Prometheus and Grafana services; optional simulator profile |
| [CI definition](https://github.com/HaziqBinAfzal/AquaVigil/blob/main/.github/workflows/ci.yml) | Configured pytest, compilation, Bandit, dependency audit, model evaluation/manifest steps and container build |
| [Demonstration guide](https://github.com/HaziqBinAfzal/AquaVigil/blob/main/docs/DEMONSTRATION_GUIDE.md) | Review sequence and interpretation limits |
| [Requirement matrix](https://github.com/HaziqBinAfzal/AquaVigil/blob/main/docs/REQUIREMENT_MATRIX.md) | Implemented demonstration versus remaining deployment work |

A workflow definition is evidence of configured checks, not proof that the latest run passed.

## Boundaries and lessons

The prototype sends no industrial-control commands. Zeek/Suricata exports are evidence inputs; live sensors are not installed by the default stack. Synthetic ML screening, heuristic indicators and evidence-to-framework mappings do not establish field validation or regulatory certification.

The core lesson is to make provenance and operational context visible while retaining human authority over interpretation and response.


