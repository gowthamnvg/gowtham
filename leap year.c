#include<stdio.h>
#include<conio.h>
void main()
{
int a;
clrscr();
scanf("%d",&a);
if(a%100!=0&&a%400!=0||a%4==0)
printf("it is aleap year");
else
printf("it is not leap year");
getch();
}
