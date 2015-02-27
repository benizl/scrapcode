
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

int data[2][2];
int currentSlot[2];
int lastWrittenPair = 1, lastReadPair = 1;

static void *readerLoop(void *priv)
{
	int readPair, readSlot;
	int item;

	while(1) {
		readPair = lastWrittenPair;
		lastReadPair = readPair;
		readSlot = currentSlot[readPair];
		__sync_synchronize();
		item = data[readPair][readSlot];
		printf("r:%d::%d %d\n", item, readPair, readSlot);
		sleep(1);
	}

	return NULL;
}

static void *writerLoop(void *priv)
{
	int writePair, writeSlot;
	int item = 0;

	while(1) {
		item++;

		writePair = !lastReadPair;
		writeSlot = !currentSlot[writePair];
		data[writePair][writeSlot] = item;
		__sync_synchronize();
		currentSlot[writePair] = writeSlot;
		lastWrittenPair = writePair;
		printf("w:%d::%d %d\n", item, writePair, writeSlot);
		sleep(1);
	}

	return NULL;
}

int main(int argc, char **argv)
{

	pthread_t r, w;

	pthread_create(&r, NULL, readerLoop, NULL);
	pthread_create(&w, NULL, writerLoop, NULL);

	pthread_join(r, NULL);
	pthread_join(w, NULL);

	return 0;
}

