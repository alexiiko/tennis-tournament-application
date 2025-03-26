import 'dart:convert';
import 'package:http/http.dart' as http;
import 'db_credentials.dart';

Future<Map> returnTournamentData(String ageClass) async {
    final response = await http.post(
    Uri.parse(url),
    headers: {
          'Authorization': 'Bearer $authToken',
          'Content-Type': 'application/json',
    },
    body: jsonEncode({
        "requests": [
                {"type": "execute", "stmt": {"sql": "SELECT * FROM $ageClass"}},
                {"type": "close"},
            ],
        }),
    );

    if (response.statusCode == 200) {
        return jsonDecode(response.body);
    } else {
        return jsonDecode(response.body);
    }
}

Future<List> returnTournamentDataFromAgeClass() async {
    var ageClassArray = ["M11", "M12", "M13", "M14", "M16", "M18"];
    var result = await returnTournamentData(ageClassArray[0]);
    var tournamentDataAPI = result["results"][0]["response"]["result"]["rows"];

    var allTournaments = [];

    var tournament = [];

    for (var i = 0; i < tournamentDataAPI.length; i++) {
        for (var j = 1; j < tournamentDataAPI[i].length; j++) {
            tournament.add(tournamentDataAPI[i][j]["value"]);
        }
        allTournaments.add(tournament);
        tournament = [];
    }
    
    return allTournaments;
}
