#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("values.dat", "w"); // Open file for writing

    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    int n = 15; // Number of terms
    int sum = 0;
    int a = 3, b = 8;

    for (int i = 0; i <= n; i++) {
        printf("%d * %d\n", a, b);
        sum += (a * b);
        fprintf(fp, "%d\n", sum); 
        a += 3;
        b += 3;

    }

    // Write sum to file
    fclose(fp);

    return 0;
}
