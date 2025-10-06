MOVIES_SORT_LIMIT = 10000
WARMUP_ITERATIONS = 25000

INFO = {
    'ONE_DIMENSIONAL_ARRAY': {
        'key': 'one_dimensional_array',
        'name': 'Arreglo unidimensional (Array 1D)',
        'description': 'Estructura lineal donde los elementos se almacenan de forma contigua en memoria y se accede a ellos mediante un índice entero. Ofrece acceso aleatorio en tiempo constante y favorece recorridos secuenciales eficientes. Su tamaño suele ser fijo o costoso de cambiar, y las inserciones o eliminaciones en posiciones intermedias implican desplazamientos de elementos.',
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
                'description': 'Explora secuencialmente los elementos comparando con el objetivo hasta hallarlo o agotar el arreglo. No requiere orden previo y funciona con cualquier tipo de dato comparable.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(n)',
                'worst_time_complexity': r'O(n)',
                'space_complexity': r'O(1)'
            },
            'BINARY_SEARCH': {
                'key': 'binary_search',
                'name': 'Búsqueda binaria (Binary search, versión iterativa)',
                'description': 'Opera sobre un arreglo ordenado. En cada paso examina el elemento central y descarta la mitad que no puede contener el objetivo, repitiendo hasta encontrarlo o vaciar el rango. La versión iterativa evita costo de pila adicional.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(\log n)',
                'worst_time_complexity': r'O(\log n)',
                'space_complexity': r'O(1)'
            },
            'JUMP_SEARCH': {
                'key': 'jump_search',
                'name': 'Búsqueda por saltos (Jump search)',
                'description': 'Requiere arreglo ordenado. Avanza en bloques de tamaño aproximadamente raíz de n hasta sobrepasar el posible rango del objetivo y después realiza una búsqueda lineal dentro del bloque identificado.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(\sqrt{n})',
                'worst_time_complexity': r'O(\sqrt{n})',
                'space_complexity': r'O(1)'
            },
            'EXPONENTIAL_SEARCH': {
                'key': 'exponential_search',
                'name': 'Búsqueda exponencial (Exponential search)',
                'description': 'Requiere arreglo ordenado. Amplía exponencialmente el índice de búsqueda para acotar rápidamente un intervalo candidato y luego ejecuta búsqueda binaria dentro de ese intervalo.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(\log n)',
                'worst_time_complexity': r'O(\log n)',
                'space_complexity': r'O(1)'
            },
            'INTERPOLATION_SEARCH': {
                'key': 'interpolation_search',
                'name': 'Búsqueda por interpolación (Interpolation search)',
                'description': 'Requiere arreglo ordenado por una clave numérica aproximadamente uniforme. Estima la posición del objetivo mediante interpolación lineal y refina iterativamente. En distribuciones muy sesgadas su desempeño puede degradarse significativamente.',
                'best_time_complexity': r'O(1)',
                'average_time_complexity': r'O(\log\log n)',
                'worst_time_complexity': r'O(n)',
                'space_complexity': r'O(1)'
            },
        },
    },
}
