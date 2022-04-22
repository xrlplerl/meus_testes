/*
  O pino clock deve ser ligado ao pino STEP do drive(sinalizado de amarelo).
  E o pino DIR ao próprio DIR do drive (sinalizado de verde).
 */
 

int clock = 8;
int dir = 9;
int tempo =5;
int steps =25;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pins as an output.
  pinMode(clock, OUTPUT);     
  pinMode(dir,OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  
  
  //Move para frente
  
  digitalWrite(dir,HIGH);
  
  for(int i=0;i<=steps;i++){
  digitalWrite(clock, HIGH);   
  delay(tempo);               
  digitalWrite(clock, LOW);    
  delay(tempo);               
  }
  
  
  //Move para trás
  
   digitalWrite(dir,LOW);
   
   delay(1000);
  
  for(int i=0;i<=steps;i++){
  digitalWrite(clock, HIGH);   
  delay(tempo);               
  digitalWrite(clock, LOW);    
  delay(tempo);               
  }
  
  delay(1000);
}
