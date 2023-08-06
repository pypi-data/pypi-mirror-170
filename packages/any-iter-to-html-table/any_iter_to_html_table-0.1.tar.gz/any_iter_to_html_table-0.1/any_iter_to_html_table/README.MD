### Converts any nested iterable (json, dict, list ...) to an HTML table

```python
    #pip install any-iter-to-html-table 
    from any_iter_to_html_table import create_html_table_from_iterable
    data = {
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "S",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                            "GlossSeeAlso": ["GML", "XML"],
                        },
                        "GlossSee": "markup",
                    }
                },
            },
        }
    }

    """https://json.org/example.html"""  

        fromjsonorg_result = create_html_table_from_iterable(
        data, filename="fromjsonorg.html", title="Pandas - DataFrame", sparsify=True
    )
```

![](https://github.com/hansalemaos/screenshots/raw/main/fromjsonorg.png)

```python
    jsonfile = r"F:\jsonstackoverflow.json"
    #'https://api.stackexchange.com/2.2/answers?order=desc&sort=activity&site=stackoverflow'
        json_from_file = create_html_table_from_iterable(
        jsonfile,
        filename="json_from_file.html",
        title="Pandas - DataFrame",
        sparsify=False,
    )
```

![](https://github.com/hansalemaos/screenshots/raw/main/json_from_file.png)

```python
     sparsify=True
```

![](https://github.com/hansalemaos/screenshots/raw/main/json_from_file_sp.png)

### Without CSS

Design is separated from data. You can use the preset, but if you want,
 you can easily create your own CSS style

![](https://github.com/hansalemaos/screenshots/raw/main/noformat.png)



```python
    #'https://stackoverflow.com/questions/64359762/constructing-a-pandas-dataframe-with-columns-and-sub-columns-from-nested-diction
    nesteddict = {
        "level1": {
            "t1": {
                "s1": {"col1": 5, "col2": 4, "col3": 4, "col4": 9},
                "s2": {"col1": 1, "col2": 5, "col3": 4, "col4": 8},
                "s3": {"col1": 11, "col2": 8, "col3": 2, "col4": 9},
                "s4": {"col1": 5, "col2": 4, "col3": 4, "col4": 9},
            },
            "t2": {
                "s1": {"col1": 5, "col2": 4, "col3": 4, "col4": 9},
                "s2": {"col1": 1, "col2": 5, "col3": 4, "col4": 8},
                "s3": {"col1": 11, "col2": 8, "col3": 2, "col4": 9},
                "s4": {"col1": 5, "col2": 4, "col3": 4, "col4": 9},
            },
            "t3": {
                "s1": {"col1": 1, "col2": 2, "col3": 3, "col4": 4},
                "s2": {"col1": 5, "col2": 6, "col3": 7, "col4": 8},
                "s3": {"col1": 9, "col2": 10, "col3": 11, "col4": 12},
                "s4": {"col1": 13, "col2": 14, "col3": 15, "col4": 16},
            },
        },
        "level2": {
            "t1": {
                "s1": {"col1": 5, "col2": 4, "col3": 9, "col4": 9},
                "s2": {"col1": 1, "col2": 5, "col3": 4, "col4": 5},
                "s3": {"col1": 11, "col2": 8, "col3": 2, "col4": 13},
                "s4": {"col1": 5, "col2": 4, "col3": 4, "col4": 20},
            },
            "t2": {
                "s1": {"col1": 5, "col2": 4, "col3": 4, "col4": 9},
                "s2": {"col1": 1, "col2": 5, "col3": 4, "col4": 8},
                "s3": {"col1": 11, "col2": 8, "col3": 2, "col4": 9},
                "s4": {"col1": 5, "col2": 4, "col3": 4, "col4": 9},
            },
            "t3": {
                "s1": {"col1": 1, "col2": 2, "col3": 3, "col4": 4},
                "s2": {"col1": 5, "col2": 6, "col3": 7, "col4": 8},
                "s3": {"col1": 9, "col2": 10, "col3": 11, "col4": 12},
                "s4": {"col1": 13, "col2": 14, "col3": 15, "col4": 16},
            },
        },
    }   

        nested_dict = create_html_table_from_iterable(
        nesteddict,
        filename="from_nested_dict.html",
        title="Pandas - DataFrame",
        sparsify=False,
    )
```

![](https://github.com/hansalemaos/screenshots/raw/main/from_nested_dict.png)

```python
    Convert any nested iterable to an HTML table. Design is separated from data. You can use the preset, but if you want,
    you can easily create your own CSS style.



        Parameters:
            data: Any
                You can pass any iterable (list, dict, tuple …), json file path (str) or json URL (str)
            filename: Union[None,str]
                File path for output, will be saved in your current working directory
                If None, no files will be written.
            title: str
                Title  for HTML
                (default =  'Pandas DataFrame')
            sparsify: bool
                Repeat keys in every line
                (default = False)

        Returns:
            tuple[str,str]
```
