#include "lists.h"

/**
 * check_cycle - check if the singly linked list has a cycle
 * @list: pointer to head
 * Return: 0 if no, 1 if yes.
 */
int check_cycle(listint_t *list)
{
	listint_t *speed= list;
	listint_t *slow = list;

	if (list == NULL)
		return (0);

	while (speed->next != NULL && speed->next->next != NULL)
	{
		slow = slow->next;
		speed = speed->next->next;

		if (speed == slow)
		{
			slow = list;
			while (slow != speed)
			{
				slow = slow->next;
				speed = speed->next;
			}

			return (1);
		}
	}
	return (0);
}
