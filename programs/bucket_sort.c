// #include <stdlib.h>

void bucket_sort(int a[], int n, int max) {
    int **buckets = calloc(n, sizeof(int *));
    int count[n];
    for (int i = 0; i < n; i++) {
        buckets[i] = calloc(n, sizeof(int));
        count[i] = 0;
    }

    for (int i = 0; i < n; i++) {
        int idx = (a[i] * n) / (max + 1);
        buckets[idx][count[idx]++] = a[i];
    }

    int k = 0;
    for (int i = 0; i < n; i++) {
        insertion_sort(buckets[i], count[i]);
        for (int j = 0; j < count[i]; j++)
            a[k++] = buckets[i][j];
        free(buckets[i]);
    }
    free(buckets);
}
