import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(primaryColor: Colors.blueAccent),
      title: "v2",
      home: V2()));
}

class V2 extends StatefulWidget {
  @override
  _V2State createState() => _V2State();
}

class _V2State extends State<V2> {
  var im = "images/em.jpg";
  void Nr() {
    setState(() {
      if (im == "images/em.jpg") {
        im = "images/mac.jpg";
      } 
      else {
        im = "images/em.jpg";
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: <Widget>[
        Image.asset(im, fit: BoxFit.cover, height: 1000.0),
        Container(
            width: double.infinity,
            child: Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      FlatButton(
                        child: Text("Ola Seja Bem Vindo",
                            style:
                                TextStyle(color: Colors.white, fontSize: 20)),
                        onPressed: () {
                          Nr();
                        },
                      )
                    ],
                  )
                ],
              ),
            ))
      ],
    );
  }
}
