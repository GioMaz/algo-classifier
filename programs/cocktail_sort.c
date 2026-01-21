void cocktail_sort(int a[], int n) {
    int start = 0, end = n - 1, swapped = 1;
    while (swapped) {
        swapped = 0;
        for (int i = start; i < end; i++)
            if (a[i] > a[i + 1]) {
                int t = a[i]; a[i] = a[i + 1]; a[i + 1] = t;
                swapped = 1;
            }
        end--;
        for (int i = end; i > start; i--)
            if (a[i] < a[i - 1]) {
                int t = a[i]; a[i] = a[i - 1]; a[i - 1] = t;
                swapped = 1;
            }
        start++;
    }
}
