import 'package:binaru_mobile/app.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('displays the Binaru app shell', (WidgetTester tester) async {
    await tester.pumpWidget(const BinaruApp());

    expect(find.text('Binaru'), findsOneWidget);
    expect(find.text('Main. Jelajah. Bertumbuh.'), findsOneWidget);
  });
}
