## List All Environments

```
conda info --envs
```

comes out to be

```
base                  *  /Users/brock/opt/anaconda3
MyDjangoEnv              /Users/brock/opt/anaconda3/envs/MyDjangoEnv
```

## Create Virtual Environment

```
 conda create --name MyDjangoEnv django
 # python > 3.5
```

## Activate Environment

```
conda activate MyDjangoEnv
```

## Deactive Environment

```
conda deactivate MyDjangoEnv
```

## Remove Env

```
conda env remove --name MyDjangoEnv
```

# Django CLI

```
django-admin startproject first_project
```
