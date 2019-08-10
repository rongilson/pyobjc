#define PY_SSIZE_T_CLEAN
#include "pyobjc-api.h"
#include <Python.h>

#import <Foundation/Foundation.h>
#import <OSLog/OSLog.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_OSLog_protocols.m"

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

/* Python glue */
PyObjC_MODULE_INIT(_OSLog)
{
    PyObject* m;
    m = PyObjC_MODULE_CREATE(_OSLog) if (!m) { PyObjC_INITERROR(); }

    if (PyObjC_ImportAPI(m) == -1)
        PyObjC_INITERROR();

    PyObjC_INITDONE();
}