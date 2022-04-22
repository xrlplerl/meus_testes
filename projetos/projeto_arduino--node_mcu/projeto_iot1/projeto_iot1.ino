#define rele1  D2
#define rele2  D1
#define rele3  D0
int r1 = 0;
int r2 = 0;
int r3 = 0;

void setup(){
  
  pinMode(rele1,OUTPUT);
  pinMode(rele2,OUTPUT);
  pinMode(rele3,OUTPUT);
  Serial.begin(9600);
  Serial.println("Digite o caracter da tomada a ter o estado auterado: ");
  
}

void loop(){
  
  if(Serial.available()!=0){
    char result = Serial.read();
    if(result == '1'){
      if(r1 == 0){
        r1 = 1;
      }
      else{
      	r1 = 0;
      }
    }
    if(result == '2'){
      if(r2 == 0){
        r2 = 1;
      }
      else{
      	r2 = 0;
      }
    }
    if(result == '3'){
      if(r3 == 0){
        r3 = 1;
      }
      else{
      	r3 = 0;
      }
    }
    digitalWrite(rele1,r1);
    digitalWrite(rele2,r2);
    digitalWrite(rele3,r3);
    
  }
  
}
