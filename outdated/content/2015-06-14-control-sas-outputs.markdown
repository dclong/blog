UUID: be888709-55cc-47cd-83d1-10be7540afc8
Status: published
Date: 2015-06-14 17:27:03
Author: Ben Chuanlong Du
Slug: control-sas-outputs
Title: Control SAS Outputs
Category: Software
Tags: software, SAS, output, print

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

1. it is suggested that you use 
`ods select none;` at the beginning of a user-defined macro to supress unnecessary output.
and 
`ods select all;` at the end of the macro to enable output.

2. `noPrint` is for the corresponding procedure only while `ods select none` is for all procedures.
However, `ods` allows more specific control over which results to output/display
rather than supress all of them.

`ods select none`
`noPrint` 
`noList`

The `noPrint` option in the logistic procedure supresses all displayed output.
It also supresses the logistic procedure from sending any result to ODS,
so ODS select statment will not work in this case.
A better way is to use ODS to control output.


ODS and the NOPRINT Option

Many SAS procedures support a NOPRINT option that you can use when you want to create an output data set but without displaying any output. You use an option (such as OUTEST= or an OUTPUT statement with an OUT= option) in addition to the procedure’s NOPRINT option to create a data set and suppress displayed output.

You can also use ODS to create output data sets by using the ODS OUTPUT statement. However, if you specify the NOPRINT option, the procedure might not send any output to ODS. In most procedures that support a NOPRINT option, NOPRINT means no ODS. (However, there are a few procedures that for historical reasons still might produce some output even when NOPRINT is specified.) When you want to create output data sets through the ODS OUTPUT statement, and you want to suppress the display of all output, specify the following statement instead of using the NOPRINT option:

ods select none;

Alternatively, you can close the active ODS destinations, for example, like this:

ods html close;
ods listing close;

Note that ODS statements do not instruct a procedure to generate output. Instead, they specify how ODS should manage output once it is created. You must ensure that the proper procedure options are in effect, or the output will not be generated. For example, the following statements do not create the requested data set Parms:

proc glm;
    ods output ParameterEstimates=Parms;
    class x;
    model y=x;
run; quit;

This is because the SOLUTION option was not specified in the MODEL statement. Since PROC GLM did not create the table, ODS cannot make the output data set. When you execute these statements, the following message is displayed in the log:

WARNING: Output 'ParameterEstimates' was not created.

The following step creates the output data set:

proc glm;
    ods output ParameterEstimates=Parms;
    class x;
    model y=x / solution;
run; quit;

