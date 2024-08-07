#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORDS 100
#define MAX_WORD_LEN 50

void toLowerCase(char str[]) {
    for (int i = 0; str[i]; i++) {
        str[i] = tolower(str[i]);
    }
}

int main() {
    char paragraph[1000], word[MAX_WORDS][MAX_WORD_LEN];
    int count[MAX_WORDS] = {0};
    int wordIndex = 0, i, j;

    printf("Enter a paragraph:\n");
    gets(paragraph);

    char *token = strtok(paragraph, " ,.?!;\n");
    while (token != NULL) {
        toLowerCase(token);
        for (i = 0; i < wordIndex; i++) {
            if (strcmp(word[i], token) == 0) {
                count[i]++;
                break;
            }
        }
        if (i == wordIndex) {
            strcpy(word[wordIndex], token);
            count[wordIndex]++;
            wordIndex++;
        }
        token = strtok(NULL, " ,.?!;\n");
    }

    printf("\nWord Frequencies:\n");
    for (i = 0; i < wordIndex; i++) {
        printf("%s: %d\n", word[i], count[i]);
    }

    return 0;
}
