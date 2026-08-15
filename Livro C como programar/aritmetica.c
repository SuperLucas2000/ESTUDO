#include<stdio.h>

int main(void)
{
   printf("Digite dois números: ");

   int número1, número2;

   scanf("%d%d", &número1, &número2);

   printf("a soma dos dois números é %d\n", número1 + número2);
   printf("o produto dos dois números é %d\n", número1 * número2);
   printf("a diferença dos dois números é %d\n", número1 - número2);
   printf("o quociente dos dois números é %d\n", número1 / número2);
   printf("o módulo dos dois números é %d\n", número1 % número2);

}
