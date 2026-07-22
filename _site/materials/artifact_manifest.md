# Artifact Manifest — Loop Engineering For Everyone

> This document inventories every artifact changed or created during the production of the "Loop Engineering For Everyone" course package, organized by durability class and role in the engineering loop.

---

## Overview Diagram

![Artifact Loop](./illustrations/fig_05_artifact_loop.excalidraw) — [PNG](./illustrations/fig_05_artifact_loop.png) *(rendered)*

---

## 1. Durable Project Worktree Deliverables (currently uncommitted)

These are the final deliverables — course materials that live in the project worktree. They are currently unstaged and uncommitted pending final review.

| # | Path | Role | State |
|---|------|------|-------|
| 1 | `/Users/li/github/SylphAI-Inc/adal/docs/adal/wip_docs/loop_engineering_for_everyone/lesson.md` | Main 30-minute lesson script (Markdown) | Created, then revised (3 correction passes) |
| 2 | `/Users/li/github/SylphAI-Inc/adal/docs/adal/wip_docs/loop_engineering_for_everyone/demo_runbook.md` | Demo companion: setup, narration cues, fallbacks | Created |
| 3 | `/Users/li/github/SylphAI-Inc/adal/docs/adal/wip_docs/loop_engineering_for_everyone/artifact_manifest.md` | This file — inventory and loop documentation | Created |
| 4 | `.../illustrations/fig_01_prompting_vs_loop.excalidraw` | Diagram: Prompting vs Loop Engineering | Created, then fixed (2 visual corrections) |
| 5 | `.../illustrations/fig_01_prompting_vs_loop.png` | Rendered PNG of fig_01 | Re-rendered after each source fix |
| 6 | `.../illustrations/fig_02_loop_anatomy.excalidraw` | Diagram: Loop Anatomy (7+1 primitives) | Created, then enhanced (added Context/Skills + feedback arrow) |
| 7 | `.../illustrations/fig_02_loop_anatomy.png` | Rendered PNG of fig_02 | Rendered once |
| 8 | `.../illustrations/fig_03_good_vs_bad_loop.excalidraw` | Diagram: Good Loop vs Bad Loop | Created, then fixed (JSON quote issue) |
| 9 | `.../illustrations/fig_03_good_vs_bad_loop.png` | Rendered PNG of fig_03 | Rendered once |
| 10 | `.../illustrations/fig_04_adal_mapping.excalidraw` | Diagram: AdaL Engineer Mapping | Created, then enhanced (State connection + legend) |
| 11 | `.../illustrations/fig_04_adal_mapping.png` | Rendered PNG of fig_04 | Re-rendered after fix |
| 12 | `.../illustrations/fig_05_artifact_loop.excalidraw` | Diagram: The production loop itself (this task) | Created |
| 13 | `.../illustrations/fig_05_artifact_loop.png` | Rendered PNG of fig_05 | Created and rendered |

---

## 2. Durable Local Engineer Files (persist across sessions)

These are the engineer's working memory — contracts, plans, and evaluator criteria that governed the loop. They live in `~/.adal/engineer/` and are NOT committed to the project repo but persist locally to enable resumption and audit.

| # | Path | Role in the Loop | State |
|---|------|-----------------|-------|
| 1 | `/Users/li/.adal/engineer/contracts/2026-07-contract.md` | **Contract** — The approved scope, acceptance criteria, and constraints governing this task | Created by supervisor, read by builder |
| 2 | `/Users/li/.adal/engineer/tasks/loop-engineering-class/builder_plan.md` | **Builder plan** — Investigation results, proposed timing, source ledger, delivery steps, evaluator-response appendices, scope corrections | Created by builder, iterated (4 appendices added) |
| 3 | `/Users/li/.adal/engineer/tasks/loop-engineering-class/evaluator_plan.md` | **Evaluator plan** — Independent review rubric, blockers, acceptance criteria, adversarial checklist | Created by evaluator agent |

---

## 3. Ephemeral Tooling (not a deliverable)

These existed temporarily in `/tmp/` during PNG rendering and are not part of the course package. They may be deleted at any time.

| Path | Purpose | Lifetime |
|------|---------|----------|
| `/tmp/excalidraw-render-local/` | Self-contained Node project: esbuild-bundled Excalidraw + Playwright renderer | Ephemeral — created for rendering, survives until system reboot |
| `/tmp/excalidraw-render-local/excalidraw-bundle.js` | Bundled @excalidraw/excalidraw + React (IIFE, ~2MB) | Part of renderer |
| `/tmp/excalidraw-render-local/render-local.mjs` | Rendering script: local HTTP server + Playwright + screenshot | Part of renderer |
| `/tmp/excalidraw-render-local/render-template.html` | HTML template loading the bundle | Part of renderer |

---

## 4. Loop Relationship Map

How each artifact class participates in the engineering loop:

```
User Goal
    │
    ▼
┌─────────────────────────────────────┐
│  Contract (engineer/contracts/)      │ ← Defines "done"
└─────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────┐
│  Builder Plan + Evaluator Plan       │ ← Investigation + review criteria
│  (engineer/tasks/)                   │   (disk-backed state for the loop)
└─────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────┐
│  Implementation Artifacts            │ ← lesson.md, diagrams, PNGs
│  (docs/adal/wip_docs/...)           │   (project-committed deliverables)
└─────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────┐
│  Independent Review / Validation     │ ← Evaluator checks against rubric
│  (evaluator_plan.md criteria)        │   (pass/fail per category)
└─────────────────────────────────────┘
    │
    ├── PASS → Final Delivery
    │
    └── FAIL → Correction (loop back to Implementation)
              Specific blockers identified → surgical fixes only
```

The **human checkpoint** occurs at contract approval (before implementation begins) and at final delivery acceptance (after all evaluator gates pass).

---

## 5. Preceding Workflow Artifact (Demonstrates the Pattern)

The Excalidraw skill installation task (Turns 0–6) directly preceded and demonstrated the same loop pattern used for this course:

| Path | Role |
|------|------|
| `/Users/li/.adal/engineer/tasks/excalidraw-diagram-skill/builder_plan.md` | Builder plan for skill installation |
| `/Users/li/.adal/engineer/tasks/excalidraw-diagram-skill/ag_ui_protocol_streaming.excalidraw` | Test artifact validating the skill |

This task served as a proof-of-concept for: task contract → implementation → validation → correction loop — the same pattern the course teaches.

---

## 6. What Is NOT Here

- **No adaptation/personalization files** — excluded by scope constraint
- **No product source modifications** — documentation-only changes
- **No git commits** — all changes are unstaged
- **No installed skill modifications** — the `~/.adal/skills/excalidraw-diagram/` directory is untouched
