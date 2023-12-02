#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int is_palindrome = 1;
	listint_t *slow = *head, *fast = *head, *temp;
	listint_t *prev_slow = NULL, *mid = NULL;

	if (head == NULL || *head == NULL)
		return (is_palindrome);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow->next;
		slow->next = prev_slow;
		prev_slow = slow;
		slow = temp; }
	if (fast != NULL)
		mid = slow->next;
	else
		mid = slow;
	while (mid != NULL)
	{
		if (prev_slow->n != mid->n)
		{
			is_palindrome = 0;
			break; }
		prev_slow = prev_slow->next;
		mid = mid->next; }
	return (is_palindrome); }
