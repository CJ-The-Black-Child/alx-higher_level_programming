#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: is an integer
 * @next: it points to the next node
 *
 * Desc: This is a singly linked list node structure declaration
 *
 */

typedef struct listint_s
{
	int n;
	struct listint *next;
} listint_t

size_t print_listint(const lisint_t *h);
listint_t *add_nodoeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif
