#include <Python.h>

/**
 * print_python_list - Prints the basic info about Python Lists
 * @p: PyObject pointer
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *type = Py_TYPE(item)->tp_name;

		printf("Element %zd: %s\n", i, type);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	unsigned char *str;
	PyObject *repr;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}


	size = PyBytes_Size(p);
	str = (unsigned char *)PyBytes_AsString(p);
	repr = PyObject_Repr(p);

	printf(" size: %zd\n", size);
	printf(" trying string: %s\n", PyUnicode_AsUTF8(repr));
	printf(" first %zd bytes:", size + 1 > 10 ? 10 : size + 1);

	for (i = 0; i < (size + 1 > 10 ? 10 : size + 1); i++)
		printf(" %02x", str[i]);

	printf("\n");
	Py_DECREF(repr);
}
