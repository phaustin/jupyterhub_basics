# building the image for eosc 350

1) build the meta-package with the basic notebook dependencies

```
conda build base_recipe
```

which should upload the package to anaconda in the eoas_ubc channel as base_notebook version 2020.08.24
(given a `~/.condarc` with the `anaconda_token` set)

2) build the conda-lock file

```
cd notebook_image
conda-lock --file environment.yml -p linux-64
```

3) build the two condtainers

```
docker-compose build jupyterhub
docker-compose build notebook
```

4) bring up the hub on port 8000

```
docker-compose up
```

5) if it looks good, upload the images



