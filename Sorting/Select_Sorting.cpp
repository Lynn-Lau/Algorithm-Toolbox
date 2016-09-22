/*
 * Data Structure and Algorithm in C
 * Sorting Algorithm， Select Sorting
 * 
 * Author:Lynn Lau
 * Date:2016/09/22
 */
#include <stdio.h>

int main()
{
    int Arr[8] = {14, 33, 27, 10, 35, 19, 42, 44};
    int Min, temp;

    for (int index = 0; index < 7; index++)
    {
        Min = index;
        for (int m = index; m < 8 ; m++)
        {
            if (Arr[m] < Arr[Min])
                Min = m;
        }
        if (index != Min)
            temp = Arr[Min];
            Arr[Min] = Arr[index];
            Arr[index] = temp;
    }
    for (int i = 0; i < 8; i++)
        printf("%d ", Arr[i]);
    return 0;

}