d={n:n*n for n in range(1,5)}
print(d)

old={'rice':60,'dhaal':120,'oil':150}

new={product:price*5 for (product,price) in old.items()}
print(new)

real={'ksr':19,'pbr':19}
n1={name:age for (name,age) in real.items() if age>18}
print(n1)
