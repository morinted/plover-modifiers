plover-modifiers
================

Script to create a `modifiers.json` dictionary to facilitate modifiers in [Plover](http://stenoknight.com/wiki/FAQ#What_is_Plover.3F).

## Usage

* Edit the `make-modifiers.py` file and add desired keys to the `hotkeys` variable. For example, add `["KH-FG", "grave"],` to the `hotkeys` array to create a shortcut for `` ⌘ ` `` to switch windows. 
  * See also: [available key names](https://sites.google.com/site/ploverdoc/appendix-the-dictionary-format#TOC-Available-Key-Names)
  * See also: [Unicode character recognition](http://shapecatcher.com/)

* Run the Python script:

```
$ python make-modifiers.py
```

* Copy the newly created `modifiers.json` file to your dictionary folder:

```
$ cp modifiers.json $HOME/path_to_your_dictionary_folder/modifiers.json
```

* In your Plover dictionary configuration, add the `modifiers.json` dictionary.
