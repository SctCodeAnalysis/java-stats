# Java Project Statistics

Forms project statistics based on Java files within repository.
Provides API for getting stats as well as export into common project model.

The statistics include:
- number of (.java) files
- number of classes (total; per file)
- avg number of methods within a class
- avg/max length of a method (in LoC)

# Java Project Model

```
folder
 |- .java file (LoC)
   |- classA
     |- package
     |- import
     |- annotation
     |- method (LoC, cyclomatic complexity)
       |- argument (final/non-final)
       |- variables 
     |- field (static/instance, final/non-final)
     |- ...
   |- classB
     |- ... 
   |- ...
 |- .java file
 |- ... 
```
