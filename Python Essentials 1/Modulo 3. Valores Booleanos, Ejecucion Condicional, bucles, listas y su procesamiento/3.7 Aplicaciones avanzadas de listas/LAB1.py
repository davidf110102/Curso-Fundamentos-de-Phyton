
tablero = [["" for _ in range(8)] for _ in range(8)]

tablero[0][0] = "torre"    
tablero[0][1] = "caballo"  
tablero[0][2] = "alfil"     
tablero[0][3] = "reina"     
tablero[0][4] = "rey"       
tablero[0][5] = "alfil"     
tablero[0][6] = "caballo"  
tablero[0][7] = "torre"   
for i in range(8):
    tablero[1][i] = "peon"   

# Piezas blancas
tablero[7][0] = "torre"    
tablero[7][1] = "caballo"  
tablero[7][2] = "alfil"    
tablero[7][3] = "reina"    
tablero[7][4] = "rey"      
tablero[7][5] = "alfil"     
tablero[7][6] = "caballo"   
tablero[7][7] = "torre"     
for i in range(8):
    tablero[6][i] = "peon"   


for fila in tablero:
    print(fila)
