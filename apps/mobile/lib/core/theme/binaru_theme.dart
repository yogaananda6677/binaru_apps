import 'package:flutter/material.dart';

import 'binaru_colors.dart';
import 'binaru_radii.dart';
import 'binaru_spacing.dart';

abstract final class BinaruTheme {
  static ThemeData get light {
    const colorScheme = ColorScheme(
      brightness: Brightness.light,
      primary: BinaruColors.forestGreen,
      onPrimary: BinaruColors.cream,
      secondary: BinaruColors.warmYellow,
      onSecondary: BinaruColors.darkBrown,
      error: BinaruColors.coral,
      onError: BinaruColors.darkBrown,
      surface: BinaruColors.cream,
      onSurface: BinaruColors.primaryText,
    );

    return ThemeData(
      colorScheme: colorScheme,
      scaffoldBackgroundColor: BinaruColors.cream,
      textTheme: const TextTheme(
        headlineLarge: TextStyle(
          color: BinaruColors.primaryText,
          fontSize: 40,
          fontWeight: FontWeight.w700,
        ),
        bodyLarge: TextStyle(
          color: BinaruColors.secondaryText,
          fontSize: 18,
          fontWeight: FontWeight.w600,
        ),
        labelLarge: TextStyle(fontSize: 18, fontWeight: FontWeight.w700),
      ),
      filledButtonTheme: FilledButtonThemeData(
        style: FilledButton.styleFrom(
          minimumSize: const Size(200, 56),
          padding: const EdgeInsets.symmetric(
            horizontal: BinaruSpacing.lg,
            vertical: BinaruSpacing.md,
          ),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(BinaruRadii.lg),
          ),
        ),
      ),
    );
  }
}
