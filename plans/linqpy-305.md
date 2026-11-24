---
ticket: linqpy-305
concepts: []
new_concepts: []
paths:
  - .github/workflows/ci.yml
  - plans/linqpy-305.md
contracts_changed:
  - "CI: new check `ci` on pull requests to main (becomes a required check in onboarding on-354)"
acceptance:
  - "A pull request to main from a branch in this repo shows a check named `ci`."
  - "`ci` needs `lint` and `build` and fails when either of them fails, is cancelled, or is skipped on a pull request to main."
  - "`lint` and `build` run on pull requests to main (same-repo and fork), so `ci` reflects real results rather than skipped jobs."
  - "Push-triggered `lint`/`build` behaviour on non-PR branches is unchanged."
tests: []
decisions:
  - q: "lint and build currently run only on push events or fork PRs, so on a same-repo PR they are skipped and an aggregate `ci` would pass with nothing checked. How should `ci` get real results?"
    options:
      - "A: Let lint and build also run on every pull_request to main, and have `ci` (pull_request only) require both to succeed. Same-repo PRs run lint/build twice (push + PR), a few extra minutes of runner time."
      - "B: Run `ci` on push too, requiring success when deps ran and treating skipped as pass. No extra runs, but the PR-event `ci` passes vacuously and the required check can be satisfied by the empty run."
      - "C: Leave lint/build gating alone; `ci` treats skipped as pass. Smallest diff, but `ci` checks nothing on same-repo PRs, which defeats the requirement."
    recommend: A
    why: "Only A makes the required `ci` check on a PR actually depend on lint and build passing for that PR. The cost is a duplicate ~2-minute run on same-repo PRs. ci.yml is Stainless-generated; Stainless keeps custom edits through its merge, but a regen could touch these lines, worth watching on the next codegen PR."
epic:
---

Edit `.github/workflows/ci.yml`:

1. Extend the `if:` on `lint` and `build` so they also run when
   `github.base_ref == 'main'` (only set on pull_request events),
   keeping the existing `codegen metadata` guard for pushes.
2. Add job `ci` (name `ci`), `needs: [lint, build]`,
   `if: always() && github.event_name == 'pull_request' && github.base_ref == 'main'`, that fails unless
   every `needs.*.result` is `success`. In push runs the job is skipped, so
   its `name:` is an expression that resolves to `ci-gate (push, unused)`
   there: a skipped job named `ci` would satisfy the required check.
   The head commit must carry exactly one `ci` check, and it is not skipped.

No change to triggers, release workflows, or other jobs.
