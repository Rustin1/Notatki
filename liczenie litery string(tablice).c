#include <stdio.h>
#include <string.h>

size_t letter_count( const char *s, char c )
{
    size_t n = 0;
    if ( c != '\0' )
    {
        for ( const char *p = s; ( p = strchr( p, c ) ) != NULL; ++p )
        {
            ++n;
        }
    }

    return n;
}

int main(void)
{
    char words[] = "hahaha";
    char c= 'a';
    printf( "Litera %c pojawia sie %zu razy w tym napisie.\n",
            c, letter_count( words, c ) );
    return 0;
}
