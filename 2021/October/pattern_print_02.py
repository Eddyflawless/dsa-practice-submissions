
def init(end_length  = 5):
    print(end_length)
    for row in range(1, end_length + 1):
        spaces = " " * (end_length - row)
        pattern = " * " * row
        output = spaces + pattern + spaces
        print(output)
    
    
if __name__ == '__main__':
    init(10)

    """
        output
        -----------
          *          
         *  *         
        *  *  *        
       *  *  *  *       
      *  *  *  *  *      
     *  *  *  *  *  *     
    *  *  *  *  *  *  *    
   *  *  *  *  *  *  *  *   
  *  *  *  *  *  *  *  *  *  
 *  *  *  *  *  *  *  *  *  * 
       
    """