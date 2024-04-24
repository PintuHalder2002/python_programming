
def two_level_sort(scores):
    mini=scores[0]
    while scores!=[] :
        for i in range(len(scores)):
            l=[]
            if scores[i][1] < mini :
                  mini=scores[i]
                  if (scores[i][1]==mini and scores[i][0]<mini[0]):
                    mini=scores[i]
                    
                                           
                        
                        
                  
    
    




