#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the linked list.
 * Return: 0 if it is not a palindrome, 1 if otherwise.
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *next, *mid = NULL;
	int is_palindrome = 1;
	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	while (slow != NULL)
	{
		if (prev->n != slow->n)
		{
			is_palindrome = 0;
			break;
		}
		prev = prev->next;
		slow = slow->next;
	}

	while (mid != NULL)
	{
		next = prev->next;
		prev->next = mid;
		mid = prev;
		prev = next;
	}

	*head = mid;

	return (is_palindrome);
}
