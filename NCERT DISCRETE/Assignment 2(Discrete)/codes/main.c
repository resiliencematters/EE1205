#include <stdio.h>

double sum2(int n) {
    return 2.0 * n * (n+1) + 10.0 * (n+1);
}
int x(int n) {
    return (4*n+10);
}
int u(int n) {
    return (n >= 0) ? 1 : 0; // Unit step function u(n)
}


int main() {
    FILE *fp;
    fp = fopen("output.dat", "w"); // Open file for writing

    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    int n = 15; // Number of terms
    int a=10;
    int d=4;
    int sum=0;

    // Store the first five terms in a text file
   
    
    for (n = 0; n < 15; n++) {
        fprintf(fp, "%d\n", x(n));
    }
    fclose(fp);

    return 0;
}
