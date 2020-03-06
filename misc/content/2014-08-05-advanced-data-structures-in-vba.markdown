UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2016-06-14 02:09:10
Author: Ben Chuanlong Du
Slug: advanced-data-structures-in-vba
Title: Advanced Data Structures in VBA
Category: Computer Science
Tags: programming, VBA, data structure, dictionary

Things on this page are 
fragmentary and immature notes/thoughts of the author.
It is not meant to readers 
but rather for convenient reference of the author and future improvement.
            
## Dictionary/Hashtable

1. Set a reference to MS Scripting runtime

        Set dict = CreateObject("Scripting.Dictionary")

or

        Dim dict As New Scripting.Dictionary 

2. Example of use:

        If Not dict.Exists(key) Then 
            dict.Add key, value
        End If 

3. Don't forget to set the dictionary to Nothing when you have finished using it.

        Set dict = Nothing 

## Your Own Data Structure

You can define your own type in VBA.

        Dim numbers = New Integer() {1, 2, 4, 8}
        Dim doubles = {1.5, 2, 9.9, 18}

        Dim myarray As Variant
        myarray = Array("Cat", "Dog", "Rabbit")
