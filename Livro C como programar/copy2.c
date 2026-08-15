#include <inttypes.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define USE_LTM
#define LTM_DESC
#include <tomcrypt.h>

#define STD_BUF_SIZE 0x100

#define min(a, b) (((a) < (b)) ? (a) : (b))

static const char *TSKEY = "b9dfaa7bee6ac57ac7b65f1094a1c155"
                           "e747327bc2fe5d51c512023fe54a2802"
                           "01004e90ad1daaae1075d53b7d571c30"
                           "e063b5a62a4a017bb394833aa0983e6e";

static void* safealloc(size_t len)
{
    void* result = calloc(1, len);
    if (result == NULL) {
        printf("A memory allocation error ocurred.\n");
        exit(-1);
    }

    return result;
}

static void safefree(void* ptr)
{
    if (ptr != NULL)
    {
        free(ptr);
    }
}







