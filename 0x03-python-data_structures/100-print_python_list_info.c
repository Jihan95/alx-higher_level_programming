#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <Python.h>
#include <listobject.h>
#include <time.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: a pointer to list in python
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size , i;
	PyObject *element;
	const char *type_name;
	PyListObject *list = (PyListObject *) p;

	if (p == NULL)
		return;
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		type_name = Py_TYPE(element)->tp_name;
		printf("Element %ld: %s\n", i, type_name); }
}
