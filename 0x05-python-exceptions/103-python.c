#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[*] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n",size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		printf("[.] byte object info\n");
		printf(" size: %ld\n", size);
		printf(" trying string: %s\n", str);
		printf(" first %ld bytes:", (size < 10) ? size + 1 : 10);
		for (i = 0; i < size && i < 10; i++)
			printf(" %.2x", (unsigned char)str[i]);
		printf("\n");
	}

	void print_python_float(PyObject *p)
	{
		PyObject *repr;

		if (!PyFloat_Check(p))
		{
			printf("[.] Invalid Float Object\n");
			return;
		}

		repr = PyObject_Repr(p);
		printf("[.] flaot object info\n");
		printf(" value: %s\n" PyUnicode_AsUTF8(repr));
		Py_DECREF(repr);
	}
