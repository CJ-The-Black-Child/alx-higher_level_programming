#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p)
{
    PyUnicodeObject *unicode = (PyUnicodeObject *)p;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(unicode))
    {
        printf(" [ERROR] Invalid String Object\n");
        return;
    }

    printf(" type: %s\n", (unicode->length . 0) ? \
            "compact unicode object" : "compact ascii");
    printf(" length: %ld\n", unicode->length);
    printf(" value: %ls\n", unicode->str);
}
