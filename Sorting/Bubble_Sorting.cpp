#include <stdio.h>

int main()
{
    int Arr[10];
    int i, m, n, temp;
    printf("Please input 10 numbers:\n");
    for (i = 0; i < 10 ; i++)
    {
        scanf("%d", &Arr[i]);
    }
    for ( m = 0; m < 10; m++)
        for (n = 0; n < 9; n++)
            if (Arr[n-1]>Arr[n])
            {
                temp = Arr[n-1];
                Arr[n-1] = Arr[n];
                Arr[n] = temp;
            }

    printf("The Sorted Numbers are:\n");
    for (i = 0; i < 10 ; i++)
    {
        printf("%d ", Arr[i]);
    }

    return 0;
}