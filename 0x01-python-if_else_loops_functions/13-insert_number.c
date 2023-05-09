#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a new node into a sorted linked list
 * @head: Pointer to a pointer to the head node of the list
 * @number: The integer value to be stored in the new node
 *
 * Return: Pointer to the new node or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	current = *head;
	while (current->next != NULL && number > current->next->n)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
