# LinuxOps Enterprise Lab — Baselines and evidence-led troubleshooting

[Profile](../../README.md) · [Demo gallery](../demo-gallery.md) · [Repository](https://github.com/HaziqBinAfzal/linuxops-enterprise-lab)

**Focus:** Linux administration · Ubuntu · Rocky Linux · Hyper-V · troubleshooting · peer review  
**Status:** Phase 01 completed; Phases 02–10 planned.

## The problem

A server baseline must explain which system was checked, what it reported and which evidence supports the result. In virtualized environments, guest observations may differ substantially from host configuration.

## Responsibilities

| Contributor | Environment | Documented work |
| :--- | :--- | :--- |
| **Haziq** | Ubuntu Server, web01 | Identity, sudo/SSH, CPU, memory, disks, networking and systemd checks; documentation and peer review |
| **Ruveeha** | Rocky Linux, backup01 | Rocky baseline, storage inspection and Hyper-V memory troubleshooting; documentation and peer review |

We use separate personal hosts. Inter-host VM connectivity has not been established. Ruveeha's troubleshooting work is credited to Ruveeha; it is included here as evidence of our collaboration.

## Haziq's baseline

The [Ubuntu baseline](https://github.com/HaziqBinAfzal/linuxops-enterprise-lab/blob/main/phases/phase-01/docs/web01-baseline.md) records the administration checks. The original screenshot shows resource and filesystem observations; the evidence index describes its coverage.

[![Haziq's Ubuntu resource and health checks](https://raw.githubusercontent.com/HaziqBinAfzal/linuxops-enterprise-lab/main/phases/phase-01/evidence/haziq-web01-health.png)](https://github.com/HaziqBinAfzal/linuxops-enterprise-lab/blob/main/phases/phase-01/evidence/haziq-web01-health.png)

## The memory investigation

Ruveeha's Rocky guest reported approximately **609 MiB** RAM despite **4 GiB** configured startup memory. The record also captured `hv_balloon` warnings and enabled Hyper-V Dynamic Memory.

| Stage | Recorded observation or action |
| :--- | :--- |
| Identify | Guest memory substantially below configured startup allocation |
| Compare | Inspect guest memory/kernel messages and host memory settings |
| Change | Shut down VM, disable Dynamic Memory, retain 4 GiB startup allocation |
| Verify | Approximately 3.6 GiB guest-visible RAM, zero swap use and zero failed systemd units |
| Record | Preserve before/after screenshots and peer-reviewed documentation |

Disabling Dynamic Memory and restarting restored the observed allocation. The record does not isolate the effect of restarting or establish why the host originally reduced allocation; host-pressure history was not captured.

## Evidence and review

- [Incident report](https://github.com/HaziqBinAfzal/linuxops-enterprise-lab/blob/main/phases/phase-01/docs/memory-troubleshooting.md): commands, investigation, interpretation and unresolved cause questions.
- [Six-image evidence index](https://github.com/HaziqBinAfzal/linuxops-enterprise-lab/blob/main/phases/phase-01/evidence/README.md): health, memory, host settings and review evidence.
- [PR #1](https://github.com/HaziqBinAfzal/linuxops-enterprise-lab/pull/1): Ubuntu baseline.
- [PR #2](https://github.com/HaziqBinAfzal/linuxops-enterprise-lab/pull/2): Rocky baseline and troubleshooting.
- [Phase 01 overview](https://github.com/HaziqBinAfzal/linuxops-enterprise-lab/blob/main/phases/phase-01/README.md): completed observations, contributor roles and pending fresh-build validation.

## Results and limits

Phase 01 provides documented baselines and a resolved guest-memory symptom. The screenshots are historical point-in-time evidence, not proof of every installation, update, access or security detail. The public reconstruction guide still awaits a separately recorded fresh-build test.

The main lesson is to compare host and guest state, verify recovery and preserve enough context for someone else to review the reasoning. A successful fix and a proven root cause are different outcomes.
