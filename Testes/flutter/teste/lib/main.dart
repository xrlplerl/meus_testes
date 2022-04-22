import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "teste",
      theme: ThemeData(primarySwatch: Colors.blue),
      home: Home()));
}

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  var num = 0;
  var nom = "Pode entrar";
  void z(int n) {
    setState(() {
      num = num + n;
      if (num < 0) {
        nom = "Mundo inverso";
      } else if (num >= 10) {
        nom = "Cheio";
        num = 10;
      } else {
        nom = "Pode entrar";
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: <Widget>[
        Image.asset("images/wallpaper.jpg", fit: BoxFit.cover, height: 1000.0),
        Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text("Pessoas $num",
                textDirection: TextDirection.ltr,
                style: TextStyle(color: Colors.white, fontSize: 40)),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Padding(
                  padding: EdgeInsets.all(10),
                  child: FlatButton(
                    child: Text("+1",
                        textDirection: TextDirection.ltr,
                        style: TextStyle(color: Colors.white, fontSize: 30)),
                    onPressed: () {
                      z(1);
                    },
                  ),
                ),
                Padding(
                  padding: EdgeInsets.all(10),
                  child: FlatButton(
                    child: Text("-1",
                        textDirection: TextDirection.ltr,
                        style: TextStyle(color: Colors.white, fontSize: 30)),
                    onPressed: () {
                      z(-1);
                    },
                  ),
                ),
              ],
            ),
            Text("$nom",
                textDirection: TextDirection.ltr,
                style: TextStyle(color: Colors.white, fontSize: 35))
          ],
        )
      ],
    );
  }
}
