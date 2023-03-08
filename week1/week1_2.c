#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (){

    char a_lower[] = "abcdefghijklmnopqrstuvwxyz";
    char a_upper[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char b_lower[] = "EKSZJTCMXOQUDYLFABGPHNRVIW";
    char b_upper[] = "ekszjtcmxoqudylfabgphnrviw";

    char frase[] = "Pmj tuec xg: fxslSPT{5HK5717H710Y_3N0UH710Y_59533E2J}";

    for(int i = 0; i <(int) strlen(frase); i++) {

        int j;
        if(frase[i] >= 65 && frase[i] <= 90){
        
            for(j = 0; frase[i] != b_upper[j]; j++);
            frase[i] = a_upper[j];

        }
        if(frase[i] >= 97 && frase[i] <= 122){
        
            for(j = 0; frase[i] != b_lower[j]; j++);
            frase[i] = a_lower[j];

        }
    }
    printf("%s\n", frase);

    return 0;
}
