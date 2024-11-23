#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define MAX_READERS 10
#define MAX_WRITERS 10

void *read_function(void *arg);
void *write_function(void *arg);

int readcount = 0;
pthread_mutex_t r_mutex, w_mutex;

int main() {
    int n1, n2;
    pthread_t readers[MAX_READERS], writers[MAX_WRITERS];

    pthread_mutex_init(&r_mutex, NULL);
    pthread_mutex_init(&w_mutex, NULL);

    printf("Enter the number of readers you want to create (max %d):\n", MAX_READERS);
    scanf("%d", &n1);
    printf("Enter the number of writers you want to create (max %d):\n", MAX_WRITERS);
    scanf("%d", &n2);

    if (n1 > MAX_READERS || n2 > MAX_WRITERS) {
        printf("Number of readers or writers exceeds the limit.\n");
        return 1;
    }

    for (int i = 0; i < n1; i++) {
        pthread_create(&readers[i], NULL, read_function, NULL);
    }
    for (int i = 0; i < n2; i++) {
        pthread_create(&writers[i], NULL, write_function, NULL);
    }

    for (int i = 0; i < n1; i++) {
        pthread_join(readers[i], NULL);
    }
    for (int i = 0; i < n2; i++) {
        pthread_join(writers[i], NULL);
    }

    pthread_mutex_destroy(&r_mutex);
    pthread_mutex_destroy(&w_mutex);

    return 0;
}

void *read_function(void *arg) {
    pthread_mutex_lock(&r_mutex);
    readcount++;
    if (readcount == 1) {
        pthread_mutex_lock(&w_mutex);
    }
    pthread_mutex_unlock(&r_mutex);

    printf("Reader %ld is inside\n", pthread_self());
    sleep(3); // Simulate reading

    pthread_mutex_lock(&r_mutex);
    readcount--;
    if (readcount == 0) {
        pthread_mutex_unlock(&w_mutex);
    }
    pthread_mutex_unlock(&r_mutex);

    printf("Reader %ld is leaving\n", pthread_self());
    return NULL;
}

void *write_function(void *arg) {
    printf("Writer %ld is trying to enter\n", pthread_self());
    pthread_mutex_lock(&w_mutex);
    printf("Writer %ld entered the class\n", pthread_self());
    sleep(2); // Simulate writing
    pthread_mutex_unlock(&w_mutex);
    printf("Writer %ld left the class\n", pthread_self());
    return NULL;
}