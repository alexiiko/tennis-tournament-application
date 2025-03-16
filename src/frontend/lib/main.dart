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
      home: NavigationBar(),
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primaryColor: Colors.white,
        scaffoldBackgroundColor: Colors.white,

        bottomNavigationBarTheme: BottomNavigationBarThemeData(
            backgroundColor: Colors.white,
            selectedItemColor: Colors.black,
            unselectedItemColor: Colors.grey
        )
      ),
    );
  }
}

class NavigationBar extends StatefulWidget {
    @override 
    _NavigationBarState createState() => _NavigationBarState();
}

class _NavigationBarState extends State<NavigationBar> {
    int _selectedPageIndex = 0;

    final List<Widget> _pages = [
        SearchTournamentsPage(),
        SignedInTournamentsPage(),
        SettingsPage()
    ];

    void _onTappedPage(int pageIndex) {
        setState(() {
            _selectedPageIndex = pageIndex;
        });
    }

    @override 
    Widget build(BuildContext context) {
        return Scaffold(
            body: _pages[_selectedPageIndex],
            bottomNavigationBar: BottomNavigationBar(
                items: [
                    BottomNavigationBarItem(label: "Turniere suchen", icon: Icon(Icons.search)),
                    BottomNavigationBarItem(label: "angemeldete Turniere", icon: Icon(Icons.description)),
                    BottomNavigationBarItem(label: "Einstellungen", icon: Icon(Icons.settings)),
                ],
                currentIndex: _selectedPageIndex,
                onTap: _onTappedPage,
            ),
        );
    }
}
