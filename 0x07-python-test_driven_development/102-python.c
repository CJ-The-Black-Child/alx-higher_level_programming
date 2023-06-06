#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about a Python string object
 * @p: PyObject pointer to the string object
 */

void print_python_string(PyObject *p)
{
	PyUnicodeObject *unicode = (PyUnicodeObject *)p;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf(" [ERROR] Invalid String Object\n");
		return;
	}
	printf(" type: %s\n", PyUnicode_IS_COMPACT_ASCII(unicode) ?
			"compact ascii" : "compact unicode object");
	printf(" length: %ld\n", PyUnicode_GET_LENGTH(p));
	printf(" value: %s\n", PyUnicode_AsUTF8(p));
}
