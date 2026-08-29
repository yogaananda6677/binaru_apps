import 'package:flutter/material.dart';

class BinaruApp extends StatelessWidget {
  const BinaruApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Binaru',
      home: Scaffold(
        body: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text('Binaru', style: Theme.of(context).textTheme.headlineLarge),
              const SizedBox(height: 8),
              const Text('Main. Jelajah. Bertumbuh.'),
            ],
          ),
        ),
      ),
    );
  }
}
