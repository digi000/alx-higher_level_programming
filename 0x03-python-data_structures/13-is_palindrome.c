#include <string.h>
#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int hl, ln, lt, sz;
	int *ar = malloc(sizeof(int) * 1);
	
	if (head == NULL)
		return (1);
	ln = 0;
	current = *head;
	sz = 1;
	while (current)
	{
		ar[ln] = current->n;
		ln++;
		sz += 1;
		current = current->next;
		if (current)
		{
			ar = realloc(ar, sizeof(int) * sz);
			if (ar == NULL)
				printf("Realloc Failed\n");
		}
	}

	hl = 0;
	lt = ln - 1;
	current = *head;
	while (hl < ln / 2)
	{
		if (ar[hl] != ar[lt])
		{
			free(ar);
			return (0);
		}
		hl++;
		lt--;
	}
	free(ar);
	return (1);
}
