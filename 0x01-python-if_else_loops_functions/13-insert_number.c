#include <stdlib.h>
#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;
	listint_t *temp;

	current = *head;
	while (current)
	{
		if (current->next)
		{
		if (current->next->n > number)
		{
			temp = current->next;
			new = malloc(sizeof(listint_t));
			current->next = new;
			new->n = number;
			new->next = temp;
			return current;
		}
		}
		current = current->next;
	}
	return (NULL);
}
