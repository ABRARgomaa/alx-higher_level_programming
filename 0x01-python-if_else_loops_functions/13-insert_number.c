#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - inserts a number
 * @head: head
 * @number: nuber
 * Return: the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		listint_t *c = *head;

		while (c->next != NULL && number > c->next->n)
			c = c->next;
		new->next = c->next;
		c->next = new;
	}
	return (new);
}
