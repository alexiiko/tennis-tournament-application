import 'dart:convert';
import 'package:http/http.dart' as http;
import 'db_credentials.dart';

void returnTournamentsFromAgeClass (String ageClass) async {
  final response = await http.post(
    Uri.parse(url),
    headers: {
      'Authorization': 'Bearer $authToken',
      'Content-Type': 'application/json',
    },
    body: jsonEncode({
      "requests": [
        {"type": "execute", "stmt": {"sql": "SELECT link FROM $ageClass"}},
        {"type": "close"},
      ],
    }),
  );

  if (response.statusCode == 200) {
    print(jsonDecode(response.body));
  } else {
    print('Error: ${response.statusCode}, ${response.body}');
  }
}

void main() {
    var ageClassArray = ["M11", "M12", "M13", "M14", "M16", "M18"];
    for (var i = 0; i < ageClassArray.length; i++) {
        returnTournamentsFromAgeClass(ageClassArray[i]);
        print("\n");
    }
}
