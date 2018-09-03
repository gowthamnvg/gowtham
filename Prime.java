import java.io.*;
import java.util.*;
class Prime
{
public static void main(String args[])
{		
System.out.println("Enter any number:");
Scanner scan= new Scanner(System.in);
int num=scan.nextInt();
if(num%2==0)
{
System.out.println("it is a prime number");
 }
else
{
System.out.println("it is not a prime number");
}
}
}
