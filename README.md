# Binaru

[![Flutter CI](https://github.com/yogaananda6677/binaru_apps/actions/workflows/flutter-ci.yml/badge.svg)](https://github.com/yogaananda6677/binaru_apps/actions/workflows/flutter-ci.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

Binaru is an offline-first adaptive learning app for children ages 5–7, built with Flutter, featuring skill mastery, personalized learning experiences, interactive activities, and parent insights.

## About Binaru

Binaru aims to make foundational learning playful, adaptive, and accessible even without a continuous internet connection. Its first MVP focuses on basic numeracy.

## Project Status

**Pre-development / MVP architecture stage.** The repository has been bootstrapped, but product architecture and feature implementation have not begun.

## MVP Scope

The initial Android MVP will focus on basic numeracy, interactive learning activities, skill-mastery progression, personalized experiences, and useful parent insights. See the [Product Requirements Document](docs/PRD.md) for the current product scope.

## Tech Stack

- Flutter and Dart
- Android as the initial target platform
- GitHub Actions for continuous integration

Architecture, persistence, navigation, state management, and other technology choices remain pending and must be documented through Architecture Decision Records.

## Repository Structure

```text
apps/mobile/   Flutter Android application
design/        Future design references and assets
docs/          Product, architecture, ADR, and maintainer documentation
.github/       Contribution templates and automation
```

## Getting Started

### Prerequisites

- A current stable [Flutter SDK](https://docs.flutter.dev/get-started/install)
- Android Studio or the Android SDK and a configured emulator/device
- Git

Verify the environment with `flutter doctor` before continuing.

### Running the Mobile App

```bash
cd apps/mobile
flutter pub get
flutter run
```

## Code Quality

From `apps/mobile`, format and analyze changes before opening a pull request:

```bash
dart format .
flutter analyze
```

## Testing

```bash
cd apps/mobile
flutter test
```

## Documentation

- [Product Requirements](docs/PRD.md)
- [Architecture status](docs/ARCHITECTURE.md)
- [Maintainer Guide](docs/MAINTAINER_GUIDE.md)

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before beginning work. Binaru uses an Issue-first workflow.

### Contribution Workflow

Issue → discussion → fork → branch → implementation → tests → pull request → maintainer review → merge

Never push directly to `main`, and do not merge your own pull request.

## Release Strategy

Semantic version tags (`v*.*.*`) trigger validation and a release APK build without production signing configuration. Google Play signing and distribution will be designed later; the current workflow does not deploy to Google Play.

## License

Source code is licensed under the [Apache License 2.0](LICENSE). The Binaru name, logo, characters, and other brand assets are not granted as trademarks by the source-code license.
