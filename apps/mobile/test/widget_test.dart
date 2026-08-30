import 'package:binaru_mobile/app/binaru_app.dart';
import 'package:binaru_mobile/shared/development/development_screen.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('BinaruApp renders', (WidgetTester tester) async {
    await tester.pumpWidget(const BinaruApp());

    expect(find.byType(DevelopmentScreen), findsOneWidget);
  });

  testWidgets('development screen shows the Binaru foundation', (
    WidgetTester tester,
  ) async {
    await tester.pumpWidget(const BinaruApp());

    expect(find.text('Binaru'), findsOneWidget);
    expect(find.text('Main. Jelajah. Bertumbuh.'), findsOneWidget);
    expect(find.text('Tombol Utama'), findsOneWidget);
  });
}
