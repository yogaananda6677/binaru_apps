# Contributing to Binaru

Thank you for helping improve Binaru. By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Issue-first policy

1. Open an Issue before implementing any change.
2. Do not begin significant implementation until the Issue has been discussed or acknowledged.
3. Opening an Issue does not guarantee that a proposal will be accepted. Maintainers may request changes or reject proposals.
4. Fork the repository and create a dedicated branch in your fork.
5. Never push directly to `main`.
6. Submit every change through a pull request.
7. Every pull request must reference an existing Issue in this repository. Prefer `Closes #123` or `Fixes #123` in its description.
8. Keep pull requests small and focused.
9. Run formatting, analysis, and tests locally. CI must pass before merge.
10. Resolve all review comments.
11. Do not merge your own pull request. The repository maintainer reviews and merges accepted pull requests into `main`.

## Standard workflow

Issue → discussion → fork → branch → implementation → tests → pull request → maintainer review → merge

1. Search existing Issues, then open a focused Issue if none covers the work.
2. Wait for discussion or maintainer acknowledgement before significant implementation.
3. Fork the repository and branch from the latest `main`.
4. Implement and test the smallest coherent change.
5. Open a pull request that references the Issue with a closing keyword.
6. Address review feedback and keep CI green.
7. A maintainer performs the final merge.

## Branch naming

- `feat/<issue-number>-short-description`
- `fix/<issue-number>-short-description`
- `docs/<issue-number>-short-description`
- `refactor/<issue-number>-short-description`
- `test/<issue-number>-short-description`
- `chore/<issue-number>-short-description`

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/) with `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`, or `ci:` prefixes.

Examples:

```text
feat: add counting activity engine
fix: prevent duplicate activity attempts
docs: document learning mastery model
```

## Local validation

Run from `apps/mobile`:

```bash
dart format .
flutter analyze
flutter test
```
