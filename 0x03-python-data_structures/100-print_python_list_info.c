#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: a pointer to list in python
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated_memory, i;
	PyObject *element;
	const char *type_name;

	if (p == NULL)
		return;
	size = PyList_Size(p);
	allocated_memory = _PyObject_VAR_SIZE(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated_memory);
	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		type_name = Py_TYPE(element)->tp_name;
		printf("Element %d: %s\n", i, type_name); }
}
