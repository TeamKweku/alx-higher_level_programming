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
	listint_t *current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (current == NULL || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current && current->next &&
			current->next->n < number)
		current = current->next;
	new->next = current->next;
	current->next = new;

	return (new);
}
