# Demo Runbook — Loop Engineering For Everyone

> Companion to `lesson.md`. Contains reproducible setup, narration cues, and fallback transcripts for all demos.

---

## Demo 1: Fix a Documentation Issue (Live/Reproducible)

### Prerequisites

- AdaL CLI installed (`adal` or `adal-dev`)
- A local clone of a repo with a `docs/` directory containing Markdown files
- `markdown-link-check` installed: `npm install -g markdown-link-check`
- Internet access for model API calls

### Setup (Before Class)

```bash
# Create a test branch to isolate changes
cd /path/to/your/repo
git checkout -b demo/loop-engineering-fix-link

# Verify there are broken links to find
markdown-link-check docs/**/*.md 2>&1 | grep -c "dead"
# Should show >= 1 dead link
```

### Task Contract (Show on Screen)

```yaml
goal: "Find and fix one broken Markdown link in docs/"
scope: "Only files in docs/. Do not touch source code."
verification: "markdown-link-check passes on changed files"
stop_condition: "1 fix verified, OR 3 iterations with no candidate, OR $1 budget"
human_gate: "Review diff before any commit"
```

### Run Command

```bash
adal -q "Find one broken link in docs/ using markdown-link-check, fix it, \
  and verify the fix passes. Only edit files in docs/. Stop after 1 fix \
  or 3 attempts. Do not commit." --allowed-tools "Read,Bash,Edit"
```

### Narration Cues

| Timestamp | What to say |
|-----------|-------------|
| Start | "Watch the task contract — bounded goal, clear scope, measurable verification." |
| Worker runs checker | "The agent's first action: run the verification tool to find the problem." |
| Worker proposes fix | "One-line edit. Notice it stays in scope — only docs/ files." |
| Verification passes | "The loop's built-in check: re-run the tool. Green means done." |
| Loop ends | "Stop condition met. Total: 2 iterations, ~$0.15, one reviewable diff." |
| Diff shown | "This is what the human reviews. Small, scoped, verifiable." |

### Fallback Transcript

If the live run fails (model error, no broken links found, network issue), show this static transcript:

```
$ adal -q "Find one broken link in docs/..."

[Engineer] Planning: Run markdown-link-check to identify broken links.
[Worker:coding] Executing: bash("markdown-link-check docs/adal/README.md")
  → Found: line 42: https://old-domain.com/api/v1 — Status: 404

[Worker:coding] Proposing fix: Replace URL with https://docs.new-domain.com/api/v1
[Worker:coding] Executing: edit docs/adal/README.md (line 42)

[Engineer] Verifying: bash("markdown-link-check docs/adal/README.md")
  → All links OK ✅

[Engineer] Stop condition met: 1 fix verified.
[Engineer] Presenting diff for review:

--- a/docs/adal/README.md
+++ b/docs/adal/README.md
@@ -42 +42 @@
-[API Reference](https://old-domain.com/api/v1)
+[API Reference](https://docs.new-domain.com/api/v1)

Cost: $0.12 | Iterations: 2 | Duration: 34s
```

---

## Demo 2: Landing-Page Clone (Prerecorded)

### Recording Setup

- Screen resolution: 1920×1080
- Terminal: split-screen showing AdaL output + browser preview
- Target page: any public landing page with distinct visual elements
- Duration target: 4 minutes (speed up idle/loading sections)

### Recording Checklist

| Phase | What to capture | Duration |
|-------|-----------------|----------|
| Research | Agent navigates to URL, takes screenshot, runs JS to extract CSS values | 60s |
| Code | Agent writes React components, starts dev server | 90s |
| QA | Agent screenshots its output, runs pixel diff | 60s |
| Fix | Agent corrects mismatches, re-verifies | 30s |

### Narration Script (Voiceover)

```
[0:00] "This is a single browser-use worker running the cloning loop.
        It navigates to the target, extracts exact design tokens — not guessing."

[1:00] "Now it writes code using those extracted values.
        React plus Tailwind. One agent, no coordination overhead."

[2:30] "The verification step: screenshot its own work and pixel-diff
        against the original. This is the loop's built-in evaluator."

[3:30] "Deltas found — wrong padding here, missing gradient there.
        The agent fixes them and re-verifies. Diff drops below threshold."

[4:00] "Loop complete. The stop condition was measurable:
        pixel diff under 5%. All state is on disk — screenshots, components, diff results."
```

### Fallback

If recording is not available at class time, show annotated screenshots of each phase with the narration text as captions.

---

## Demo 3: Minecraft Game Build (Optional — Pending)

### Status

⚠️ **Not yet recorded.** This demo requires:
- An existing Minecraft-style game project built with AdaL
- OR: a reproducible task contract for building one from scratch

### If Recording Becomes Available

Show: Engineer delegates game logic (player movement, block placement) to coding worker → worker writes code → engineer runs game to verify → iterates on bugs.

### If Not Available

Skip gracefully: "We have a third demo showing a multi-file game build, but I'll share that recording separately. The loop mechanics are identical — task contract, scoped worker, test verification, human review."

---

## General Presentation Notes

### Timing Budget

| Section | Allocated | Flex |
|---------|-----------|------|
| Demo 1 (live) | 5 min | +1 min if audience questions |
| Demo 2 (prerecorded) | 4 min | Fixed (recording length) |
| Demo 3 (optional) | 0–3 min | Only if footage exists |
| Wrap-up | 1 min | Fixed |

### Technical Failure Plan

| Failure | Response |
|---------|----------|
| Model API down | Use fallback transcript (Demo 1) |
| No broken links in repo | Pre-plant a broken link in a test branch before class |
| Recording won't play | Show annotated screenshots |
| Internet drops | All fallbacks work offline |

### What NOT to Say

- ❌ "AdaL learns your style" (adaptation is not production-ready)
- ❌ "This replaces you as an engineer" (loops amplify, not replace)
- ❌ "Set it and forget it" (human review is always the final gate)
- ❌ "Revolutionary / game-changing / next-gen" (no hype words)
