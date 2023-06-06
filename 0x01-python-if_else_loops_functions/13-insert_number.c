#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - functin that inserts a node in sorted linked
 * listint_t
 * @head: pointer to pointer of head node
 * @number: value to be inserted at sorted position
 *
 * Return: pointer to new address or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *previous;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (number < current->n)
			{
				new->next = current;
				previous->next = new;
				break;
			}
			else
			{
				previous = current;
				current = current->next;
			}
		}
	}

	return (new);
}
