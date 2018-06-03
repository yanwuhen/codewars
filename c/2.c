#include <stdio.h>
#include <stdlib.h>

int removeDuplicates(int* nums, int numsSize) {
    int *dup = malloc(numsSize * sizeof(int));
    int dupSize = 0;
    int i,j;
    for(i=0;i<numsSize;i++) {
        int isDup = 0;
        for(j=0;j<dupSize;j++) {
            if(nums[i] == dup[j]) {
                isDup = 1;
            }    
        }
        if(isDup) {
            continue;
        }
        dup[dupSize++] = nums[i];
    }
    for(i=0;i<dupSize;i++) {
        nums[i] =dup[i];
    }
    return dupSize;
}

int main() {
    int nums[] = {1,2,1,2};
    int newsize = removeDuplicates(nums, 3);
    for(int i=0;i<newsize;i++) {
        printf("%d,", nums[i]);
    }
}