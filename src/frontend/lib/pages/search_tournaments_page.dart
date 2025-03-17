import 'package:flutter/material.dart';
import 'package:libsql_dart/libsql_dart.dart';
import 'package:sqflite/sqflite.dart';

class SearchTournamentsPage extends StatefulWidget {
    const SearchTournamentsPage({super.key});

    @override
    State<SearchTournamentsPage> createState() => _SearchTournamentsPageState();
}

class _SearchTournamentsPageState extends State<SearchTournamentsPage> {
    @override
    Widget build(BuildContext context) {
        return Scaffold(
          body: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Text('Search Tournaments Page'),
              ],
            ),
          ),
        );
    }
}
