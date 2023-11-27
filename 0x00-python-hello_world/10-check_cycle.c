#include "lists.h"

/**
 * check_cycle - checks of the single linked list has a cycle
 * @head: the head of the list
 *
 * Return: 0 if there is no cycle, 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *sp = list, *fp = list ->next;

	if (list == NULL || list->next == NULL)
		return (0);
	while (fp != NULL && fp->next != NULL)
	{
		if (sp == fp)
			return (1);
		sp = sp->next;
		fp = fp->next->next; }
	return (0); }
