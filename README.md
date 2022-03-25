# Machine-Learning-Playground
A playground for various ML algorithm implementations. 

## Structure of this Repository
At the root of this repository, the implementation will be grouped by algorithm. For example, the first algorithm I will implement here is linear regression, stored in the `./linear-regression/hello-world/`. More generally, a given implementation will live at `./name-of-algorithm/name-of-implementation`. Instructions on how to run individual implementations are blow. 

##  How to Run Any of the Implementations in this Repository
Although my initial decision was to write all of these implementation in Python, I will most likely write some in other languages as a way to expirement with other tools. Above all, this is a playground for learning purposes. Regardless of the languages and tools used, I will attempt to stay consistent with the dependency managers used so that different implementations in the same language can be run in the same way.

### Languages Used: 
This will be updated in case as the list of tools used across implementations increases.
- [Python](#python)

### Python
The dependency manager of choice is `Pipenv`, and installation instructions can be found [here](https://packaging.python.org/en/latest/tutorials/managing-dependencies/). Once `Pipenv` has been installed, change into the implementation directory, and start the virtual environment, as such: 

```
# starting from the root directory of this repository
cd name-of-algorithm/name-of-implementation && pipenv run python main.py
```

This will install any implementation specific dependencies (eg. `matploblib`, `numpy`, etc.) so that they are available for use. 

