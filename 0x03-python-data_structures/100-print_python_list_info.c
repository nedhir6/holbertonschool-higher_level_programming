#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * print_python_list_info - function that prints python list
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
int i;
PyObject *po;
Py_ssize_t psize;

psize = PyList_Size(p);
printf("[*] Size of the Python List = %li\n", psize);
printf("[*] Allocated = %li\n", (((PyListObject *)p)-> allocated));
for (i = 0; i < psize; i++)
{
	po = PyList_GetItem(p, i);
	printf("Element %i: %s\n", i, Py_TYPE(po)->tp_name);
}
}
