#include <stdio.h>

double sum2(int n) {
    return (9.0/6.0) * n * (n+1) * (2*n+1) + (33.0/2.0) * n * (n+1) + 24 * (n+1);
}
int x(int n) {
    return (3*n + 3)*(3*n + 8);
}
int u(int n) {
    return (n >= 0) ? 1 : 0;
}


int main() {
    FILE *fp;
    fp = fopen("output.dat", "w");

    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    int n = 15; // no of terms
    int sum = 0;
    int a = 3, b = 8;
    fprintf(fp,"Writing the sum of n terms through C\n");
    for (int i = 0; i <= n; i++) {
        printf("%d * %d\n", a, b);
        sum += (a * b);
        fprintf(fp, "%d\n", sum); 
        a += 3;
        b += 3;

    }

    // Write sum to file


    int y[5];
    fprintf(fp,"Writing Sum values through convolution\n");

    // Convolution sum for the first 5 elements
    for (n = 0; n < 5; n++) {
        y[n] = 0;
        for (int k = 0; k <= n; k++) {
            y[n] += x(k) * u(n - k);
        }
    }

    // Store the first 5 elements of y(n) in a text file
    

    fprintf(fp, "n\t\ty(n)\n");
    for (n = 0; n < 5; n++) {
        fprintf(fp, "%d\t\t%d\n", n, y[n]);
    }


    double sumvalues[5];
    fprintf(fp,"Generating the first five terms of the seqyence using the formula of y(n)\n");
    // Generate the first five terms of the sequence
    for (n = 0; n < 5; n++) {
        sumvalues[n] = sum2(n);
    }

    // Store the first five terms in a text file
   
    fprintf(fp, "n\t\ty(n)\n");
    for (n = 0; n < 5; n++) {
        fprintf(fp, "%d\t\t%.2f\n", n, sumvalues[n]);
    }

    fclose(fp);

    return 0;
}
