#include<stdio.h>
#include<conio.h>
void main()
{
char s;
clrscr();
printf("enter the character");            

scanf("%c",&s);
if(s>='a'&&s<='z'||s>='A'&&s>='Z')
{
printf("it is character");
}
else
{
printf("it is not a character");
}
getch();
}                        
