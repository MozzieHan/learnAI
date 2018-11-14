#### 向量化公式

- 向前传播
```python
import numpy as np
W = [] 
b = [] 
Z = []
A = []
l = 1 
g = []
Z[l] = np.dot(W[l], A[l-1]) + b[l]  
A[l] = g[l](Z[l])
``` 

- 向后传播
```python
import numpy as np

```