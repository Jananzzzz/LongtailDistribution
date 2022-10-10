# Skills & Bugfixs

## Vscode Extension
Markdown Preview Github Styling <br>
`Github`

## codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
File path error: python regard "C:\User\16591" as string instead of a file path <br>
Instead, we use `slash` replace `backslash`: "C:/User/16591/" <br>

## <span style="color:red">   length limit (not fixed yet)  </span>
<div style="color:red"> 
the output length has a limit in terminal  
</div>

## show pytorch version and cuda version in windows terminal
- torch: ```pip show torch```
- cuda version: ```nvidia-smi```

## <span style="color:red"> can't open 'data' (no fixed yet) </span> 
<div style="color:red">

```
with open('C:/') as csvin:
    data = csv.reader(csvin)
    print(data)
```
why can't i print(data) here 
but these code is valid:
```
for line in csvin:
    print(line[0])
```
</div>


