#include <stdio.h>
#include <curl/curl.h>

FILE* f;  

size_t imgwrite(char* buffer, size_t itemsize, size_t nitems, void* ignorethis) 
{
    size_t r = itemsize * nitems;

    fwrite(buffer, itemsize, nitems, f);

    return r;
}

int main(void)
{
    CURL *c = curl_easy_init();
    f = fopen("christ.jpg", "wb");

    curl_easy_setopt(c, CURLOPT_URL, "https://assetsnffrgf-a.akamaihd.net/assets/m/2019604/univ/art/2019604_univ_lsr_lg.jpg");
    curl_easy_setopt(c, CURLOPT_WRITEFUNCTION, imgwrite);



    curl_easy_perform(c); 


    curl_easy_cleanup(c); 
    fclose(f); 
    return 0; 
}
