def spiral(W,H,Y,X,D):#top down view of a spiral 	   	 		 				 		  
    # W width H height X & Y point of start X = left or right Y = top or bottom D direction of spiral horizontal or vertical 	   	 		 				 		   	 		 				 		  
 	   	 		 				 		  
    if(D == "h" and X == "l" and Y == "t"):
        r = W - 1 	   	 		 				 		  
        l = 0 	   	 		 				 		  
        u = 0 	 		 				 		  
        d = 1   

        for i in range(1,H+1):#print H lines 	   	 		 				 		  	 		 				 		  
 	   	 		 				 		  
            print(u * "^", r * ">", l * "<", d * "v", sep="")

            if i <= 2:
                r-=1
                d+=1
            if i >= H-2:
                r = 0
                d -=1
                u = i - H + 1
                l = W - u - d
            elif i > 2 and i < H-2:
                u+=1 
                u = d
                d-=1
	   	 		 		

spiral(5,5,"t","l","h")		 		  