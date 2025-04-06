#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *temp = list;

	while (current)
	{
		if (current->next == temp)
			return (1);
		current = current->next;
	}
	return (0);
}
