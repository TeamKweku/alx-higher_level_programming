#include <stddef.h>
#include "lists.h"
/**
  * reverse_linkedlist - a function that reverses a linked list
  * @head: pointer to head of list
  *
  * Return: reversed linked list
  */
listint_t *reverse_linkedlist(listint_t *head)
{
	listint_t *prev = NULL, *current = head;
	listint_t *next_node;

	while (current != NULL)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}

	return (prev);
}

/**
  * is_palindrome - function that checks if a singly linked
  * list is a palindrome
  * @head: pointer to address to begining of list
  *
  * Return: 1 or 0 if palindrome or not
  */
int is_palindrome(listint_t **head)
{
	listint_t *first_half, *second_half;
	listint_t *slow = *head;
	listint_t *fast = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	first_half = *head;
	second_half = reverse_linkedlist(slow->next);

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
			return (0);
		first_half = first_half->next;
		second_half = second_half->next;
	}

	return (1);
}
