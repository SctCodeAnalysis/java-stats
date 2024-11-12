# Java Project Model

Forms project model based on Java files within repository as well as provide base statistics.
Provides API for traversing the model as well as export in common format (TBP).

The model for Java looks like below:
```
folder
 |- .java file (LoC)
   |- classA
     |- modifier
     |- package
     |- import
     |- annotation
     |- method (LoC, cyclomatic complexity)
       |- modifier
       |- annotation
       |- parameter
         |- modifier
         |- annotation
       |- variables
         |- modifier
         |- annotation
     |- field
       |- modifier
       |- annotation
     |- ...
   |- classB
     |- ... 
   |- ...
 |- .java file
 |- ... 
```

Base statistics include:
- number of Java files
- number of classes
- avg/max number of methods per class
- avg/max method size (LoC)
