# Application Foundation

## Purpose

Phase 0 provides the smallest consistent Flutter foundation for future Binaru work. It proves application bootstrapping and the initial visual direction without implementing a product feature.

## Current Structure

```text
lib/
├── main.dart
├── app/
│   └── binaru_app.dart
├── core/
│   └── theme/
│       ├── binaru_colors.dart
│       ├── binaru_radii.dart
│       ├── binaru_spacing.dart
│       └── binaru_theme.dart
└── shared/
    └── development/
        └── development_screen.dart
```

`main.dart` starts `BinaruApp`. The app root configures `MaterialApp`, applies the shared theme, and currently selects the temporary development screen.

## Design-system Foundation

- `BinaruColors` is the single source for the approved Phase 0 palette.
- `BinaruSpacing` provides the `xs` through `xxl` spacing scale.
- `BinaruRadii` provides reusable rounded-surface values.
- `BinaruTheme.light` supplies the cream background, green primary actions, readable text defaults, and a large rounded `FilledButton` style.

Baloo 2 and Nunito are the intended display and body families. No verified font assets exist in the repository, so Phase 0 intentionally uses system fallbacks and adds no runtime font dependency.

## App Bootstrap Flow

```text
main()
→ runApp(BinaruApp)
→ MaterialApp with BinaruTheme.light
→ DevelopmentScreen
```

The development screen is a temporary visual check, not a splash or welcome screen. It will be replaced in Phase 1.

## Testing

Widget tests verify that `BinaruApp` renders, selects the temporary screen, and displays the Binaru title, tagline, and primary button.

## Limitations

- The primary button is intentionally inert.
- No production screen, navigation, state management, persistence, content, audio, analytics, or learning logic exists.
- Aru artwork and Rive integration are not included.
- The theme is a foundation, not a complete reproduction of final designs.

## Extension Points

Phase 1 can replace `DevelopmentScreen` with its approved entry experience while reusing the existing tokens and theme. Any choice that establishes a broader architectural convention or adds a package must be justified by an active requirement and recorded through an ADR when significant.
