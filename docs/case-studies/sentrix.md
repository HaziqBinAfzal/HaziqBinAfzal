# Sentrix V1 — Bringing Python analysis into one workflow

[Profile](../../README.md) · [Demo gallery](../demo-gallery.md) · [Public LinkedIn overview](https://www.linkedin.com/in/haziq-afzal/)

**Focus:** Python · code security · quality · complexity · reporting  
**Credits:** Jointly developed by Haziq Afzal and Ruveeha Ashfaq under HR-Presents.

## The problem

A Python program can execute successfully while still containing insecure patterns, quality problems, unnecessary complexity or inconsistent formatting. Developers need both findings and enough supporting detail to decide what to fix.

## Our approach

Sentrix brings Bandit, Pylint, Radon and Black into one application workflow, alongside syntax validation, analysis history and structured reports.

| Tool | Publicly described purpose |
| :--- | :--- |
| Bandit | Identify potential insecure Python coding patterns |
| Pylint | Examine code quality, conventions and possible programming issues |
| Radon | Evaluate complexity and maintainability indicators |
| Black | Check formatting consistency |

The public description includes analysis of Python files and ZIP projects, source locations, severity, complexity, formatting results and remediation guidance. OWASP, CWE and NIST references supply context; they do not certify compliance.

## My contribution and shared ownership

Ruveeha and I contribute throughout product planning, design, implementation, testing, troubleshooting, documentation and release preparation. This is a jointly developed HR-Presents product with equal founder credit.

## Public demonstration path

1. Read the [public product announcement](https://www.linkedin.com/feed/update/urn:li:activity:7518587436281688064/).
2. Review the [public reporting discussion](https://www.linkedin.com/feed/update/urn:li:activity:7497246132910178304/), which explains findings, evidence and remediation context.
3. Use the product demonstration or access instructions offered through those public channels.

This case study summarizes information already published on LinkedIn. The [source repository is private](https://github.com/HR-Presents/HR-Presents-Sentrix), so public visitors cannot inspect its implementation.

## Evidence boundaries

This page does not publish private source, reports, customer information or internal screenshots. It makes no claim about parallel execution, runtime performance, scan accuracy or deployment security. Those require separate implementation review or measurement.

## Engineering lesson

Combining tools is only part of the problem. Results also need consistent organization, affected locations, explainable context and a review workflow that helps the developer verify a fix.
