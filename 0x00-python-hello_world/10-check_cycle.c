#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks if the list is cycle
 * @list: points to list to check
 * Return: 1 if list is cycle, else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list, *new = list;
	
	while (new && new->next)
	{
		current = current->next;
		new = new->next->next;
		if (current == new)
		return (1);
	}
	return (0);
}	
