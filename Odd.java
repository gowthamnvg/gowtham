import java.io.*;
import java.util.*;
class Odd
{
public static void main(String args[])
{
Scanner scan= new Scanner(System.in);		
System.out.println("Enter first number:");
int num1=scan.nextInt();
System.out.println("Enter second number:");
int num2=scan.nextInt();
for(int j=num1;j<num2;j++)
{
if(num1%2!=0)
{
System.out.println(num1);
 }
num1=num1+1;
}
}
}
