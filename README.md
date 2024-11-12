# Java Project Model

Forms project model based on Java files within repository.
Provides API for traversing the model as well as export in common format (TBP).

The model for Java looks like below:
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
