#include <Python.h>
#include <stdio.h>

/**
* print_python_float - prints data of the PyFloatObject
* @p: the PyObject
*/
void print_python_float(PyObject *p)
{
	double float_value = 0;

	char *string_representation = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	float_value = ((PyFloatObject *)p)->ob_fval;
	string_representation = PyOS_double_to_string(
	float_value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", string_representation);
}

/**
* print_python_bytes - prints data of the PyBytesObject
* @p: the PyObject
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, i = 0;
	char *byte_string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);

	byte_string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", byte_string);

	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", byte_string[i]);
		i++;
	}

	printf("\n");
}

/**
* print_python_list - prints data of the PyListObject
* @p: the PyObject
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *list_item;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");

	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (i < size)
		{
			list_item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, list_item->ob_type->tp_name);

			if (PyBytes_Check(list_item))
				print_python_bytes(list_item);
			else if (PyFloat_Check(list_item))
				print_python_float(list_item);

			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
