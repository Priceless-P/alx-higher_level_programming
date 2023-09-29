#include <Python.h>
#include <stdio.h>

/**
* print_python_list - Prints information about Python lists.
* @p: Pointer to the Python list.
*/
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "[*] Python list info\n  [ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *item_type = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, item_type);

		if (strcmp(item_type, "bytes") == 0)
		{
			print_python_bytes(item);
		} else if (strcmp(item_type, "float") == 0)
		{
			print_python_float(item);
		}
	}
}

/**
* print_python_bytes - Prints information about Python bytes.
* @p: Pointer to the Python bytes object.
*/
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	const char *string = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	printf("  first %d bytes: ", (int)(size < 10 ? size : 10));
	for (Py_ssize_t i = 0; i < (size < 10 ? size : 10); ++i)
	{
		printf("%02x ", string[i] & 0xff);
	}
	printf("\n");
}

/**
* print_python_float - Prints information about Python floats.
* @p: Pointer to the Python float object.
*/
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[.] float object info\n  [ERROR] Invalid Float Object\n");
		return;
	}

	double value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %lf\n", value);
}
