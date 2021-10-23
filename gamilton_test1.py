from itertools import permutations

# Функция для нахождения минимального пути обхода
# Возвращает порядок городов и минимальное время
def minimumPathStations(graph, start_vertex, total_maxweight, V): 
    # Все перестановки, кроме первой точки
    vertex = [i for i in range(V) if i!=start_vertex]
    # Запоминаем максимум для сравнения и варианты обхода без начальной точки
    min_path = total_maxweight 
    min_vertex_order = []
    next_permutation=permutations(vertex)
    # Проверяем каждый обход
    for i in next_permutation:

        current_pathweight = 0
        current_vertex_order = [start_vertex]
        k = start_vertex 
        for j in i:
            # Заполняем лист
            current_pathweight += graph[k][j]
            current_vertex_order.append(j)
            k = j 
        # Возвращаемся к первой станции
        current_pathweight += graph[k][start_vertex]
        current_vertex_order.append(start_vertex) 

        # Проверяем на кратчайший
        if min_path > current_pathweight:
            min_vertex_order = current_vertex_order
            min_path = current_pathweight

    return min_vertex_order, min_path
 
 
if __name__ == "__main__": 

    stations = ["Барикадная", "Кропоткинская", "Библиотека имени Ленина",
                "Охотный ряд", "Третьяковская"]
    # Матрица смежности графа
    # Возможно придётся оформить ввод согласно выбору точки
    # И ввод названия станции
    station = input("Введите название станции: ")
    graph = [[0, 13, 11, 9, 8], [13, 0, 2, 4, 13],

             [11, 2, 0, 2, 11],

             [9, 4, 2, 0, 9], [8, 13, 11, 9, 0]]

    # Начальная точка
    start_vertex = 0
    # Максимальное время
    max_weight = 100
    # Количество станций
    vertex_count = len(graph)
    # Запоминаем выводимые значения
    vertexes, min_path_length = minimumPathStations(graph, start_vertex, max_weight, vertex_count)
    # Выводим улицы в порядке обхода
    for i in vertexes:
        print(stations[i])
    # Выводим количество минут
    print("\n")
    print(min_path_length, "минуты")
