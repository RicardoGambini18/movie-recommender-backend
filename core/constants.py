from config.environment import Environment

MOVIES_SORT_LIMIT = Environment.MOVIES_SORT_LIMIT()
WARMUP_ITERATIONS = Environment.WARMUP_ITERATIONS()

INFO = {
    'VECTOR': {
        'key': 'vector',
        'name': 'Vector',
        'description': 'Estructura de datos lineal donde los elementos se almacenan de forma contigua en memoria y se accede a ellos mediante un índice entero. Ofrece acceso aleatorio en tiempo constante y favorece recorridos secuenciales eficientes. Su tamaño suele ser fijo o costoso de cambiar, y las inserciones o eliminaciones en posiciones intermedias implican desplazamientos de elementos.',
        'sort_algorithms': {
            'BUBBLE_SORT': {
                'key': 'bubble_sort',
                'name': 'Ordenamiento de burbuja (Bubble sort)',
                'description': 'Algoritmo basado en comparaciones adyacentes. En cada pasada recorre el arreglo e intercambia pares fuera de orden, haciendo que el elemento extremo “burbujee” hasta su posición final. Esta implementación optimizada se detiene si no hay intercambios en una pasada.',
                'best_time_complexity': r'O(n)',
                'average_time_complexity': r'O(n^2)',
                'worst_time_complexity': r'O(n^2)',
                'space_complexity': r'O(1)'
            },
            'SELECTION_SORT': {
                'key': 'selection_sort',
                'name': 'Ordenamiento por selección (Selection sort)',
                'description': 'En cada iteración localiza el mínimo del segmento no ordenado y lo coloca en su posición final mediante un intercambio. Minimiza el número de escrituras en memoria, aunque realiza muchas comparaciones. No es estable en su forma básica.',
                'best_time_complexity': r'O(n^2)',
                'average_time_complexity': r'O(n^2)',
                'worst_time_complexity': r'O(n^2)',
                'space_complexity': r'O(1)'
            },
            'INSERTION_SORT': {
                'key': 'insertion_sort',
                'name': 'Ordenamiento por inserción (Insertion sort)',
                'description': 'Construye gradualmente un subarreglo ordenado insertando cada elemento en su posición correcta hacia la izquierda. Es estable y muy eficaz en arreglos pequeños o datos casi ordenados, simulando cómo se ordenan cartas en la mano.',
                'best_time_complexity': r'O(n)',
                'average_time_complexity': r'O(n^2)',
                'worst_time_complexity': r'O(n^2)',
                'space_complexity': r'O(1)'
            },
            'MERGE_SORT': {
                'key': 'merge_sort',
                'name': 'Ordenamiento por fusión (Merge sort)',
                'description': 'Estrategia de divide y vencerás: divide el arreglo en mitades, ordena recursivamente y luego aplica una fusión ordenada de las sublistas. Garantiza un rendimiento estable O(n log n) incluso en el peor caso, a costa de memoria adicional.',
                'best_time_complexity': r'O(n\log n)',
                'average_time_complexity': r'O(n\log n)',
                'worst_time_complexity': r'O(n\log n)',
                'space_complexity': r'O(n)'
            },
            'QUICK_SORT': {
                'key': 'quick_sort',
                'name': 'Ordenamiento rápido (Quick sort)',
                'description': 'Selecciona un pivote y particiona el arreglo en elementos menores y mayores a este, ordenando recursivamente. Es uno de los algoritmos más rápidos en la práctica (promedio), aunque su peor caso es cuadrático si el pivote no es ideal.',
                'best_time_complexity': r'O(n\log n)',
                'average_time_complexity': r'O(n\log n)',
                'worst_time_complexity': r'O(n^2)',
                'space_complexity': r'O(\log n)'
            },
        },
        'search_algorithms': {
            'LINEAR_SEARCH': {
                'key': 'linear_search',
                'name': 'Búsqueda lineal (Linear search)',
                'needs_sort': False,
                'description': 'Realiza un recorrido secuencial comparando cada elemento con el objetivo. Es el único método viable para datos desordenados. Su simplicidad lo hace útil para arreglos pequeños.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(n)',
                'worst_time_complexity': r'O(n)',
                'space_complexity': r'O(1)'
            },
            'BINARY_SEARCH': {
                'key': 'binary_search',
                'name': 'Búsqueda binaria (Binary search)',
                'needs_sort': True,
                'description': 'Requiere arreglo ordenado. Divide repetidamente el intervalo de búsqueda a la mitad comparando con el elemento central. Esta implementación es iterativa para optimizar el uso de memoria (stack).',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(\log n)',
                'worst_time_complexity': r'O(\log n)',
                'space_complexity': r'O(1)'
            },
            'JUMP_SEARCH': {
                'key': 'jump_search',
                'name': 'Búsqueda por saltos (Jump search)',
                'needs_sort': True,
                'description': 'Requiere arreglo ordenado. Salta un bloque fijo de elementos (raíz de n) hasta superar el objetivo, y luego realiza una búsqueda lineal en el bloque anterior. Es un punto medio entre búsqueda lineal y binaria.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(\sqrt{n})',
                'worst_time_complexity': r'O(\sqrt{n})',
                'space_complexity': r'O(1)'
            },
            'EXPONENTIAL_SEARCH': {
                'key': 'exponential_search',
                'name': 'Búsqueda exponencial (Exponential search)',
                'needs_sort': True,
                'description': 'Requiere arreglo ordenado. Útil para listas infinitas o de tamaño desconocido. Encuentra el rango donde reside el elemento creciendo exponencialmente y luego aplica búsqueda binaria.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(\log n)',
                'worst_time_complexity': r'O(\log n)',
                'space_complexity': r'O(1)'
            },
            'INTERPOLATION_SEARCH': {
                'key': 'interpolation_search',
                'name': 'Búsqueda por interpolación (Interpolation search)',
                'needs_sort': True,
                'description': 'Requiere arreglo ordenado y distribución uniforme. Estima la posición probable del objetivo usando una fórmula de interpolación (como buscar en un diccionario telefónico). Muy rápido en datos uniformes, pero se degrada a O(n) en peores casos.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(\log\log n)',
                'worst_time_complexity': r'O(n)',
                'space_complexity': r'O(1)'
            },
        },
    },
    'STACK': {
        'key': 'stack',
        'name': 'Pila',
        'description': 'Estructura de datos lineal que sigue el principio LIFO (Last In, First Out). El acceso está restringido estrictamente a la cima (tope). Es fundamental para la gestión de memoria (call stack), recursividad y evaluación de expresiones.',
        'sort_algorithms': {
            'SORT_STACK': {
                'key': 'sort_stack',
                'name': 'Ordenamiento de Pila (Sort Stack)',
                'description': 'Algoritmo iterativo que ordena una pila utilizando únicamente una pila auxiliar y operaciones push/pop/peek. Simula una inserción ordenada moviendo elementos entre las dos pilas. Respeta estrictamente la restricción LIFO.',
                'best_time_complexity': r'O(n^2)',
                'average_time_complexity': r'O(n^2)',
                'worst_time_complexity': r'O(n^2)',
                'space_complexity': r'O(n)'
            },
        },
        'search_algorithms': {
            'LINEAR_SEARCH': {
                'key': 'linear_search',
                'name': 'Búsqueda lineal con restauración (Linear search with restoration)',
                'needs_sort': False,
                'description': 'Busca un elemento desapilando secuencialmente (pop) y guardando los datos en una pila auxiliar. Al finalizar, restaura los elementos a la pila original para no perder información. Costosa pero necesaria dada la restricción LIFO.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(n)',
                'worst_time_complexity': r'O(n)',
                'space_complexity': r'O(n)'
            },
        },
    },
    'QUEUE': {
        'key': 'queue',
        'name': 'Cola',
        'description': 'Estructura de datos lineal que sigue el principio FIFO (First In, First Out). Las inserciones ocurren por el final y las extracciones por el frente. Modela procesos de atención en orden de llegada.',
        'sort_algorithms': {
            'SELECTION_SORT': {
                'key': 'selection_sort',
                'name': 'Ordenamiento por selección (Selection sort)',
                'description': 'Ordena la cola rotando todos los elementos para encontrar el mínimo en cada pasada y moverlo a una estructura ordenada. Implementación iterativa que respeta el acceso FIFO sin usar acceso aleatorio.',
                'best_time_complexity': r'O(n^2)',
                'average_time_complexity': r'O(n^2)',
                'worst_time_complexity': r'O(n^2)',
                'space_complexity': r'O(n)'
            },
            'MERGE_SORT': {
                'key': 'merge_sort',
                'name': 'Ordenamiento por fusión (Merge sort)',
                'description': 'Adapta el algoritmo divide y vencerás a estructuras secuenciales. Divide la cola en mitades, ordena recursivamente y fusiona comparando los frentes. Es la opción más eficiente para estructuras enlazadas como las colas.',
                'best_time_complexity': r'O(n\log n)',
                'average_time_complexity': r'O(n\log n)',
                'worst_time_complexity': r'O(n\log n)',
                'space_complexity': r'O(n)'
            },
        },
        'search_algorithms': {
            'LINEAR_SEARCH': {
                'key': 'linear_search',
                'name': 'Búsqueda lineal por rotación (Linear search by rotation)',
                'needs_sort': False,
                'description': 'Busca un elemento procesando el frente (dequeue) y reinsertándolo inmediatamente al final (enqueue). Realiza una rotación completa para garantizar que la cola regrese a su estado original. Operación O(n) obligatoria por la naturaleza FIFO.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(n)',
                'worst_time_complexity': r'O(n)',
                'space_complexity': r'O(1)'
            },
        },
    },
}
