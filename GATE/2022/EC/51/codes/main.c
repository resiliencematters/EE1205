#include <stdio.h>
#include <math.h>

#define PI 3.14159265359

int main() {
    FILE *fp;
    fp = fopen("output.dat", "w");

    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    double w, Hw, magnitude_dB;
    for (w = 0.1; w <= 1000; w *= 1.1) {
        Hw = sqrt(1 + 0.0001 * w * w);
        magnitude_dB = 20 * log10(Hw);
        fprintf(fp, "%.6f %.6f\n", log10(w), magnitude_dB);
    }

    fclose(fp);
    return 0;
}
