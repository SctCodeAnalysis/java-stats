# Code Repository Java Stats

Taking source code repository as an input calculate base statistics for Java source files.  

Base statistics include:
- number of Java files
- number of classes
- avg/max number of methods per class
- avg/max method size (in LoC)
- avg/max cyclomatic complexity of method
- _(to be extended)_ 

The stats are exposed as an API as well as exported report (in XML format)

## API Usage

```python
import ca-python-stats as st

stats = JavaStats("path/to/repo")

# Print available metrics
print(stats.list())

# Print number of classes
print(stats.metric("NUMBER_OF_CLASSES"))

# Print XML report
print(stats.as_xml())
```

## CLI Usage

```shell
\> python3 ca-java-stats --report path_to_xml.xml path_to_repo
```
