#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: the head of the list
 * @number: the number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t **temp;
	listint_t *new;

	temp = head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (head == NULL)
	{
		*head = new;
		return (new); }
	if ((*temp)->next == NULL)
	{
		if (number < (*temp)->n)
		{
			new->next = *temp;
			*head = new;
			return (new); }
		new->next = NULL;
		(*temp)->next = new;
		return (new);
	}
	while (number > (*temp)->n && number < (*temp)->next->n)
		*temp = (*temp)->next;
	new->next = (*temp)->next;
	(*temp)->next = new;
	return (new); }
