#include "lists.h"
#include <stdio.h>

/**
	* cpy_listint - copies a linked list from src to dest
	* @src: source linked list
	* @dest: destination linked list
	* Description: copies a linked list from src to dest
	* Return: void
*/
void cpy_listint(listint_t *src, listint_t *dest)
{
	int i = 0;
	while (src[i].next != NULL)
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = src[i];
}

/**
	* len_list - returns the length of a linked list
	* Description: returns the length of a linked list
	* Return: int
*/
int len_list(listint_t *list)
{
	int i = 0;
	listint_t *current;

	current = list;
	while (current != NULL)
	{
		current = current->next;
		i++;
	}

	return (i + 1);
}

/**
	* in_list - checks if a node is inside a linked list
	* Description: checks if a node is inside a linked list
	* Return: int
*/
int in_list(listint_t node, listint_t *list)
{
	int i = 0;

	for(; list[i].next != NULL; i++)
	{
		if (list[i].n == node.n && list[i].next == node.next)
			return (1);
	}

	return (list[i].n == node.n && list[i].next == node.next);
}

/**
	* check_cycle - checks if a singly linked list has a cycle in it
	* Description: checks if a singly linked list has a cycle in it
	* Return: int
*/
int check_cycle(listint_t *list)
{
	listint_t *tmpArr = { &list[0] };
	listint_t *current;
	int i = 0;
	int j = 0;

	current = list;
	while (current->next != NULL)
	{
	/* 	/1* if (i != 0 && in_list(*current, tmpArr)) *1/ */
	/* 	/1* { *1/ */
	/* 	/1* 	return (1); *1/ */
	/* 	/1* } *1/ */
		/* tmpArr[j++] = *current; */
		current = current->next;
		i++;
	}
	return (0);
}
