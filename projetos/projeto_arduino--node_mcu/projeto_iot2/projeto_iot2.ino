#include <ESP8266WiFi.h>

#define LED D2

int estado = 0;
const char* ssid = "F";
const char* pass = "asdflkjh";

WiFiServer server(80);

void setup() {
  
  Serial.begin(9600);
  pinMode(D2,OUTPUT);
  digitalWrite(LED,LOW);
  Serial.println("\n");
  Serial.print(F("Conectando a: "));
  Serial.println(ssid);
  
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, pass);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(F("."));
  }

  Serial.println(F("WiFi connected"));
  server.begin();
  Serial.println("\n");
  Serial.println(F("Servidor inicado"));
  Serial.println(WiFi.localIP());
  
}

void loop() {

  digitalWrite(LED,estado);
  WiFiClient client = server.available();
   
  client.setTimeout(100);

  String req = client.readStringUntil('\r');


  if(req.indexOf(F("/low")) != -1){
    estado = 0;
  }

  else if(req.indexOf(F("/high")) != -1){
    estado = 1;
  }

  else {}


  while (client.available()) {
    client.read();  
  }

  client.print(F("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<!DOCTYPE HTML>\r\n"));
  client.print(F("<html><head><title>PROJETO IOT - Automação de Lampadas</title><meta charset='utf-8'>"));
  client.print(F("<style type='text/css'>*{font-family: 'arial';}body{padding: 20px;}.main_header{max-width: 500px;margin: 0 auto;display: flex;flex-wrap: wrap;justify-content: center;border: 2px solid #999;padding: 20px;border-radius: 40px;}h1{font-size: 2em;padding: 20px;text-align: center;margin-bottom: 40px;}.ligar, .desligar{text-decoration: none;color: #fff;padding: 30px 60px;border-radius: 10px;flex-basis: 100%;margin-bottom: 20px;text-align: center;font-size: 1.5em;font-weight: 700;}.ligar{background-color: #61CE70;}.desligar{background-color: #aa1818;}</style>"));
  client.print(F("</head><body><div class='main_header'><header><h1>PROJETO IOT <br/> Automação de Lampadas</h1></header><a href='http://"));
  client.print(WiFi.localIP());
  client.print(F("/high' class='ligar'>LIGAR</a><a href='http://"));
  client.print(WiFi.localIP());
  client.print(F("/low' class='desligar'>DESLIGAR</a></div></body></html>"));

  digitalWrite(LED,estado);
  
}
