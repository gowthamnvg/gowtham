import java.io.*;
class ArmstrongNumber
 {  
    public static void main(String[] args)  	
    {  
      int c=0,a,t;  
      int n=153;  
      t=n;  
      while(n>0)  
      {  
       a=n%10;  
       n=n/10;  
       c=c+(a*a*a);  
      }  
      if(t==c)  
      System.out.println("yes");   
      else  
      System.out.println("No");   
    }  
 }  
