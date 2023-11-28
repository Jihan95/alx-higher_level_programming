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
	listint_t *temp, *prev, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (head == NULL)
	{
		*head = new;
		return (new); }
	temp = *head;
	prev = NULL;
	while(temp != NULL && number > temp->n)
	{
		prev = temp;
		temp = temp->next; }
	if (prev == NULL)
	{
		new->next = *head;
		*head = new; }
	else
	{
		prev->next = new;
		new->next = temp; }
	return (new); }
