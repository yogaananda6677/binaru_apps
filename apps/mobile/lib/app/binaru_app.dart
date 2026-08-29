import 'package:flutter/material.dart';

import '../core/theme/binaru_theme.dart';
import '../shared/development/development_screen.dart';

class BinaruApp extends StatelessWidget {
  const BinaruApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Binaru',
      debugShowCheckedModeBanner: false,
      theme: BinaruTheme.light,
      home: const DevelopmentScreen(),
    );
  }
}
