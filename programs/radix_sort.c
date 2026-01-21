static void counting_sort_exp(int a[], int n, int exp) {
    int out[n], count[10] = {0};

    for (int i = 0; i < n; i++)
        count[(a[i] / exp) % 10]++;

    for (int i = 1; i < 10; i++)
        count[i] += count[i - 1];

    for (int i = n - 1; i >= 0; i--) {
        int d = (a[i] / exp) % 10;
        out[--count[d]] = a[i];
    }

    for (int i = 0; i < n; i++) a[i] = out[i];
}

void radix_sort(int a[], int n) {
    int max = a[0];
    for (int i = 1; i < n; i++)
        if (a[i] > max) max = a[i];

    for (int exp = 1; max / exp > 0; exp *= 10)
        counting_sort_exp(a, n, exp);
}
