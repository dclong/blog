UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Check Whether an Email Address Is Valid in Java
Date: 2016-07-12 23:58:54
Slug: valid-email-address-java
Author: Ben Chuanlong Du
Category: Computer Science
Tags: pattern, match, Java, programming, email address

See the following code.

```Java
String email = "test@test.com";
Pattern p = Pattern.compile(".+@.+\\.[a-z]+");
Matcher m = p.matcher(email);
boolean matchFound = m.matches();
if(matchFound){
    System.out.println("EMAIL OK");
}else{
    System.out.println("EMAIL ERROR");
}
```
