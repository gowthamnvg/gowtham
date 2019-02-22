import java.io.*;
import java.util.*;
class Array
{
public static void main(String args[])
{
 Scanner sc=new Scanner(System.in);
System.out.print("Enter the array size");
int a=sc.nextInt();
int array[]=new int[a];
System.out.print("Enter the array elements");
for(int i=0;i<a;i++)
{
array[i]=sc.nextInt();
}
System.out.print("Entered elements");
for(int i=0;i<a;i++)
{
System.out.println(array[i]); 
}
int max = array[0];
for(int i = 0; i < a; i++)
{
if(max < array[i])
{
max = array[i];
}
}
System.out.println("Maximum value:"+max);
}
}
