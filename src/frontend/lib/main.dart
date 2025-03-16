import 'package:flutter/material.dart';
import 'package:frontend/pages/search_tournaments_page.dart';
import 'package:frontend/pages/signed_in_tournaments_page.dart';
import 'package:frontend/pages/settings_page.dart';

void main() {
  runApp(const App());
}

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'test',
      home: const SignedInTournamentsPage(), // replace with search tournaments page 
      debugShowCheckedModeBanner: false,
    );
  }
}
