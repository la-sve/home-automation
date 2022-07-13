# Statistiken mit python in jupyter Notebooks

## Bauen
```bash
docker build --rm -t jupyter/my-datascience-notebook .
```

## Starten
```bash
#    -p 8888:8888 allows the container to use the web server port 8888 on your computer
#    -v makes the current directory accessible as the work/ directory
#    jupyter lab … starts the jupyter lab server 

docker run --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work --name jupiterdatacsience jupyter/my-datascience-notebook jupyter lab --ip=0.0.0.0 --allow-root 
```

Die jupyter Oberfläche wird dann erreicht, indem in der Konsole der entsprechende Link mit Token genutzt wird.