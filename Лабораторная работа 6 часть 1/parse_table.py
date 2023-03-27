def get_table() -> dict:
    
    with open("table.txt", 'r') as file:
       
        lines = file.readlines() 
          
        matrix = []
        table = {}
        
        for i in lines[1:]:
            matrix.append(i.split())   
        
        for row in matrix:
            for j in range(0, len(row), 2):
                table[row[j+1]] = float(row[j])
    
        table = dict(sorted(table.items()))
        
        #print(len(table))
    
        #for i in table:
        #    print(f'{i}:{table[i]}')
        
        return table