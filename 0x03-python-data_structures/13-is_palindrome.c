#include "lists.h"
#include <stdlib.h>

/**
	* cpy_linked_list - makes a new copy of a linked list
	* Description: makes a new copy of a linked list
	* Return: listint_t
*/
listint_t *copy_linked_list(listint_t **head)
{
	listint_t *h;
	listint_t *current = *head;

	h = NULL;
	while (current != NULL)
	{
		add_nodeint_end(&h, current->n);
		current = current->next;
	}

	return (h);
}

/**
	* reverse_linked_list - reverses a linked list
	* Description: reverses a linked list
	* Return: reversed linked list
*/
listint_t *reverse_linked_list(listint_t **head)
{
	listint_t *current;
	listint_t *prev = NULL;
	listint_t *next = NULL;

	current = copy_linked_list(head);

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
	* get_length - returns the length of a linked list
	* Description: returns the length of a linked list
	* Return: int
*/
int get_length(listint_t *head)
{
	listint_t *current = head;
	int length = 0;

	while (current != NULL)
	{
		length++;
		current = current->next;
	}

	return (length);
}

/**
	* is_palindrom - checks if a linked lists is a palindrome
	* Description: checks if a linked lists is a palindrome
	* Return: int
*/
int is_palindrome(listint_t **head)
{
	listint_t *reversed_list;
	listint_t *current;
	int length;
	int i = 0;

	if (*head == NULL)
		return (1);

	reversed_list = reverse_linked_list(head);
	current = *head;
	length = get_length(current);

	while (i < length)
	{
		if (current->n != reversed_list->n)
			return (0);
		i++;
		reversed_list = reversed_list->next;
		current = current->next;
	}

	return (1);
}
