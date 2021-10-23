from itertools import permutations

# Функция для нахождения минимального пути обхода
# Возвращает порядок станций и минимальное время
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

    # Станции
    stations = ["Барикадная", "Библиотека имени Ленина", "Третьяковская", 
                "Кропоткинская","Охотный ряд"]
    
    # Матрица смежности графа
    station = input("Введите название станции: ")
    
    station_dist = [
                    # Барикадная
                    [[0, 14, 12, 10, 12],
                     [14, 0, 2, 4, 14],
                     [12, 2, 0, 2, 12],
                     [10, 4, 2, 0, 10],
                     [12, 14, 12, 10, 0]],

                    # Библиотека имени Ленина
                    [[0, 2, 12, 2, 12],
                     [2, 0, 14, 4, 14],
                     [12, 14, 0, 10, 12],
                     [2, 4, 10, 0, 10],
                     [12, 14, 12, 10, 0]],

                    # Третьяковская
                    [[0, 14, 12, 10, 12],
                     [14, 0, 2, 4, 14],
                     [12, 2, 0, 2, 12],
                     [10, 4, 2, 0, 10],
                     [12, 14, 12, 10, 0]],

                    # Кропоткинская
                    [[0, 14, 2, 4, 14],
                     [14, 0, 12, 10, 12],
                     [2, 12, 0, 2, 12],
                     [4, 10, 2, 0, 10],
                     [14, 12, 12, 10, 0]],
                    
                    # Охотный ряд
                    [[0, 4, 2, 10, 10],
                     [4, 0, 2, 14, 14],
                     [2, 2, 0, 12, 12],
                     [10, 14, 12, 0, 12],
                     [10, 14, 12, 12, 0]]]
    
    station_order = [["Барикадная", "Кропоткинская", "Библиотека имени Ленина",
                    "Охотный ряд", "Третьяковская"],
                    
                    ["Библиотека имени Ленина", "Кропоткинская", "Барикадная",
                    "Охотный ряд", "Третьяковская"],
                    
                    ["Третьяковская", "Кропоткинская", "Библиотека имени Ленина",
                    "Охотный ряд", "Барикадная"],
                    
                    ["Кропоткинская", "Барикадная", "Библиотека имени Ленина",
                    "Охотный ряд", "Третьяковская"],
                    
                    ["Охотный ряд", "Кропоткинская", "Библиотека имени Ленина",
                     "Барикадная", "Третьяковская"]]

    # Находим требуемую станцию
    k = 0
    for i in stations:
        if i == station:
            k = stations.index(i)
            
    # Создаём файл с матрицей
    graph = station_dist[k]
    stations = station_order[k]
    import numpy as np
    graph_npy = np.asarray(graph)
    np.save("adjacency.npy", graph)
    
    #adj = np.load("adjacency.npy")
    #print(adj)
    #print("\n")

    # Начальная точка
    start_vertex = 0
    # Максимальные веса точки
    max_weight = 1000000
    # Количество станций
    vertex_count = len(graph)
    # Запоминаем выводимые значения
    vertexes, min_path_length = minimumPathStations(graph, start_vertex, max_weight, vertex_count)
    # Выводим станции в порядке обхода
    final_stations=[]
    for i in vertexes:
        final_stations.append(stations[i])
        
    print(final_stations)
    print("\n")
    
    # Создаём файл с решением    
    import csv
    with open("answer.csv", 'w') as f:

        # Записываем в файл полученный путь
        write = csv.writer(f)
        write.writerow(final_stations)
        
    with open("answer.csv", 'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            print(line)

