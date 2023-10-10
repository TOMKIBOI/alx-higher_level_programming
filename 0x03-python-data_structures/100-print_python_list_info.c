#include <Python.h>

/**
 * print_python_list_info - Prints info on Python lists.
 * @p: A Python object
 */

void print_python_list_info(PyObject *p)
{
    long int size, i;
    PyObject *item;

    size = Py_SIZE(p);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
