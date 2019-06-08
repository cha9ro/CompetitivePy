#include <stdio.h>

int func(int n, int k);

int main(void){
    int N, out;
    scanf("%d", &N);
    out = func(N, 0);
    printf("%d", out);
    return 0;
}

int func(int n, int k){
    int i6 = 1, i9 = 1;
    while(i6*6 <= n)    i6 *= 6;
    while(i9*9 <= n)    i9 *= 9;
    int n6 = n-i6, n9 = n-i9;
    if (i6==1 && i9==1) return k+n;
    else if (n6==0 || n9==9)    return k+1;
    else if (n6<=n9) func(n6, k+1);
    else    return func(n9, k+1);
}
