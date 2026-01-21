void comb_sort(int a[], int n) {
    int gap = n;
    const float shrink = 1.3;
    int sorted = 0;

    while (!sorted) {
        gap = (int)(gap / shrink);
        if (gap <= 1) { gap = 1; sorted = 1; }

        for (int i = 0; i + gap < n; i++)
            if (a[i] > a[i + gap]) {
                int t = a[i]; a[i] = a[i + gap]; a[i + gap] = t;
                sorted = 0;
            }
    }
}
