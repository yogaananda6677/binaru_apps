# Maintainer Guide

## Protecting `main`

Repository files cannot fully prevent direct pushes or enforce review. Configure a GitHub Ruleset or branch protection rule in repository settings for the `main` branch.

Recommended rules:

- Require a pull request before merging.
- Require at least one approving review.
- Require review from CODEOWNERS.
- Require all conversations to be resolved.
- Require status checks to pass, including **Flutter CI** and **PR Policy**.
- Block force pushes.
- Block branch deletion.
- Restrict direct contributor pushes to `main`.
- Require the maintainer to perform the final merge; contributors must not merge their own pull requests.

After workflows have run at least once, select their exact check names in the ruleset. Apply the ruleset to administrators too if the project's operating policy requires it.

## Security reporting

Enable GitHub private vulnerability reporting under the repository's security settings so reporters have a private channel.

## Android distribution

The release workflow produces a release APK artifact without production signing configuration. Play Store signing, credentials, and distribution must be designed separately before production release.
