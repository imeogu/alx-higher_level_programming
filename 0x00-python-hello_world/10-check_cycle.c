#include "lists.h"

/**
<<<<<<< HEAD
 * check_cycle - cycle tortoise and hare
 * @list: pointer to head
 * Return: 1 on success, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise;
	listint_t *hare;

	if (list == NULL)
		return (0);
	tortoise = list;
	hare = list;
	while (hare->next != NULL && hare->next->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
		{
			tortoise = list;
			while (tortoise != hare)
			{
				tortoise = tortoise->next;
				hare = hare->next;
			}
			return (1);
		}
=======
* check_cycle - checks if singly linked list has a cycle in it
* @list: linked list
*
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *current = malloc(sizeof(listint_t));

	current = list;
	while (current != NULL)
	{
		if (current->next == list)
		{
			free(current);
			return (1);
		}
		current = current->next;
>>>>>>> ce1f32da5529042a2ebb8d8a3545b39d6b3baae4
	}
	free(current);
	return (0);
}
}
