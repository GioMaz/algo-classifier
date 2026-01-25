#include <string.h>

void counting_sort(int a[], int n, int max) {
    int count[max + 1];
    memset(count, 0, sizeof(count));

    for (int i = 0; i < n; i++) count[a[i]]++;

    for (int i = 0, k = 0; i <= max; i++)
        while (count[i]--) a[k++] = i;
}
