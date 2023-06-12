#include <Python.h>
/**
  * print_python_list_info - function that prints information
  * about Python lists
  * @list_obj: the python list object
  *
  * Return: None
  */
void print_python_list_info(PyObject *list_obj)
{
	int list_size, list_alloc, index;
	PyObject *list_item;

	list_size = PyList_Size(list_obj);
	list_alloc = ((PyListObject *)list_obj)->allocated;

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", list_alloc);

	for (index = 0; index < list_size; index++)
	{
		printf("Element %d: ", index);

		list_item = PyList_GetItem(list_obj, index);
		printf("%s\n", Py_TYPE(list_item)->tp_name);
	}
}
