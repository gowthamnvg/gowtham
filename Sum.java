import java.io.*;

import java.util.*;

class Sum

{

public static void main(String args[])

{

int i,n,k,c=0;
System.out.println("enter the value for n");
Scanner s = new Scanner(System.in);
n=s.nextInt();
int [] a=new int[n];
System.out.println("enter  n values\n");
for(i=0;i<n;i++)
{
Scanner s1=new Scanner(System.in);
a[i]=s1.nextInt();
}
System.out.println("enter k values\n");
Scanner s2=new Scanner(System.in);
k=s2.nextInt();
System.out.println("The values\n");
for(i=0;i<k;i++)
{
c=a[i]+c;
}
System.out.println(c);
}
}
