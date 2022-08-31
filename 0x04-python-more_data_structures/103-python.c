#include "Python.h"


/**
 * printElement - print element info
 * @p: python object
 * @num: number of items in object
 * Return: none
 */
void printElement(PyObject *p, int num)
{
	char *pyTypes[5] = { "str", "int", "float", "tuple", "list" };
	int i;
	PyObject *item = NULL;

	if (num > 0)
	{
		for (i = 0; i < num; i++)
		{
			item = PyList_GetItem(p, i);
			if (PyUnicode_Check(item))
			{
				printf("Element %d: %s\n", i, pyTypes[0]);
			}
			else if (PyLong_Check(item))
				printf("Element %d: %s\n", i, pyTypes[1]);
			else if (PyFloat_Check(item))
				printf("Element %d: %s\n", i, pyTypes[2]);
			else if (PyTuple_Check(item))
				printf("Element %d: %s\n", i, pyTypes[3]);
			else if (PyList_Check(item))
				printf("Element %d: %s\n", i, pyTypes[4]);
		}
	}
}

/**
 * print_python_list - Create a C function that prints
 * basic info about Python lists
 * @p: python object
 * Return: none
 */
void print_python_list(PyObject *p)
{
	int number = 0, numAllocated = 0;

	if (!p)
		return;

	number = (int)PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", number);

	numAllocated = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", numAllocated);
	printElement(p, number);
}

/**
 * print_python_list_info - Create a C function that prints some
 * basic info about Python lists
 * @p: python object
 * Return: none
 */
void print_python_list_info(PyObject *p)
{
	int number = 0, numAllocated = 0;

	if (!p)
		return;

	number = (int)PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", number);

	numAllocated = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", numAllocated);
	printElement(p, number);
}

/**
 * print_python_bytes - Create a C function that prints
 * basic byte info about Python lists
 * @p: python object
 * Return: none
 */
void print_python_bytes(PyObject *p)
{
	int i, size = 0, nBytes = 0;
	char *myString = "";

	p = p;

	printf("[.] bytes object info\n");

	/*Some type of checking*/
	if (p)
	{
		printf("size: %d\n", size);
		printf("trying string: %s?\n", myString);
		printf("first %d bytes: ", nBytes);
		for (i = 0; i < nBytes; i++)
			printf("%x ", myString[i]);
	} else
	{
		printf("[ERROR] Invalid Bytes Object\n");
	}
}
