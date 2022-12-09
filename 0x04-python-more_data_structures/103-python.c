#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {

    	// Check that the input is a list
    if (!PyList_Check(p)) {
        printf("Error: input is not a list\n");
        return;
    }

    // Get the number of elements in the list
    int len = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %d\n", len);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    // Iterate over the elements in the list and print their info
    int i;
    for (i = 0; i < len; i++) {
        PyObject *elem = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(elem)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    // Check that the input is a bytes object
    if (!PyBytes_Check(p))
    {
        printf("Error: input is not a bytes object\n");
        return;
    }

    // Get the size of the bytes object
    int size = PyBytes_Size(p);
    printf("[*] Python bytes object info\n");
    printf("[*] Size: %d\n", size);

    // Get a pointer to the underlying data of the bytes object
    char *data = PyBytes_AsString(p);

    // Print the hexadecimal representation of the data
    printf("[*] Hexadecimal: ");
    int i;
    for (i = 0; i < size; i++)
    {
        printf("%02x ", (unsigned char)data[i]);
    }
    printf("\n");
}

