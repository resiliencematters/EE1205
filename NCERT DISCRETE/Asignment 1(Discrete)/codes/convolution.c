#include <stdio.h>

// below function returns the value of sum till n terms using the formula we got in the end of document
double sum2(int n) {
    return (9.0/6.0) * n * (n+1) * (2*n+1) + (33.0/2.0) * n * (n+1) + 24 * (n+1);
}

// Define the functions x(n) and u(n)
int x(int n) {
    return (3*n + 3)*(3*n + 8);
}

int u(int n) {
    return (n >= 0) ? 1 : 0; // Unit step function u(n)
}

int main() {
    int n, y[5];

    // Convolution sum for the first 5 elements
    for (n = 0; n < 5; n++) {
        y[n] = 0;
        for (int k = 0; k <= n; k++) {
            y[n] += x(k) * u(n - k);
        }
    }

    // Store the first 5 elements of y(n) in a text file
    FILE *fp;
    fp = fopen("y_sequence_through_convolution.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    fprintf(fp, "n\t\ty(n)\n");
    for (n = 0; n < 5; n++) {
        fprintf(fp, "%d\t\t%d\n", n, y[n]);
    }

    fclose(fp);

    double sumvalues[5];

    // Generate the first five terms of the sequence
    for (n = 0; n < 5; n++) {
        sumvalues[n] = sum2(n);
    }

    // Store the first five terms in a text file
    FILE *fp2;
    fp2 = fopen("sequence_values_using_function.txt", "w");
    if (fp2 == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    fprintf(fp2, "n\t\ty(n)\n");
    for (n = 0; n < 5; n++) {
        fprintf(fp2, "%d\t\t%.2f\n", n, sumvalues[n]);
    }

    fclose(fp2);

    

    return 0;

    
}





