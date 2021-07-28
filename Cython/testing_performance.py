import timeit

cy = timeit.timeit('''helloworld_cy.samplefunc(5)''',setup='import helloworld_cy',number=10000)
py = timeit.timeit('''helloworld.samplefunc(5)''',setup='import helloworld', number=10000)

print(cy, py)
print('Cython is {}x faster'.format(py/cy))