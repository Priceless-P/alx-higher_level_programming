#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *low, *new;
    low = (*head);
    new = malloc(sizeof(listint_t));
    if (!new)
    {
        return NULL;
    }
    new->n = number;
    if (!(*head))
    {
        new->next = NULL;
        low = new;
    }

    if ((*head) == NULL || (*head)->n >= number)
    {
        new->next = (*head);
        (*head) = new;
        return (new);
    }
    while (low->next != NULL && low->next->n <= number)
    {
    
        low = low->next;
    }
    new->next = low->next;
    low->next = new;
    return (new);
}