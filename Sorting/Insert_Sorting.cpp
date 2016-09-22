#include <stdio.h>

int main()
{
    int Arr[8] = {14, 33, 27, 10, 35, 19, 42, 44};
    int index, m;
    int temp;
    for (index = 1; index < 8 ; index++)
    {
        temp = Arr[index];
        for (m = index; m>0 && Arr[m-1]>temp; m--)
            Arr[m] = Arr[m-1];
        Arr[m] = temp;

    }
    //printf("hello world\n");
    for (int i = 0; i < 8 ; i++)
        printf("%d ", Arr[i]);
}