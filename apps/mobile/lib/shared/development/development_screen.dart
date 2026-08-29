import 'package:flutter/material.dart';

import '../../core/theme/binaru_spacing.dart';

/// Temporary visual check for the application foundation.
/// Replaced by the Phase 1 experience.
class DevelopmentScreen extends StatelessWidget {
  const DevelopmentScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(BinaruSpacing.lg),
          child: Center(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  'Binaru',
                  style: Theme.of(context).textTheme.headlineLarge,
                ),
                const SizedBox(height: BinaruSpacing.sm),
                Text(
                  'Main. Jelajah. Bertumbuh.',
                  style: Theme.of(context).textTheme.bodyLarge,
                  textAlign: TextAlign.center,
                ),
                const SizedBox(height: BinaruSpacing.xl),
                FilledButton(
                  onPressed: () {},
                  child: const Text('Tombol Utama'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
