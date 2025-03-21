import 'package:flutter/material.dart';

class SearchTournamentsPage extends StatefulWidget {
    const SearchTournamentsPage({super.key});

    @override
    State<SearchTournamentsPage> createState() => _SearchTournamentsPageState();
}

class _SearchTournamentsPageState extends State<SearchTournamentsPage> {
    @override
    Widget build(BuildContext context) {
        return Scaffold(
            body: SingleChildScrollView(
                child: Column(
                    children: [
                        Container(
                            padding: EdgeInsets.only(top: 40, right: 20, left: 20),
                            child: Row(
                                children: [
                                    Expanded(flex: 2, child: AgeClassesDropdownMenu(),),
                                    Expanded(flex: 1, child: SearchButton(),)
                                ],         
                            ),
                        ),
                        Container(
                        padding: EdgeInsets.only(bottom: 20, top: 13, left: 5, right: 5),
                            child: Row(
                                children: [
                                    Expanded(
                                        child: Column(
                                            children: [
                                                Card(
                                                    color: Colors.white,
                                                    child: Column(
                                                        children: [
                                                            Text("Academy Cup - DTB Jugend"),
                                                            Row(
                                                                children: [
                                                                    Expanded(flex: 1, child: Text("29.03.2025")),
                                                                    Expanded(flex: 1, child: Text("8 Tage"))
                                                                ],
                                                            ),
                                                            Row(
                                                                children: [
                                                                    Expanded(flex: 1, child: Text("Berliner Str. 83")),
                                                                    Expanded(flex: 1, child: Text("500 KM"))
                                                                ],
                                                            )
                                                        ],
                                                    ),
                                                )
                                            ],
                                        ),
                                    ),
                                    Expanded(
                                        child: Column(
                                            children: [
                                                Card(
                                                    color: Colors.white,
                                                    child: Column(
                                                        children: [
                                                            Text("Academy Cup - DTB Jugend"),
                                                            Row(
                                                                children: [
                                                                    Expanded(flex: 1, child: Text("29.03.2025")),
                                                                    Expanded(flex: 1, child: Text("8 Tage"))
                                                                ],
                                                            ),
                                                            Row(
                                                                children: [
                                                                    Expanded(flex: 1, child: Text("Berliner Str. 83")),
                                                                    Expanded(flex: 1, child: Text("500 KM"))
                                                                ],
                                                            )
                                                        ],
                                                    ),
                                                )
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        )
                    ],
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
            items: <String>['M18', 'M16', 'M14', 'M13', 'M12', 'M11', 'W18', 'W16', 'W14', 'W13', 'W12', 'W11']
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
