import java.io.*;
import java.util.*;
class Even numbers
{
public static void main(String args[])
{
System.out.println("Enter the starting number:");
Scanner s=new Scanner(System.in);
int a=s.nextInt();
System.out.println("Enter the ending number:");
int b=s.nextInt();
int i;
for(i=a; i<=b; i++)
{
if(i%2==0)
{
System.out.println(i);
}
}
}
}
