---
title: "Readme"
author: Vijayaraghavan Sundararaman
date: Nov 2, 2019
output: pdf_document
---

# Intro

## GCD Of Two Numbers

```sequence
st=>start: Start
num=>inputoutput: Take 2 Numbers (Num1, Num2)
while=>condition: While Num2 != 0
gcd=>inputoutput: GCD
stp1=>operation: Temp = Num1
stp2=>operation: Num1 = Num2
stp3=>operation: Num2 = Temp % Num2
e=>end


st()->num->while
while(yes)->stp1->stp2->stp3(left)->while
while(no)->gcd->e
```
