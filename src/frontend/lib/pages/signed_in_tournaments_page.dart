import 'package:flutter/material.dart';

class SignedInTournamentsPage extends StatefulWidget {
    const SignedInTournamentsPage({super.key});

    @override
    State<SignedInTournamentsPage> createState() => _SignedInTournamentsPage();
}

class _SignedInTournamentsPage extends State<SignedInTournamentsPage> {
    @override
    Widget build(BuildContext context) {
        return Scaffold(
            body: Center(
            child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                        Text("Signed in tournaments page")
                    ],
                ),
            ),
        );
    }
}
