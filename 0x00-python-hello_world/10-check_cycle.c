#include "lists.h"
/**
  * check_cycle - function that checks for loop in a linked list
  * @list: pointer to provided list
  *
  * Return: 0 if there is no cycle, 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr;
	listint_t *fast_ptr;

	if (!list)
		return (2);
	slow_ptr = fast_ptr = list;

	while (fast_ptr != NULL && fast_ptr->next != NULL &&
			slow_ptr != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;

		if (slow_ptr == fast_ptr)
			return (1);
	}

	return (0);
}

