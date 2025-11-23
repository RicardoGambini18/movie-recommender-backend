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
                'name': 'Ordenamiento burbuja (Bubble sort)',
                'description': 'Algoritmo basado en comparaciones adyacentes. En cada pasada recorre el arreglo e intercambia pares fuera de orden, haciendo que el elemento extremo “burbujee” hasta su posición final. Puede detenerse antes si en una pasada no se realizan intercambios. Es estable y sencillo, pero poco eficiente para tamaños grandes.',
                'best_time_complexity': r'O(n)',
                'average_time_complexity': r'O(n^2)',
                'worst_time_complexity': r'O(n^2)',
                'space_complexity': r'O(1)'
            },
            'SELECTION_SORT': {
                'key': 'selection_sort',
                'name': 'Ordenamiento por selección (Selection sort)',
                'description': 'En cada iteración localiza el mínimo (o máximo) del segmento no ordenado y lo coloca en su posición final mediante un intercambio. Reduce intercambios, pero realiza muchas comparaciones. No es estable en su forma básica.',
                'best_time_complexity': r'O(n^2)',
                'average_time_complexity': r'O(n^2)',
                'worst_time_complexity': r'O(n^2)',
                'space_complexity': r'O(1)'
            },
            'INSERTION_SORT': {
                'key': 'insertion_sort',
                'name': 'Ordenamiento por inserción (Insertion sort)',
                'description': 'Construye gradualmente un subarreglo ordenado insertando cada elemento en su posición correcta hacia la izquierda mediante desplazamientos. Es estable y especialmente eficaz en arreglos pequeños o datos casi ordenados.',
                'best_time_complexity': r'O(n)',
                'average_time_complexity': r'O(n^2)',
                'worst_time_complexity': r'O(n^2)',
                'space_complexity': r'O(1)'
            },
            'MERGE_SORT': {
                'key': 'merge_sort',
                'name': 'Ordenamiento por mezcla (Merge sort)',
                'description': 'Estrategia de divide y vencerás: divide el arreglo en mitades, ordena cada mitad de forma recursiva y luego fusiona las sublistas ordenadas. Ofrece rendimiento garantizado y es estable, a costa de memoria adicional para la fusión.',
                'best_time_complexity': r'O(n\log n)',
                'average_time_complexity': r'O(n\log n)',
                'worst_time_complexity': r'O(n\log n)',
                'space_complexity': r'O(n)'
            },
            'QUICK_SORT': {
                'key': 'quick_sort',
                'name': 'Ordenamiento rápido (Quick sort)',
                'description': 'Selecciona un pivote, particiona el arreglo en elementos menores y mayores que el pivote y ordena recursivamente cada partición. Presenta excelente rendimiento promedio; el peor caso se mitiga con elección de pivote aleatoria o mediana de tres. No es estable en su implementación clásica.',
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
                'description': 'Explora secuencialmente los elementos comparando con el objetivo hasta hallarlo o agotar el arreglo. No requiere orden previo y funciona con cualquier tipo de dato comparable.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(n)',
                'worst_time_complexity': r'O(n)',
                'space_complexity': r'O(1)'
            },
            'BINARY_SEARCH': {
                'key': 'binary_search',
                'name': 'Búsqueda binaria (Binary search, versión iterativa)',
                'needs_sort': True,
                'description': 'Opera sobre un arreglo ordenado. En cada paso examina el elemento central y descarta la mitad que no puede contener el objetivo, repitiendo hasta encontrarlo o vaciar el rango. La versión iterativa evita costo de pila adicional.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(\log n)',
                'worst_time_complexity': r'O(\log n)',
                'space_complexity': r'O(1)'
            },
            'JUMP_SEARCH': {
                'key': 'jump_search',
                'name': 'Búsqueda por saltos (Jump search)',
                'needs_sort': True,
                'description': 'Requiere arreglo ordenado. Avanza en bloques de tamaño aproximadamente raíz de n hasta sobrepasar el posible rango del objetivo y después realiza una búsqueda lineal dentro del bloque identificado.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(\sqrt{n})',
                'worst_time_complexity': r'O(\sqrt{n})',
                'space_complexity': r'O(1)'
            },
            'EXPONENTIAL_SEARCH': {
                'key': 'exponential_search',
                'name': 'Búsqueda exponencial (Exponential search)',
                'needs_sort': True,
                'description': 'Requiere arreglo ordenado. Amplía exponencialmente el índice de búsqueda para acotar rápidamente un intervalo candidato y luego ejecuta búsqueda binaria dentro de ese intervalo.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(\log n)',
                'worst_time_complexity': r'O(\log n)',
                'space_complexity': r'O(1)'
            },
            'INTERPOLATION_SEARCH': {
                'key': 'interpolation_search',
                'name': 'Búsqueda por interpolación (Interpolation search)',
                'needs_sort': True,
                'description': 'Requiere arreglo ordenado por una clave numérica aproximadamente uniforme. Estima la posición del objetivo mediante interpolación lineal y refina iterativamente. En distribuciones muy sesgadas su desempeño puede degradarse significativamente.',
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
        'description': 'Estructura de datos lineal con comportamiento LIFO (Last In, First Out). Solo permite acceso al elemento de la cima mediante operaciones push (insertar) y pop (extraer). Útil para algoritmos que requieren procesamiento en orden inverso o gestión de estados.',
        'sort_algorithms': {
            'SORT_STACK': {
                'key': 'sort_stack',
                'name': 'Ordenamiento con Pila Auxiliar (Sort Stack)',
                'description': 'Algoritmo iterativo que ordena una pila usando una pila auxiliar. Extrae elementos de la pila original y los inserta en la pila auxiliar en orden, luego transfiere de vuelta para obtener el ordenamiento final. Respeta estrictamente las operaciones LIFO de la estructura.',
                'best_time_complexity': r'O(n^2)',
                'average_time_complexity': r'O(n^2)',
                'worst_time_complexity': r'O(n^2)',
                'space_complexity': r'O(n)'
            },
        },
        'search_algorithms': {
            'LINEAR_SEARCH': {
                'key': 'linear_search',
                'name': 'Búsqueda Lineal con Restauración',
                'needs_sort': False,
                'description': 'Recorre la pila extrayendo elementos de la cima y comparándolos con el objetivo. Usa una pila auxiliar para preservar el estado original y restaura todos los elementos después de la búsqueda. Respeta estrictamente las operaciones LIFO.',
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
        'description': 'Estructura de datos lineal con comportamiento FIFO (First In, First Out). Solo permite acceso al elemento del frente mediante operaciones enqueue (insertar al final) y dequeue (extraer del frente). Útil para algoritmos que requieren procesamiento en orden de llegada o simulaciones.',
        'sort_algorithms': {
            'SELECTION_SORT': {
                'key': 'selection_sort',
                'name': 'Ordenamiento por selección (Selection sort)',
                'description': 'Algoritmo iterativo que ordena una cola rotándola para encontrar el valor mínimo en cada iteración. Extrae el mínimo y lo coloca en una cola ordenada. Complejidad cuadrática pero respeta estrictamente las operaciones FIFO de la estructura.',
                'best_time_complexity': r'O(n^2)',
                'average_time_complexity': r'O(n^2)',
                'worst_time_complexity': r'O(n^2)',
                'space_complexity': r'O(n)'
            },
            'MERGE_SORT': {
                'key': 'merge_sort',
                'name': 'Ordenamiento por mezcla (Merge sort)',
                'description': 'Estrategia de divide y vencerás adaptada para colas. Divide la cola en dos mitades, ordena cada mitad recursivamente y luego fusiona las colas ordenadas comparando los frentes. Respeta estrictamente las operaciones FIFO y ofrece rendimiento garantizado.',
                'best_time_complexity': r'O(n\log n)',
                'average_time_complexity': r'O(n\log n)',
                'worst_time_complexity': r'O(n\log n)',
                'space_complexity': r'O(n)'
            },
        },
        'search_algorithms': {
            'LINEAR_SEARCH': {
                'key': 'linear_search',
                'name': 'Búsqueda Lineal por Rotación',
                'needs_sort': False,
                'description': 'Recorre la cola rotándola completamente: extrae elementos del frente, los compara con el objetivo y los vuelve a insertar al final. La cola vuelve automáticamente a su estado original sin necesidad de estructuras auxiliares. Respeta estrictamente las operaciones FIFO.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(n)',
                'worst_time_complexity': r'O(n)',
                'space_complexity': r'O(1)'
            },
        },
    },
}
