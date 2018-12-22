public class ArmstrongNumberIntervals
 {

    public static void main(String[] args) 
 	{
          int low = 100, high = 2000;

	        for(int num = low + 1; num < high; ++num)
		 {
        	    int d = 0;
            	    int r = 0;
            	    int o = num;
            	   while (o != 0) 
			{
                	  o /= 10;
                	  ++d;
      		         }

                     o = num;
        	    while (o!= 0) 
			{
                	int rem= o % 10;
                	r += Math.pow(rem, d);
                	o /= 10;
            		}

         	       if (r == num)
        	       System.out.print(num + " ");
      	        }
     }
}
