import 'dart:convert';
import 'package:http/http.dart' as http;

void main() async {
  final url = "https://tournaments-alexiiko.turso.io/v2/pipeline";
  final authToken = "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NDI1NTc4ODcsImlkIjoiY2Q2YWU3ODItZDExYy00YjM2LTg4ZmQtZmUzODdlMTY4NmE1In0.84CZOwb9ObGS2YnOG_L4H8LN-GXriXXk44arpgNvBX9J1Dgc52npPSle8EYn5UewCRw3H3iJG0-sQrW_vMRfAw";

  final response = await http.post(
    Uri.parse(url),
    headers: {
      'Authorization': 'Bearer $authToken',
      'Content-Type': 'application/json',
    },
    body: jsonEncode({
      "requests": [
        {"type": "execute", "stmt": {"sql": "SELECT link FROM M12"}},
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
