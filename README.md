# Implementación de algoritmos de búsqueda no informados

**BFS** = BreadthFirstSearch

**DFS** = DepthFirstSearch

## Ejecución

        python App.py

## Problema: Ruta de un viajero

Implementar los algoritmos DFS y BFS para encontrar el camino del viajero de la ciudad de Tumbes hacia la ciudad de Arequipa según el mapa.

![Ruta de un viajero](http://www.solocodigoweb.com/wp-content/uploads/2019/10/ruta_de_un_viajero_dfs_bfs.jpg)

## Rutas en JSON

        {
            "Tumbes": {
                "Trujillo": null,
                "Moyobamba": null,
                "Iquitos": null
            },
            "Trujillo": {
                "Lima": null,
                "Huancayo": null
            },
            "Moyobamba": {
                "Huancayo": null
            },
            "Iquitos": {
                "Huancayo": null,
                "Cusco": null
            },
            "Lima": {
                "Nazca": null
            },
            "Huancayo": {
                "Arequipa": null,
                "Puno": null
            },
            "Nazca": {
                "Arequipa": null
            },
            "Puno": {
                "Arequipa": null
            },
            "Cusco": {
                "Arequipa": null
            },
            "Arequipa": {
                "Arequipa":null
            }
        }