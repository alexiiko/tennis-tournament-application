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
    return (
            Center(
                child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [ 
                    AgeClassesDropdownMenu(),
                    SearchButton()
                    ]
                ),
            )
        );
    }
}

class AgeClassesDropdownMenu extends StatefulWidget {
    const AgeClassesDropdownMenu({super.key});

    @override
    State<AgeClassesDropdownMenu> createState() => _AgeClassesDropdownMenuState();
}

class _AgeClassesDropdownMenuState extends State<AgeClassesDropdownMenu> {
    String currentAgeClass = "M18";
    
    @override
    Widget build(BuildContext context) {
        return DropdownButton<String>(
            value: currentAgeClass,
            onChanged: (String? otherAgeClass) {
                setState(() {
                    currentAgeClass = otherAgeClass!; 
                });
            },
            items: <String>['M18', 'M16', 'M14', 'M13']
              .map<DropdownMenuItem<String>>((String value) {
            return DropdownMenuItem<String>(
              value: value,
              child: Text(value),
            );
          }).toList(),
            dropdownColor: Colors.white,
            style: const TextStyle(color: Colors.black),
        );
    }
}
 
class SearchButton extends StatefulWidget {
    const SearchButton({super.key});

    @override
    State<SearchButton> createState() => _SearchButtonState();
}

class _SearchButtonState extends State<SearchButton> {
    onButtonPress() {
        return {};
    }

    @override
    Widget build(BuildContext context) {
        return ElevatedButton(
            onPressed: onButtonPress,
            style: ElevatedButton.styleFrom(
                backgroundColor: Colors.white,
                foregroundColor: Colors.black,
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10)
                ),
            ),
            child: Icon(Icons.search),
        );
    }
}
