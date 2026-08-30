# Binaru Development Roadmap

This roadmap guides incremental, reviewable delivery. It may change as product evidence and approved architecture decisions evolve. Only the current phase should be implemented.

## Phase 0 — Application Foundation — COMPLETED

- **Objective:** Establish a small Flutter foundation that future screens can extend consistently.
- **Major deliverable:** Minimal app bootstrap, centralized color/spacing/radius tokens, a base theme, and one temporary development screen.
- **Not included:** Product screens, navigation, state management, persistence, learning logic, fonts, mascot assets, or Rive.
- **Dependencies:** Flutter SDK only, following the repository bootstrap.
- **Expected testing:** App-root and temporary-screen widget tests, formatting, analysis, and Android debug build when tooling permits.
- **Completion criteria:** Foundation renders with the Binaru theme, automated widget tests pass, and implementation documentation matches the code.

## Phase 1 — Splash & Welcome — NEXT

- **Objective:** Introduce the first approved child-facing entry experience.
- **Major deliverable:** Focused splash and welcome flow based on reviewed designs.
- **Not included:** Child profiles, baseline assessment, home, lessons, or mascot animation.
- **Dependencies:** Phase 0 and approved screen requirements/assets.
- **Expected testing:** Widget tests for content, accessibility, and the entry transition.
- **Completion criteria:** Reviewed entry flow works on target Android sizes without speculative downstream navigation.

## Phase 2 — Child Profile — PLANNED

- **Objective:** Capture the minimum child profile data required by the PRD.
- **Major deliverable:** Privacy-conscious nickname, age-band, and avatar setup.
- **Not included:** Authentication, cloud accounts, precise personal data, or parent analytics.
- **Dependencies:** Phase 1 plus approved profile model and storage decision if persistence is required.
- **Expected testing:** Validation and profile-flow widget tests; persistence tests only if selected.
- **Completion criteria:** A child profile can be created with only approved minimum data.

## Phase 3 — Baseline Introduction — PLANNED

- **Objective:** Explain baseline play without presenting it as a test.
- **Major deliverable:** A short baseline introduction and clear start action.
- **Not included:** The complete baseline activity set or adaptive scoring.
- **Dependencies:** Phase 2 and approved baseline copy/design.
- **Expected testing:** Widget tests for child-friendly content and navigation intent.
- **Completion criteria:** The child can understand and begin the future baseline flow.

## Phase 4 — Child Home — PLANNED

- **Objective:** Provide a simple child-facing starting point after setup.
- **Major deliverable:** Home screen with one obvious recommended action.
- **Not included:** Parent analytics, complete rewards, or all learning destinations.
- **Dependencies:** Earlier onboarding phases and an approved navigation decision.
- **Expected testing:** Widget, accessibility, and navigation tests.
- **Completion criteria:** Home communicates the next action clearly with low cognitive load.

## Phase 5 — Adventure Map — PLANNED

- **Objective:** Represent learning progress as an understandable journey.
- **Major deliverable:** Initial map shell and one reachable checkpoint.
- **Not included:** Every numeracy world, elaborate animation, or final reward art.
- **Dependencies:** Phase 4 and approved journey/progress representation.
- **Expected testing:** Map-state and checkpoint interaction widget tests.
- **Completion criteria:** One checkpoint accurately reflects available journey state.

## Phase 6 — Lesson Shell — PLANNED

- **Objective:** Establish the minimal reusable flow for one lesson.
- **Major deliverable:** Lesson introduction, activity host, and completion boundaries.
- **Not included:** Full content engine, all activity types, or mastery adaptation.
- **Dependencies:** Phase 5 plus approved lesson/content boundaries.
- **Expected testing:** Lesson lifecycle and host-state tests.
- **Completion criteria:** A stub lesson can progress through defined states without hard-coding future curricula.

## Phase 7 — Counting 1–5 Vertical Slice — PLANNED

- **Objective:** Validate one complete learning experience for counting 1–5.
- **Major deliverable:** Instruction, one activity type, answer evaluation, feedback, and completion.
- **Not included:** Remaining numeracy modules or generalized adaptive behavior.
- **Dependencies:** Phase 6 and approved content/evaluation decisions.
- **Expected testing:** Unit tests for evaluation and widget/integration tests for the vertical slice.
- **Completion criteria:** The child can complete the slice reliably from start to finish.

## Phase 8 — Learning Feedback — PLANNED

- **Objective:** Provide encouraging, actionable correct and retry feedback.
- **Major deliverable:** Reusable feedback states for the vertical slice.
- **Not included:** Rive character integration, punitive feedback, or broad reward systems.
- **Dependencies:** Phase 7 and approved feedback language/design.
- **Expected testing:** State, copy, accessibility, and interaction tests.
- **Completion criteria:** Both outcomes are immediate, supportive, and permit the intended next action.

## Phase 9 — Progress Persistence — PLANNED

- **Objective:** Preserve the vertical slice's essential progress offline.
- **Major deliverable:** Approved local persistence implementation for current progress data.
- **Not included:** Cloud sync, accounts, analytics vendors, or speculative schemas.
- **Dependencies:** Stable Phase 7 data needs and an accepted persistence ADR.
- **Expected testing:** Serialization, repository behavior, restart, and failure tests.
- **Completion criteria:** Approved progress survives normal app restarts without data loss.

## Phase 10 — Skill Mastery — PLANNED

- **Objective:** Represent learning development by skill rather than a global score.
- **Major deliverable:** Initial deterministic mastery state updates for the vertical slice.
- **Not included:** Machine learning or all numeracy skills.
- **Dependencies:** Phase 9 and approved mastery rules/model.
- **Expected testing:** Pure unit tests for every transition and boundary.
- **Completion criteria:** Recorded attempts produce explainable mastery changes.

## Phase 11 — Adaptive Rules — PLANNED

- **Objective:** Adjust the next activity using transparent rules.
- **Major deliverable:** A small deterministic recommendation rule set.
- **Not included:** Machine learning, opaque scoring, or remote personalization.
- **Dependencies:** Phase 10 and enough validated activity outcomes.
- **Expected testing:** Table-driven unit tests for each rule and fallback.
- **Completion criteria:** Identical inputs produce explainable, repeatable recommendations.

## Phase 12 — Rewards — PLANNED

- **Objective:** Reinforce learning progress without competitive pressure.
- **Major deliverable:** One modest reward tied to completed learning.
- **Not included:** Leaderboards, gacha, loot boxes, or punishment streaks.
- **Dependencies:** Reliable lesson completion and approved reward design.
- **Expected testing:** Awarding, duplicate prevention, and presentation tests.
- **Completion criteria:** The reward is granted correctly and never obstructs learning.

## Phase 13 — Parent Mode — PLANNED

- **Objective:** Present understandable progress privately to a parent or guardian.
- **Major deliverable:** Parental gate and concise progress summary.
- **Not included:** Cloud accounts, teacher dashboards, or vendor analytics.
- **Dependencies:** Meaningful persisted mastery data and an approved parental-gate design.
- **Expected testing:** Gate, privacy, summary calculation, and accessibility tests.
- **Completion criteria:** Accidental child access is discouraged and progress is understandable.

## Phase 14 — Rive Character Integration — PLANNED

- **Objective:** Integrate approved Aru assets as a presentation companion.
- **Major deliverable:** Rive adapter responding to semantic learning events.
- **Not included:** Business logic inside Rive or generated/unapproved mascot art.
- **Dependencies:** Maintainer-approved assets and an accepted Rive integration ADR.
- **Expected testing:** Event mapping, fallback behavior, performance, and device tests.
- **Completion criteria:** Aru responds reliably without controlling learning decisions.

## Phase 15 — Remaining Numeracy Skills — PLANNED

- **Objective:** Expand the validated learning system across the remaining MVP curriculum.
- **Major deliverable:** Reviewed content and activities for the approved numeracy skills.
- **Not included:** Literacy, English, or unrelated subjects.
- **Dependencies:** A proven vertical slice, stable content model, and curriculum review.
- **Expected testing:** Content validation plus unit, widget, and integration coverage per skill.
- **Completion criteria:** Each required skill meets its reviewed learning and quality criteria.

## Phase 16 — MVP Polish & Testing — PLANNED

- **Objective:** Prepare the numeracy MVP for structured evaluation.
- **Major deliverable:** Accessibility, reliability, performance, usability, and release-readiness improvements.
- **Not included:** New product domains or major speculative features.
- **Dependencies:** Completion of the agreed MVP feature phases.
- **Expected testing:** Full automated suite, real-device checks, offline tests, and usability testing.
- **Completion criteria:** MVP Definition of Done is evidenced and critical defects are resolved.
