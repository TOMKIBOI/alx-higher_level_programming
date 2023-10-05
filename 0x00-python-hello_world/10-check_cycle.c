#include "lists.h"
/**
* check_cycle - look for singly linked list that has a cycle.
* @list: the head of the linked list.
* Return: 1 for acycle, 0 for no cycle.
*/
int check_cycle(listint_t *list)
{
	listint_t *fiona_gallagher = list;
	listint_t *frank_gallagher = list;

	while (fiona_gallagher != NULL && frank_gallagher != NULL && frank_gallagher->next != NULL)
	{
		fiona_gallagher = fiona_gallagher->next;
		frank_gallagher = frank_gallagher->next->next;

		if (fiona_gallagher == frank_gallagher)
		{
			return (1);
		}
	}

	return (0);
}
