Status: published
Author: Ben Chuanlong Du
Date: 2012-10-22 14:34:53
Title: Collections in Java
Slug: collections-in-java
Category: Computer Science
Tags: ArrayList, programming, Java, array, collections, vector
Modified: 2020-05-22 14:34:53

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


[Oracel Java Tutorial on Collections](http://docs.oracle.com/javase/tutorial/collections/index.html)

## ArrayList

1. You can point an element of `Array` or `ArrayList` to `null`, 
    but remember that a `null` reference cannot invoke any method. 
    For example, 
    if you have an object `set` of `ArrayList<ArrayList<Point>>` whose first element is `null`. 
    Then you cannot add points (objects of Point) to the first element 
    (which is of type `ArrayList<Point>`) of `set` by invoking `set.get(0).add`. 
    To achieve the goal, 
    you have to first create a new object of `ArrayList<Point>`, 
    point the first element of `set` to it, 
    and then add points by invoking `set.get(0).add`.

3. Elements added into an `ArrayList` or returned by `get` from an
    ArrayList are by reference.

4. To insert an element into an `ArrayList` with size `n` (using the `add` method), 
    the legal range of index is `0` to `n`. 
    The `add` method without specifying location add the element to the end of the `ArrayList`.

6. An `Array` or `ArrayList` in Java is essentially a sequence of addresses. 
    Since an address can point to anything, 
    `Array` or `ArrayList` in Java can be used as container for anything. 
    Specially, 
    you can use an array as a container for `ArrayLists` 
    and you can also use an ArrayList as a container for `Arrays`. 
    For example 

        :::java
        ArrayList<double[]> list;

    and 
        :::java
        ArrayList<Integer>[] array;

    are both legitimate in Java.

### Capacity

7. The `clear` method of `ArrayList` does not affect its capacity.

5. The capacity of an `ArrayList` can be 0.

3. You might be curious that why the methods `boolean add(E e)` and `void add(int index, E e)` have different signatures. 
    The reason is that `boolean add(E e)` is inherited from the `Collection` interface. 
    For other collections such as set and map, etc., 
    it is beneficial to know whether an elements to be added to it already exists or not.
    The return value (indicating whether the ...) is then very helpful. 
    For the list specific method `void add(int index, E e)`,
    there is no need to define the signature as boolean because a list does not force uniqueness 
    and whether an element will be added has nothing to do with whether an element of the same value already exists in the list or not.

## Array

1. The `Arrays` class contains many userful static methods for array operations,
    but generally speaing, 
    they can only be applied to 1-d array directly. 
    To applied to multi-dimensional arrays, 
    you have to iterate into the array until you have 1-d arrays. 
    For example, 
    if you want to compare whether two 1-d integer arrays are equal or not,
    you can use the static `equals` in the `Arrays`. 
    To compare whether two 2-d interger arrays are equal or not, 
    you can compare whether the two arrays have the same length, 
    and whether each corresponding elements (which are 1-d arrays) of the two arrays are equal 
    (using the static `Arrays.equals` method). 
    Applying `Arrays.equals` on a 2-d intger arrays directly compares whether the two 2-d arrays 
    contain same references to 1-d arrays. 
    The static `Arrays.equals` method is overloaded for double arrays,
    but it is no a good idea to compare whether two double arrays are equal using `Arrays.equals`
    because it does not allow an error tolerance.

2. A 2-d array in java is just an array of arrays, 
    so even if you define 

        :::java
        int[][] a = new int[2][3]; 

    you can still point `a[i]` to another 1-d array. 
    This means that you can change the
    length of each element of the 2-d array`a` whenever you want.

3. To copy arrays quicly, 
    you can use `System.arraycopy` which is implemented in native code. 
    It is preferred to other ways such as `clone`, 
    user-defined method and so on. 
    Notice that `System.arraycopy` performs shallow copys for arrays of objects,
    i.e., only references of objects will be copied. 
    If you want to make a deep copy of an array of objects, 
    you have to do it by yourself.

4. A container in Java can be initialized using curly braces 
    (similar to the universal initializer list in C++11), 
    and in this case you do not have to specified the dimensions of the container. 
    To initialized all elements of a 1-dimensional array to a single value, 
    you can the static `Arrays.fill` method.
    Note that arrays in Java are automatically initialized to default values, 
    so you need not to initialize an array if the default value is what you want.



