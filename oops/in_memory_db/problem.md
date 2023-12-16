### Assessment Criteria

Code is expected to be Working, Readable, Modular and easily Extensible. Use suitable data structures and efficient algorithms as deemed fit.

### In Memory Database

Design and implement an in-memory SQL-like database, which should support the following set of operations / functionality. The functionality could be exposed as any API - REST or command line or simply function calls inside your program.

Level 1:

- It should be possible to create (or delete) tables in a database.
- A table definition comprises columns which have types.
- The supported column types are string and int.
- The string type can have a maximum length of 20 characters.
- The int type can have a minimum value of -1024 and a maximum value of 1024.
- Support for mandatory fields (tagging a column as required)
- It should be possible to insert records in a table.
- It should be possible to print all records in a table.

Level 2:

- It should be possible to filter and display records whose column values match a given value.
