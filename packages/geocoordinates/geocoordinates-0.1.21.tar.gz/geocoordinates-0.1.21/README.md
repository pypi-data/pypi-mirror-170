# Geographic coordinates coding problem 

Contained is my solution for the geographic coordinates coding problem. The Julia version of this code can be found at https://github.com/kathesch/GeoCoordinates.

## Installation 

Run the following in terminal to install geocoordinates with pip

`pip install geocoordinates`

## Running 

1. Open a python REPL
2. `import geocoordinates as gc`
3. `gc.time_series_analysis()`

```python
~ % python
Python 3.10.7 (main, Sep 14 2022, 22:38:23) [Clang 14.0.0 (clang-1400.0.29.102)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import geocoordinates as gc
>>> gc.time_series_analysis()
Velocity at Unix time  1532334000 :
 [ -995.91526875 -2514.43889398    55.92122005] m/s
Velocity at Unix time  1532335268 :
 [-3471.02128308  1760.25788787 -4867.4760627 ] m/s
 ```