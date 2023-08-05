# Minikube Services

__minikservices__ is a small and very simple python project that aims to help with the start and stop of __Minikube__ services.

Instead of creating multiple terminal tabs to expose minikube services, you can use __kservice__ command line tool to start and stop services. It will also display the exposed services and its addresses. 


## Build/Dev local
```
git clone https://github.com/dszortyka/minikservices.git
cd minikservices
python3 -m venv .pyenv
source .pyenv/bin/activate
pip install -r requirements.txt
pip install . 
kservice -h
```

## Python Package (PyPI)


