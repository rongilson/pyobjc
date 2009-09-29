/*
# AUTOGENERATED DO NOT EDIT

# If you edit this file, delete the AUTOGENERATED line to prevent re-generation
# BUILD api_versions [0x001]
*/

%module color_subtable

#define __version__ "$Revision: 1.1.2.1 $"
#define __date__ "$Date: 2004/11/15 07:38:07 $"
#define __api_version__ API_VERSION
#define __author__ "PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>"
#define __doc__ ""

%{
/**
 *
 * GL.EXT.color_subtable Module for PyOpenGL
 * 
 * Authors: PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>
 * 
***/
%}

%include util.inc
%include gl_exception_handler.inc

%{
#ifdef CGL_PLATFORM
# include <OpenGL/glext.h>
#else
# include <GL/glext.h>
#endif

#if !EXT_DEFINES_PROTO || !defined(GL_EXT_color_subtable)
DECLARE_VOID_EXT(glColorSubTableEXT, (GLenum target, GLsizei start, GLsizei count, GLenum format, GLenum type, const GLvoid *data), (target, start, count, format, type, data))
DECLARE_VOID_EXT(glCopyColorSubTableEXT, (GLenum target, GLsizei start, GLint x, GLint y, GLsizei width), (target, start, x, y, width))
#endif
%}

/* FUNCTION DECLARATIONS */
void glColorSubTableEXT(GLenum target, GLsizei start, GLsizei count, GLenum format, GLenum type, const GLvoid *data);
DOC(glColorSubTableEXT, "glColorSubTableEXT(target, start, count, format, type, data)")
void glCopyColorSubTableEXT(GLenum target, GLsizei start, GLint x, GLint y, GLsizei width);
DOC(glCopyColorSubTableEXT, "glCopyColorSubTableEXT(target, start, x, y, width)")

/* CONSTANT DECLARATIONS */



%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_color_subtable)
"glColorSubTableEXT",
"glCopyColorSubTableEXT",
#endif
	NULL
};

#define glInitColorSubtableEXT() InitExtension("GL_EXT_color_subtable", proc_names)
%}

int glInitColorSubtableEXT();
DOC(glInitColorSubtableEXT, "glInitColorSubtableEXT() -> bool")

%{
PyObject *__info()
{
	if (glInitColorSubtableEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();
