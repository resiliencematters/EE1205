#include <stdio.h>

// Function to generate the terms of the series and calculate the sum
int generateAndSumSeries(int n) {
    int sum = 0;
    int first = 3;
    int second = 8;
    int i, term;

    printf("Generated series: ");

    for (i = 0; i < n; i++) {
        term = first * second;
        printf("%d ", term);
        sum += term;

        // Update the values for the next term
        first += 3;
        second += 3;
    }

    printf("\n");

    return sum;
}

int main() {
    int n;
    printf("Enter the number of terms: ");
    scanf("%d", &n);

    int sum = generateAndSumSeries(n);
    printf("Sum of the series till %d terms: %d\n", n, sum);

    return 0;
}
