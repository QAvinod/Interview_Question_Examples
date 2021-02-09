"""
There is no such thing as Python private constructors.

However, as I worked on wrapping some C-based code with Cython,
I ended up with the following pattern.
Some (boring) technical issues do not allow me to
just have the make_foo processing in the constructor.

"""