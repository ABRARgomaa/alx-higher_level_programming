#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the point to check with
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
