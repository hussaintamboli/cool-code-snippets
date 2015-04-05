Mock
----

It allows you to replace parts of your system under test with mock objects

Use cases
---------
Sometimes we don't want some part of the code to be called when unittesting
- api calls
- heavy db operations
- reading big files

Sometimes it's impossible to unittest that part. Because the result keeps on changing
- timestamp
- random number generation
- data not present in deverloper machine / locally

In case of a continuous integration, these tests will be run periodically
- tests will be run by Jenkins periodically

Using python's `mock` functionality, we can change it's behaviour accordingly

P.S. Feel free to express your thoughts on this
