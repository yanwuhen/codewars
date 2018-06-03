#include <stdlib.h>
#include <stdio.h>

int multiply(int a, char *b) {
  return a * (*b-48);
}

int main() {
    char a;
    int b;
    a = '2';
    b = multiply(1, &a);
    printf("%d\n", b);
}