#include <stdio.h>

// Programa simples de adição de dois inteiros.
int main (void)
{
    int inteiro1; //Declara a variável do primeiro inteiro.
    int inteiro2; //Declara a variável do segundo inteiro.
    int soma; //Declara a variável que armazenará o resultado da soma.

    printf("Digite o primeiro inteiro\n"); //Imprime a ordem para o usuário na tela.
    scanf("%d", &inteiro1); //Recebe o input do usuário, e armaneza o valor na variável inteiro1.

    printf("Digite o segundo inteiro\n");//Faz a mesma coisa que o comentário anterior, com a variável inteiro2.
    scanf("%d", &inteiro2);

    soma = inteiro1 + inteiro2; /*Realiza a soma dos valores informados pelo usuário,
                                 e armazena o resultado na variável soma. */

    printf("A soma é %d\n", soma); //Imprime o resultado da soma dos dois inteiros.

    return 0;
}
